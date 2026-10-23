(function () {
  const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- anonymous visit stats (no cookies, no personal data) ----------
     For this tab only (session storage, gone when the tab closes): a random visit id,
     where the visit came from and the page it started on. Counts page views, how far
     each page is scrolled, time with the page open, button clicks, and the lead
     actions (brief started / sent, Telegram, email).
     The site owner's own browser is left out: opening /scoreboard or any page with
     ?me=1 marks it (localStorage sv_me), ?me=0 undoes that. */
  const ME = (() => {
    try {
      const q = new URLSearchParams(location.search).get("me");
      if (q === "1") localStorage.setItem("sv_me", "1");
      if (q === "0") localStorage.removeItem("sv_me");
      if (q === "1" || q === "0") {
        const n = document.createElement("div");
        n.setAttribute("role", "status");
        n.textContent = q === "1" ? "This browser is now left out of the site stats" : "This browser is counted in the site stats again";
        n.style.cssText = "position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:9999;padding:10px 16px;border-radius:10px;background:#111;color:#fff;font:14px/1.4 system-ui,sans-serif;box-shadow:0 10px 30px rgba(0,0,0,.35)";
        document.body.appendChild(n); setTimeout(() => n.remove(), 3500);
      }
      return localStorage.getItem("sv_me") === "1";
    } catch (e) { return false; }
  })();
  if (ME) {
    // keep Cloudflare Web Analytics from counting the owner's own visits too
    const rum = (u) => /cdn-cgi\/rum|cloudflareinsights/.test(String((u && u.url) || u));
    try {
      const sb = navigator.sendBeacon && navigator.sendBeacon.bind(navigator);
      if (sb) navigator.sendBeacon = (u, d) => (rum(u) ? true : sb(u, d));
      const f = window.fetch && window.fetch.bind(window);
      if (f) window.fetch = (u, o) => (rum(u) ? Promise.resolve(new Response(null, { status: 204 })) : f(u, o));
      const op = XMLHttpRequest.prototype.open, sd = XMLHttpRequest.prototype.send;
      XMLHttpRequest.prototype.open = function (m, u) { this._svSkip = rum(u); return op.apply(this, arguments); };
      XMLHttpRequest.prototype.send = function () { if (!this._svSkip) return sd.apply(this, arguments); };
    } catch (e) {}
  }
  const SRC = (() => {
    try {
      let v = JSON.parse(sessionStorage.getItem("sv_src") || "null");
      if (!v || !v.id) {
        const q = new URLSearchParams(location.search), ref = document.referrer ? new URL(document.referrer).hostname : "";
        v = Object.assign({ s: q.get("utm_source") || (ref && ref !== location.hostname ? ref : "direct"), l: location.pathname }, v || {});
        v.id = Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4);
        sessionStorage.setItem("sv_src", JSON.stringify(v));
      }
      return v;
    } catch (e) { return { s: "direct", l: location.pathname, id: "" }; }
  })();
  const track = (t, k, v) => {
    if (ME) return;
    try {
      const body = JSON.stringify({ t, p: location.pathname, s: SRC.s, l: SRC.l, i: SRC.id, k, v });
      if (!(navigator.sendBeacon && navigator.sendBeacon("/api/e", body))) fetch("/api/e", { method: "POST", body, keepalive: true }).catch(() => {});
    } catch (e) {}
  };
  track("view");
  // clicks: the lead actions, plus any link or button, labelled by its visible text
  document.addEventListener("click", (e) => {
    const a = e.target.closest && e.target.closest("a[href], button, [data-track]");
    if (!a) return;
    const h = a.getAttribute("href") || "";
    if (/^https:\/\/t\.me\//.test(h)) track("telegram");
    else if (/^mailto:/.test(h)) track("email");
    let label = a.getAttribute("data-track") || a.getAttribute("aria-label") || (a.innerText || a.textContent || "").replace(/\s+/g, " ").trim();
    if (!label && a.querySelector("img[alt]")) label = a.querySelector("img[alt]").alt;
    if (!label) return;
    let to = "";
    try { if (h && !/^(mailto:|tel:|#)/.test(h)) { const u = new URL(h, location.href); to = u.host === location.host ? (u.pathname.replace(/\.html$/, "").replace(/\/index$/, "/") || "/") : u.host.replace(/^www\./, ""); } } catch (er) {}
    track("click", (label.slice(0, 48) + (to ? " → " + to : "")).slice(0, 110));
  }, { capture: true });
  // how far down the page people get (each mark once per page view)
  (() => {
    const hit = new Set();
    const check = () => {
      const full = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);
      const pct = full <= innerHeight + 4 ? 100 : (scrollY + innerHeight) / full * 100;
      [25, 50, 75, 100].forEach((m) => { if (pct >= m - 2 && !hit.has(m)) { hit.add(m); track("scroll", String(m)); } });
    };
    let tm = 0;
    addEventListener("scroll", () => { if (!tm) tm = setTimeout(() => { tm = 0; check(); }, 400); }, { passive: true });
    addEventListener("load", () => setTimeout(check, 1500));
  })();
  // time with the page visible, sent in pieces when the tab is hidden or closed
  (() => {
    let since = document.visibilityState === "visible" ? Date.now() : 0, acc = 0;
    const flush = () => {
      if (since) { acc += Date.now() - since; since = 0; }
      const s = Math.round(acc / 1000); acc = 0;
      if (s >= 1) track("time", "", Math.min(s, 1800));
    };
    document.addEventListener("visibilitychange", () => { if (document.visibilityState === "hidden") flush(); else since = Date.now(); });
    addEventListener("pagehide", flush);
  })();

  /* ---------- intro ---------- */
  const go = () => requestAnimationFrame(() => document.documentElement.classList.add("is-loaded"));
  (document.fonts && document.fonts.ready ? Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 900))]) : Promise.resolve()).then(go);

  /* ---------- buttons: track the cursor for the spotlight / fill origin ---------- */
  document.querySelectorAll(".btn").forEach((b) => {
    const set = (e) => {
      const r = b.getBoundingClientRect();
      b.style.setProperty("--mx", e.clientX - r.left + "px");
      b.style.setProperty("--my", e.clientY - r.top + "px");
    };
    b.addEventListener("pointerenter", set);
    b.addEventListener("pointermove", set);
    b.addEventListener("pointerleave", set);   // the fill shrinks back toward where the cursor left
  });

  /* ---------- showcase scene ----------
     Real screenshots: put full-page captures in website/img/work/ and fill `desktop` / `mobile`
     (e.g. desktop: "img/work/cofimd-desktop.jpg"). Until then each project shows a drawn mock. */
  const cases = [
    { name: "Fintech platform", tags: "Brand, Website, Webflow", url: "fintech-platform.com", theme: "", desktop: "", mobile: "" },
    { name: "AI analytics SaaS", tags: "Website, Product UI, Framer", url: "ai-analytics.io", theme: "mint", desktop: "", mobile: "" },
    { name: "Recruiting platform", tags: "Website, Design system, WordPress", url: "recruit-platform.com", theme: "light", desktop: "", mobile: "" },
  ];
  const mockPage = (theme) => `<div class="pg${theme ? " pg--" + theme : ""}">
      <div class="pg__nav"><b></b><i></i><i></i><i></i><u></u></div>
      <div class="pg__hero"><div><div class="pg__h"></div><div class="pg__h" style="width:78%"></div><div class="pg__h" style="width:55%"></div>
        <div class="pg__p" style="margin-top:3cqw"></div><div class="pg__p" style="width:80%"></div><div class="pg__btns"><u></u><s></s></div></div><div class="pg__vis"></div></div>
      <div class="pg__logos"><i></i><i></i><i></i><i></i><i></i></div>
      <div class="pg__sec"><div class="pg__h"></div><div class="pg__p"></div></div>
      <div class="pg__grid"><div class="pg__card"><i></i><div class="pg__p"></div><div class="pg__p" style="width:60%"></div></div><div class="pg__card"><i></i><div class="pg__p"></div></div><div class="pg__card"><i></i><div class="pg__p"></div></div></div>
      <div class="pg__band"><div><b></b><div class="pg__p"></div></div><div><b></b><div class="pg__p"></div></div><div><b></b><div class="pg__p"></div></div></div>
      <div class="pg__cta"><div class="pg__h"></div><div class="pg__p"></div></div>
    </div>`;
  const screenHTML = (c, kind) => {
    const src = kind === "phone" ? c.mobile : c.desktop;
    return `<div class="scr">${src ? `<img class="scroll" src="${src}" alt="" loading="lazy" />` : mockPage(c.theme)}</div>`;
  };
  const screens = {};
  document.querySelectorAll("[data-screen]").forEach((el) => {
    const kind = el.dataset.screen;
    el.innerHTML = cases.map((c) => screenHTML(c, kind)).join("");
    screens[kind] = [...el.children];
  });
  // section mocks: any .pg--auto gets the drawn page
  document.querySelectorAll(".pg--auto").forEach((el) => {
    const theme = el.classList.contains("pg--mint") ? "mint" : el.classList.contains("pg--light") ? "light" : "";
    el.outerHTML = mockPage(theme).replace('class="pg', 'class="pg--auto pg');
  });
  // how far each page can scroll inside its screen
  const measure = () => {
    Object.values(screens).flat().forEach((scr) => {
      const inner = scr.firstElementChild, view = scr.parentElement;
      if (!inner) return;
      inner.style.setProperty("--dist", Math.max(0, inner.offsetHeight - view.clientHeight) + "px");
    });
    document.querySelectorAll(".pg--auto").forEach((pg) => {
      pg.style.setProperty("--dist", Math.max(0, pg.offsetHeight - pg.parentElement.clientHeight) + "px");
    });
  };
  document.querySelectorAll(".scr img").forEach((im) => im.addEventListener("load", measure));
  addEventListener("resize", measure);

  const bars = document.querySelector(".show__bars"), nameEl = document.querySelector(".show__name"),
        tagsEl = document.querySelector(".show__tags"), urlEl = document.querySelector(".win__url");
  if (bars && screens.front) {
    const DUR = 7000;
    bars.innerHTML = cases.map((c) => `<button type="button" aria-label="Show ${c.name}"><i></i></button>`).join("");
    bars.style.setProperty("--slide", DUR / 1000 + "s");
    const bEls = [...bars.children];
    let cur = 0, timer = 0;
    const show = (n) => {
      cur = n;
      const next = (n + 1) % cases.length;
      screens.front.forEach((s, i) => s.classList.toggle("is-on", i === n));
      screens.phone.forEach((s, i) => s.classList.toggle("is-on", i === n));
      screens.back.forEach((s, i) => s.classList.toggle("is-on", i === next));
      bEls.forEach((b, i) => { b.classList.toggle("is-done", i < n); b.classList.remove("is-on"); });
      void bEls[n].offsetWidth; bEls[n].classList.add("is-on");
      nameEl.textContent = cases[n].name; tagsEl.textContent = cases[n].tags; urlEl.textContent = cases[n].url;
      clearTimeout(timer);
      if (!REDUCED) timer = setTimeout(() => show((cur + 1) % cases.length), DUR);
    };
    bEls.forEach((b, i) => b.addEventListener("click", () => show(i)));
    measure(); show(0);
    document.fonts && document.fonts.ready.then(measure);
  }

  // depth: layers drift a little with the cursor
  const stage = document.querySelector(".stage");
  if (stage && !REDUCED && matchMedia("(hover: hover)").matches) {
    addEventListener("pointermove", (e) => {
      stage.style.setProperty("--px", (e.clientX / innerWidth - .5).toFixed(3));
      stage.style.setProperty("--py", (e.clientY / innerHeight - .5).toFixed(3));
    }, { passive: true });
  }

  /* ---------- counters ---------- */
  const run = (el) => {
    const end = +el.dataset.count, dur = 1500, t0 = performance.now();
    const fmt = (n) => (end >= 1000 ? n.toLocaleString("en-US") : String(n));
    if (REDUCED) { el.textContent = fmt(end); return; }
    const step = (t) => {
      const k = Math.min(1, (t - t0) / dur);
      el.textContent = fmt(Math.round(end * (1 - Math.pow(1 - k, 4))));
      if (k < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  const io = new IntersectionObserver((es) => es.forEach((e) => {
    if (e.isIntersecting) { setTimeout(() => run(e.target), 700); io.unobserve(e.target); }
  }), { threshold: .3 });
  document.querySelectorAll("[data-count]:not([data-dec])").forEach((c) => io.observe(c));

  /* ---------- services: list drives the preview ---------- */
  const items = [...document.querySelectorAll(".svc__item")], vis = [...document.querySelectorAll(".svc > .svc__stage .vis")];
  const narrowMQ = matchMedia("(max-width: 1000px)");
  /* desktop: one open row drives the big preview. phones: rows open and close on their own,
     each with its own preview inside, so nothing above the tapped row ever moves */
  const setSvc = (n) => {
    items.forEach((it, i) => { it.classList.toggle("is-active", i === n); it.querySelector(".svc__btn").setAttribute("aria-expanded", String(i === n)); });
    vis.forEach((v, i) => v.classList.toggle("is-on", i === n));
    setTimeout(measure, 50);
  };
  items.forEach((it, i) => {
    const b = it.querySelector(".svc__btn");
    b.addEventListener("click", () => {
      if (narrowMQ.matches) { const open = !it.classList.contains("is-active"); it.classList.toggle("is-active", open); b.setAttribute("aria-expanded", String(open)); }
      else setSvc(i);
    });
    if (matchMedia("(hover: hover) and (min-width: 1001px)").matches) it.addEventListener("pointerenter", () => setSvc(i));
  });

  /* ---------- FAQ: smooth open and close ---------- */
  document.querySelectorAll(".acc__item").forEach((d) => {
    const sum = d.querySelector("summary"), body = d.querySelector(".acc__a");
    if (!sum || !body || REDUCED) return;
    let anim = null;
    sum.addEventListener("click", (e) => {
      e.preventDefault();
      if (anim) anim.cancel();
      if (!d.open) {
        d.open = true;
        const h = body.scrollHeight;
        anim = body.animate([{ height: "0px", opacity: 0 }, { height: h + "px", opacity: 1 }], { duration: 480, easing: "cubic-bezier(.16,1,.3,1)" });
        anim.onfinish = () => { anim = null; };
      } else {
        d.classList.add("is-closing");
        const h = body.offsetHeight;
        anim = body.animate([{ height: h + "px", opacity: 1 }, { height: "0px", opacity: 0 }], { duration: 340, easing: "cubic-bezier(.4,0,.2,1)" });
        anim.onfinish = () => { d.open = false; d.classList.remove("is-closing"); anim = null; };
        anim.oncancel = () => d.classList.remove("is-closing");
      }
    });
  });

  /* ---------- pause looping animations while their section is off screen ---------- */
  if ("IntersectionObserver" in window) {
    const offIO = new IntersectionObserver((es) => es.forEach((e) => e.target.classList.toggle("is-off", !e.isIntersecting)), { rootMargin: "120px 0px" });
    document.querySelectorAll("main > section, main > div, .foot").forEach((el) => offIO.observe(el));
  }

  /* ---------- reviews marquee ----------
     Real client reviews, quoted word for word. Sentences naming a person or a platform are cut and marked with "…".
     Fields: ini (avatar letter), who, meta (project type and length), repeat (shows a "Repeat client" chip), text. */
  const reviews = [
    { ini: "V", who: "Client from the United States", meta: "2-week project", text: "Extremely responsive and moved quickly. The website was exactly what I was looking for." },
    { ini: "R", who: "Client from Austria", meta: "4-week project", text: "Excellent work and great communication! I am very happy with the final result. … Communication was very good throughout the whole process. The final website turned out exactly the way I had imagined it." },
    { ini: "S", who: "Client from Saudi Arabia", meta: "6-day project", repeat: true, text: "Great outcome, quick and exactly what I wanted." },
    { ini: "B", who: "Client from Uruguay", meta: "9-day project", text: "The final product was great, but what really stood out was the excellent communication throughout the project as well as the willingness to adjust the product as we were working. Thanks!" },
    { ini: "A", who: "Client from Hong Kong", meta: "13-day project", repeat: true, text: "Very reliable, easy to communicate with, and always responded quickly when we had questions or wanted to make changes. … The final result turned out very well." },
    { ini: "M", who: "Client from the United States", meta: "3-week project", repeat: true, text: "… an amazing job with our website. … It took very few rounds of feedback to get exactly what we were looking for." },
    { ini: "P", who: "Client from Zimbabwe", meta: "7-day project", repeat: true, text: "We going to work on many more projects. … the great work, great turn around time and highest quality work." },
    { ini: "S", who: "Client from Iceland", meta: "7-day project", text: "Very quick response time, and professional answers. … will 100% come back." },
    { ini: "B", who: "Client from the United States", meta: "2-week project", repeat: true, text: "Efficient, polite, and understanding. … Understood the vision and executed our project perfectly." },
    { ini: "J", who: "Client from the United States", meta: "3-week project", repeat: true, text: "There's few people that take pride in their work … I really love my new website." },
    { ini: "M", who: "Client from Canada", meta: "4-day project", repeat: true, text: "Listened carefully, moved fast, and delivered a beautiful design that truly reflects our brand. Highly recommend!" },
    { ini: "S", who: "Client from Saudi Arabia", meta: "1-day project", repeat: true, text: "Very professional and achieved exactly as promised." },
    { ini: "P", who: "Client from Zimbabwe", meta: "3-week project", repeat: true, text: "Great experience 10/10" },
  ];
  const initials = (n) => n.split(/\s+/).map((w) => w[0]).slice(0, 2).join("").toUpperCase();
  const esc = (t) => t.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const rcard = (r) => `<figure class="rcard"><div class="rcard__top"><span class="rcard__ava">${esc(r.ini)}</span>
      <span class="rcard__who"><b>${esc(r.who)}</b><span>${esc(r.meta)}</span></span>${r.repeat ? '<span class="rcard__src">Repeat client</span>' : ""}</div>
      <div class="rcard__stars" role="img" aria-label="5 out of 5"><i></i><i></i><i></i><i></i><i></i></div><p>${esc(r.text)}</p></figure>`;
  const rcols = [...document.querySelectorAll(".rv__col")];
  if (rcols.length) {
    const narrow = matchMedia("(max-width: 640px)").matches, mid = matchMedia("(max-width: 1000px)").matches;
    const n = narrow ? 1 : mid ? 2 : 3;
    rcols.forEach((col, c) => {
      const list = reviews.filter((_, i) => i % n === c);
      if (!list.length) return;
      const html = list.map(rcard).join("");
      col.innerHTML = `<div class="rv__track" style="--dur:${30 + c * 6}s"><div style="display:contents">${html}</div><div aria-hidden="true" style="display:contents">${html}</div></div>`;
    });
  }

  /* ---------- reveal on scroll ---------- */
  const rio = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); rio.unobserve(e.target); } }), { threshold: 0, rootMargin: "0px 0px -10% 0px" });
  document.querySelectorAll("[data-reveal]").forEach((el) => rio.observe(el));
  /* safety net for fast flicks: anything already scrolled past is shown */
  let revT = 0;
  const sweep = () => { revT = 0; document.querySelectorAll("[data-reveal]:not(.in)").forEach((el) => { if (el.getBoundingClientRect().top < innerHeight * .9) { el.classList.add("in"); rio.unobserve(el); } }); };
  addEventListener("scroll", () => { if (!revT) revT = setTimeout(sweep, 200); }, { passive: true });

  /* ---------- footer clock (studio time) ---------- */
  const clock = document.querySelector(".clock");
  if (clock) {
    const tick = () => { clock.textContent = new Intl.DateTimeFormat("en-GB", { hour: "2-digit", minute: "2-digit", timeZone: "Europe/Madrid" }).format(new Date()); };
    tick(); setInterval(tick, 30000);
  }
  const yr = document.querySelector(".year"); if (yr) yr.textContent = new Date().getFullYear();

  /* ---------- brief form ----------
     FORM_ENDPOINT: paste a form service URL here to receive briefs straight to your inbox
     (e.g. Web3Forms "https://api.web3forms.com/submit" + FORM_KEY, or a Formspree URL).
     While it's empty, submitting opens the visitor's email app with the brief already written. */
  const FORM_ENDPOINT = "https://api.web3forms.com/submit";
  const FORM_KEY = "7235f83a-d867-455b-9959-4e51983e0b64";
  const TO_EMAIL = "hello@sorvel.agency";
  const form = document.getElementById("brief");
  if (form) {
    const msg = form.querySelector(".brief__msg"), done = form.querySelector(".brief__done");
    const fieldOf = (el) => el.closest(".field");
    const f = (n) => form.elements.namedItem(n);
    form.addEventListener("input", (e) => { const fl = e.target.closest(".field"); if (fl) fl.classList.remove("is-bad"); });

    /* two-step brief: contact details first, project details second */
    const okEmail = (v) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim());
    const rows = [...form.children];
    const firstRow = form.querySelector(":scope > .brief__row"), company = f("company") && f("company").closest(".field");
    let goStep = () => {};
    if (firstRow && company) {
      const head = document.createElement("div");
      head.className = "bsteps";
      head.innerHTML = '<p class="bsteps__lbl">Step <b>1</b> of 2</p><div class="bsteps__bar" aria-hidden="true"><i class="is-on"></i><i></i></div><h3 class="bsteps__title">Your details</h3>';
      const s1 = document.createElement("div"); s1.className = "bstep bstep--1";
      const s2 = document.createElement("div"); s2.className = "bstep bstep--2"; s2.hidden = true;
      const keep = (el) => el.matches(".picked, .brief__msg, .brief__done, input[type=hidden], script, .hp");
      const picked = form.querySelector(":scope > .picked");
      (picked || firstRow).before(head);
      if (picked) head.after(picked);
      firstRow.before(s1);
      s1.append(firstRow, company);
      const cont = document.createElement("div"); cont.className = "bstep__go";
      cont.innerHTML = '<button class="btn btn--primary btn--lg bstep__next" type="button"><span class="btn__roll"><span data-text="Continue">Continue</span></span><span class="btn__arrow" aria-hidden="true"><svg viewBox="0 0 20 20"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg><svg viewBox="0 0 20 20"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg></span></button>' +
        '<p class="bstep__note">Two short steps, about a minute. Your details stay private. <a href="' + (location.pathname.includes("/work/") || location.pathname.includes("/services/") ? "../" : "") + 'privacy.html">Privacy policy</a></p>';
      s1.append(cont);
      s1.after(s2);
      [...form.children].filter((el) => el !== head && el !== s1 && el !== s2 && !keep(el)).forEach((el) => s2.append(el));
      const foot = s2.querySelector(".brief__foot");
      const back = document.createElement("button"); back.type = "button"; back.className = "bstep__back"; back.innerHTML = '<span aria-hidden="true">←</span> Back';
      if (foot) foot.prepend(back);
      const lbl = head.querySelector("b"), bars = head.querySelectorAll(".bsteps__bar i"), title = head.querySelector(".bsteps__title");
      let partialSent = false;
      goStep = (n, focus) => {
        s1.hidden = n !== 1; s2.hidden = n !== 2;
        lbl.textContent = n; bars[1].classList.toggle("is-on", n === 2);
        title.textContent = n === 1 ? "Your details" : "Your project";
        form.dataset.step = n;
        if (focus) {
          const top = form.getBoundingClientRect().top;
          if (top < 60 || top > 220) scrollTo({ top: top + scrollY - 100, behavior: "smooth" });
          const first = n === 1 ? f("name") : s2.querySelector("input, select, textarea");
          first && first.focus({ preventScroll: true });
        }
      };
      const next = () => {
        msg.textContent = "";
        const bad = [];
        if (!f("name").value.trim()) bad.push(f("name"));
        if (!okEmail(f("email").value)) bad.push(f("email"));
        bad.forEach((el) => fieldOf(el).classList.add("is-bad"));
        if (bad.length) { msg.textContent = "Please add your name and a valid email."; bad[0].focus(); return; }
        if (!partialSent) track("brief_start");
        if (FORM_ENDPOINT && !partialSent) {
          partialSent = true;
          fetch(FORM_ENDPOINT, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" },
            body: JSON.stringify({ access_key: FORM_KEY || undefined, subject: "Started a brief: " + f("name").value.trim(), from_name: "Sorvel website",
              name: f("name").value.trim(), email: f("email").value.trim(), company: f("company").value.trim(), plan: (f("plan") && f("plan").value) || "", note: "Step 1 only so far" }) }).catch(() => {});
        }
        goStep(2, true);
      };
      cont.querySelector(".bstep__next").addEventListener("click", next);
      s1.addEventListener("keydown", (e) => { if (e.key === "Enter" && e.target.tagName === "INPUT") { e.preventDefault(); next(); } });
      back.addEventListener("click", () => goStep(1, true));
      form.addEventListener("reset", () => setTimeout(() => goStep(1), 0));
      goStep(1);
    }
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      msg.textContent = "";
      if (f("botcheck").value) return;
      const bad = [];
      if (!f("name").value.trim()) bad.push(f("name"));
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f("email").value.trim())) bad.push(f("email"));
      if (f("details").value.trim().length < 10) bad.push(f("details"));
      bad.forEach((el) => fieldOf(el).classList.add("is-bad"));
      if (bad.length) { if (bad[0] !== f("details")) goStep(1); msg.textContent = "Please add a few words about the project."; bad[0].focus(); return; }

      const needs = [...form.querySelectorAll('input[name="need"]:checked')].map((i) => i.value).join(", ") || "Not specified";
      const timeline = form.querySelector('input[name="timeline"]:checked')?.value || "Not specified";
      const opt = (n) => (f(n) && f(n).value) || "";
      const data = { name: f("name").value.trim(), email: f("email").value.trim(), company: f("company").value.trim(), plan: opt("plan"), needs, timeline, platform: opt("platform"), budget: opt("budget"), details: f("details").value.trim() };
      const showDone = () => { done.hidden = false; form.reset(); form.querySelectorAll(".is-bad").forEach((x) => x.classList.remove("is-bad")); };

      if (!FORM_ENDPOINT) {
        const body = `Name: ${data.name}\nEmail: ${data.email}\nCompany: ${data.company || "-"}\nPicked on the site: ${data.plan || "-"}\nNeeds: ${data.needs}\nPlatform: ${data.platform || "-"}\nBudget: ${data.budget || "-"}\nStart: ${data.timeline}\n\n${data.details}`;
        location.href = `mailto:${TO_EMAIL}?subject=${encodeURIComponent((data.plan ? "[" + data.plan.split(" (")[0] + "] " : "") + "New project brief from " + data.name)}&body=${encodeURIComponent(body)}`;
        setTimeout(showDone, 600);
        return;
      }
      form.classList.add("is-sending");
      try {
        const res = await fetch(FORM_ENDPOINT, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify({ access_key: FORM_KEY || undefined, subject: (data.plan ? "[" + data.plan.split(" (")[0] + "] " : "") + "New project brief from " + data.name, from_name: "Sorvel website", ...data }) });
        if (!res.ok) throw new Error(res.status);
        track("brief");
        showDone();
      } catch (err) {
        msg.innerHTML = `Something went wrong. Please email <a href="mailto:${TO_EMAIL}">${TO_EMAIL}</a> or write on Telegram.`;
      } finally { form.classList.remove("is-sending"); }
    });
  }

  /* ---------- mobile menu ---------- */
  const burger = document.querySelector(".nav__burger"), mnav = document.getElementById("mnav");
  if (burger && mnav) {
    const root = document.documentElement;
    const isOpen = () => root.classList.contains("menu-open");
    const set = (open) => {
      root.classList.toggle("menu-open", open);
      burger.setAttribute("aria-expanded", String(open));
      burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      if (open) mnav.removeAttribute("inert"); else mnav.setAttribute("inert", "");
    };
    burger.addEventListener("click", () => set(!isOpen()));
    mnav.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => set(false)));
    addEventListener("keydown", (e) => { if (e.key === "Escape" && isOpen()) { set(false); burger.focus(); } });
    matchMedia("(min-width: 761px)").addEventListener("change", (e) => { if (e.matches) set(false); });
    addEventListener("pageshow", (e) => { if (e.persisted) set(false); });
    const acc = mnav.querySelector(".mnav__acc");
    acc && acc.addEventListener("click", () => {
      const open = acc.getAttribute("aria-expanded") !== "true";
      acc.setAttribute("aria-expanded", String(open));
      acc.closest("li").classList.toggle("is-open", open);
    });
  }
})();
