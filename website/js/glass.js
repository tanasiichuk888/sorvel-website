// Liquid glass: move the specular highlight with the pointer.
(function () {
  if (!matchMedia("(hover: hover) and (pointer: fine)").matches) return;
  const SEL = ".rcard, .ask, .crew__tile, .crew__lead, .letter, .brief, .case, .svc__stage, .pcard, .pnote, .cbox, .rbig, .legal__meta, .px__box, .px__panel, .sprice, .sx, .fl-card, .cs-cover, .cs-stage, .ccp, .cip, .wvs, .plat > div, .trust > div, .step li";
  let last = null, raf = 0, ev = null;
  const reset = (el) => { el.style.removeProperty("--gx"); el.style.removeProperty("--gy"); };
  document.addEventListener("pointermove", (e) => {
    ev = e; if (raf) return;
    raf = requestAnimationFrame(() => {
      raf = 0; const el = ev.target.closest && ev.target.closest(SEL);
      if (last && last !== el) reset(last);
      last = el; if (!el) return;
      const r = el.getBoundingClientRect();
      el.style.setProperty("--gx", (ev.clientX - r.left).toFixed(0) + "px");
      el.style.setProperty("--gy", (ev.clientY - r.top).toFixed(0) + "px");
    });
  }, { passive: true });
  document.addEventListener("pointerleave", () => { if (last) reset(last); last = null; });
})();

// images marked data-src load right after the page itself (decorative walls etc.)
(function () {
  const go = () => setTimeout(() => document.querySelectorAll("img[data-src]").forEach((im) => {
    im.addEventListener("load", () => im.classList.add("is-in"), { once: true });
    im.src = im.dataset.src; im.removeAttribute("data-src");
  }), 200);
  if (document.readyState === "complete") go(); else addEventListener("load", go, { once: true });
})();
