// Inner pages: pricing toggle, work filters, contact prefill
(function () {
  /* pricing: one-time projects vs monthly plans */
  const tg = document.querySelector(".ptoggle");
  if (tg) {
    const btns = [...tg.querySelectorAll("button")], panels = [...document.querySelectorAll(".ppanel")];
    const set = (k) => {
      btns.forEach((b) => { const on = b.dataset.p === k; b.classList.toggle("is-on", on); b.setAttribute("aria-selected", String(on)); });
      panels.forEach((pn) => { pn.hidden = pn.dataset.panel !== k; if (!pn.hidden) pn.querySelectorAll("[data-reveal]").forEach((el) => el.classList.add("in")); });
    };
    btns.forEach((b) => b.addEventListener("click", () => set(b.dataset.p)));
    if (location.hash === "#plans") set("plans");
  }

  /* work: filter cards by kind */
  const fl = document.querySelector(".filters");
  if (fl) {
    const cards = [...document.querySelectorAll(".pcards [data-kind]")];
    const cta = document.querySelector(".pcard--cta");
    const balance = () => {
      /* equal 2-column grid: the "your project" card only appears when it fills an empty slot */
      const n = cards.filter((c) => c !== cta && !c.classList.contains("is-hidden")).length;
      if (cta) cta.classList.toggle("is-hidden", n % 2 === 0);
    };
    balance();
    fl.addEventListener("click", (e) => {
      const b = e.target.closest("button"); if (!b) return;
      fl.querySelectorAll("button").forEach((x) => x.classList.toggle("is-on", x === b));
      const f = b.dataset.f;
      cards.forEach((c) => {
        if (c === cta) return;
        const show = f === "all" || c.dataset.kind.split(" ").includes(f);
        c.classList.toggle("is-hidden", !show);
        if (show) c.classList.add("in");
      });
      balance();
    });
  }

  /* contact: show what the visitor picked on the pricing or service page (?plan=id), keep ?need= as a fallback */
  const form = document.getElementById("brief");
  if (form) {
    const qs = new URLSearchParams(location.search);
    let plans = {}; try { plans = JSON.parse(document.getElementById("plans-data").textContent); } catch (e) {}
    const tick = (v) => { const box = [...form.querySelectorAll('input[name="need"]')].find((i) => i.value.toLowerCase() === String(v).toLowerCase()); if (box) box.checked = true; return !!box; };
    const card = form.querySelector(".picked"), hidden = form.elements.namedItem("plan");
    const p = plans[qs.get("plan")];
    if (p && card && hidden) {
      hidden.value = `${p.name} (${p.group}, ${p.price})`;
      card.querySelector(".picked__name").textContent = p.name;
      card.querySelector(".picked__price").textContent = `${p.group} · ${p.price}`;
      card.querySelector(".picked__change").href = "pricing.html#" + qs.get("plan");
      card.hidden = false;
      if (p.need) tick(p.need);
      const budget = form.elements.namedItem("budget");
      if (p.monthly && budget) budget.value = "Monthly plan";
      form.classList.add("in");
      requestAnimationFrame(() => scrollTo({ top: form.getBoundingClientRect().top + scrollY - 100, behavior: "auto" }));
      card.querySelector(".picked__x").addEventListener("click", () => {
        card.hidden = true; hidden.value = "";
        try { history.replaceState(null, "", location.pathname); } catch (e) {}
      });
      form.addEventListener("reset", () => { card.hidden = true; hidden.value = ""; });
    } else if (qs.get("need")) {
      const need = qs.get("need");
      if (!tick(need)) { const d = form.elements.namedItem("details"); if (d && !d.value) d.value = "Interested in: " + need + "\n\n"; }
    }
  }
})();

// Pricing explorer: tabs (projects / plans) + option list + detail card.
// On small screens the open card moves directly under its row.
(function () {
  const px = document.querySelector(".px"); if (!px) return;
  const tabs = document.querySelector(".ptabs"), stage = px.querySelector(".px__stage");
  const sets = [...px.querySelectorAll(".px__set")], rows = [...px.querySelectorAll(".px__row")], panels = [...px.querySelectorAll(".px__panel")];
  const small = matchMedia("(max-width: 960px)");
  let cur = rows[0].dataset.id;
  const setOf = (id) => document.getElementById("pxr-" + id).closest(".px__set").dataset.set;
  const place = () => { const pn = document.getElementById("px-" + cur), r = document.getElementById("pxr-" + cur); if (small.matches) r.after(pn); else stage.appendChild(pn); };
  const showSet = (k) => {
    sets.forEach((s) => { s.hidden = s.dataset.set !== k; });
    if (tabs) { tabs.dataset.on = k; tabs.querySelectorAll("button").forEach((b) => { const on = b.dataset.tab === k; b.classList.toggle("is-on", on); b.setAttribute("aria-selected", String(on)); }); }
  };
  const select = (id) => {
    if (!document.getElementById("px-" + id)) return false;
    cur = id; showSet(setOf(id));
    rows.forEach((r) => { const on = r.dataset.id === id; r.classList.toggle("is-on", on); r.setAttribute("aria-selected", String(on)); });
    panels.forEach((p) => { p.hidden = p.id !== "px-" + id; });
    place(); return true;
  };
  const go = (el) => scrollTo({ top: el.getBoundingClientRect().top + scrollY - 100, behavior: "smooth" });
  rows.forEach((r) => r.addEventListener("click", () => {
    select(r.dataset.id);
    if (small.matches) setTimeout(() => { if (r.getBoundingClientRect().top < 80) go(r); }, 30);
    try { history.replaceState(null, "", "#" + r.dataset.id); } catch (e) {}
  }));
  if (tabs) tabs.addEventListener("click", (e) => {
    const b = e.target.closest("button"); if (!b) return;
    const first = px.querySelector(`.px__set[data-set="${b.dataset.tab}"] .px__row`);
    select(first.dataset.id);
  });
  px.addEventListener("keydown", (e) => {
    if (!e.target.classList.contains("px__row") || !["ArrowDown", "ArrowUp"].includes(e.key)) return;
    const vis = rows.filter((r) => !r.closest(".px__set").hidden), i = vis.indexOf(e.target);
    const n = vis[(i + (e.key === "ArrowDown" ? 1 : vis.length - 1)) % vis.length];
    e.preventDefault(); n.focus(); select(n.dataset.id);
  });
  document.querySelectorAll("[data-pick]").forEach((a) => a.addEventListener("click", (e) => {
    e.preventDefault(); if (select(a.dataset.pick)) go(small.matches ? document.getElementById("pxr-" + a.dataset.pick) : px);
  }));
  px.addEventListener("click", (e) => { const m = e.target.closest(".px__more"); if (m) m.setAttribute("aria-expanded", String(m.getAttribute("aria-expanded") !== "true")); });
  small.addEventListener ? small.addEventListener("change", place) : small.addListener(place);
  const h = location.hash.replace("#", ""), alias = { plans: "plan-full", monthly: "plan-full" };
  if (h && select(alias[h] || h)) setTimeout(() => go(small.matches ? document.getElementById("pxr-" + cur) : px), 300); else place();
})();
