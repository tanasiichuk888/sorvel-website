// Sorvel site worker
// 1. www.sorvel.agency -> sorvel.agency (301)
// 2. POST /api/e        -> anonymous visit events (page views, scroll, time, clicks, lead actions) into a Durable Object
// 3. /scoreboard        -> private growth dashboard (behind Cloudflare Access), data from /scoreboard/api
// 4. everything else    -> the static site in ./website
//
// Secrets (Workers > sorvel-website > Settings > Variables and Secrets):
//   CF_ACCOUNT_ID   Cloudflare account id
//   CF_API_TOKEN    API token with "Account Analytics: Read"
//   ACCESS_TEAM     Zero Trust team domain, e.g. sorvel.cloudflareaccess.com
//   ACCESS_AUD      Access application audience (AUD) tag for /scoreboard
//   GSC_KEY         Google service account JSON key (Search Console read access), optional

import { DurableObject } from "cloudflare:workers";
import DASHBOARD from "./scoreboard.html";

const HOST = "sorvel.agency";
const EVENT_TYPES = new Set(["brief_start", "brief", "telegram", "email", "view", "scroll", "click", "time"]);
const TARGET = new Set(["United States", "United Kingdom", "Canada", "Australia", "Ireland", "Germany", "Netherlands", "Switzerland",
  "Sweden", "Norway", "Denmark", "France", "Belgium", "Austria", "Finland", "Spain", "Italy", "Israel", "United Arab Emirates", "Singapore", "New Zealand"]);

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.hostname === "www." + HOST) {
      url.hostname = HOST;
      return Response.redirect(url.toString(), 301);
    }
    if (url.pathname === "/api/e") return collect(request, env);
    if (url.pathname === "/scoreboard" || url.pathname.startsWith("/scoreboard/")) return scoreboard(request, env, url);
    return env.ASSETS.fetch(request);
  },
};

/* ------------------------------------------------------------------ events */

async function collect(request, env) {
  if (request.method !== "POST") return new Response(null, { status: 405 });
  const ok = new Response(null, { status: 204 });
  const ua = request.headers.get("user-agent") || "";
  if (/bot|crawl|spider|headless|lighthouse/i.test(ua) || (request.cf && request.cf.botManagement && request.cf.botManagement.verifiedBot)) return ok;
  let b;
  try { b = JSON.parse((await request.text()).slice(0, 2000)); } catch { return ok; }
  if (!b || !EVENT_TYPES.has(b.t) || !env.LEADS) return ok;
  const clip = (v, n = 120) => String(v || "").replace(/[^\w\-./:@ ]/g, "").slice(0, n);
  const v = Number.isFinite(+b.v) ? Math.max(0, Math.min(1800, Math.round(+b.v))) : null;
  const k = b.t === "click" ? String(b.k || "").replace(/[<>\u0000-\u001f]/g, "").slice(0, 110) : b.t === "scroll" ? clip(b.k, 3) : "";
  const path = (x) => (clip(x).replace(/\.html$/, "").replace(/\/index$/, "/") || "/");
  await leadStore(env).add({ t: b.t, p: path(b.p), s: clip(b.s, 60) || "direct", c: (request.cf && request.cf.country) || "", l: path(b.l),
    i: String(b.i || "").replace(/[^a-z0-9]/g, "").slice(0, 16), k, v: b.t === "time" ? v : null });
  return ok;
}
const leadStore = (env) => env.LEADS.get(env.LEADS.idFromName("leads"));

/* One SQLite-backed Durable Object keeps every lead event (a few per day, tiny). */
export class LeadStore extends DurableObject {
  constructor(ctx, env) {
    super(ctx, env);
    this.sql = ctx.storage.sql;
    this.sql.exec(`CREATE TABLE IF NOT EXISTS ev (ts INTEGER NOT NULL, t TEXT NOT NULL, p TEXT, s TEXT, c TEXT, l TEXT)`);
    this.sql.exec(`CREATE INDEX IF NOT EXISTS ev_ts ON ev (ts)`);
    // v2: visit id (i), detail (k: click label or scroll mark), number (v: seconds on page)
    const cols = this.sql.exec(`PRAGMA table_info(ev)`).toArray().map((r) => r.name);
    for (const [c, ty] of [["i", "TEXT"], ["k", "TEXT"], ["v", "INTEGER"]]) if (!cols.includes(c)) this.sql.exec(`ALTER TABLE ev ADD COLUMN ${c} ${ty}`);
  }
  add(e) {
    this.sql.exec(`INSERT INTO ev (ts, t, p, s, c, l, i, k, v) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`, Date.now(), e.t, e.p, e.s, e.c, e.l, e.i || "", e.k || "", e.v);
  }
  /* What people do on the site: funnel, pages (time, scroll), clicks, exits, recent visits */
  behavior(a, b) {
    const ev = this.sql.exec(`SELECT ts, t, p, s, c, i, k, v FROM ev WHERE ts >= ? AND ts < ? AND i != '' ORDER BY ts LIMIT 60000`, a, b).toArray();
    const S = new Map();
    for (const e of ev) {
      let x = S.get(e.i);
      if (!x) S.set(e.i, x = { i: e.i, start: e.ts, end: e.ts, s: e.s, c: e.c, pages: [], secs: 0, brief: 0, start_b: 0, contact: 0, clicks: [] });
      x.end = e.ts;
      if (e.t === "view") { x.pages.push({ p: e.p, ts: e.ts, secs: 0, depth: 0 }); }
      const cur = x.pages[x.pages.length - 1];
      if (e.t === "time") { x.secs += e.v || 0; const pg = [...x.pages].reverse().find((q) => q.p === e.p); if (pg) pg.secs += e.v || 0; }
      if (e.t === "scroll") { const pg = [...x.pages].reverse().find((q) => q.p === e.p); if (pg) pg.depth = Math.max(pg.depth, +e.k || 0); }
      if (e.t === "brief") x.brief = 1;
      if (e.t === "brief_start") x.start_b = 1;
      if (e.t === "telegram" || e.t === "email") x.contact = 1;
      if (e.t === "click" && x.clicks.length < 12) x.clicks.push(e.k);
      void cur;
    }
    const sess = [...S.values()].filter((x) => x.pages.length);
    const isCase = (p) => /^\/work\/[^/]+/.test(p);
    const f = (fn) => sess.filter(fn).length;
    const funnel = [
      ["Visited the site", sess.length],
      ["Opened a case study", f((x) => x.pages.some((q) => isCase(q.p)))],
      ["Opened pricing", f((x) => x.pages.some((q) => /^\/pricing/.test(q.p)))],
      ["Started a brief", f((x) => x.start_b)],
      ["Sent a brief", f((x) => x.brief)],
      ["Clicked Telegram or email", f((x) => x.contact)],
    ].map(([k, v]) => ({ k, v }));
    const P = new Map();
    for (const x of sess) for (const q of x.pages) {
      let r = P.get(q.p); if (!r) P.set(q.p, r = { k: q.p, views: 0, secs: 0, timed: 0, deep: 0, depthSum: 0 });
      r.views++; r.secs += q.secs; if (q.secs) r.timed++; if (q.depth >= 75) r.deep++; r.depthSum += q.depth;
    }
    const pages = [...P.values()].sort((x, y) => y.views - x.views).slice(0, 20)
      .map((r) => ({ k: r.k, views: r.views, avg: r.timed ? Math.round(r.secs / r.timed) : null, deep: r.views ? r.deep / r.views : 0, depth: r.views ? Math.round(r.depthSum / r.views) : 0 }));
    const C = new Map(); for (const e of ev) if (e.t === "click" && e.k) C.set(e.k, (C.get(e.k) || 0) + 1);
    const clicks = [...C].sort((x, y) => y[1] - x[1]).slice(0, 15).map(([k, v]) => ({ k, v }));
    const X = new Map(); for (const x of sess) { const last = x.pages[x.pages.length - 1].p; X.set(last, (X.get(last) || 0) + 1); }
    const exits = [...X].sort((x, y) => y[1] - x[1]).slice(0, 10).map(([k, v]) => ({ k, v }));
    const single = f((x) => x.pages.length === 1 && x.secs < 10);
    const secsAll = sess.map((x) => x.secs).sort((m, n) => m - n);
    const median = secsAll.length ? secsAll[Math.floor(secsAll.length / 2)] : 0;
    const recent = sess.slice().sort((x, y) => y.start - x.start).slice(0, 40)
      .map((x) => ({ at: x.start, s: x.s, c: x.c, secs: x.secs, brief: x.brief, started: x.start_b, contact: x.contact, pages: x.pages.slice(0, 30).map((q) => ({ p: q.p, secs: q.secs, depth: q.depth })), clicks: x.clicks }));
    return { sessions: sess.length, bounce: sess.length ? single / sess.length : 0, median, funnel, pages, clicks, exits, recent };
  }
  report(a, b, withGroups) {
    const rows = this.sql.exec(`SELECT t, strftime('%Y-%m-%d', ts / 1000, 'unixepoch') AS d, COUNT(*) AS n FROM ev WHERE ts >= ? AND ts < ? GROUP BY t, d ORDER BY d`, a, b).toArray();
    if (!withGroups) return { rows: rows.filter((r) => ["brief", "brief_start", "telegram", "email"].includes(r.t)) };
    const grp = (col) => this.sql.exec(`SELECT ${col} AS k, COUNT(*) AS v FROM ev WHERE ts >= ? AND ts < ? AND t IN ('brief','telegram','email') GROUP BY k ORDER BY v DESC LIMIT 10`, a, b).toArray();
    // lead chart keeps to lead actions only
    rows.splice(0, rows.length, ...rows.filter((r) => ["brief", "brief_start", "telegram", "email"].includes(r.t)));
    return { rows, src: grp("s"), land: grp("l") };
  }
}

/* ------------------------------------------------------------- scoreboard */

async function scoreboard(request, env, url) {
  const who = await accessUser(request, env);
  if (!who.ok) {
    return new Response(`<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex"><title>Private</title>
<body style="font:16px/1.6 system-ui;background:#0B0C0F;color:#F2EFEA;display:grid;place-items:center;min-height:100vh;margin:0">
<div style="max-width:440px;padding:24px"><h1 style="font-size:22px">This page is private</h1><p style="color:#8E9099">${who.why}</p></div>`,
      { status: 403, headers: { "content-type": "text/html; charset=utf-8", "cache-control": "no-store", "x-robots-tag": "noindex" } });
  }
  const sec = { "cache-control": "no-store", "x-robots-tag": "noindex, nofollow", "x-frame-options": "DENY", "referrer-policy": "no-referrer" };
  if (url.pathname === "/scoreboard/api") {
    const days = url.searchParams.get("days") === "28" ? 28 : 7;
    const data = await stats(env, days);
    return new Response(JSON.stringify(data), { headers: { ...sec, "content-type": "application/json" } });
  }
  return new Response(DASHBOARD, { headers: { ...sec, "content-type": "text/html; charset=utf-8" } });
}

/* Cloudflare Access: verify the signed JWT the Access proxy adds to every request. Fails closed. */
let certCache = { at: 0, keys: [] };
async function accessUser(request, env) {
  if (env.DEV_OPEN === "1") return { ok: true, email: "dev" };
  if (!env.ACCESS_TEAM || !env.ACCESS_AUD) return { ok: false, why: "Turn on Cloudflare Access for this page first (ACCESS_TEAM and ACCESS_AUD are not set)." };
  const jwt = request.headers.get("cf-access-jwt-assertion");
  if (!jwt) return { ok: false, why: "Sign in through Cloudflare Access to see this page." };
  try {
    const [h, p, s] = jwt.split(".");
    const head = JSON.parse(b64urlText(h)), body = JSON.parse(b64urlText(p));
    const auds = Array.isArray(body.aud) ? body.aud : [body.aud];
    if (!auds.includes(env.ACCESS_AUD)) return { ok: false, why: "Wrong Access application." };
    if (!body.exp || body.exp * 1000 < Date.now()) return { ok: false, why: "Your sign-in expired. Reload to sign in again." };
    if (Date.now() - certCache.at > 3600e3 || !certCache.keys.some((k) => k.kid === head.kid)) {
      const r = await fetch(`https://${env.ACCESS_TEAM}/cdn-cgi/access/certs`);
      certCache = { at: Date.now(), keys: (await r.json()).keys || [] };
    }
    const jwk = certCache.keys.find((k) => k.kid === head.kid);
    if (!jwk) return { ok: false, why: "Unknown signing key." };
    const key = await crypto.subtle.importKey("jwk", jwk, { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["verify"]);
    const valid = await crypto.subtle.verify("RSASSA-PKCS1-v1_5", key, b64urlBytes(s), new TextEncoder().encode(h + "." + p));
    return valid ? { ok: true, email: body.email } : { ok: false, why: "Invalid sign-in token." };
  } catch (e) {
    return { ok: false, why: "Could not check your sign-in." };
  }
}
const b64urlBytes = (s) => Uint8Array.from(atob(s.replace(/-/g, "+").replace(/_/g, "/").padEnd(Math.ceil(s.length / 4) * 4, "=")), (c) => c.charCodeAt(0));
const b64urlText = (s) => new TextDecoder().decode(b64urlBytes(s));
const b64url = (buf) => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");

/* ------------------------------------------------------------------ stats */

const day = (d) => d.toISOString().slice(0, 10);
function ranges(days) {
  const end = new Date(); end.setUTCHours(0, 0, 0, 0); end.setUTCDate(end.getUTCDate() + 1);      // tomorrow 00:00 UTC (today included)
  const start = new Date(end); start.setUTCDate(start.getUTCDate() - days);
  const pstart = new Date(start); pstart.setUTCDate(pstart.getUTCDate() - days);
  const list = []; for (let d = new Date(start); d < end; d.setUTCDate(d.getUTCDate() + 1)) list.push(day(d));
  return { cur: [start, end], prev: [pstart, start], days: list };
}

async function stats(env, days) {
  const r = ranges(days);
  if (env.DEV_MOCK === "1") return mock(r, days);
  const errors = [];
  const safe = (name, p) => p.catch((e) => { if (!/not connected/.test(e.message)) errors.push(name + ": " + String(e.message || e).slice(0, 300)); return null; });
  const [rumCur, rumPrev, leadsCur, leadsPrev, behavior, behaviorPrev, gsc] = await Promise.all([
    safe("Web Analytics", rum(env, r.cur, true)),
    safe("Web Analytics (previous)", rum(env, r.prev, false)),
    safe("Leads", leadReport(env, r.cur, true)),
    safe("Leads (previous)", leadReport(env, r.prev, false)),
    safe("Behaviour", env.LEADS ? leadStore(env).behavior(r.cur[0].getTime(), r.cur[1].getTime()) : Promise.reject(new Error("not connected"))),
    safe("Behaviour (previous)", env.LEADS ? leadStore(env).behavior(r.prev[0].getTime(), r.prev[1].getTime()).then((x) => ({ sessions: x.sessions, bounce: x.bounce, median: x.median, funnel: x.funnel })) : Promise.reject(new Error("not connected"))),
    env.GSC_KEY ? safe("Search Console", searchConsole(env, r)) : Promise.resolve(null),
  ]);
  return {
    days, list: r.days, start: day(r.cur[0]), end: day(new Date(r.cur[1] - 864e5)),
    rum: rumCur, rumPrev, leads: leadsCur && leadsCur.rows, leadsPrev: leadsPrev && leadsPrev.rows,
    leadSrc: leadsCur && leadsCur.src, leadLand: leadsCur && leadsCur.land, gsc, behavior, behaviorPrev,
    connected: { analytics: !!(env.CF_API_TOKEN && env.CF_ACCOUNT_ID), events: !!env.LEADS, gsc: !!env.GSC_KEY },
    errors, at: new Date().toISOString(),
  };
}

/* Cloudflare Web Analytics (RUM) through the GraphQL Analytics API */
async function cfgql(env, query) {
  if (!env.CF_API_TOKEN || !env.CF_ACCOUNT_ID) throw new Error("not connected");
  const res = await fetch("https://api.cloudflare.com/client/v4/graphql", {
    method: "POST", headers: { authorization: "Bearer " + env.CF_API_TOKEN, "content-type": "application/json" },
    body: JSON.stringify({ query }),
  });
  const j = await res.json();
  if (j.errors && j.errors.length) throw new Error(j.errors.map((e) => e.message).join("; "));
  return j.data.viewer.accounts[0] || {};
}

async function rum(env, [a, b], full) {
  const run = async (withBot) => {
    const f = `{AND:[{datetime_geq:"${a.toISOString()}"},{datetime_lt:"${b.toISOString()}"},{requestHost_in:["${HOST}","www.${HOST}"]}${withBot ? ",{bot:0}" : ""}]}`;
    const g = (alias, dim, n, order = "count_DESC") => `${alias}: rumPageloadEventsAdaptiveGroups(filter:${f},limit:${n},orderBy:[${order}]){count sum{visits} dimensions{${dim}}}`;
    const q = `{viewer{accounts(filter:{accountTag:"${env.CF_ACCOUNT_ID}"}){
      total: rumPageloadEventsAdaptiveGroups(filter:${f},limit:1){count sum{visits}}
      ${g("countries", "countryName", 60, "sum_visits_DESC")}
      ${full ? `${g("byDay", "date", 100, "date_ASC")}
      ${g("refs", "refererHost", 12, "sum_visits_DESC")}
      ${g("paths", "requestPath", 15)}
      ${g("devices", "deviceType", 5, "sum_visits_DESC")}` : ""}
      vitals: rumWebVitalsEventsAdaptiveGroups(filter:${f},limit:5){count quantiles{largestContentfulPaintP75} dimensions{deviceType}}
    }}}`;
    return cfgql(env, q);
  };
  let d;
  try { d = await run(true); } catch (e) { if (/bot/i.test(e.message)) d = await run(false); else throw e; }
  const n = (x) => (x && x[0] ? x[0] : null);
  const tot = n(d.total);
  const visits = tot ? tot.sum.visits : 0, views = tot ? tot.count : 0;
  // Web Analytics returns ISO country codes ("US"); show full names
  const countries = (d.countries || []).map((x) => ({ k: countryName(x.dimensions.countryName), v: x.sum.visits }));
  const target = countries.filter((c) => TARGET.has(c.k)).reduce((s, c) => s + c.v, 0);
  const vit = {}; (d.vitals || []).forEach((x) => { vit[(x.dimensions.deviceType || "other").toLowerCase()] = { p75: lcpMs(x.quantiles.largestContentfulPaintP75), n: x.count }; });
  const out = { visits, views, countries, target, targetShare: visits ? target / visits : 0, lcp: vit };
  if (full) {
    out.byDay = (d.byDay || []).map((x) => ({ d: x.dimensions.date, visits: x.sum.visits, views: x.count }));
    out.refs = (d.refs || []).map((x) => ({ k: x.dimensions.refererHost || "Direct", v: x.sum.visits }));
    out.paths = (d.paths || []).map((x) => ({ k: x.dimensions.requestPath || "/", v: x.count }));
    out.devices = (d.devices || []).map((x) => ({ k: x.dimensions.deviceType || "other", v: x.sum.visits }));
  }
  return out;
}

let regionNames = null;
function countryName(v) {
  if (!v) return "Unknown";
  if (/^[A-Z]{2}$/.test(v)) {
    try { regionNames = regionNames || new Intl.DisplayNames(["en"], { type: "region" }); return regionNames.of(v) || v; } catch { return v; }
  }
  return v;
}
/* LCP comes back in microseconds; keep milliseconds */
const lcpMs = (v) => Math.round((Number(v) || 0) / 1000);

/* Lead events from the LeadStore Durable Object */
async function leadReport(env, [a, b], withGroups) {
  if (!env.LEADS) throw new Error("not connected");
  const r = await leadStore(env).report(a.getTime(), b.getTime(), withGroups);
  const num = (rows) => (rows || []).map((x) => ({ ...x, n: x.n != null ? Number(x.n) : undefined, v: x.v != null ? Number(x.v) : undefined }));
  return { rows: num(r.rows), src: num(r.src), land: num(r.land) };
}

/* Google Search Console (service account, read-only) */
let gToken = { at: 0, tok: "" };
async function googleToken(env) {
  if (gToken.tok && Date.now() < gToken.at) return gToken.tok;
  const sa = JSON.parse(env.GSC_KEY);
  const now = Math.floor(Date.now() / 1000);
  const enc = (o) => b64url(new TextEncoder().encode(JSON.stringify(o)));
  const unsigned = enc({ alg: "RS256", typ: "JWT" }) + "." + enc({ iss: sa.client_email, scope: "https://www.googleapis.com/auth/webmasters.readonly", aud: "https://oauth2.googleapis.com/token", iat: now, exp: now + 3600 });
  const pem = sa.private_key.replace(/-----[^-]+-----/g, "").replace(/\s+/g, "");
  const key = await crypto.subtle.importKey("pkcs8", Uint8Array.from(atob(pem), (c) => c.charCodeAt(0)), { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["sign"]);
  const sig = await crypto.subtle.sign("RSASSA-PKCS1-v1_5", key, new TextEncoder().encode(unsigned));
  const res = await fetch("https://oauth2.googleapis.com/token", { method: "POST", headers: { "content-type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ grant_type: "urn:ietf:params:oauth:grant-type:jwt-bearer", assertion: unsigned + "." + b64url(sig) }) });
  const j = await res.json();
  if (!j.access_token) throw new Error(j.error_description || j.error || "Google sign-in failed");
  gToken = { tok: j.access_token, at: Date.now() + 3000e3 };
  return gToken.tok;
}
async function searchConsole(env, r) {
  const tok = await googleToken(env);
  const q = async ([a, b], dims, limit = 1000) => {
    const res = await fetch(`https://www.googleapis.com/webmasters/v3/sites/${encodeURIComponent("sc-domain:" + HOST)}/searchAnalytics/query`, {
      method: "POST", headers: { authorization: "Bearer " + tok, "content-type": "application/json" },
      body: JSON.stringify({ startDate: day(a), endDate: day(new Date(b - 864e5)), dimensions: dims, rowLimit: limit, dataState: "all" }) });
    const j = await res.json();
    if (j.error) throw new Error(j.error.message);
    return j.rows || [];
  };
  const [daysCur, daysPrev, qCur, qPrev, pages] = await Promise.all([q(r.cur, ["date"]), q(r.prev, ["date"]), q(r.cur, ["query"]), q(r.prev, ["query"]), q(r.cur, ["page"], 15)]);
  const sum = (rows, k) => rows.reduce((s, x) => s + (x[k] || 0), 0);
  const brand = (s) => /sorvel/i.test(s);
  const nb = (rows) => rows.filter((x) => !brand(x.keys[0]));
  return {
    clicks: sum(daysCur, "clicks"), impressions: sum(daysCur, "impressions"),
    prevClicks: sum(daysPrev, "clicks"), prevImpressions: sum(daysPrev, "impressions"),
    nbClicks: sum(nb(qCur), "clicks"), prevNbClicks: sum(nb(qPrev), "clicks"),
    byDay: daysCur.map((x) => ({ d: x.keys[0], clicks: x.clicks, impressions: x.impressions })),
    queries: qCur.slice().sort((x, y) => y.impressions - x.impressions).slice(0, 20).map((x) => ({ k: x.keys[0], clicks: x.clicks, impressions: x.impressions, pos: Math.round(x.position * 10) / 10, brand: brand(x.keys[0]) })),
    pages: pages.map((x) => ({ k: x.keys[0].replace(/^https?:\/\/[^/]+/, "") || "/", clicks: x.clicks, impressions: x.impressions })),
  };
}

/* local preview only (.dev.vars DEV_MOCK=1): believable sample data, never used in production */
function mock(r, days) {
  const rnd = (a, b) => Math.round(a + Math.random() * (b - a));
  const leads = []; r.days.forEach((d) => { leads.push({ t: "brief", d, n: rnd(0, 2) }, { t: "telegram", d, n: rnd(0, 3) }, { t: "email", d, n: rnd(0, 1) }, { t: "brief_start", d, n: rnd(1, 4) }); });
  const byDay = r.days.map((d) => { const v = rnd(18, 70); return { d, visits: v, views: Math.round(v * 2.3) }; });
  const visits = byDay.reduce((s, x) => s + x.visits, 0);
  const countries = [["United States", .34], ["United Kingdom", .14], ["Spain", .1], ["Germany", .08], ["Ukraine", .07], ["India", .06], ["Canada", .05], ["Australia", .04]].map(([k, f]) => ({ k, v: Math.round(visits * f) }));
  const target = countries.filter((c) => TARGET.has(c.k)).reduce((s, c) => s + c.v, 0);
  const rumObj = (scale) => ({ visits: Math.round(visits * scale), views: Math.round(visits * 2.3 * scale), countries, target: Math.round(target * scale), targetShare: target / visits * (scale < 1 ? .93 : 1),
    lcp: { mobile: { p75: scale < 1 ? 2840 : 2210, n: 140 }, desktop: { p75: 1180, n: 210 } } });
  return { days, list: r.days, start: day(r.cur[0]), end: day(new Date(r.cur[1] - 864e5)),
    rum: { ...rumObj(1), byDay, refs: [{ k: "Direct", v: 120 }, { k: "www.google.com", v: 64 }, { k: "www.linkedin.com", v: 31 }, { k: "www.behance.net", v: 18 }, { k: "dribbble.com", v: 9 }],
      paths: [{ k: "/", v: 300 }, { k: "/work", v: 120 }, { k: "/pricing", v: 90 }, { k: "/work/valhalla-capital", v: 44 }, { k: "/services/websites", v: 38 }, { k: "/contact", v: 30 }],
      devices: [{ k: "desktop", v: 210 }, { k: "mobile", v: 140 }, { k: "tablet", v: 6 }] },
    rumPrev: rumObj(.8), leads, leadsPrev: leads.map((x) => ({ ...x, n: Math.max(0, x.n - 1) })),
    leadSrc: [{ k: "www.google.com", v: 6 }, { k: "direct", v: 4 }, { k: "www.linkedin.com", v: 3 }], leadLand: [{ k: "/", v: 6 }, { k: "/pricing", v: 4 }, { k: "/work/serverscamp", v: 2 }],
    gsc: { clicks: 41, impressions: 5071, prevClicks: 30, prevImpressions: 2035, nbClicks: 6, prevNbClicks: 5,
      byDay: r.days.map((d) => ({ d, clicks: rnd(0, 6), impressions: rnd(80, 400) })),
      queries: [{ k: "sorvel agency", clicks: 22, impressions: 60, pos: 1.1, brand: true }, { k: "webflow agency for saas", clicks: 3, impressions: 820, pos: 18.4, brand: false }, { k: "fintech website design", clicks: 2, impressions: 610, pos: 22.7, brand: false }],
      pages: [{ k: "/", clicks: 30, impressions: 2100 }, { k: "/services/websites", clicks: 6, impressions: 900 }] },
    behavior: mockBehavior(r), behaviorPrev: { sessions: 61, bounce: .48, median: 41, funnel: [] },
    connected: { analytics: true, events: true, gsc: true }, errors: [], at: new Date().toISOString() };
}

function mockBehavior(r) {
  const now = Date.now(), m = (min) => now - min * 60e3;
  return { sessions: 74, bounce: .41, median: 52,
    funnel: [{ k: "Visited the site", v: 74 }, { k: "Opened a case study", v: 29 }, { k: "Opened pricing", v: 17 }, { k: "Started a brief", v: 4 }, { k: "Sent a brief", v: 2 }, { k: "Clicked Telegram or email", v: 5 }],
    pages: [{ k: "/", views: 70, avg: 48, deep: .38, depth: 61 }, { k: "/work", views: 31, avg: 35, deep: .52, depth: 70 }, { k: "/pricing", views: 19, avg: 64, deep: .63, depth: 78 },
      { k: "/work/valhalla-capital", views: 14, avg: 92, deep: .57, depth: 72 }, { k: "/services/saas-website-design", views: 9, avg: 41, deep: .33, depth: 55 }, { k: "/contact", views: 8, avg: 71, deep: .75, depth: 88 }],
    clicks: [{ k: "Start a project → /contact", v: 21 }, { k: "Work → /work", v: 18 }, { k: "Valhalla Capital → /work/valhalla-capital", v: 11 }, { k: "Pricing → /pricing", v: 9 }, { k: "Telegram → t.me", v: 3 }],
    exits: [{ k: "/", v: 33 }, { k: "/work", v: 12 }, { k: "/pricing", v: 9 }, { k: "/contact", v: 6 }],
    recent: [
      { at: m(12), s: "www.linkedin.com", c: "GB", secs: 214, brief: 1, started: 1, contact: 0, pages: [{ p: "/", secs: 40, depth: 75 }, { p: "/work/valhalla-capital", secs: 96, depth: 100 }, { p: "/pricing", secs: 38, depth: 75 }, { p: "/contact", secs: 40, depth: 100 }], clicks: ["Valhalla Capital → /work/valhalla-capital", "Pricing → /pricing", "Start a project → /contact"] },
      { at: m(47), s: "www.google.com", c: "US", secs: 58, brief: 0, started: 0, contact: 0, pages: [{ p: "/services/saas-website-design", secs: 41, depth: 50 }, { p: "/work", secs: 17, depth: 25 }], clicks: ["Work → /work"] },
      { at: m(130), s: "direct", c: "DE", secs: 6, brief: 0, started: 0, contact: 0, pages: [{ p: "/", secs: 6, depth: 25 }], clicks: [] },
      { at: m(300), s: "www.behance.net", c: "CA", secs: 133, brief: 0, started: 0, contact: 1, pages: [{ p: "/", secs: 70, depth: 100 }, { p: "/about", secs: 63, depth: 75 }], clicks: ["Telegram → t.me"] },
    ] };
}
