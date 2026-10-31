// Hero background: a grid of dots that reacts to the cursor.
// Dots near the cursor light up, lean away from it like a magnetic field and
// leave a soft fading trail; a click sends a ripple across the grid.
// Sizes itself from the canvas box (ResizeObserver), so it stays aligned when
// fonts or images change the hero height after load. Draws only while something moves.
const DOTS_LITE = matchMedia("(hover: none), (max-width: 760px)").matches; // cursor effect: desktop only
if (DOTS_LITE) document.querySelectorAll(".hero__dots").forEach((c) => c.remove());
else document.querySelectorAll(".hero__dots").forEach(function (canvas) {
  const ctx = canvas.getContext("2d");
  const hero = canvas.parentElement;
  const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;

  const GAP = 26, R = 170, PUSH = 9;               // grid spacing, glow radius, max displacement (css px)
  let dpr = 1, w = 0, h = 0, cols = 0, rows = 0, ox = 0, oy = 0, energy = new Float32Array(0);
  let tx = -9999, ty = -9999, mx = -9999, my = -9999, active = false, raf = 0;
  const waves = [];                                 // click ripples: {x, y, t}

  function resize() {
    const r = canvas.getBoundingClientRect();
    if (!r.width || !r.height) return;
    dpr = Math.min(devicePixelRatio || 1, 2);
    w = r.width; h = r.height;
    canvas.width = Math.round(w * dpr); canvas.height = Math.round(h * dpr);
    cols = Math.ceil(w / GAP) + 1; rows = Math.ceil(h / GAP) + 1;
    ox = (w - (cols - 1) * GAP) / 2; oy = (h - (rows - 1) * GAP) / 2;
    energy = new Float32Array(cols * rows);
    draw(performance.now());
  }

  function draw(now) {
    // ease the glow towards the real cursor for a smooth, liquid feel
    if (active) { mx += (tx - mx) * 0.22; my += (ty - my) * 0.22; }
    for (let n = waves.length - 1; n >= 0; n--) if (now - waves[n].t > 1400) waves.splice(n, 1);

    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);

    // soft spotlight under the cursor
    if (active) {
      const g = ctx.createRadialGradient(mx, my, 0, mx, my, R * 1.6);
      g.addColorStop(0, "rgba(59,107,255,0.10)"); g.addColorStop(1, "rgba(59,107,255,0)");
      ctx.fillStyle = g; ctx.fillRect(mx - R * 1.6, my - R * 1.6, R * 3.2, R * 3.2);
    }

    let alive = active || waves.length > 0;
    for (let j = 0; j < rows; j++) {
      const y0 = oy + j * GAP;
      for (let i = 0; i < cols; i++) {
        const x0 = ox + i * GAP, k = j * cols + i;
        let x = x0, y = y0, e = energy[k];
        if (active) {
          const dx = x0 - mx, dy = y0 - my, d = Math.hypot(dx, dy);
          if (d < R) {
            const t = 1 - d / R;
            if (t * t > e) e = t * t;
            const p = t * t * PUSH / (d || 1); x += dx * p; y += dy * p;
          }
        }
        for (const wv of waves) {                    // ripple ring
          const age = (now - wv.t) / 1000, rad = age * 620, d = Math.hypot(x0 - wv.x, y0 - wv.y);
          const band = 1 - Math.abs(d - rad) / 46;
          if (band > 0) { const s = band * (1 - age / 1.4); if (s > e) e = s; const p = s * 6 / (d || 1); x += (x0 - wv.x) * p; y += (y0 - wv.y) * p; }
        }
        if (e > 0.004) { alive = true; energy[k] = e * 0.93; } else energy[k] = e = 0;

        if (e === 0) {
          ctx.fillStyle = "rgba(242,239,234,0.11)";
          ctx.fillRect(x - 0.8, y - 0.8, 1.6, 1.6);
        } else {
          const hot = Math.min(1, e * 1.5);
          const r = Math.round(242 + (124 - 242) * hot), gg = Math.round(239 + (155 - 239) * hot), b = Math.round(234 + (255 - 234) * hot);
          const s = 0.9 + e * 1.7;
          if (e > 0.3) { ctx.fillStyle = `rgba(59,107,255,${(e - 0.3) * 0.32})`; ctx.beginPath(); ctx.arc(x, y, s * 3, 0, 6.2832); ctx.fill(); }
          ctx.fillStyle = `rgba(${r},${gg},${b},${0.12 + e * 0.88})`;
          ctx.beginPath(); ctx.arc(x, y, s, 0, 6.2832); ctx.fill();
        }
      }
    }
    return alive;
  }

  function loop(now) {
    const alive = draw(now);
    raf = alive ? requestAnimationFrame(loop) : 0;
  }
  const kick = () => { if (!raf && !REDUCED) raf = requestAnimationFrame(loop); };

  function point(clientX, clientY) {
    const r = canvas.getBoundingClientRect();
    tx = clientX - r.left; ty = clientY - r.top;
    const inside = tx >= 0 && tx <= r.width && ty >= 0 && ty <= r.height;
    if (inside && !active) { mx = tx; my = ty; }
    active = inside;
    kick();
  }
  // listen on the window, so links, buttons and the 3D scene in the hero don't break the effect
  addEventListener("pointermove", (e) => { if (e.pointerType !== "touch") point(e.clientX, e.clientY); }, { passive: true });
  document.documentElement.addEventListener("pointerleave", () => { active = false; });
  addEventListener("blur", () => { active = false; });
  addEventListener("scroll", () => { if (active) active = canvas.getBoundingClientRect().bottom > 0; }, { passive: true });
  hero.addEventListener("pointerdown", (e) => {
    if (REDUCED || e.target.closest("a, button, input, textarea, select")) return;
    const r = canvas.getBoundingClientRect();
    waves.push({ x: e.clientX - r.left, y: e.clientY - r.top, t: performance.now() });
    if (waves.length > 3) waves.shift();
    kick();
  });

  new ResizeObserver(resize).observe(canvas);
  resize();
});
