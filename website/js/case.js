// Case study pages: gentle parallax on screenshots, decimal-aware counters, live node-failure diagram.
(function () {
  const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* parallax: elements drift a little against the scroll (data-parallax = strength) */
  const par = [...document.querySelectorAll("[data-parallax]")];
  if (par.length && !REDUCED) {
    let ticking = false;
    const update = () => {
      ticking = false;
      const vh = innerHeight;
      par.forEach((el) => {
        const r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        const k = parseFloat(el.dataset.parallax) || 0.05;
        const off = (r.top + r.height / 2 - vh / 2) * -k;
        el.style.translate = `0 ${off.toFixed(1)}px`;
      });
    };
    addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    update();
  }

  /* decimal counters (main.js handles integers; these override any data-dec) */
  const decs = document.querySelectorAll("[data-count][data-dec]");
  decs.forEach((el) => {
    const end = parseFloat(el.dataset.count), dec = +el.dataset.dec;
    el.removeAttribute("data-count");
    const io = new IntersectionObserver(([e]) => {
      if (!e.isIntersecting) return; io.disconnect();
      if (REDUCED) { el.textContent = end.toFixed(dec); return; }
      const t0 = performance.now(), dur = 1500;
      const step = (t) => { const k = Math.min(1, (t - t0) / dur); el.textContent = (end * (1 - Math.pow(1 - k, 4))).toFixed(dec); if (k < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    }, { threshold: .4 });
    io.observe(el);
  });
  /* node diagram: blocks of "your disk" spread over three nodes; node B fails and recovers */
  const nodes = document.querySelector(".nodes");
  if (nodes) {
    const grids = [...nodes.querySelectorAll(".node__grid")];
    grids.forEach((g) => { g.innerHTML = "<i></i>".repeat(24); });
    const shuffle = () => grids.forEach((g) => [...g.children].forEach((c) => c.classList.toggle("on", Math.random() < .38)));
    shuffle();
    if (!REDUCED) {
      let down = false;
      setInterval(() => { down = !down; nodes.classList.toggle("is-down", down); if (!down) shuffle(); }, 2600);
    }
  }
})();

/* Valhalla: working replica of the accredited-investor check (same questions and rules as the live site) */
(function () {
  const root = document.querySelector(".elig");
  if (!root) return;
  const Q = [
    { key: "income", tab: "Income", title: "Has your annual income exceeded $200,000?", text: "Or $300,000 combined with a spouse or partner, in each of the prior two years, with a reasonable expectation of reaching the same level this year.", yes: "Yes, it has", no: "Not quite" },
    { key: "worth", tab: "Net worth", title: "Is your net worth more than $1 million?", text: "Individually or with a spouse or partner, excluding the value of your primary residence.", yes: "Yes", no: "No" },
    { key: "license", tab: "License", title: "Do you hold a qualifying financial license?", text: "The SEC currently recognises the Series 7, Series 65 and Series 82 licenses for this purpose.", yes: "Yes, I do", no: "No" },
  ];
  const stepsEl = root.querySelector(".elig__steps"), body = root.querySelector(".elig__body");
  let step = 0, answers = {}, done = false;
  const next = (from) => { for (let n = 1; n <= Q.length; n++) { const i = (from + n) % Q.length; if (!answers[Q[i].key]) return i; } return -1; };
  const tabs = () => { stepsEl.innerHTML = Q.map((q, i) => `<button type="button" class="elig__tab${!done && i === step ? " is-active" : ""}${answers[q.key] ? " is-done" : ""}" data-step="${i}"><span>${i + 1}</span>${q.tab}</button>`).join(""); };
  const render = () => {
    tabs();
    if (!done) {
      const q = Q[step];
      body.innerHTML = `<div class="elig__screen"><h3 class="elig__title">${q.title}</h3><p class="elig__text">${q.text}</p><div class="elig__answers"><button type="button" class="elig__btn" data-a="yes">${q.yes}</button><button type="button" class="elig__btn" data-a="no">${q.no}</button></div></div>`;
    } else if (Object.values(answers).includes("yes")) {
      body.innerHTML = `<div class="elig__screen"><p class="elig__eyebrow">Based on these answers</p><h3 class="elig__title">You may qualify as an accredited investor.</h3><p class="elig__text">On the live site, a short form appears here and the team follows up with access to the offering materials.</p><div class="elig__fields"><span>Full name</span><span>Email address</span></div><div class="elig__answers"><button type="button" class="elig__btn elig__btn--solid" data-restart>Request access</button><button type="button" class="elig__btn elig__btn--ghost" data-restart>Start over</button></div><p class="elig__note">Demo only. Nothing is sent from this page.</p></div>`;
    } else {
      body.innerHTML = `<div class="elig__screen"><p class="elig__eyebrow">Based on these answers</p><h3 class="elig__title">You may not currently meet these individual criteria.</h3><p class="elig__text">Other paths may apply to entities, family offices or company insiders, so visitors can still contact the team.</p><div class="elig__answers"><button type="button" class="elig__btn elig__btn--solid" data-restart>Contact Valhalla</button><button type="button" class="elig__btn elig__btn--ghost" data-restart>Start over</button></div><p class="elig__note">Demo only. Nothing is sent from this page.</p></div>`;
    }
  };
  root.addEventListener("click", (e) => {
    const a = e.target.closest("[data-a]");
    if (a) {
      answers[Q[step].key] = a.dataset.a;
      if (a.dataset.a === "yes") done = true; else { const n = next(step); if (n === -1) done = true; else step = n; }
      return render();
    }
    const t = e.target.closest(".elig__tab");
    if (t) { step = +t.dataset.step; delete answers[Q[step].key]; done = false; return render(); }
    if (e.target.closest("[data-restart]")) { step = 0; answers = {}; done = false; render(); }
  });
  render();
})();

/* AWS Wrap: replica of the PPF price calculator */
(function () {
  const root = document.querySelector(".ppf");
  if (!root) return;
  const L = [["Full front PPF", 1799], ["Track pack PPF", 2099], ["Full body PPF", 4999]];
  const range = root.querySelector(".ppf__range"), price = root.querySelector(".ppf__price"), name = root.querySelector(".ppf__name");
  const imgs = [...root.querySelectorAll(".ppf__car img")], btns = [...root.querySelectorAll(".ppf__steps button")];
  let shown = 2099, raf;
  const fmt = (n) => "$" + Math.round(n).toLocaleString("en-US");
  const set = (i) => {
    range.value = i; range.style.setProperty("--p", (i / 2) * 100 + "%");
    imgs.forEach((im, k) => im.classList.toggle("is-on", k === i));
    btns.forEach((b, k) => b.classList.toggle("is-on", k === i));
    name.textContent = L[i][0];
    const from = shown, to = L[i][1], t0 = performance.now();
    cancelAnimationFrame(raf);
    const step = (t) => { const k = Math.min(1, (t - t0) / 600), e = 1 - Math.pow(1 - k, 3); shown = from + (to - from) * e; price.textContent = fmt(shown); if (k < 1) raf = requestAnimationFrame(step); };
    raf = requestAnimationFrame(step);
  };
  range.addEventListener("input", () => set(+range.value));
  btns.forEach((b) => b.addEventListener("click", () => set(+b.dataset.i)));
  set(1);
})();

/* v2: reading progress, chapter dock, more-work preview */
(function () {
  const bar = document.querySelector(".cs-progress i");
  const dock = document.querySelector(".cs-dock");
  const chapters = [...document.querySelectorAll("[data-chapter]")];
  if (dock && chapters.length) {
    chapters.forEach((s, i) => { if (!s.id) s.id = "ch-" + s.dataset.chapter.toLowerCase(); const a = document.createElement("a"); a.href = "#" + s.id; a.textContent = s.dataset.chapter; dock.appendChild(a); });
  }
  const links = dock ? [...dock.querySelectorAll("a")] : [];
  const hero = document.querySelector(".cs-hero, .pg-hero"), more = document.querySelector(".cs-more, .pg-cta");
  let ticking = false;
  const update = () => {
    ticking = false;
    const max = document.documentElement.scrollHeight - innerHeight;
    if (bar) bar.style.setProperty("--p", max > 0 ? (scrollY / max).toFixed(4) : 0);
    if (!dock) return;
    const past = hero && hero.getBoundingClientRect().bottom < innerHeight * .4;
    const end = more && more.getBoundingClientRect().top < innerHeight * .8;
    dock.classList.toggle("is-shown", !!past && !end);
    let cur = -1; chapters.forEach((s, i) => { if (s.getBoundingClientRect().top < innerHeight * .45) cur = i; });
    links.forEach((a, i) => a.classList.toggle("is-on", i === cur));
  };
  addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  addEventListener("resize", update); update();

  const float = document.querySelector(".cs-more__float");
  if (float && matchMedia("(hover: hover)").matches) {
    const img = float.querySelector("img");
    let x = 0, y = 0, tx = 0, ty = 0, raf = 0;
    const loop = () => { x += (tx - x) * .14; y += (ty - y) * .14; float.style.left = x + "px"; float.style.top = y + "px"; raf = Math.abs(tx - x) + Math.abs(ty - y) > .5 ? requestAnimationFrame(loop) : 0; };
    document.querySelectorAll(".cs-more__row").forEach((r) => {
      r.addEventListener("mouseenter", (e) => { img.src = r.dataset.img; if (!float.classList.contains("is-on")) { x = tx = e.clientX; y = ty = e.clientY; } float.classList.add("is-on"); });
      r.addEventListener("mouseleave", () => float.classList.remove("is-on"));
      r.addEventListener("mousemove", (e) => { tx = e.clientX; ty = e.clientY; if (!raf) raf = requestAnimationFrame(loop); });
    });
  }
})();

/* College Classics colourway picker */
(() => {
  const root = document.querySelector(".ccp");
  if (!root) return;
  const name = root.querySelector(".ccp__name");
  const cur = {};
  root.querySelectorAll(".ccp__sw.is-on").forEach(b => { cur[b.dataset.g] = b.dataset.n; });
  const let_ = root.querySelector(".ccp__letter"), letT = root.querySelector(".ccp__let");
  if (let_ && letT) let_.addEventListener("input", () => { letT.textContent = (let_.value || "").toUpperCase(); });
  root.querySelectorAll(".ccp__sw").forEach(b => b.addEventListener("click", () => {
    const g = b.dataset.g;
    root.querySelectorAll(`.ccp__sw[data-g="${g}"]`).forEach(x => { x.classList.toggle("is-on", x === b); x.setAttribute("aria-pressed", x === b); });
    root.style.setProperty("--" + g, b.dataset.c);
    cur[g] = b.dataset.n;
    name.textContent = cur.body + " / " + cur.sleeve;
  }));
})();

/* WaveAds banner demo */
(() => {
  const root = document.querySelector(".wad");
  if (!root) return;
  const txt = root.querySelector(".wad__txt"), input = root.querySelector("input");
  input.addEventListener("input", () => { txt.textContent = input.value.trim() || "Display your ad."; });
  root.querySelectorAll(".wad__c").forEach(b => b.addEventListener("click", () => {
    root.querySelectorAll(".wad__c").forEach(x => { x.classList.toggle("is-on", x === b); x.setAttribute("aria-pressed", x === b); });
    root.style.setProperty("--bg", b.dataset.bg); root.style.setProperty("--fg", b.dataset.fg);
  }));
})();

/* CI-ISAC pillar explorer */
(() => {
  const root = document.querySelector(".cip");
  if (!root) return;
  const tabs = [...root.querySelectorAll(".cip__tab")], panels = [...root.querySelectorAll(".cip__panel")], num = root.querySelector(".cip__count span");
  tabs.forEach((t, i) => t.addEventListener("click", () => {
    tabs.forEach((x, j) => { x.classList.toggle("is-on", j === i); x.setAttribute("aria-pressed", j === i); });
    panels.forEach((p, j) => p.classList.toggle("is-on", j === i));
    num.textContent = t.querySelector("b").textContent;
  }));
})();
