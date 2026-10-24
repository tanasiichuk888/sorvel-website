(function () {
  const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- anonymous visit stats (no cookies, no personal data) ----------
     For this tab only (session storage, gone when the tab closes): a random visit id,
     where the visit came from and the page it started on. Counts page views, how far
     each page is scrolled, time with the page open, button clicks, and the lead
     actions (brief started / sent, Telegram, email).
     The site owner's own browser is left out: opening /scoreboard or any page with
     ?me=1 marks it (localStorage sv_me), ?me=0 undoes that. */
  const ME = (() => {
    try {
      const q = new URLSearchParams(location.search).get("me");
      if (q === "1") localStorage.setItem("sv_me", "1");
      if (q === "0") localStorage.removeItem("sv_me");
      if (q === "1" || q === "0") {
        const n = document.createElement("div");
        n.setAttribute("role", "status");
        n.textContent = q === "1" ? "This browser is now left out of the site stats" : "This browser is counted in the site stats again";
        n.style.cssText = "position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:9999;padding:10px 16px;border-radius:10px;background:#111;color:#fff;font:14px/1.4 system-ui,sans-serif;box-shadow:0 10px 30px rgba(0,0,0,.35)";
        document.body.appendChild(n); setTimeout(() => n.remove(), 3500);
      }
      return localStorage.getItem("sv_me") === "1";
    } catch (e) { return false; }
  })();
  if (ME) {
    // keep Cloudflare Web Analytics from counting the owner's own visits too
    const rum = (u) => /cdn-cgi\/rum|cloudflareinsights/.test(String((u && u.url) || u));
    try {
      const sb = navigator.sendBeacon && navigator.sendBeacon.bind(navigator);
      if (sb) navigator.sendBeacon = (u, d) => (rum(u) ? true : sb(u, d));
      const f = window.fetch && window.fetch.bind(window);
      if (f) window.fetch = (u, o) => (rum(u) ? Promise.resolve(new Response(null, { status: 204 })) : f(u, o));
      const op = XMLHttpRequest.prototype.open, sd = XMLHttpRequest.prototype.send;
      XMLHttpRequest.prototype.open = function (m, u) { this._svSkip = rum(u); return op.apply(this, arguments); };
      XMLHttpRequest.prototype.send = function () { if (!this._svSkip) return sd.apply(this, arguments); };
    } catch (e) {}
  }
  const SRC = (() => {
    try {
      let v = JSON.parse(sessionStorage.getItem("sv_src") || "null");
      if (!v || !v.id) {
        const q = new URLSearchParams(location.search);
        let ref = "";
        try { ref = document.referrer ? new URL(document.referrer).hostname : ""; } catch (er) {}
        if (ref === location.hostname) ref = "";
        // short links and Android apps send their own names; map them to the service
        const REF = { "lnkd.in": "linkedin.com", "com.linkedin.android": "linkedin.com app", "t.co": "x.com", "com.google.android.gm": "gmail",
          "org.telegram.messenger": "telegram", "web.telegram.org": "telegram", "l.facebook.com": "facebook.com", "lm.facebook.com": "facebook.com",
          "l.instagram.com": "instagram.com", "com.slack": "slack", "away.vk.com": "vk.com" };
        ref = REF[ref] || ref.replace(/^(www|m)\./, "");
        // in-app browsers (LinkedIn, Instagram, Facebook, X) open links without a referrer; their user agent still says who they are
        const ua = navigator.userAgent || "";
        const app = /LinkedInApp/i.test(ua) ? "linkedin.com" : /Instagram/.test(ua) ? "instagram.com" : /FBAN|FBAV|FB_IAB/.test(ua) ? "facebook.com"
          : /Twitter/i.test(ua) ? "x.com" : /Telegram/i.test(ua) ? "telegram" : "";
        const utm = (q.get("utm_source") || q.get("ref") || "").toLowerCase().replace(/[^a-z0-9.\-_ ]/g, "").slice(0, 40);
        v = Object.assign({ s: utm || ref || (app ? app + " app" : "direct"), l: location.pathname }, v || {});
        // tidy the address bar so a shared link doesn't carry the source along
        if (q.has("utm_source") || q.has("utm_medium") || q.has("utm_campaign") || q.has("ref")) {
          ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "ref"].forEach((k) => q.delete(k));
          try { history.replaceState(history.state, "", location.pathname + (q.toString() ? "?" + q : "") + location.hash); } catch (er) {}
        }
        v.id = Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4);
        sessionStorage.setItem("sv_src", JSON.stringify(v));
      }
      return v;
    } catch (e) { return { s: "direct", l: location.pathname, id: "" }; }
  })();
  const track = (t, k, v) => {
    if (ME) return;
    try {
      const body = JSON.stringify({ t, p: location.pathname, s: SRC.s, l: SRC.l, i: SRC.id, k, v });
      if (!(navigator.sendBeacon && navigator.sendBeacon("/api/e", body))) fetch("/api/e", { method: "POST", body, keepalive: true }).catch(() => {});
    } catch (e) {}
  };
  track("view");
  // clicks: the lead actions, plus any link or button, labelled by its visible text
  document.addEventListener("click", (e) => {
    const a = e.target.closest && e.target.closest("a[href], button, [data-track]");
    if (!a) return;
    const h = a.getAttribute("href") || "";
    if (/^https:\/\/t\.me\//.test(h)) track("telegram");
    else if (/^mailto:/.test(h)) track("email");
    let label = a.getAttribute("data-track") || a.getAttribute("aria-label") || (a.innerText || a.textContent || "").replace(/\s+/g, " ").trim();
    if (!label && a.querySelector("img[alt]")) label = a.querySelector("img[alt]").alt;
    if (!label) return;
    let to = "";
    try { if (h && !/^(mailto:|tel:|#)/.test(h)) { const u = new URL(h, location.href); to = u.host === location.host ? (u.pathname.replace(/\.html$/, "").replace(/\/index$/, "/") || "/") : u.host.replace(/^www\./, ""); } } catch (er) {}
    track("click", (label.slice(0, 48) + (to ? " → " + to : "")).slice(0, 110));
  }, { capture: true });
  // how far down the page people get (each mark once per page view)
  (() => {
    const hit = new Set();
    const check = () => {
      const full = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);
      const pct = full <= innerHeight + 4 ? 100 : (scrollY + innerHeight) / full * 100;
      [25, 50, 75, 100].forEach((m) => { if (pct >= m - 2 && !hit.has(m)) { hit.add(m); track("scroll", String(m)); } });
    };
    let tm = 0;
    addEventListener("scroll", () => { if (!tm) tm = setTimeout(() => { tm = 0; check(); }, 400); }, { passive: true });
    addEventListener("load", () => setTimeout(check, 1500));
  })();
  // time with the page visible, sent in pieces when the tab is hidden or closed
  (() => {
    let since = document.visibilityState === "visible" ? Date.now() : 0, acc = 0;
    const flush = () => {
      if (since) { acc += Date.now() - since; since = 0; }
      const s = Math.round(acc / 1000); acc = 0;
      if (s >= 1) track("time", "", Math.min(s, 1800));
    };
    document.addEventListener("visibilitychange", () => { if (document.visibilityState === "hidden") flush(); else since = Date.now(); });
    addEventListener("pagehide", flush);
  })();

  /* ---------- intro ---------- */
  const go = () => requestAnimationFrame(() => document.documentElement.classList.add("is-loaded"));
  (document.fonts && document.fonts.ready ? Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 900))]) : Promise.resolve()).then(go);

  /* ---------- buttons: track the cursor for the spotlight / fill origin ---------- */
  document.querySelectorAll(".btn").forEach((b) => {
    const set = (e) => {
      const r = b.getBoundingClientRect();
      b.style.setProperty("--mx", e.clientX - r.left + "px");
      b.style.setProperty("--my", e.clientY - r.top + "px");
    };
    b.addEventListener("pointerenter", set);
    b.addEventListener("pointermove", set);
    b.addEventListener("pointerleave", set);   // the fill shrinks back toward where the cursor left
  });

  /* ---------- showcase scene ----------
     Real screenshots: put full-page captures in website/img/work/ and fill `desktop` / `mobile`
     (e.g. desktop: "img/work/cofimd-desktop.jpg"). Until then each project shows a drawn mock. */
  const cases = [
    { name: "Fintech platform", tags: "Brand, Website, Webflow", url: "fintech-platform.com", theme: "", desktop: "", mobile: "" },
    { name: "AI analytics SaaS", tags: "Website, Product UI, Framer", url: "ai-analytics.io", theme: "mint", desktop: "", mobile: "" },
    { name: "Recruiting platform", tags: "Website, Design system, WordPress", url: "recruit-platform.com", theme: "light", desktop: "", mobile: "" },
  ];
  const mockPage = (theme) => `<div class="pg${theme ? " pg--" + theme : ""}">
      <div class="pg__nav"><b></b><i></i><i></i><i></i><u></u></div>
      <div class="pg__hero"><div><div class="pg__h"></div><div class="pg__h" style="width:78%"></div><div class="pg__h" style="width:55%"></div>
        <div class="pg__p" style="margin-top:3cqw"></div><div class="pg__p" style="width:80%"></div><div class="pg__btns"><u></u><s></s></div></div><div class="pg__vis"></div></div>
      <div class="pg__logos"><i></i><i></i><i></i><i></i><i></i></div>
      <div class="pg__sec"><div class="pg__h"></div><div class="pg__p"></div></div>
      <div class="pg__grid"><div class="pg__card"><i></i><div class="pg__p"></div><div class="pg__p" style="width:60%"></div></div><div class="pg__card"><i></i><div class="pg__p"></div></div><div class="pg__card"><i></i><div class="pg__p"></div></div></div>
      <div class="pg__band"><div><b></b><div class="pg__p"></div></div><div><b></b><div class="pg__p"></div></div><div><b></b><div class="pg__p"></div></div></div>
      <div class="pg__cta"><div class="pg__h"></div><div class="pg__p"></div></div>
    </div>`;
  const screenHTML = (c, kind) => {
    const src = kind === "phone" ? c.mobile : c.desktop;
    return `<div class="scr">${src ? `<img class="scroll" src="${src}" alt="" loading="lazy" />` : mockPage(c.theme)}</div>`;
  };
  const screens = {};
  document.querySelectorAll("[data-screen]").forEach((el) => {
    const kind = el.dataset.screen;
    el.innerHTML = cases.map((c) => screenHTML(c, kind)).join("");
    screens[kind] = [...el.children];
  });
  // section mocks: any .pg--auto gets the drawn page
  document.querySelectorAll(".pg--auto").forEach((el) => {
    const theme = el.classList.contains("pg--mint") ? "mint" : el.classList.contains("pg--light") ? "light" : "";
    el.outerHTML = mockPage(theme).replace('class="pg', 'class="pg--auto pg');
  });
  // how far each page can scroll inside its screen
  const measure = () => {
    Object.values(screens).flat().forEach((scr) => {
      const inner = scr.firstElementChild, view = scr.parentElement;
      if (!inner) return;
      inner.style.setProperty("--dist", Math.max(0, inner.offsetHeight - view.clientHeight) + "px");
    });
    document.querySelectorAll(".pg--auto").forEach((pg) => {
      pg.style.setProperty("--dist", Math.max(0, pg.offsetHeight - pg.parentElement.clientHeight) + "px");
    });
  };
  document.querySelectorAll(".scr img").forEach((im) => im.addEventListener("load", measure));
  addEventListener("resize", measure);

  const bars = document.querySelector(".show__bars"), nameEl = document.querySelector(".show__name"),
        tagsEl = document.querySelector(".show__tags"), urlEl = document.querySelector(".win__url");
  if (bars && screens.front) {
    const DUR = 7000;
    bars.innerHTML = cases.map((c) => `<button type="button" aria-label="Show ${c.name}"><i></i></button>`).join("");
    bars.style.setProperty("--slide", DUR / 1000 + "s");
    const bEls = [...bars.children];
    let cur = 0, timer = 0;
    const show = (n) => {
      cur = n;
      const next = (n + 1) % cases.length;
      screens.front.forEach((s, i) => s.classList.toggle("is-on", i === n));
      screens.phone.forEach((s, i) => s.classList.toggle("is-on", i === n));
      screens.back.forEach((s, i) => s.classList.toggle("is-on", i === next));
      bEls.forEach((b, i) => { b.classList.toggle("is-done", i < n); b.classList.remove("is-on"); });
      void bEls[n].offsetWidth; bEls[n].classList.add("is-on");
      nameEl.textContent = cases[n].name; tagsEl.textContent = cases[n].tags; urlEl.textContent = cases[n].url;
      clearTimeout(timer);
      if (!REDUCED) timer = setTimeout(() => show((cur + 1) % cases.length), DUR);
    };
    bEls.forEach((b, i) => b.addEventListener("click", () => show(i)));
    measure(); show(0);
    document.fonts && document.fonts.ready.then(measure);
  }

  // depth: layers drift a little with the cursor
  const stage = document.querySelector(".stage");
  if (stage && !REDUCED && matchMedia("(hover: hover)").matches) {
    addEventListener("pointermove", (e) => {
      stage.style.setProperty("--px", (e.clientX / innerWidth - .5).toFixed(3));
      stage.style.setProperty("--py", (e.clientY / innerHeight - .5).toFixed(3));
    }, { passive: true });
  }

  /* ---------- counters ---------- */
  const run = (el) => {
    const end = +el.dataset.count, dur = 1500, t0 = performance.now();
    const fmt = (n) => (end >= 1000 ? n.toLocaleString("en-US") : String(n));
    if (REDUCED) { el.textContent = fmt(end); return; }
    const step = (t) => {
      const k = Math.min(1, (t - t0) / dur);
      el.textContent = fmt(Math.round(end * (1 - Math.pow(1 - k, 4))));
      if (k < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  const io = new IntersectionObserver((es) => es.forEach((e) => {
    if (e.isIntersecting) { setTimeout(() => run(e.target), 700); io.unobserve(e.target); }
  }), { threshold: .3 });
  document.querySelectorAll("[data-count]:not([data-dec])").forEach((c) => io.observe(c));

  /* ---------- services: list drives the preview ---------- */
  const items = [...document.querySelectorAll(".svc__item")], vis = [...document.querySelectorAll(".svc > .svc__stage .vis")];
  const narrowMQ = matchMedia("(max-width: 1000px)");
  /* desktop: one open row drives the big preview. phones: rows open and close on their own,
     each with its own preview inside, so nothing above the tapped row ever moves */
  const setSvc = (n) => {
    items.forEach((it, i) => { it.classList.toggle("is-active", i === n); it.querySelector(".svc__btn").setAttribute("aria-expanded", String(i === n)); });
    vis.forEach((v, i) => v.classList.toggle("is-on", i === n));
    setTimeout(measure, 50);
  };
  items.forEach((it, i) => {
    const b = it.querySelector(".svc__btn");
    b.addEventListener("click", () => {
      if (narrowMQ.matches) { const open = !it.classList.contains("is-active"); it.classList.toggle("is-active", open); b.setAttribute("aria-expanded", String(open)); }
      else setSvc(i);
    });
    if (matchMedia("(hover: hover) and (min-width: 1001px)").matches) it.addEventListener("pointerenter", () => setSvc(i));
  });

  /* ---------- FAQ: smooth open and close ---------- */
  document.querySelectorAll(".acc__item").forEach((d) => {
    const sum = d.querySelector("summary"), body = d.querySelector(".acc__a");
    if (!sum || !body || REDUCED) return;
    let anim = null;
    sum.addEventListener("click", (e) => {
      e.preventDefault();
      if (anim) anim.cancel();
      if (!d.open) {
        d.open = true;
        const h = body.scrollHeight;
        anim = body.animate([{ height: "0px", opacity: 0 }, { height: h + "px", opacity: 1 }], { duration: 480, easing: "cubic-bezier(.16,1,.3,1)" });
        anim.onfinish = () => { anim = null; };
      } else {
        d.classList.add("is-closing");
        const h = body.offsetHeight;
        anim = body.animate([{ height: h + "px", opacity: 1 }, { height: "0px", opacity: 0 }], { duration: 340, easing: "cubic-bezier(.4,0,.2,1)" });
        anim.onfinish = () => { d.open = false; d.classList.remove("is-closing"); anim = null; };
        anim.oncancel = () => d.classList.remove("is-closing");
      }
    });
  });

  /* ---------- pause looping animations while their section is off screen ---------- */
  if ("IntersectionObserver" in window) {
    const offIO = new IntersectionObserver((es) => es.forEach((e) => e.target.classList.toggle("is-off", !e.isIntersecting)), { rootMargin: "120px 0px" });
    document.querySelectorAll("main > section, main > div, .foot").forEach((el) => offIO.observe(el));
  }

  /* ---------- reviews ----------
     Real client reviews from Upwork and Fiverr, quoted word for word (x = a shorter verbatim excerpt, marked with "…").
     Fields: ini (avatar letter), who, meta (project type and length), repeat (shows a "Repeat client" chip), text. */
  const reviews = /*REVIEWS*/[
   {
    "n": "Mark R.",
    "ini": "M",
    "role": "Agency owner",
    "d": "20+ projects",
    "src": "Upwork",
    "rep": true,
    "top": true,
    "t": "Mykola is a fantastic web designer. Our agency has hired him for 20+ different projects to design websites in Figma for a range of clients. The projects range from designs for small local businesses all the way through to international ecommerce brands. Mykola always sticks to the brief and will suggest any ideas he may have. He always takes feedback on board and makes any amendments swiftly. At the forefront of all of Mykola's designs are conversion rate optimisation techniques, to help drive enquiries and sales. These have been a game changer for our business and clients. We continue to work with Mykola on a monthly basis. I would highly recommend Mykola and his services to anyone looking for a professional designer.",
    "x": "Mykola is a fantastic web designer. Our agency has hired him for 20+ different projects… We continue to work with Mykola on a monthly basis."
   },
   {
    "n": "Andrei B.",
    "ini": "A",
    "role": "Owner",
    "d": "UX/UI design",
    "src": "Upwork",
    "rep": true,
    "top": true,
    "t": "We have contracted Mykola to redesign our company's website, and the result was fantastic! First and foremost, the website design looks incredibly modern, from the colors to the layout. We requested 5 pages initially, and Mykola delivered that with layout variation for both Mobile and Desktop, but also one of our pages had several tabs with different type of content, and Mykola went through and provided updated designs for each of those tabs. Overall I am very happy with his work, and continue using him today for further iteration and other projects. The biggest reason I would recommend working with Mykola, is that the design process with him feels just right. There is a great balance between his designer thinking and input/guidance provided by us when it comes to making updates.",
    "x": "We have contracted Mykola to redesign our company's website, and the result was fantastic! … The biggest reason I would recommend working with Mykola, is that the design process with him feels just right."
   },
   {
    "n": "mmmwyld",
    "ini": "M",
    "c": "Canada",
    "d": "2 weeks",
    "src": "Fiverr",
    "top": true,
    "t": "Working with our website designer was one of the best decisions we made this year. They didn't just “build a site” — they truly understood our business, our brand, and what we were trying to accomplish. The design is clean, modern, fast, and actually converts leads, which is something we struggled with before. Communication was excellent throughout the entire process. Deadlines were met, revisions were handled quickly, and every detail was thought through — from mobile usability to SEO basics and lead flow. If you're looking for someone who treats your business like their own and delivers real results, I would recommend them without hesitation.",
    "x": "Working with our website designer was one of the best decisions we made this year. … The design is clean, modern, fast, and actually converts leads, which is something we struggled with before."
   },
   {
    "n": "alexandrzakiyan",
    "ini": "A",
    "c": "United States",
    "d": "3 weeks · Webflow",
    "src": "Fiverr",
    "top": true,
    "t": "Outstanding work and communication! Mykola did an amazing job developing our website. He was always responsive, detail-oriented, and very patient throughout the entire process. He even recorded personalized video tutorials so we could manage our site ourselves — that was a game-changer! Highly recommend him to anyone looking for a professional and reliable web developer. Will definitely work with him again!",
    "x": "Mykola did an amazing job developing our website. … He even recorded personalized video tutorials so we could manage our site ourselves — that was a game-changer!"
   },
   {
    "n": "theborodin",
    "ini": "T",
    "c": "United States",
    "d": "4 weeks",
    "src": "Fiverr",
    "top": true,
    "t": "Mykola has delivered a highly professional, creative, and modern Website Design with 5 pages. This design was done in modern style, and many small bits from buttons, textboxes, product cards, etc, was custom designed by Mykola to match the overall theme. I worked with great designers before, and highly recommend Mykola.",
    "x": "Mykola has delivered a highly professional, creative, and modern Website Design with 5 pages. … I worked with great designers before, and highly recommend Mykola."
   },
   {
    "n": "raderin",
    "ini": "R",
    "c": "United States",
    "d": "4 weeks · Webflow",
    "src": "Fiverr",
    "top": true,
    "t": "Attentive, responsive, and patient as we had to work through some design changes. Appreciate the thoroughness, professionalism, and flexibility, coupled with great design skills and strong ability to get our site done. Thank you!! Worth it and you won't be disappointed."
   },
   {
    "n": "comladesas",
    "ini": "C",
    "c": "France",
    "d": "3 weeks",
    "src": "Fiverr",
    "top": true,
    "t": "I want to express my gratitude to Mykola for his excellent work. He showed great professionalism and listened to every one of our comments and requests. On some projects it's hard to make decisions and we need to try different options. Mykola handled this efficiently, professionally and quickly. Thank you very much for your commitment, and we won't hesitate to work with you again on future projects.",
    "x": "He showed great professionalism and listened to every one of our comments and requests. … we won't hesitate to work with you again on future projects.",
    "tr": "French"
   },
   {
    "n": "jacob_skyline",
    "ini": "J",
    "c": "United States",
    "d": "2 weeks · Webflow",
    "src": "Fiverr",
    "rep": true,
    "top": true,
    "t": "Mykola was exceptional to work with on this project. He is advanced in his coding knowledge and was able to complete the website from design in Figma all the way through to coding and completion."
   },
   {
    "n": "bob_lux",
    "ini": "B",
    "c": "Italy",
    "d": "8 days",
    "src": "Fiverr",
    "top": true,
    "t": "Happy with the work done by Mykola. He works fast, communicates well, and will continue working until you are satisfied with the result. He did a great job of incorporating my brand colors into the new website design, and I myself did not find them the easiest colors to work with. Visually appealing work. Well done Mykola, thank you.",
    "x": "He works fast, communicates well, and will continue working until you are satisfied with the result. He did a great job of incorporating my brand colors into the new website design…"
   },
   {
    "n": "mehrconsulting",
    "ini": "M",
    "c": "Austria",
    "d": "2 weeks",
    "src": "Fiverr",
    "rep": true,
    "top": true,
    "t": "This was not the first project with this seller and will not be in the last period. He has a very good eye for clean and modern design, and is very responsive, as well as clear and direct in his communications, which makes it a breeze to work together."
   },
   {
    "n": "samanthamgray",
    "ini": "S",
    "c": "United States",
    "d": "7 days",
    "src": "Fiverr",
    "top": true,
    "t": "Great project results! I'm really happy with how it turned out. Delivery was fast, and the creator is extremely professional and easy to work with. Will absolutely be hiring him for more opportunities and projects soon! Wouldn't hire anyone else for the job!"
   },
   {
    "n": "wojciech_farmer",
    "ini": "W",
    "c": "Canada",
    "d": "5 days",
    "src": "Fiverr",
    "top": true,
    "t": "Delivered super fast with a visually appealing design that clearly shows great experience and skill. Extremely responsive — revisions were done quickly until I was fully satisfied. Understood my requests perfectly and implemented them without any delay. Highly recommended for anyone needing quality work fast.",
    "x": "Delivered super fast with a visually appealing design that clearly shows great experience and skill. … Highly recommended for anyone needing quality work fast."
   },
   {
    "n": "markbarrettdev",
    "ini": "M",
    "c": "Ireland",
    "d": "6 days",
    "src": "Fiverr",
    "top": true,
    "t": "Mykola is great! He followed the brand guidelines very well and when I had a some things that I needed changing in terms of layout and content after I saw the first revision, he had no problem doing it until it was perfect!"
   },
   {
    "n": "jacob_skyline",
    "ini": "J",
    "c": "United States",
    "d": "3 weeks",
    "src": "Fiverr",
    "rep": true,
    "t": "Exceptional work! Our site design looks great, very well branded with the flexibility for us to add and change small things later on as the business evolves."
   },
   {
    "n": "aura_printing",
    "ini": "A",
    "c": "United States",
    "d": "6 weeks",
    "src": "Fiverr",
    "t": "Mykola T truly stood out in WEBSITE DESIGN with impeccable professionalism, an impressive level of creativity, and keen attention to detail. Working with him was a breeze. His politeness, cooperative nature, and timely delivery made the process SMOOTH and enjoyable!"
   },
   {
    "n": "Client on Upwork",
    "ini": "U",
    "d": "Figma, desktop & mobile",
    "src": "Upwork",
    "t": "Very good (western) design understanding, super quick in changes and revision! Definetly recommend working with Mykola."
   },
   {
    "n": "millerhawkins_p",
    "ini": "M",
    "c": "United States",
    "d": "5 weeks",
    "src": "Fiverr",
    "t": "He really did an incredible job on my site design. He was creative, but also gave me ample space to provide feedback and revisions. I would recommend him, and will be working with him again."
   },
   {
    "n": "willie6969",
    "ini": "W",
    "c": "United States",
    "d": "7 days",
    "src": "Fiverr",
    "t": "I would highly recommend using the services for Figma and other UX web design. his understanding of what elements are important is great. His design ability is awesome and his responsiveness is perfect."
   },
   {
    "n": "mvbeers",
    "ini": "M",
    "c": "Netherlands",
    "d": "8 days",
    "src": "Fiverr",
    "t": "I'm very happy with the website mockup. The seller was fast and flexible. He understood what I wanted and made a great design. He also made changes quickly when I asked. Thank you for the good work! I will order again."
   },
   {
    "n": "nicti1111",
    "ini": "N",
    "c": "Netherlands",
    "d": "3 days",
    "src": "Fiverr",
    "t": "Mykola was exceptionally nice to work with. Polite, professional and fast. Also, things went very smooth even though I am not tech savy at all. Will definitely return to him for more work. English very good. Highly recommended."
   },
   {
    "n": "jompeterson",
    "ini": "J",
    "c": "United States",
    "d": "3 days",
    "src": "Fiverr",
    "t": "Really great to work with. Even with confusion, he was patient with me and worked through any problems during the process. Very professional. I liked the end result too. Will definitely go through him again for future designs."
   },
   {
    "n": "karlyoungmedia",
    "ini": "K",
    "c": "United States",
    "d": "6 days",
    "src": "Fiverr",
    "t": "Mykola T truly IMPRESSED with his website design skills, going beyond what I imagined while emphasizing visual appeal and attention to detail. Working with him was seamless due to his deep understanding and proactive communication, ensuring everything was completed right on time."
   },
   {
    "n": "roll82",
    "ini": "R",
    "c": "Australia",
    "d": "3 weeks",
    "src": "Fiverr",
    "rep": true,
    "t": "Mykola T has A TRUE TALENT for website design! His creativity and visual appeal perfectly aligned with our brand, making the final product outstanding. Working with him was a delight, as his politeness and deep understanding meant he went above and beyond our expectations."
   },
   {
    "n": "roll82",
    "ini": "R",
    "c": "Australia",
    "d": "1 day",
    "src": "Fiverr",
    "rep": true,
    "t": "Mykola T delivered a visually stunning and creative website that perfectly aligned with our brand—truly impressive work! His proactive communication, quick turnaround, and seamless collaboration made the entire process a breeze. Highly recommend working with him!"
   },
   {
    "n": "jakubsj1",
    "ini": "J",
    "c": "United States",
    "d": "7 days",
    "src": "Fiverr",
    "t": "Mykola T truly always impresses with his website design skills, delivering work that is visually stunning and uniquely creative. Highly recommend his services!"
   },
   {
    "n": "thrive2024",
    "ini": "T",
    "c": "Canada",
    "d": "3 days",
    "src": "Fiverr",
    "rep": true,
    "t": "Always a pleasure to work with. The quality of work speaks for itself. Will be in touch for future projects! Thank you."
   },
   {
    "n": "audreymtn",
    "ini": "A",
    "c": "United States",
    "d": "5 days",
    "src": "Fiverr",
    "rep": true,
    "t": "very happy to have found a real partner to help design our new website"
   },
   {
    "n": "claudia_orr",
    "ini": "C",
    "c": "United Kingdom",
    "d": "1 day",
    "src": "Fiverr",
    "rep": true,
    "t": "I can never fault working with Mykola - he is beyond excellent!"
   },
   {
    "n": "markroberts721",
    "ini": "M",
    "c": "United Kingdom",
    "d": "5 days",
    "src": "Fiverr",
    "t": "Great service from Mykola. Highly recommended to anyone looking for a talented web designer."
   },
   {
    "n": "karstenj",
    "ini": "K",
    "c": "Germany",
    "d": "2 days",
    "src": "Fiverr",
    "t": "Thanks for the fine-tuned update to the site. Very quick turnaround, exactly what I had in mind, thanks!"
   },
   {
    "n": "synoagmbh",
    "ini": "S",
    "c": "Germany",
    "d": "1 day",
    "src": "Fiverr",
    "rep": true,
    "t": "Another project we did together. Again very happy with the result."
   },
   {
    "n": "maluve2462",
    "ini": "M",
    "c": "United States",
    "d": "1 day",
    "src": "Fiverr",
    "rep": true,
    "t": "Thanks for the quick delivery and your responsiveness looking forward to work on the next pages"
   },
   {
    "n": "steindlconsult",
    "ini": "S",
    "c": "Austria",
    "d": "5 days",
    "src": "Fiverr",
    "t": "I'm really very happy with the result. Thank you so much!"
   },
   {
    "n": "aamer_1986",
    "ini": "A",
    "c": "Saudi Arabia",
    "d": "4 days",
    "src": "Fiverr",
    "rep": true,
    "t": "Very good. Exceeded my expectation."
   },
   {
    "n": "vamvanderburg",
    "ini": "V",
    "c": "Netherlands",
    "d": "1 day",
    "src": "Fiverr",
    "t": "Perfect cooperation, recommended"
   },
   {
    "n": "audreymtn",
    "ini": "A",
    "c": "United States",
    "d": "11 days",
    "src": "Fiverr",
    "rep": true,
    "t": "Great collaboration! Definitely recommend"
   },
   {
    "n": "joe_epx",
    "ini": "J",
    "c": "United Kingdom",
    "d": "10 days",
    "src": "Fiverr",
    "top": true,
    "t": "Mykola was a pleasure to work with. First of all, the work is really good, it's creative, and in line with how our business wants to come across, whilst being different enough to stand out. Mykola was quick, thorough, and amenable to some feedback points, even if one or two of them were things we had missed off the requirements",
    "x": "First of all, the work is really good, it's creative, and in line with how our business wants to come across, whilst being different enough to stand out."
   },
   {
    "n": "agniusnark",
    "ini": "A",
    "c": "Canada",
    "d": "9 days",
    "src": "Fiverr",
    "rep": true,
    "top": true,
    "t": "Mykola is an incredible UI/UX designer. We have hired him for the second time and he delivered incredible results in a short period of time. I should mention his quick responding to messages even though we work on different parts of the world. 10/10"
   },
   {
    "n": "imranp88",
    "ini": "I",
    "c": "United States",
    "d": "7 days",
    "src": "Fiverr",
    "top": true,
    "t": "Delivered exactly to requirement and well inside of desired timelines. The work will enable further progress to continue on schedule and we'll be working together again in the future as more design services are needed. A+ partner, would highly recommend!"
   },
   {
    "n": "optident",
    "ini": "O",
    "c": "Spain",
    "d": "10 days",
    "src": "Fiverr",
    "top": true,
    "t": "I had the pleasure of working with Mykola on the redesign of our main marketplace page (optident.es) and I couldn't be more satisfied with the results. From start to finish, Mykola demonstrated exceptional skill, professionalism, and attention to detail."
   },
   {
    "n": "geardiscounter",
    "ini": "G",
    "c": "Netherlands",
    "d": "4 weeks",
    "src": "Fiverr",
    "t": "Mykola T delivered an OUTSTANDING website design that was both professional and perfectly aligned with our brand. His fluency and deep understanding made communication effortless, and he exceeded expectations with timely delivery. Highly recommend working with him!"
   },
   {
    "n": "fay_plut",
    "ini": "F",
    "c": "United States",
    "d": "4 weeks",
    "src": "Fiverr",
    "t": "Working with Mykola T was a very positive experience! His eagerness to please and patience through my many revisions made it a pleasure to work with him. He created a stunning visually appealing website that was exactly what we wanted. His website design really exceeded my expectations. Plus, his quick responsiveness and proactive communication and flexibility made the process smooth and enjoyable."
   },
   {
    "n": "profjohnk",
    "ini": "P",
    "c": "United States",
    "d": "4 weeks",
    "src": "Fiverr",
    "t": "Mykola T delivered an AMAZING design using our branding guidelines, showing exceptional creativity and professionalism. Communication was excellent, and he worked very quickly, ensuring we were satisfied with every element before finalizing. I HIGHLY recommend him and look forward to working with him again."
   },
   {
    "n": "nlagrange",
    "ini": "N",
    "c": "United States",
    "d": "2 weeks",
    "src": "Fiverr",
    "t": "Mykola's work is always outstanding! The design is creative and visually appealing, with great attention to detail. Working with him is a pleasure, thanks to his proactive communication and cooperative spirit. Highly recommended!"
   },
   {
    "n": "max_yar",
    "ini": "M",
    "c": "Ukraine",
    "d": "6 days · Webflow",
    "src": "Fiverr",
    "rep": true,
    "t": "Great experience working with Mykola again! The work was completed before the agreed deadline. I would like to point out his politeness, proactive communication, and attention to details. I highly recommend him as a high-level specialist. It was a pleasure to work with you!"
   },
   {
    "n": "max_yar",
    "ini": "M",
    "c": "Ukraine",
    "d": "10 days",
    "src": "Fiverr",
    "rep": true,
    "t": "Mykola was a pleasure to work with. I recommend him as a highly professional specialist, strong in communication, brand alignment, and design vision. The order was delivered on time, and I would like to compliment his politeness. I can't wait to place my next order. Thank you, Mykola!"
   },
   {
    "n": "f_yousu",
    "ini": "F",
    "c": "United States",
    "d": "5 days",
    "src": "Fiverr",
    "rep": true,
    "t": "He created something very visually appealing especially catered towards social media users coming to our website. Social media platforms are effective at keeping attention of their users but I believe the web page that was designed will engage users in the same way and therefore be effective in delivering the message of our company and lead to very little \"bounce\" rate. Excellent work, couldn't be happier with the result. Thank you."
   },
   {
    "n": "f_yousu",
    "ini": "F",
    "c": "United States",
    "d": "12 days",
    "src": "Fiverr",
    "rep": true,
    "t": "Mykola T delivered EXCEPTIONAL work on our website design project, exceeding expectations with their professionalism and meticulous attention to detail! The page is very clean and draws readers in clearly explaining what the business does."
   },
   {
    "n": "f_yousu",
    "ini": "F",
    "c": "United States",
    "d": "9 days",
    "src": "Fiverr",
    "rep": true,
    "t": "Mykola T brought true artistry to our web design project, blending creativity, exceeding expectations, and stellar visual appeal seamlessly. Working with them was a breeze, thanks to their proactive communication, lightning-fast responses, and swift delivery."
   },
   {
    "n": "m_kamile",
    "ini": "M",
    "c": "United Arab Emirates",
    "d": "3 weeks",
    "src": "Fiverr",
    "t": "Your cooperation was exceptional, truly professional, and deeply aligned with my vision. I am super happy with the work you've produced. Your responsiveness and amiable demeanor made the experience even more enjoyable. I eagerly anticipate the opportunity to collaborate again in the future."
   },
   {
    "n": "agniusnark",
    "ini": "A",
    "c": "Canada",
    "d": "11 days",
    "src": "Fiverr",
    "rep": true,
    "t": "It was my first time here on Fiverr and I am exceptionally happy with Mykola's design. He designed a home page for our website and it is stunning. Mykola is super responsive, extremely skilled and can come up with creative decisions which is impressive. Thank you so much for your time. I will always think of you when I will be in need for a graphic designer."
   },
   {
    "n": "mikekosk",
    "ini": "M",
    "c": "United States",
    "d": "7 days · Webflow",
    "src": "Fiverr",
    "t": "Fantastic to work with him. Super good turnaround with every revision, high high quality work, and he really understands what I wanted, but jazzing things up in his own style"
   },
   {
    "n": "julia_vitte_vu",
    "ini": "J",
    "c": "Netherlands",
    "d": "5 weeks",
    "src": "Fiverr",
    "t": "It was truly a pleasure to work with Mykola, he supported me so much with all the changes! Especially amazing was when I had limited knowledge on some things and he really helped understand them."
   },
   {
    "n": "divyajyotipatra",
    "ini": "D",
    "c": "United Kingdom",
    "d": "13 days",
    "src": "Fiverr",
    "t": "All the feedback was incorporated. The first design was different from expectation, Mykola did the complete design again and we really liked the end result."
   },
   {
    "n": "neoeon",
    "ini": "N",
    "c": "Australia",
    "d": "6 days",
    "src": "Fiverr",
    "t": "I had a design in my head and he nailed it on his first try, I will be coming back in the future, don't hesitate to use his services."
   },
   {
    "n": "plondyr",
    "ini": "P",
    "c": "Czech Republic",
    "d": "6 days",
    "src": "Fiverr",
    "rep": true,
    "t": "Mykola T is a top-tier website designer! His professionalism and creativity exceeded my expectations, and he nailed it with his language fluency and prompt delivery time. Working with him was a breeze—he went above and beyond!"
   },
   {
    "n": "ericaeym",
    "ini": "E",
    "c": "Singapore",
    "d": "4 days",
    "src": "Fiverr",
    "rep": true,
    "t": "Working with Mykola has been a pleasure. He always completes his work on time and responds very quickly to feedback and revisions. Will come back again for future projects."
   },
   {
    "n": "mrtonrsek",
    "ini": "M",
    "c": "Hungary",
    "d": "10 days",
    "src": "Fiverr",
    "rep": true,
    "t": "Professional graphics designer, it's our second order from him, we are more than happy with the result. Recommended to anyone who looking for a reliable Designer!"
   },
   {
    "n": "murrum2020",
    "ini": "M",
    "c": "United Kingdom",
    "d": "3 weeks",
    "src": "Fiverr",
    "rep": true,
    "t": "Another superb website created. Seller was extremely patient working around my schedules and delivered exactly what was required."
   },
   {
    "n": "jmcalisto",
    "ini": "J",
    "c": "Spain",
    "d": "12 days",
    "src": "Fiverr",
    "t": "Working with Mykola was easy. Would definitely recommend if you want a professional and effective designer!"
   },
   {
    "n": "hypescale",
    "ini": "H",
    "c": "Germany",
    "d": "8 days",
    "src": "Fiverr",
    "t": "I really enjoyed working with Mykola and I will continue working with him in the future."
   },
   {
    "n": "thiagowehbe",
    "ini": "T",
    "c": "Brazil",
    "d": "2 weeks",
    "src": "Fiverr",
    "t": "Very responsive and seller went above and beyond. Highly recommend him!"
   },
   {
    "n": "aamer_1986",
    "ini": "A",
    "c": "Saudi Arabia",
    "d": "11 days · Webflow",
    "src": "Fiverr",
    "rep": true,
    "t": "Very good, professional, fast and accommodative. Very happy to have worked with him."
   },
   {
    "n": "kamyabmohager",
    "ini": "K",
    "c": "United States",
    "d": "2 days",
    "src": "Fiverr",
    "t": "Very prompt, great quality work, and very creative"
   },
   {
    "n": "mrtonrsek",
    "ini": "M",
    "c": "Hungary",
    "d": "8 days",
    "src": "Fiverr",
    "rep": true,
    "t": "Very pleased with the seller, profesionnal design and understanding of the gig!"
   },
   {
    "n": "plondyr",
    "ini": "P",
    "c": "Czech Republic",
    "d": "3 days",
    "src": "Fiverr",
    "rep": true,
    "t": "Great designs as always!"
   },
   {
    "n": "synoagmbh",
    "ini": "S",
    "c": "Germany",
    "d": "12 days",
    "src": "Fiverr",
    "rep": true,
    "t": "Great work again."
   },
   {
    "n": "clark_jdc",
    "ini": "C",
    "c": "Singapore",
    "d": "3 weeks",
    "src": "Fiverr",
    "t": "Very easy to work with and delivered successfully!"
   },
   {
    "n": "artasca",
    "ini": "A",
    "c": "France",
    "d": "2 weeks",
    "src": "Fiverr",
    "t": "Many thanks, a pleasure to work with"
   },
   {
    "ini": "V",
    "c": "United States",
    "d": "2-week project",
    "t": "Extremely responsive and moved quickly. The website was exactly what I was looking for."
   },
   {
    "ini": "R",
    "c": "Austria",
    "d": "4-week project",
    "t": "Excellent work and great communication! I am very happy with the final result. … Communication was very good throughout the whole process. The final website turned out exactly the way I had imagined it."
   },
   {
    "ini": "S",
    "c": "Saudi Arabia",
    "d": "6-day project",
    "rep": true,
    "t": "Great outcome, quick and exactly what I wanted."
   },
   {
    "ini": "B",
    "c": "Uruguay",
    "d": "9-day project",
    "t": "The final product was great, but what really stood out was the excellent communication throughout the project as well as the willingness to adjust the product as we were working. Thanks!"
   },
   {
    "ini": "A",
    "c": "Hong Kong",
    "d": "13-day project",
    "rep": true,
    "t": "Very reliable, easy to communicate with, and always responded quickly when we had questions or wanted to make changes. … The final result turned out very well."
   },
   {
    "ini": "M",
    "c": "United States",
    "d": "3-week project",
    "rep": true,
    "t": "… an amazing job with our website. … It took very few rounds of feedback to get exactly what we were looking for."
   },
   {
    "ini": "P",
    "c": "Zimbabwe",
    "d": "7-day project",
    "rep": true,
    "t": "We going to work on many more projects. … the great work, great turn around time and highest quality work."
   },
   {
    "ini": "S",
    "c": "Iceland",
    "d": "7-day project",
    "t": "Very quick response time, and professional answers. … will 100% come back."
   },
   {
    "ini": "B",
    "c": "United States",
    "d": "2-week project",
    "rep": true,
    "t": "Efficient, polite, and understanding. … Understood the vision and executed our project perfectly."
   },
   {
    "ini": "J",
    "c": "United States",
    "d": "3-week project",
    "rep": true,
    "t": "There's few people that take pride in their work … I really love my new website."
   },
   {
    "ini": "M",
    "c": "Canada",
    "d": "4-day project",
    "rep": true,
    "t": "Listened carefully, moved fast, and delivered a beautiful design that truly reflects our brand. Highly recommend!"
   },
   {
    "ini": "S",
    "c": "Saudi Arabia",
    "d": "1-day project",
    "rep": true,
    "t": "Very professional and achieved exactly as promised."
   },
   {
    "ini": "P",
    "c": "Zimbabwe",
    "d": "3-week project",
    "rep": true,
    "t": "Great experience 10/10"
   }
  ]/*/REVIEWS*/;
  const initials = (n) => n.split(/\s+/).map((w) => w[0]).slice(0, 2).join("").toUpperCase();
  const esc = (t) => String(t).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const rvName = (r) => r.n || ("Client from " + (/^(United|Netherlands)/.test(r.c) ? "the " : "") + r.c);
  const rvSub = (r) => [r.role, r.n ? r.c : "", r.d].filter(Boolean).join(" · ");
  const rvTags = (r) => (r.src ? `<span class="rvx__tag rvx__tag--src" title="Verified ${esc(r.src)} review"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8.3l2.8 2.7L12.5 5"/></svg>${esc(r.src)}</span>` : "") + (r.rep ? '<span class="rvx__tag">Repeat client</span>' : "");
  const rvx = document.querySelector(".rvx");
  if (rvx) {
    const NAMED = reviews.filter((r) => r.n), F = NAMED.map((r, k) => (r.top ? k : -1)).filter((k) => k >= 0);
    const stage = rvx.querySelector(".rvx__stage"), by = rvx.querySelector(".rvx__by"), bars = rvx.querySelector(".rvx__bars");
    const count = rvx.querySelector(".rvx__count b"), strip = document.querySelector(".rvx__strip");
    // every quote sits in the same grid cell, so the card is as tall as the longest one and never jumps
    stage.innerHTML = NAMED.map((r, k) => `<blockquote class="rvx__q" data-k="${k}"><p>${esc(r.x || r.t)}</p>${r.tr ? `<small>Translated from ${esc(r.tr)}</small>` : ""}</blockquote>`).join("");
    bars.innerHTML = F.map((_, n) => `<button type="button" aria-label="Review ${n + 1}" data-f="${n}"><i></i></button>`).join("");
    const card = (r, k) => `<button type="button" class="rvx__mini" data-k="${k}"><span class="rvx__ava">${esc(r.ini)}</span><span class="rvx__mt"><b>${esc(rvName(r))}${r.src ? `<em>${esc(r.src)}</em>` : ""}</b><span>${esc(r.t)}</span></span></button>`;
    const minis = NAMED.map(card).join("");
    strip.innerHTML = `<div class="rvx__track">${minis}<div aria-hidden="true" style="display:contents">${minis.replace(/<button /g, '<button tabindex="-1" ')}</div></div>`;
    const qs = [...stage.children], bs = [...bars.children];
    let cur = -1, pos = -1, timer = 0, paused = false;
    const DUR = 8000;
    const show = (k) => {
      if (k === cur) return;
      const r = NAMED[k], f = F.indexOf(k);
      if (f >= 0) pos = f;
      qs.forEach((q, n) => q.classList.toggle("is-on", n === k));
      bs.forEach((x, n) => { x.classList.toggle("is-on", n === f); x.classList.toggle("is-done", n < pos && f >= 0); });
      by.innerHTML = `<span class="rvx__ava rvx__ava--lg">${esc(r.ini)}</span><span class="rvx__who"><b>${esc(rvName(r))}</b><span>${esc(rvSub(r))}</span></span><span class="rvx__tags">${rvTags(r)}</span>`;
      count.textContent = String(pos + 1).padStart(2, "0");
      cur = k; restart();
    };
    const step = (d) => { pos = (pos + d + F.length) % F.length; show(F[pos]); };
    const restart = () => {
      clearTimeout(timer);
      rvx.style.setProperty("--rvx-dur", DUR + "ms");
      bars.classList.remove("run"); void bars.offsetWidth; bars.classList.add("run");
      if (!REDUCED && !paused) timer = setTimeout(() => step(1), DUR);
    };
    const pause = (on) => { paused = on; rvx.classList.toggle("is-paused", on); if (on) clearTimeout(timer); else restart(); };
    rvx.querySelectorAll("[data-dir]").forEach((b) => b.addEventListener("click", () => step(+b.dataset.dir)));
    bars.addEventListener("click", (e) => { const b = e.target.closest("[data-f]"); if (b) { pos = +b.dataset.f; show(F[pos]); } });
    strip.addEventListener("click", (e) => { const b = e.target.closest("[data-k]"); if (b) { show(+b.dataset.k); rvx.scrollIntoView({ behavior: REDUCED ? "auto" : "smooth", block: "center" }); } });
    const main = rvx.querySelector(".rvx__main");
    main.addEventListener("pointerenter", (e) => { if (e.pointerType === "mouse") pause(true); });
    main.addEventListener("pointerleave", (e) => { if (e.pointerType === "mouse") pause(false); });
    main.addEventListener("focusin", () => pause(true)); main.addEventListener("focusout", () => pause(false));
    main.addEventListener("keydown", (e) => { if (e.key === "ArrowRight") step(1); if (e.key === "ArrowLeft") step(-1); });
    let sx = 0;
    main.addEventListener("touchstart", (e) => { sx = e.touches[0].clientX; }, { passive: true });
    main.addEventListener("touchend", (e) => { const dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 40) step(dx < 0 ? 1 : -1); }, { passive: true });
    new IntersectionObserver((es) => es.forEach((en) => { if (en.isIntersecting) { if (cur < 0) { pos = 0; show(F[0]); } else if (!paused) restart(); } else clearTimeout(timer); })).observe(rvx);
  }

  /* ---------- reveal on scroll ---------- */
  const rio = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); rio.unobserve(e.target); } }), { threshold: 0, rootMargin: "0px 0px -10% 0px" });
  document.querySelectorAll("[data-reveal]").forEach((el) => rio.observe(el));
  /* safety net for fast flicks: anything already scrolled past is shown */
  let revT = 0;
  const sweep = () => { revT = 0; document.querySelectorAll("[data-reveal]:not(.in)").forEach((el) => { if (el.getBoundingClientRect().top < innerHeight * .9) { el.classList.add("in"); rio.unobserve(el); } }); };
  addEventListener("scroll", () => { if (!revT) revT = setTimeout(sweep, 200); }, { passive: true });

  /* ---------- footer clock (studio time) ---------- */
  const clock = document.querySelector(".clock");
  if (clock) {
    const tick = () => { clock.textContent = new Intl.DateTimeFormat("en-GB", { hour: "2-digit", minute: "2-digit", timeZone: "Europe/Madrid" }).format(new Date()); };
    tick(); setInterval(tick, 30000);
  }
  const yr = document.querySelector(".year"); if (yr) yr.textContent = new Date().getFullYear();

  /* ---------- brief form ----------
     FORM_ENDPOINT: paste a form service URL here to receive briefs straight to your inbox
     (e.g. Web3Forms "https://api.web3forms.com/submit" + FORM_KEY, or a Formspree URL).
     While it's empty, submitting opens the visitor's email app with the brief already written. */
  const FORM_ENDPOINT = "https://api.web3forms.com/submit";
  const FORM_KEY = "7235f83a-d867-455b-9959-4e51983e0b64";
  const TO_EMAIL = "hello@sorvel.agency";
  const form = document.getElementById("brief");
  if (form) {
    const msg = form.querySelector(".brief__msg"), done = form.querySelector(".brief__done");
    const fieldOf = (el) => el.closest(".field");
    const f = (n) => form.elements.namedItem(n);
    form.addEventListener("input", (e) => { const fl = e.target.closest(".field"); if (fl) fl.classList.remove("is-bad"); });

    /* two-step brief: contact details first, project details second */
    const okEmail = (v) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim());
    const rows = [...form.children];
    const firstRow = form.querySelector(":scope > .brief__row"), company = f("company") && f("company").closest(".field");
    let goStep = () => {};
    if (firstRow && company) {
      const head = document.createElement("div");
      head.className = "bsteps";
      head.innerHTML = '<p class="bsteps__lbl">Step <b>1</b> of 2</p><div class="bsteps__bar" aria-hidden="true"><i class="is-on"></i><i></i></div><h3 class="bsteps__title">Your details</h3>';
      const s1 = document.createElement("div"); s1.className = "bstep bstep--1";
      const s2 = document.createElement("div"); s2.className = "bstep bstep--2"; s2.hidden = true;
      const keep = (el) => el.matches(".picked, .brief__msg, .brief__done, input[type=hidden], script, .hp");
      const picked = form.querySelector(":scope > .picked");
      (picked || firstRow).before(head);
      if (picked) head.after(picked);
      firstRow.before(s1);
      s1.append(firstRow, company);
      const cont = document.createElement("div"); cont.className = "bstep__go";
      cont.innerHTML = '<button class="btn btn--primary btn--lg bstep__next" type="button"><span class="btn__roll"><span data-text="Continue">Continue</span></span><span class="btn__arrow" aria-hidden="true"><svg viewBox="0 0 20 20"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg><svg viewBox="0 0 20 20"><path d="M4 10h11m-4.5-4.5L15 10l-4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg></span></button>' +
        '<p class="bstep__note">Two short steps, about a minute. Your details stay private. <a href="' + (location.pathname.includes("/work/") || location.pathname.includes("/services/") ? "../" : "") + 'privacy.html">Privacy policy</a></p>';
      s1.append(cont);
      s1.after(s2);
      [...form.children].filter((el) => el !== head && el !== s1 && el !== s2 && !keep(el)).forEach((el) => s2.append(el));
      const foot = s2.querySelector(".brief__foot");
      const back = document.createElement("button"); back.type = "button"; back.className = "bstep__back"; back.innerHTML = '<span aria-hidden="true">←</span> Back';
      if (foot) foot.prepend(back);
      const lbl = head.querySelector("b"), bars = head.querySelectorAll(".bsteps__bar i"), title = head.querySelector(".bsteps__title");
      let partialSent = false;
      goStep = (n, focus) => {
        s1.hidden = n !== 1; s2.hidden = n !== 2;
        lbl.textContent = n; bars[1].classList.toggle("is-on", n === 2);
        title.textContent = n === 1 ? "Your details" : "Your project";
        form.dataset.step = n;
        if (focus) {
          const top = form.getBoundingClientRect().top;
          if (top < 60 || top > 220) scrollTo({ top: top + scrollY - 100, behavior: "smooth" });
          const first = n === 1 ? f("name") : s2.querySelector("input, select, textarea");
          first && first.focus({ preventScroll: true });
        }
      };
      const next = () => {
        msg.textContent = "";
        const bad = [];
        if (!f("name").value.trim()) bad.push(f("name"));
        if (!okEmail(f("email").value)) bad.push(f("email"));
        bad.forEach((el) => fieldOf(el).classList.add("is-bad"));
        if (bad.length) { msg.textContent = "Please add your name and a valid email."; bad[0].focus(); return; }
        if (!partialSent) track("brief_start");
        if (FORM_ENDPOINT && !partialSent) {
          partialSent = true;
          fetch(FORM_ENDPOINT, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" },
            body: JSON.stringify({ access_key: FORM_KEY || undefined, subject: "Started a brief: " + f("name").value.trim(), from_name: "Sorvel website",
              name: f("name").value.trim(), email: f("email").value.trim(), company: f("company").value.trim(), plan: (f("plan") && f("plan").value) || "", note: "Step 1 only so far" }) }).catch(() => {});
        }
        goStep(2, true);
      };
      cont.querySelector(".bstep__next").addEventListener("click", next);
      s1.addEventListener("keydown", (e) => { if (e.key === "Enter" && e.target.tagName === "INPUT") { e.preventDefault(); next(); } });
      back.addEventListener("click", () => goStep(1, true));
      form.addEventListener("reset", () => setTimeout(() => goStep(1), 0));
      goStep(1);
    }
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      msg.textContent = "";
      if (f("botcheck").value) return;
      const bad = [];
      if (!f("name").value.trim()) bad.push(f("name"));
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f("email").value.trim())) bad.push(f("email"));
      if (f("details").value.trim().length < 10) bad.push(f("details"));
      bad.forEach((el) => fieldOf(el).classList.add("is-bad"));
      if (bad.length) { if (bad[0] !== f("details")) goStep(1); msg.textContent = "Please add a few words about the project."; bad[0].focus(); return; }

      const needs = [...form.querySelectorAll('input[name="need"]:checked')].map((i) => i.value).join(", ") || "Not specified";
      const timeline = form.querySelector('input[name="timeline"]:checked')?.value || "Not specified";
      const opt = (n) => (f(n) && f(n).value) || "";
      const data = { name: f("name").value.trim(), email: f("email").value.trim(), company: f("company").value.trim(), plan: opt("plan"), needs, timeline, platform: opt("platform"), budget: opt("budget"), details: f("details").value.trim() };
      const showDone = () => { done.hidden = false; form.reset(); form.querySelectorAll(".is-bad").forEach((x) => x.classList.remove("is-bad")); };

      if (!FORM_ENDPOINT) {
        const body = `Name: ${data.name}\nEmail: ${data.email}\nCompany: ${data.company || "-"}\nPicked on the site: ${data.plan || "-"}\nNeeds: ${data.needs}\nPlatform: ${data.platform || "-"}\nBudget: ${data.budget || "-"}\nStart: ${data.timeline}\n\n${data.details}`;
        location.href = `mailto:${TO_EMAIL}?subject=${encodeURIComponent((data.plan ? "[" + data.plan.split(" (")[0] + "] " : "") + "New project brief from " + data.name)}&body=${encodeURIComponent(body)}`;
        setTimeout(showDone, 600);
        return;
      }
      form.classList.add("is-sending");
      try {
        const res = await fetch(FORM_ENDPOINT, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" },
          body: JSON.stringify({ access_key: FORM_KEY || undefined, subject: (data.plan ? "[" + data.plan.split(" (")[0] + "] " : "") + "New project brief from " + data.name, from_name: "Sorvel website", ...data }) });
        if (!res.ok) throw new Error(res.status);
        track("brief");
        showDone();
      } catch (err) {
        msg.innerHTML = `Something went wrong. Please email <a href="mailto:${TO_EMAIL}">${TO_EMAIL}</a> or write on Telegram.`;
      } finally { form.classList.remove("is-sending"); }
    });
  }

  /* ---------- mobile menu ---------- */
  const burger = document.querySelector(".nav__burger"), mnav = document.getElementById("mnav");
  if (burger && mnav) {
    const root = document.documentElement;
    const isOpen = () => root.classList.contains("menu-open");
    const set = (open) => {
      root.classList.toggle("menu-open", open);
      burger.setAttribute("aria-expanded", String(open));
      burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      if (open) mnav.removeAttribute("inert"); else mnav.setAttribute("inert", "");
    };
    burger.addEventListener("click", () => set(!isOpen()));
    mnav.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => set(false)));
    addEventListener("keydown", (e) => { if (e.key === "Escape" && isOpen()) { set(false); burger.focus(); } });
    matchMedia("(min-width: 761px)").addEventListener("change", (e) => { if (e.matches) set(false); });
    addEventListener("pageshow", (e) => { if (e.persisted) set(false); });
    const acc = mnav.querySelector(".mnav__acc");
    acc && acc.addEventListener("click", () => {
      const open = acc.getAttribute("aria-expanded") !== "true";
      acc.setAttribute("aria-expanded", String(open));
      acc.closest("li").classList.toggle("is-open", open);
    });
  }
})();
