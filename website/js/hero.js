// Home hero: a site builds itself — wireframe → design → build → live, cycling through real case studies.
(function () {
  const root = document.querySelector(".bld"); if (!root) return;
  const stage = root.querySelector(".bld__stage");
  const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const CASES = [
    { name: "Valhalla Capital", tags: "Private credit · Figma + Webflow", dir: "valhalla", url: "valhallacap.com", plat: "Webflow", slug: "valhalla-capital" }, 
    { name: "AWS Wrap", tags: "Automotive · Design + WordPress", dir: "awswrap", url: "awswrap.com", plat: "WordPress", slug: "awswrap" },
    { name: "Arlowe Baxter", tags: "Property tech · Figma + Webflow", dir: "arlowe-baxter", url: "arlowebaxter.com", plat: "Webflow", slug: "arlowe-baxter" },
    { name: "Salinas Defense", tags: "Legal · Landing page + Webflow", dir: "salinas", url: "salinasdefense.com", plat: "Webflow", slug: "salinas-defense" },
  ];
  // preload screenshots
  CASES.forEach((c) => { new Image().src = `img/work/${c.dir}/hero.webp`; new Image().src = `img/work/${c.dir}/m-hero.webp`; });

  const $ = (s) => root.querySelector(s);
  const shot = $(".bld__shot"), shotImg = $(".bld__shot img"), phoneImg = $(".bld__pv img");
  const urlText = $(".bld__urltext"), modeText = $(".bld__mode span"), plat = $(".bld__plat");
  const toastT = $(".bld__toastt"), toastS = $(".bld__toasts");
  const nameEl = $(".bld__name"), tagsEl = $(".bld__tags"), link = $(".bld__link");
  const steps = [...root.querySelectorAll(".bld__steps li")];
  const curA = $(".bld__cur--a"), curB = $(".bld__cur--b");
  const gauges = [...root.querySelectorAll(".bld__gauge")];

  const move = (cur, x, y, click) => {
    cur.style.left = x + "%"; cur.style.top = y + "%";
    if (click) setTimeout(() => { cur.classList.remove("is-click"); void cur.offsetWidth; cur.classList.add("is-click"); }, 1050);
  };
  const DUR = { wire: 2000, design: 2400, shot: 1900, build: 2400, live: 3200, out: 600 };
  const MODE = { wire: "Wireframe", design: "Design", shot: "Design", build: "Build", live: "Live" };
  const STEP = { wire: 0, design: 1, shot: 1, build: 2, live: 3 };

  const setStep = (phase) => {
    const n = STEP[phase];
    if (n === undefined) return;
    steps.forEach((s, i) => {
      const was = s.classList.contains("is-on");
      s.classList.toggle("is-done", i < n);
      if (i === n && !was) {
        const d = phase === "design" ? DUR.design + DUR.shot : DUR[phase];
        s.style.setProperty("--dur", d + "ms"); s.classList.remove("is-on"); void s.offsetWidth; s.classList.add("is-on");
      } else if (i !== n) s.classList.remove("is-on");
    });
  };
  const runGauges = () => gauges.forEach((g) => {
    const to = +g.dataset.to, b = g.querySelector("b"), arc = g.querySelector(".g"), t0 = performance.now();
    arc.style.strokeDashoffset = 97.4 * (1 - to / 100);
    const tick = (t) => { const k = Math.min(1, (t - t0) / 1300); b.textContent = Math.round(to * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(tick); };
    requestAnimationFrame(tick);
  });
  const resetGauges = () => gauges.forEach((g) => { g.querySelector("b").textContent = "0"; g.querySelector(".g").style.strokeDashoffset = 97.4; });

  let idx = 0, timer = 0, visible = true;
  const phase = (p) => { stage.dataset.phase = p; if (MODE[p]) modeText.textContent = MODE[p]; setStep(p); };

  const SEQ = [
    ["wire", (c) => {
      shot.style.transition = "none"; void shot.offsetWidth; shot.style.transition = "";
      shotImg.src = `img/work/${c.dir}/hero.webp`; phoneImg.src = `img/work/${c.dir}/m-hero.webp`;
      urlText.textContent = "Untitled · Wireframe"; plat.textContent = c.plat; resetGauges();
      toastT.textContent = c.plat === "Production" ? "Deployed to production" : "Published to " + c.plat; toastS.textContent = c.url + " · just now";
      nameEl.textContent = c.name; tagsEl.textContent = c.tags; link.href = `work/${c.slug}.html`;
      move(curA, 30, 30); setTimeout(() => move(curA, 52, 46), 700); setTimeout(() => move(curA, 66, 34, true), 1300);
      move(curB, 92, 92);
    }],
    ["design", (c) => {
      urlText.textContent = "Figma · " + c.name + " / Hero";
      move(curA, 30, 42, true); setTimeout(() => move(curA, 88, 34, true), 1200);
    }],
    ["shot", () => { move(curA, 64, 70); }],
    ["build", (c) => {
      urlText.textContent = "staging." + c.url;
      move(curB, 70, 66); setTimeout(() => move(curB, 82, 80, true), 1300);
    }],
    ["live", (c) => {
      urlText.textContent = c.url; runGauges();
      move(curB, 62, 44, true); setTimeout(() => move(curB, 74, 30), 1500);
    }],
    ["out", () => {}],
  ];

  const go = (step) => {
    clearTimeout(timer);
    const [p, fn] = SEQ[step];
    fn(CASES[idx]); phase(p);
    if (REDUCED) return;
    timer = setTimeout(() => {
      if (step === SEQ.length - 1) { idx = (idx + 1) % CASES.length; go(0); }
      else go(step + 1);
    }, DUR[p]);
  };

  if (REDUCED) {
    const c = CASES[0];
    SEQ[0][1](c); SEQ[4][1](c); phase("live");
    $(".bld__code").style.opacity = 0;
  } else {
    // start when visible, pause when the tab is hidden
    const start = () => go(0);
    setTimeout(start, 600);
    document.addEventListener("visibilitychange", () => {
      if (document.hidden) { clearTimeout(timer); visible = false; }
      else if (!visible) { visible = true; go(0); }
    });
  }

  // depth: layers drift with the cursor
  if (!REDUCED && matchMedia("(hover: hover) and (pointer: fine)").matches) {
    addEventListener("pointermove", (e) => {
      stage.style.setProperty("--px", (e.clientX / innerWidth - .5).toFixed(3));
      stage.style.setProperty("--py", (e.clientY / innerHeight - .5).toFixed(3));
    }, { passive: true });
  }
})();
