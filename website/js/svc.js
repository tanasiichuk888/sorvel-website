// "What we do" scenes: restart the active scene's animation, loop it, count numbers up.
document.querySelectorAll(".svc__stage").forEach((stage) => (function (stage) {
  const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const scenes = [...stage.querySelectorAll(".vis")];
  let timers = [], inView = false, active = null;

  const later = (fn, ms) => timers.push(setTimeout(fn, ms));
  const clear = () => { timers.forEach(clearTimeout); timers = []; };
  const fmt = (v, dec) => dec ? v.toFixed(dec) : Math.round(v).toLocaleString("en-US");
  const count = (el, delay, dur) => {
    const to = parseFloat(el.dataset.to), dec = +el.dataset.dec || 0;
    el.textContent = fmt(0, dec);
    if (REDUCED) { el.textContent = fmt(to, dec); return; }
    later(() => {
      const t0 = performance.now();
      const tick = (t) => { const k = Math.min(1, (t - t0) / dur); el.textContent = fmt(to * (1 - Math.pow(1 - k, 3)), dec); if (k < 1 && active) requestAnimationFrame(tick); };
      requestAnimationFrame(tick);
    }, delay);
  };

  const extras = {
    "vis--app": (v) => {
      const d = v.querySelector(".sp-dash"); d.classList.remove("is-light");
      v.querySelectorAll("[data-to]").forEach((el) => count(el, 300, 1400));
      later(() => d.classList.add("is-light"), 4600);
    },
    "vis--cro": (v) => {
      count(v.querySelector(".sc-src [data-to]"), 0, 3600);
      v.querySelectorAll(".sc-num [data-to]").forEach((el) => count(el, 600, 3200));
    },
    "vis--mig": (v) => {
      v.querySelectorAll(".sm-stats [data-to]").forEach((el) => count(el, 300, 4200));
      const li = [...v.querySelectorAll(".sm-list li")]; li.forEach((l) => l.classList.remove("is-ok"));
      li.forEach((l, i) => later(() => l.classList.add("is-ok"), 1400 + i * 900));
    },
  };

  const play = (v) => {
    clear();
    v.classList.remove("run"); void v.offsetWidth; v.classList.add("run");
    const key = [...v.classList].find((c) => extras[c]);
    if (key) extras[key](v);
    if (REDUCED) return;
    const loop = +v.dataset.loop || 9000;
    later(() => { v.style.transition = "opacity .35s"; v.style.opacity = "0"; }, loop - 350);
    later(() => { v.style.opacity = ""; v.style.transition = ""; if (active === v && inView) play(v); }, loop);
  };

  const sync = () => {
    const on = scenes.find((v) => v.classList.contains("is-on")) || scenes[0];
    if (on === active && on.classList.contains("run")) return;
    scenes.forEach((v) => { if (v !== on) { v.classList.remove("run"); v.style.opacity = ""; } });
    active = on;
    if (inView) play(on);
  };

  new MutationObserver(sync).observe(stage, { subtree: true, attributes: true, attributeFilter: ["class"] });
  new IntersectionObserver(([e]) => {
    inView = e.isIntersecting;
    if (inView) { active = null; sync(); } else { clear(); }
  }, { threshold: .25 }).observe(stage);
})(stage));
