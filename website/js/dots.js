// Hero background: a quiet grid of dots. Dots near the cursor light up in the
// accent color and fade out slowly, leaving a soft trail. Draws only while something glows.
const DOTS_LITE = matchMedia("(hover: none), (max-width: 760px)").matches; // cursor effect: desktop only
if (DOTS_LITE) document.querySelectorAll(".hero__dots").forEach((c) => c.remove());
else document.querySelectorAll(".hero__dots").forEach(function (canvas) {
  const ctx = canvas.getContext("2d");
  const hero = canvas.parentElement;
  const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;

  const GAP = 24, R = 150;                        // grid spacing, glow radius (css px)
  const BASE = [242, 239, 234], ACC = [59, 107, 255], HOT = [190, 206, 255];
  let dpr = 1, cols = 0, rows = 0, ox = 0, oy = 0, energy = new Float32Array(0);
  let mx = -9999, my = -9999, active = false, raf = 0;

  function resize() {
    dpr = Math.min(devicePixelRatio || 1, 2);
    const w = hero.clientWidth, h = hero.clientHeight;
    canvas.width = Math.round(w * dpr); canvas.height = Math.round(h * dpr);
    cols = Math.ceil(w / GAP) + 1; rows = Math.ceil(h / GAP) + 1;
    ox = (w - (cols - 1) * GAP) / 2; oy = (h - (rows - 1) * GAP) / 2;
    energy = new Float32Array(cols * rows);
    draw();
  }

  function draw() {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    let alive = false;
    for (let j = 0; j < rows; j++) {
      const y = oy + j * GAP;
      for (let i = 0; i < cols; i++) {
        const x = ox + i * GAP, k = j * cols + i;
        if (active) {
          const d = Math.hypot(x - mx, y - my);
          if (d < R) { const t = 1 - d / R; energy[k] = Math.max(energy[k], t * t); }
        }
        let e = energy[k];
        if (e > 0.004) { alive = true; energy[k] = e *= 0.94; } else energy[k] = e = 0;
        if (e === 0) {
          ctx.fillStyle = "rgba(242,239,234,0.09)";
          ctx.fillRect(x - 0.75, y - 0.75, 1.5, 1.5);
        } else {
          const c = e > 0.6 ? HOT : ACC, a = 0.09 + e * 0.9, s = 1.5 + e * 1.6;
          const mix = (n) => Math.round(BASE[n] + (c[n] - BASE[n]) * Math.min(1, e * 1.6));
          ctx.fillStyle = `rgba(${mix(0)},${mix(1)},${mix(2)},${a})`;
          ctx.beginPath(); ctx.arc(x, y, s / 2 + 0.2, 0, 6.2832); ctx.fill();
          if (e > 0.35) { ctx.fillStyle = `rgba(59,107,255,${(e - 0.35) * 0.25})`; ctx.beginPath(); ctx.arc(x, y, s * 2.4, 0, 6.2832); ctx.fill(); }
        }
      }
    }
    return alive;
  }

  function loop() {
    const alive = draw();
    raf = alive || active ? requestAnimationFrame(loop) : 0;
  }
  const kick = () => { if (!raf) raf = requestAnimationFrame(loop); };

  function point(clientX, clientY) {
    const r = canvas.getBoundingClientRect();
    mx = clientX - r.left; my = clientY - r.top;
    active = my >= -R && my <= r.height + R;
    if (!REDUCED) kick();
  }
  hero.addEventListener("pointermove", (e) => point(e.clientX, e.clientY), { passive: true });
  hero.addEventListener("pointerleave", () => { active = false; });
  hero.addEventListener("touchmove", (e) => { const t = e.touches[0]; point(t.clientX, t.clientY); }, { passive: true });
  hero.addEventListener("touchend", () => { active = false; });

  addEventListener("resize", resize);
  resize();

});
