// Home hero: an "exploded" website — wireframe, design and live layers lift apart in 3D, cycling through real projects.
(function () {
  const root = document.querySelector(".xp"); if (!root) return;
  const stage = root.querySelector(".xp__stage");
  const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;
  // only the strongest UI/UX work
  const CASES = [
    { name: "Valhalla Capital", tags: "Private credit · Figma + Webflow", dir: "valhalla", url: "valhallacap.com", plat: "Live · Webflow", slug: "valhalla-capital", m: "m-hero" },
    { name: "CI-ISAC Australia", tags: "Cyber security · Figma + Webflow", dir: "ci-isac", url: "ci-isac.org.au", plat: "Webflow · in build", slug: "ci-isac", m: null, wip: true },
    { name: "ServersCamp", tags: "Cloud infrastructure · Site + panel UI", dir: "serverscamp", url: "serverscamp.com", plat: "Live · Production", slug: "serverscamp", m: "m-hero" },
    { name: "Arlowe Baxter", tags: "Property tech · Figma + Webflow", dir: "arlowe-baxter", url: "arlowebaxter.com", plat: "Live · Webflow", slug: "arlowe-baxter", m: "m-hero" },
    { name: "College Classics", tags: "Fashion · Shopify design + build", dir: "college-classics", url: "College Classics · Shopify", plat: "Live · Shopify", slug: "college-classics", m: "m-hero" },
  ];
  // warm up the other projects' screens only after the page has loaded (keeps the first paint fast)
  const warm = () => setTimeout(() => CASES.forEach((c) => { new Image().src = `img/work/${c.dir}/hero.webp`; if (c.m) new Image().src = `img/work/${c.dir}/${c.m}.webp`; }), 1500);
  if (document.readyState === "complete") warm(); else addEventListener("load", warm, { once: true });

  const $ = (s) => root.querySelector(s), $$ = (s) => [...root.querySelectorAll(s)];
  const imgs = $$(".xp__img"), mimg = $(".xp__mimg"), url = $(".xp__url"), plat = $(".xp__plat");
  const status = $(".xp__status"), statusS = $(".xp__statuss");
  const nameEl = $(".bld__name"), tagsEl = $(".bld__tags"), link = $(".bld__link");
  const steps = $$(".bld__steps li");

  const DUR = { wire: 1100, design: 1700, build: 1900, live: 3200, out: 500 };
  const STEP = { wire: 0, design: 1, build: 2, live: 3 };
  const TEXT = {
    wire: ["Wireframe", "Structure and content first"],
    design: ["Design", "Pixel-perfect in Figma"],
    build: ["Building", "Code, CMS and motion"],
    live: ["Live", "Launched and handed over"],
  };

  const setStep = (p) => {
    const n = STEP[p]; if (n === undefined) return;
    steps.forEach((s, i) => {
      s.classList.toggle("is-done", i < n);
      if (i === n) { s.style.setProperty("--dur", DUR[p] + "ms"); s.classList.remove("is-on"); void s.offsetWidth; s.classList.add("is-on"); }
      else s.classList.remove("is-on");
    });
  };
  const load = (c) => {
    imgs.forEach((i) => { i.src = `img/work/${c.dir}/hero.webp`; });
    if (c.m) mimg.src = `img/work/${c.dir}/${c.m}.webp`;
    stage.classList.toggle("no-phone", !c.m);
    url.textContent = c.url; plat.textContent = c.plat;
    nameEl.textContent = c.name; tagsEl.textContent = c.tags; link.href = `work/${c.slug}.html`;
  };
  const phase = (p) => {
    stage.dataset.phase = p;
    let t = TEXT[p];
    if (p === "live" && CASES[idx].wip) t = ["Design approved", "Webflow build in progress"];
    if (t && status) { status.textContent = t[0]; statusS.textContent = t[1]; }
    stage.classList.toggle("is-wip", !!CASES[idx].wip);
    setStep(p);
  };

  let idx = 0, timer = 0, visible = true;
  const ORDER = ["wire", "design", "build", "live", "out"];
  const run = (k) => {
    if (root.dataset.freeze) return;
    clearTimeout(timer);
    const p = ORDER[k];
    if (p === "wire") load(CASES[idx]);
    phase(p);
    timer = setTimeout(() => {
      if (!visible) { timer = 0; return; }
      if (p === "out") { idx = (idx + 1) % CASES.length; run(0); } else run(k + 1);
    }, DUR[p]);
  };

  if (REDUCED) { load(CASES[0]); phase("live"); return; }
  stage.dataset.phase = "out";
  nameEl.textContent = CASES[0].name; tagsEl.textContent = CASES[0].tags; link.href = `work/${CASES[0].slug}.html`;
  const begin = () => setTimeout(() => run(0), 120);
  if (document.readyState !== "loading") begin(); else addEventListener("DOMContentLoaded", begin, { once: true });

  // pause when off-screen
  new IntersectionObserver(([e]) => { const was = visible; visible = e.isIntersecting; if (visible && !was && !timer) run(0); }, { threshold: 0.1 }).observe(stage);

  // mouse tilt
  if (matchMedia("(hover: hover) and (pointer: fine)").matches) {
    const hero = root.closest(".hero") || root; let raf = 0, mx = 0, my = 0;
    hero.addEventListener("pointermove", (e) => {
      const r = stage.getBoundingClientRect();
      mx = Math.max(-1, Math.min(1, (e.clientX - (r.left + r.width / 2)) / (r.width / 1.2)));
      my = Math.max(-1, Math.min(1, (e.clientY - (r.top + r.height / 2)) / (r.height / 1.2)));
      if (!raf) raf = requestAnimationFrame(() => { stage.style.setProperty("--mx", mx.toFixed(3)); stage.style.setProperty("--my", my.toFixed(3)); raf = 0; });
    });
    hero.addEventListener("pointerleave", () => { stage.style.setProperty("--mx", 0); stage.style.setProperty("--my", 0); });
  }
})();
