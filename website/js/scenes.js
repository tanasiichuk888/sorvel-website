// Inner-page hero illustrations: play when visible, loop, type text, count numbers, rotate decks.
(function () {
  const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const FINE = matchMedia("(hover: hover) and (pointer: fine)").matches;
  const fmt = (v, dec) => dec ? v.toFixed(dec) : Math.round(v).toLocaleString("en-US");

  document.querySelectorAll(".sx[data-scene]").forEach((el) => {
    const kind = el.dataset.scene, loop = +el.dataset.loop || 0;
    let timers = [], ivals = [], inView = false, raf = 0;
    const later = (fn, ms) => timers.push(setTimeout(fn, ms));
    const every = (fn, ms) => ivals.push(setInterval(fn, ms));
    const stop = () => { timers.forEach(clearTimeout); ivals.forEach(clearInterval); timers = []; ivals = []; cancelAnimationFrame(raf); };

    const count = (n, delay, dur) => {
      const to = parseFloat(n.dataset.to), dec = +n.dataset.dec || 0;
      n.textContent = fmt(REDUCED ? to : 0, dec); if (REDUCED) return;
      later(() => { const t0 = performance.now(); const tick = (t) => { const k = Math.min(1, (t - t0) / dur); n.textContent = fmt(to * (1 - Math.pow(1 - k, 3)), dec); if (k < 1) requestAnimationFrame(tick); }; requestAnimationFrame(tick); }, delay);
    };
    const type = (n, delay, speed) => {
      const txt = n.dataset.text; n.textContent = REDUCED ? txt : " "; if (REDUCED) return;
      later(() => { let i = 0; n.classList.add("caret"); n.textContent = "";
        const id = setInterval(() => { n.textContent = txt.slice(0, ++i); if (i >= txt.length) { clearInterval(id); later(() => n.classList.remove("caret"), 500); } }, speed);
        ivals.push(id); }, delay);
    };

    const SCENES = {
      flow() { type(el.querySelector(".fl-type"), 700, 28); },
      inbox() {
        type(el.querySelector(".ib-type"), 700, 26);
        el.querySelectorAll("[data-to]").forEach((n) => count(n, 7200, 1400));
      },
      rate() {
        el.querySelectorAll(".rt-score [data-to]").forEach((n) => count(n, 300, 1300));
        const qs = [...el.querySelectorAll(".rt-q")]; let order = qs.map((_, i) => i);
        const lay = () => order.forEach((q, k) => { qs[q].style.setProperty("--k", Math.min(k, 3)); qs[q].classList.remove("is-out"); });
        lay();
        if (!REDUCED) every(() => {
          const top = qs[order[0]]; top.classList.add("is-out");
          setTimeout(() => { order.push(order.shift()); lay(); }, 650);
        }, 3200);
      },
      fan() {
        const cards = [...el.querySelectorAll(".fn-card")], dots = [...el.querySelectorAll(".fn-dots i")];
        let order = cards.map((_, i) => i);
        const lay = () => order.forEach((c, k) => { cards[c].style.setProperty("--k", k); cards[c].classList.toggle("is-front", k === 0); dots[c].classList.toggle("is-on", k === 0); });
        lay();
        if (!REDUCED) every(() => {
          const top = cards[order[0]]; top.classList.add("is-leaving");
          setTimeout(() => { order.push(order.shift()); top.classList.remove("is-leaving"); top.style.transition = "none"; lay(); void top.offsetWidth; top.style.transition = ""; }, 700);
        }, 2800);
        if (FINE && !REDUCED) {
          el.addEventListener("pointermove", (e) => { const r = el.getBoundingClientRect();
            el.style.setProperty("--ry", ((e.clientX - r.left) / r.width - .5) * 16 + "deg");
            el.style.setProperty("--rx", -((e.clientY - r.top) / r.height - .5) * 12 + "deg"); });
          el.addEventListener("pointerleave", () => { el.style.setProperty("--rx", "0deg"); el.style.setProperty("--ry", "0deg"); });
        }
      },
      globe() { globe(el); },
    };

    const play = () => {
      stop();
      el.classList.remove("run"); void el.offsetWidth; el.classList.add("run");
      SCENES[kind] && SCENES[kind]();
      if (loop && !REDUCED) {
        later(() => { el.style.transition = "opacity .4s"; el.style.opacity = ".0"; }, loop - 400);
        later(() => { el.style.opacity = ""; if (inView) play(); }, loop);
      }
    };
    new IntersectionObserver(([e]) => {
      if (e.isIntersecting && !inView) { inView = true; play(); }
      else if (!e.isIntersecting && inView) { inView = false; stop(); el.style.opacity = ""; }
    }, { threshold: .2 }).observe(el);

    /* rotating dotted globe: real continents and borders, live projects firing to countries all over the world */
    function globe(root) {
      const cv = root.querySelector("canvas"), ctx = cv.getContext("2d"), G = window.GEO;
      if (!G) return;
      const LITE = matchMedia("(hover: none), (max-width: 760px)").matches;
      const DPR = Math.min(2, devicePixelRatio || 1), D2R = Math.PI / 180;
      let lastDraw = 0, started = false;
      const v3 = (lat, lon) => { const a = lat * D2R, b = lon * D2R; return [Math.cos(a) * Math.sin(b), Math.sin(a), Math.cos(a) * Math.cos(b)]; };
      const land = []; for (let i = 0; i < G.p.length; i += LITE ? 6 : 3) land.push([v3(G.p[i] / 10, G.p[i + 1] / 10), G.p[i + 2]]);
      const CO = G.c.map(([n, la, lo, rings, area]) => ({ n, v: v3(la, lo), rings: rings.map((r) => r.map(([a, b]) => v3(a, b))), area, home: n === "Spain" }));
      const HOME = v3(39.5, -0.6), PICK = CO.filter((c) => c.area > 3 && !c.home);
      const byName = (n) => CO.find((c) => c.n === n), USA = byName("United States");
      const PRIO = ["United States", "United Kingdom", "Canada", "Germany", "Australia", "United Arab Emirates", "Brazil", "France", "Netherlands", "Saudi Arabia", "Mexico", "Japan", "Italy", "Sweden", "India", "South Africa"].map(byName).filter(Boolean);
      const TYPES = ["Website", "Landing page", "Product UI", "Brand identity", "Webflow build", "Migration"];
      const feed = root.querySelector(".gl-feed"), feedT = feed && feed.querySelector("b"), feedS = feed && feed.querySelector("small");
      let fires = 0, pi = 0;
      let rot = 0.2, tilt = 0.42, ph = -.42, base = .35, userTilt = 0, vel = 0.0022, drag = null, hover = 0, live = [], nextFire = 0, last = performance.now();
      const autoTilt = () => { const a = Math.atan2(Math.sin(rot), Math.cos(rot)), k = Math.max(0, Math.min(1, 1 - Math.abs(a - 2.3) / 1.1)); return .42 - .5 * k * k * (3 - 2 * k); };
      const resize = () => { const r = cv.getBoundingClientRect(), w = Math.round(r.width * DPR), h = Math.round(r.height * DPR);
        if (!w || (w === cv.width && h === cv.height)) return;   // phones fire resize while scrolling; resetting the canvas would blank it
        cv.width = w; cv.height = h; if (started && !raf) start(); };
      resize(); addEventListener("resize", resize);
      cv.style.cursor = "grab"; cv.style.touchAction = "pan-y";
      cv.addEventListener("pointerdown", (e) => { drag = { x: e.clientX, y: e.clientY, r: rot, t: tilt }; cv.setPointerCapture(e.pointerId); cv.style.cursor = "grabbing"; });
      cv.addEventListener("pointermove", (e) => { if (!drag) return; rot = drag.r + (e.clientX - drag.x) * .008; tilt = Math.max(-.6, Math.min(1.1, drag.t + (e.clientY - drag.y) * .006)); });
      const end = () => { if (drag) { userTilt = tilt - autoTilt(); } drag = null; cv.style.cursor = "grab"; }; cv.addEventListener("pointerup", end); cv.addEventListener("pointercancel", end);
      root.addEventListener("pointerenter", () => hover = 1); root.addEventListener("pointerleave", () => hover = 0);
      const P = (p) => { const c = Math.cos(rot), s = Math.sin(rot); const x = p[0] * c - p[2] * s, z = p[0] * s + p[2] * c, y = p[1];
        const ct = Math.cos(tilt), st = Math.sin(tilt); return [x, y * ct - z * st, y * st + z * ct]; };
      const slerp = (a, b, t, lift) => { const d = Math.acos(Math.max(-1, Math.min(1, a[0] * b[0] + a[1] * b[1] + a[2] * b[2]))), s = Math.sin(d) || 1;
        const k1 = Math.sin((1 - t) * d) / s, k2 = Math.sin(t * d) / s, h = 1 + Math.sin(Math.PI * t) * lift * d;
        return [(a[0] * k1 + b[0] * k2) * h, (a[1] * k1 + b[1] * k2) * h, (a[2] * k1 + b[2] * k2) * h]; };
      const pill = (x, y, txt, green) => { const w = ctx.measureText(txt).width + 16 * DPR, h = 20 * DPR;
        ctx.fillStyle = "rgba(14,15,20,.9)"; ctx.strokeStyle = green ? "rgba(61,220,132,.5)" : "rgba(124,155,255,.5)"; ctx.lineWidth = DPR;
        ctx.beginPath(); ctx.roundRect(x, y - h / 2, w, h, 6 * DPR); ctx.fill(); ctx.stroke(); ctx.fillStyle = "#F2EFEA"; ctx.textBaseline = "middle"; ctx.fillText(txt, x + 8 * DPR, y + .5 * DPR); };
      const ring = (r, close) => { ctx.beginPath(); let vis = 0, f = true; r.forEach((p) => { const q = P(p); if (q[2] > 0) vis++; const [X, Y] = S(q); f ? ctx.moveTo(X, Y) : ctx.lineTo(X, Y); f = false; }); if (close) ctx.closePath(); return vis / r.length; };
      let W, H, R, cx, cy; const S = (q) => [cx + q[0] * R, cy - q[1] * R];
      const fire = (now) => {
        const ok = (c) => c && P(c.v)[2] > .25 && !live.some((l) => l.c === c && !l.keep);
        let c = null; fires++;
        if (fires % 3 === 1 && ok(USA)) c = USA;
        else if (fires % 2 === 0) { for (let k = 0; k < PRIO.length && !c; k++) { const q = PRIO[(pi + k) % PRIO.length]; if (ok(q)) { c = q; pi = (pi + k + 1) % PRIO.length; } } }
        if (!c) { const vis = PICK.filter(ok); if (!vis.length) return; c = vis[Math.floor(Math.random() * vis.length)]; }
        live.push({ c, t: now });
        if (feed) { feed.classList.remove("is-new"); void feed.offsetWidth; feed.classList.add("is-new");
          feedT.textContent = c.n; feedS.textContent = "New brief · " + TYPES[Math.floor(Math.random() * TYPES.length)]; }
      };
      const draw = (now) => {
        if (!onScreen && !drag) { raf = 0; return; }
        if (LITE && now - lastDraw < 40 && !drag) { raf = requestAnimationFrame(draw); return; }
        lastDraw = now;
        const dt = Math.min(50, now - last); last = now;
        W = cv.width; H = cv.height; R = Math.min(W, H) * .265; cx = W / 2; cy = H * .5;
        ctx.clearRect(0, 0, W, H);
        let g = ctx.createRadialGradient(cx, cy, R * .9, cx, cy, R * 1.45); g.addColorStop(0, "rgba(59,107,255,.35)"); g.addColorStop(1, "rgba(59,107,255,0)");
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(cx, cy, R * 1.45, 0, 6.283); ctx.fill();
        const orb = (front) => { const a0 = now / 9000, rx = R * 1.32, ry = R * .34, ang = -.32;
          ctx.save(); ctx.translate(cx, cy); ctx.rotate(ang);
          ctx.beginPath(); ctx.ellipse(0, 0, rx, ry, 0, front ? 0 : Math.PI, front ? Math.PI : Math.PI * 2);
          ctx.strokeStyle = front ? "rgba(124,155,255,.45)" : "rgba(124,155,255,.18)"; ctx.lineWidth = DPR; ctx.setLineDash([2 * DPR, 6 * DPR]); ctx.stroke(); ctx.setLineDash([]);
          for (let k = 0; k < 3; k++) { const t = (a0 + k / 3) % 1 * Math.PI * 2, inFront = Math.sin(t) > 0; if (inFront !== front) continue;
            const X = Math.cos(t) * rx, Y = Math.sin(t) * ry, sg = ctx.createRadialGradient(X, Y, 0, X, Y, 10 * DPR);
            sg.addColorStop(0, k === 0 ? "rgba(110,240,170,1)" : "rgba(200,215,255,1)"); sg.addColorStop(1, "rgba(91,131,255,0)");
            ctx.fillStyle = sg; ctx.beginPath(); ctx.arc(X, Y, 10 * DPR, 0, 6.283); ctx.fill();
            ctx.fillStyle = "#fff"; ctx.beginPath(); ctx.arc(X, Y, 2.2 * DPR, 0, 6.283); ctx.fill(); }
          ctx.restore(); };
        orb(false);
        g = ctx.createRadialGradient(cx - R * .35, cy - R * .4, R * .1, cx, cy, R); g.addColorStop(0, "#1A2552"); g.addColorStop(.7, "#0D1330"); g.addColorStop(1, "#080B1C");
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(cx, cy, R, 0, 6.283); ctx.fill();
        // land dots
        for (const [p, code] of land) { const q = P(p); const z = q[2]; const [X, Y] = S(q);
          if (z < 0) { if (z > -.5) { ctx.fillStyle = `rgba(124,155,255,${.05 + z * .08})`; ctx.fillRect(X, Y, DPR, DPR); } continue; }
          ctx.fillStyle = code ? `rgba(110,240,170,${.6 + z * .4})` : `rgba(170,192,255,${.25 + z * .6})`;
          if (LITE) { const d = (1.2 + z * 1.3) * DPR; ctx.fillRect(X - d / 2, Y - d / 2, d, d); }
          else { ctx.beginPath(); ctx.arc(X, Y, (.6 + z * .65) * DPR, 0, 6.283); ctx.fill(); } }
        // country borders (all) + live highlights
        ctx.lineWidth = .7 * DPR;
        if (LITE) { // phones: every country outline in one path, one stroke (cheap)
          ctx.beginPath();
          CO.forEach((c) => { if (c.home) return; c.rings.forEach((r) => { const qs = r.map(P); let vis = 0; for (const q of qs) if (q[2] > 0) vis++; if (vis / qs.length < .95) return;
            qs.forEach((q, i) => { const [X, Y] = S(q); i ? ctx.lineTo(X, Y) : ctx.moveTo(X, Y); }); ctx.closePath(); }); });
          ctx.strokeStyle = "rgba(170,192,255,.55)"; ctx.lineWidth = .8 * DPR; ctx.stroke(); ctx.lineWidth = .7 * DPR;
        }
        CO.forEach((c) => { if (LITE && !c.home) return; c.rings.forEach((r) => { if (ring(r, true) < .95) return;
          if (c.home) { ctx.fillStyle = "rgba(61,220,132,.22)"; ctx.fill(); ctx.strokeStyle = "rgba(61,220,132,.9)"; ctx.lineWidth = 1.1 * DPR; ctx.stroke(); ctx.lineWidth = .7 * DPR; }
          else { ctx.strokeStyle = "rgba(170,192,255,.6)"; ctx.lineWidth = .9 * DPR; ctx.stroke(); ctx.lineWidth = .7 * DPR; } }); });
        live.forEach((l) => { const age = (now - l.t) / 1000, a = age < .9 ? 0 : Math.min(1, (age - .9) * 3) * (age > 3.2 ? Math.max(0, 1 - (age - 3.2) * 1.5) : 1); if (!a) return;
          l.c.rings.forEach((r) => { if (ring(r, true) < .9) return; ctx.fillStyle = `rgba(59,107,255,${.42 * a})`; ctx.fill(); ctx.strokeStyle = `rgba(150,175,255,${a})`; ctx.lineWidth = 1.2 * DPR;
            ctx.shadowColor = "rgba(59,107,255,.9)"; ctx.shadowBlur = 10 * DPR; ctx.stroke(); ctx.shadowBlur = 0; }); });
        g = ctx.createRadialGradient(cx, cy, R * .82, cx, cy, R); g.addColorStop(0, "rgba(124,155,255,0)"); g.addColorStop(1, "rgba(124,155,255,.28)");
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(cx, cy, R, 0, 6.283); ctx.fill();
        // live arcs from the studio
        const labels = [];
        if (USA && !live.some((l) => l.c === USA)) live.push({ c: USA, t: now - 1500, keep: true });
        live.forEach((l) => { const age = (now - l.t) / 1000, k = Math.min(1, age / .9), fade = age > 3.2 ? Math.max(0, 1 - (age - 3.2) * 1.5) : 1;
          ctx.beginPath(); let f = true; for (let s = 0; s <= 48; s++) { const q = P(slerp(HOME, l.c.v, s / 48 * k, .22)); if (q[2] < -.12) { f = true; continue; } const [X, Y] = S(q); f ? ctx.moveTo(X, Y) : ctx.lineTo(X, Y); f = false; }
          ctx.strokeStyle = `rgba(110,145,255,${.75 * fade})`; ctx.lineWidth = 1.4 * DPR; ctx.shadowColor = "rgba(59,107,255,.9)"; ctx.shadowBlur = 8 * DPR; ctx.stroke(); ctx.shadowBlur = 0;
          const hq = P(slerp(HOME, l.c.v, k, .22)); if (hq[2] > -.12 && k < 1) { const [X, Y] = S(hq); const cg = ctx.createRadialGradient(X, Y, 0, X, Y, 8 * DPR); cg.addColorStop(0, "#fff"); cg.addColorStop(1, "rgba(91,131,255,0)"); ctx.fillStyle = cg; ctx.beginPath(); ctx.arc(X, Y, 8 * DPR, 0, 6.283); ctx.fill(); }
          if (l.keep) { const u = (now / 2400) % 1, cq = P(slerp(HOME, l.c.v, u, .22)); if (cq[2] > -.12) { const [X, Y] = S(cq); const cg = ctx.createRadialGradient(X, Y, 0, X, Y, 9 * DPR); cg.addColorStop(0, "#fff"); cg.addColorStop(1, "rgba(91,131,255,0)"); ctx.fillStyle = cg; ctx.beginPath(); ctx.arc(X, Y, 9 * DPR, 0, 6.283); ctx.fill(); } }
          if (k < 1) return; const q = P(l.c.v); if (q[2] < .05) return; const [X, Y] = S(q), pu = l.keep ? (now / 1300) % 1 : Math.min(1, (age - .9) / 1.2);
          ctx.beginPath(); ctx.arc(X, Y, (3 + pu * 18) * DPR, 0, 6.283); ctx.strokeStyle = `rgba(170,192,255,${(1 - pu) * fade})`; ctx.lineWidth = 1.2 * DPR; ctx.stroke();
          ctx.beginPath(); ctx.arc(X, Y, 3 * DPR, 0, 6.283); ctx.fillStyle = `rgba(255,255,255,${fade})`; ctx.fill();
          labels.push({ x: X + 8 * DPR, y: Y - 12 * DPR, txt: l.c.n, a: Math.min(1, (age - .9) * 4) * fade, z: l.c === USA ? 5 : q[2] }); });
        live = live.filter((l) => !l.keep && now - l.t < 4000);
        const hq = P(HOME); if (hq[2] > 0) { const [X, Y] = S(hq), pu = (now / 1250) % 1;
          ctx.beginPath(); ctx.arc(X, Y, (5 + pu * 16) * DPR, 0, 6.283); ctx.strokeStyle = `rgba(61,220,132,${(1 - pu) * .9})`; ctx.lineWidth = 1.5 * DPR; ctx.stroke();
          ctx.beginPath(); ctx.arc(X, Y, 4.5 * DPR, 0, 6.283); ctx.fillStyle = "#3DDC84"; ctx.fill();
          if (hq[2] > .3) labels.unshift({ x: X + 10 * DPR, y: Y + 14 * DPR, txt: "Studio · Spain", a: Math.min(1, (hq[2] - .3) * 4), z: 9, g: true }); }
        orb(true);
        const placed = []; ctx.font = `500 ${11 * DPR}px Inter, system-ui, sans-serif`;
        labels.sort((a, b) => b.z - a.z).forEach((l) => { const w = ctx.measureText(l.txt).width + 16 * DPR, h = 20 * DPR, r = [l.x, l.y - h / 2, l.x + w, l.y + h / 2];
          if (placed.some((p) => r[0] < p[2] + 4 && r[2] > p[0] - 4 && r[1] < p[3] + 3 && r[3] > p[1] - 3)) return;
          placed.push(r); ctx.globalAlpha = l.a; pill(l.x, l.y, l.txt, l.g); ctx.globalAlpha = 1; });
        if (!REDUCED && now > nextFire) { fire(now); nextFire = now + 650 + Math.random() * 500; }
        if (!drag && !REDUCED) { rot -= .00011 * (hover ? .45 : 1) * dt; userTilt *= .995; tilt = autoTilt() + userTilt; }
        if ((!REDUCED || drag) && onScreen) raf = requestAnimationFrame(draw); else raf = 0;
      };
      let onScreen = true;
      const start = () => { cancelAnimationFrame(raf); raf = requestAnimationFrame(draw); };
      new IntersectionObserver(([e]) => { onScreen = e.isIntersecting; if (onScreen && started) { last = performance.now(); start(); } }, { rootMargin: "80px 0px" }).observe(root);
      const begin = () => { started = true; start(); };
      if (LITE && document.readyState !== "complete") addEventListener("load", () => setTimeout(begin, 400), { once: true });
      else begin();
    }
  });
})();
