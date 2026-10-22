/* home: parallax layers on case previews */
(() => {
  if (!matchMedia("(hover: hover) and (pointer: fine)").matches || matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  document.querySelectorAll(".cv").forEach((el) => {
    let raf = 0, tx = 0, ty = 0;
    el.addEventListener("pointermove", (e) => {
      const r = el.getBoundingClientRect();
      tx = (e.clientX - r.left) / r.width - .5; ty = (e.clientY - r.top) / r.height - .5;
      if (!raf) raf = requestAnimationFrame(() => { el.style.setProperty("--mx", tx.toFixed(3)); el.style.setProperty("--my", ty.toFixed(3)); raf = 0; });
    });
    el.addEventListener("pointerleave", () => { el.style.setProperty("--mx", 0); el.style.setProperty("--my", 0); });
  });
})();
