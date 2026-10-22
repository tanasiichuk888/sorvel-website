// Ambient interaction layer: cursor glow, card spotlights, magnetic buttons, soft blue section gradients.
(function () {
  const fine = matchMedia("(hover: hover) and (pointer: fine)").matches;
  const calm = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const root = document.documentElement;

  /* 1. soft blue glow that follows the cursor across the whole page */
  if (fine && !calm) {
    const glow = document.createElement("div");
    glow.className = "fx-glow"; glow.setAttribute("aria-hidden", "true");
    document.body.appendChild(glow);
    let tx = innerWidth / 2, ty = innerHeight / 3, x = tx, y = ty, raf = 0;
    const loop = () => {
      x += (tx - x) * .12; y += (ty - y) * .12;
      glow.style.transform = `translate3d(${x}px, ${y}px, 0)`;
      raf = Math.abs(tx - x) + Math.abs(ty - y) > .3 ? requestAnimationFrame(loop) : 0;
    };
    addEventListener("pointermove", (e) => { tx = e.clientX; ty = e.clientY; glow.classList.add("is-on"); if (!raf) raf = requestAnimationFrame(loop); }, { passive: true });
    document.addEventListener("pointerleave", () => glow.classList.remove("is-on"));
  }

  /* 2. spotlight that tracks the cursor inside cards */
  const CARDS = [".pcard", ".px__box", ".px__panel", ".px__promo", ".cbox", ".trust > div", ".incl > div", ".plat > div", ".rcard",
    ".moves > div", ".vals > div", ".cs-problems > article", ".sprice", ".brief", ".case", ".step li", ".rbig", ".acc__item",
    ".cs-phase", ".cs-got", ".cs-dec__row", ".svc__stage", ".person__ph", ".note__ph", ".ask", ".cs-bento > *", ".cs-out > *"].join(",");
  if (fine) {
    document.querySelectorAll(CARDS).forEach((el) => {
      if (el.querySelector(":scope > .fx-spot")) return;
      const s = document.createElement("span"); s.className = "fx-spot"; s.setAttribute("aria-hidden", "true");
      if (getComputedStyle(el).position === "static") el.style.position = "relative";
      el.classList.add("fx-card"); el.appendChild(s);
      el.addEventListener("pointermove", (e) => {
        const r = el.getBoundingClientRect();
        el.style.setProperty("--fx-x", (e.clientX - r.left) + "px");
        el.style.setProperty("--fx-y", (e.clientY - r.top) + "px");
      }, { passive: true });
    });
  }

  /* 3. magnetic primary buttons */
  if (fine && !calm) {
    document.querySelectorAll(".btn--primary, .nav__cta").forEach((b) => {
      b.addEventListener("pointermove", (e) => {
        const r = b.getBoundingClientRect();
        const dx = (e.clientX - r.left - r.width / 2) / r.width, dy = (e.clientY - r.top - r.height / 2) / r.height;
        b.style.translate = `${dx * 8}px ${dy * 6}px`;
      });
      b.addEventListener("pointerleave", () => { b.style.translate = ""; });
    });
  }

  /* 4. drifting blue gradients behind every other section */
  const secs = [...document.querySelectorAll("main > section.sec, main > section.cs-more, main > section.cs-numbers")];
  secs.forEach((s, i) => {
    if (i % 2 === 0 || s.querySelector(":scope > .fx-amb")) return;
    const a = document.createElement("div"); a.className = "fx-amb fx-amb--" + (i % 4 === 1 ? "r" : "l"); a.setAttribute("aria-hidden", "true");
    s.prepend(a);
  });
  if (!calm) {
    const ambs = [...document.querySelectorAll(".fx-amb")];
    let ticking = false;
    const par = () => {
      ticking = false;
      ambs.forEach((a) => {
        const r = a.parentElement.getBoundingClientRect();
        const p = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;
        a.style.setProperty("--fx-p", Math.max(-1.5, Math.min(1.5, p)).toFixed(3));
      });
    };
    addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(par); } }, { passive: true });
    par();
  }
  root.classList.add("fx-ready");
})();
