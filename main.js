/* =========================================================
   AEVA.sg  ·  site engine
   Edit SITE once and it updates every page.
   ========================================================= */
/* ---------- Language ---------- */
const LANG = (document.documentElement.lang || "en").toLowerCase().startsWith("zh") ? "zh" : "en";
const BASE = LANG === "zh" ? "../" : "";
const T = {
  en: { home: "Home", about: "About", services: "Services", designs: "Designs", contact: "Contact",
        menu: "Menu", close: "Close", visit: "Visit the showroom", view: "View", loader: "Built by hand",
        gotHome: "Got a home in mind?", startConv: "Start a conversation", explore: "Explore", contactH: "Contact",
        showroom: "Showroom", follow: "Follow", switchTo: "中文", switchLabel: "切换到中文",
        hours: "Mon to Sat, 10am to 7pm", holidays: "Closed on all major public holidays",
        waGeneral: "Hi AEVA, I'd like to find out more...", waAlan: "Hi Alan, I'd like to book a free consultation.",
        homeAria: "AEVA home", waAria: "WhatsApp AEVA", on: "AEVA on" },
  zh: { home: "首页", about: "关于我们", services: "服务", designs: "设计", contact: "联系我们",
        menu: "菜单", close: "关闭", visit: "参观展厅", view: "查看", loader: "匠心手作",
        gotHome: "心中有理想的家？", startConv: "开始对话", explore: "浏览", contactH: "联系",
        showroom: "展厅", follow: "关注我们", switchTo: "EN", switchLabel: "Switch to English",
        hours: "周一至周六，上午10点至晚上7点", holidays: "所有主要公共假期休息",
        waGeneral: "你好 AEVA，我想了解更多...", waAlan: "你好 Alan，我想预约免费咨询。",
        homeAria: "AEVA 首页", waAria: "WhatsApp 联系 AEVA", on: "AEVA" }
}[LANG];

const SITE = {
  phoneDisplay: "+65 8040 5577",
  whatsapp: "6580405577",
  email: "inquiries@aeva.sg",
  address: ["Oxley Bizhub #1", "65 Ubi Road 1", "#04-29", "Singapore 408729"],
  maps: "https://www.google.com/maps/search/?api=1&query=Oxley+Bizhub+65+Ubi+Road+1+Singapore+408729",
  hours: T.hours,
  holidays: T.holidays,
  uen: "202625649E",
  instagram: "https://instagram.com/aevacarpentry",
  facebook: "coming-soon.html?p=facebook",
  tiktok: "coming-soon.html?p=tiktok",
  youtube: "coming-soon.html?p=youtube"
};

SITE.studio = SITE.address.join(", ");
const addressHTML = () => SITE.address.join("<br>");

const NAV = [
  ["index.html", T.home, BASE + "images/showroom.jpg"],
  ["about.html", T.about, BASE + "images/about-workshop.jpg"],
  ["services.html", T.services, BASE + "images/service-carpentry.jpg"],
  ["designs.html", T.designs, BASE + "images/projects/treehouse-loft-1.jpg"],
  ["contact.html", T.contact, BASE + "images/showroom.jpg"]
];

/* ---------- Social icons ---------- */
const ICONS = {
  instagram: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r=".9" fill="currentColor" stroke="none"/></svg>',
  facebook: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7.6h2.6l.4-3h-3V8.5c0-.9.3-1.5 1.6-1.5h1.6V4.3c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.9v3h2.6V21h3z"/></svg>',
  tiktok: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.6 3c.4 2.3 1.8 3.8 4 4v3.1a7.3 7.3 0 0 1-4-1.2v6.3A5.6 5.6 0 1 1 11 9.6v3.2a2.5 2.5 0 1 0 2.3 2.5V3h3.3z"/></svg>',
  youtube: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.6 7.2a2.6 2.6 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.6 2.6 0 0 0 2.4 7.2 27 27 0 0 0 2 12a27 27 0 0 0 .4 4.8 2.6 2.6 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.6 2.6 0 0 0 1.8-1.8A27 27 0 0 0 22 12a27 27 0 0 0-.4-4.8zM10 15V9l5.2 3L10 15z"/></svg>'
};
const SOCIAL_ORDER = [["tiktok", "TikTok"], ["instagram", "Instagram"], ["facebook", "Facebook"], ["youtube", "YouTube"]];
const socialsHTML = (cls = "socials") => `<div class="${cls}">${SOCIAL_ORDER.map(([k, n]) => `<a href="${SITE[k]}"${/^https?:/.test(SITE[k]) ? ' target="_blank" rel="noopener"' : ""} aria-label="AEVA on ${n}">${ICONS[k]}</a>`).join("")}</div>`;

/* ---------- AEVA mark ---------- */
let _lid = 0;
function logoSVG({ tagline = false, draw = false } = {}) {
  const id = "aevaG" + _lid++;
  const h = tagline ? 112 : 78;
  const s = draw ? ` class="stroke" pathLength="1"` : "";
  const g = draw ? ` class="stroke gold" pathLength="1"` : ` class="gold"`;
  return `<svg viewBox="0 0 400 ${h}" aria-hidden="true" fill="none">
    <defs><linearGradient id="${id}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e2c789"/><stop offset=".5" stop-color="#b8955a"/><stop offset="1" stop-color="#7f6230"/></linearGradient></defs>
    <g stroke-width="6">
      <polyline${g} points="12,72 46,6 80,72" stroke="url(#${id})"/>
      <line${s} x1="124" y1="9" x2="178" y2="9" stroke="currentColor"/>
      <line${s} x1="128" y1="39" x2="174" y2="39" stroke="currentColor"/>
      <line${s} x1="124" y1="69" x2="178" y2="69" stroke="currentColor"/>
      <polyline${s} points="222,6 256,72 290,6" stroke="currentColor"/>
      <polyline${g} points="320,72 354,6 388,72" stroke="url(#${id})"/>
    </g>
    ${tagline ? `<text x="200" y="104" text-anchor="middle" font-family="Jost, Arial, sans-serif" font-size="12.5" letter-spacing="7.6" fill="currentColor">BUILT FOR GENERATIONS</text>` : ""}
  </svg>`;
}

const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const page = (location.pathname.split("/").pop() || "index.html").replace(/\.html$/, "") || "index";
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
const fine = matchMedia("(hover: hover) and (pointer: fine)").matches;
const hasGSAP = typeof gsap !== "undefined" && typeof ScrollTrigger !== "undefined";
if (hasGSAP && !reduce) document.documentElement.classList.add("js");

/* ---------- Shell: header, menu, footer, overlays ---------- */
(function shell() {
  const isActive = (f) => f.replace(/\.html$/, "") === page;

  document.body.insertAdjacentHTML("afterbegin", `
    <div class="loader" aria-hidden="true">
      <div class="ld">
        <div class="ld-num"><span class="n">0</span><span class="pc">%</span></div>
        <svg class="ld-line" viewBox="0 0 240 14" fill="none">
          <path class="track" d="M3 8 C 38 5.5, 66 9.5, 104 7 S 170 4.5, 206 7.5 S 232 8.5, 237 6.5"/>
          <path class="fill" pathLength="1" d="M3 8 C 38 5.5, 66 9.5, 104 7 S 170 4.5, 206 7.5 S 232 8.5, 237 6.5"/>
        </svg>
        <span class="ld-cap">${T.loader}</span>
      </div>
    </div>
    <div class="curtain" aria-hidden="true"></div>
    <div class="cursor" aria-hidden="true"><div class="ring"><span>${T.view}</span></div><div class="dot"></div></div>
    <div class="preview" aria-hidden="true"><div class="ph"><i></i></div></div>
    <header class="site-head">
      <a href="index.html" class="logo" aria-label="${T.homeAria}">${logoSVG()}</a>
      <div class="head-r">
        <a class="lang-sw" href="#" lang="${LANG === "zh" ? "en" : "zh"}" aria-label="${T.switchLabel}">${T.switchTo}</a>
        <button class="menu-btn" aria-expanded="false" aria-controls="menu"><span class="t"><b>${T.menu}</b><b>${T.close}</b></span><span class="bars"></span></button>
      </div>
    </header>
    <div class="menu" id="menu">
      <nav>${NAV.map(([f, n, img], i) => `<a href="${f}" data-img="${img}" class="${isActive(f) ? "active" : ""}"><span class="num">0${i + 1}</span><span class="w">${n}</span></a>`).join("")}</nav>
      <aside>
        <div class="ph"><i style="--img:url('${BASE}images/showroom.jpg')"></i></div>
        <span class="label gold">${T.visit}</span>
        <p><a href="${SITE.maps}" target="_blank" rel="noopener">${addressHTML()}</a><br><br>${SITE.hours}<br><span class="hol">${SITE.holidays}</span></p>
        <p><a href="https://wa.me/${SITE.whatsapp}">WhatsApp ${SITE.phoneDisplay}</a><br><a href="mailto:${SITE.email}">${SITE.email}</a></p>
        ${socialsHTML()}
      </aside>
    </div>`);

  const foot = $("#site-footer");
  if (foot) {
    foot.className = "site-foot";
    foot.innerHTML = `
      <div class="ftop">
        <div><h4>${T.gotHome}</h4><a href="contact.html" class="link">${T.startConv} <span class="arr"></span></a></div>
        <div><h4>${T.explore}</h4><ul>${NAV.map(([f, n]) => `<li><a href="${f}">${n}</a></li>`).join("")}</ul></div>
        <div><h4>${T.contactH}</h4><ul>
          <li><a href="https://wa.me/${SITE.whatsapp}">WhatsApp</a></li>
          <li><a href="mailto:${SITE.email}">${SITE.email}</a></li>
          <li>${SITE.hours}<br><span class="hol">${SITE.holidays}</span></li></ul>
          <h4 style="margin-top:34px">${T.showroom}</h4>
          <a href="${SITE.maps}" target="_blank" rel="noopener">${addressHTML()}</a></div>
        <div><h4>${T.follow}</h4>${socialsHTML()}</div>
      </div>
      <div class="legal"><span>© ${new Date().getFullYear()} AEVA Private Limited · UEN ${SITE.uen}</span><span>${SITE.studio}</span></div>`;
  }

  document.body.insertAdjacentHTML("beforeend", socialsHTML("socials social-rail"));
  $$(".hero-min").forEach((h) => h.insertAdjacentHTML("beforeend", socialsHTML("socials socials-mobile")));

  const wa = document.createElement("a");
  wa.className = "wa";
  wa.href = `https://wa.me/${SITE.whatsapp}?text=${encodeURIComponent(T.waGeneral)}`;
  wa.setAttribute("aria-label", T.waAria);
  wa.innerHTML = `<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>`;
  document.body.appendChild(wa);

  $$("[data-logo]").forEach((el) => {
    const o = el.dataset.logo;
    el.innerHTML = logoSVG({ draw: o.includes("draw"), tagline: o.includes("tagline") });
  });

  $$("[data-wa]").forEach((el) => { el.href = `https://wa.me/${SITE.whatsapp}?text=${encodeURIComponent(T.waAlan)}`; el.target = "_blank"; el.rel = "noopener"; });
  $$(".lang-sw").forEach((a) => {
    const file = location.pathname.split("/").pop() || "index.html";
    a.href = (LANG === "zh" ? "../" : "zh/") + file + location.search + location.hash;
  });
  $$("[data-maps]").forEach((el) => { el.href = SITE.maps; el.target = "_blank"; el.rel = "noopener"; });

  $$("[data-site]").forEach((el) => {
    const k = el.dataset.site;
    if (k === "whatsappLink") { el.href = `https://wa.me/${SITE.whatsapp}`; el.textContent = SITE.phoneDisplay; }
    else if (k === "emailLink") { el.href = `mailto:${SITE.email}`; el.textContent = SITE.email; }
    else if (k === "address") { el.innerHTML = `<a href="${SITE.maps}" target="_blank" rel="noopener">${addressHTML()}</a>`; }
    else if (SITE[k]) el.textContent = SITE[k];
  });
})();

/* ---------- Smooth scroll ---------- */
let lenis = null;
if (!reduce && typeof Lenis !== "undefined") {
  lenis = new Lenis({ lerp: 0.085, wheelMultiplier: 0.95 });
  if (hasGSAP) {
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add((t) => lenis.raf(t * 1000));
    gsap.ticker.lagSmoothing(0);
  } else {
    const raf = (t) => { lenis.raf(t); requestAnimationFrame(raf); };
    requestAnimationFrame(raf);
  }
}

/* ---------- Menu ---------- */
(function menu() {
  const btn = $(".menu-btn");
  const aside = $(".menu aside .ph i");
  const setOpen = (open) => {
    document.documentElement.classList.toggle("menu-open", open);
    btn.setAttribute("aria-expanded", open);
    if (lenis) open ? lenis.stop() : lenis.start();
  };
  btn.addEventListener("click", () => setOpen(!document.documentElement.classList.contains("menu-open")));
  addEventListener("keydown", (e) => e.key === "Escape" && setOpen(false));
  $$(".menu nav a").forEach((a) => a.addEventListener("mouseenter", () => aside.style.setProperty("--img", `url('${a.dataset.img}')`)));
})();

/* ---------- Cursor + hover preview ---------- */
(function cursor() {
  if (!fine) return;
  document.body.classList.add("has-cursor");
  const c = $(".cursor"), dot = $(".dot", c), ring = $(".ring", c), lab = $("span", ring);
  const pv = $(".preview"), pvi = $(".preview i");
  let mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my, px = mx, py = my;
  addEventListener("mousemove", (e) => { mx = e.clientX; my = e.clientY; }, { passive: true });
  (function loop() {
    rx += (mx - rx) * 0.16; ry += (my - ry) * 0.16;
    px += (mx - px) * 0.1; py += (my - py) * 0.1;
    dot.style.transform = `translate(${mx}px,${my}px)`;
    ring.style.left = rx + "px"; ring.style.top = ry + "px";
    pv.style.transform = `translate(${px + 30}px,${py - pv.offsetHeight / 2}px) rotate(${(mx - px) * 0.04}deg)`;
    requestAnimationFrame(loop);
  })();
  document.addEventListener("mouseover", (e) => {
    const t = e.target.closest("[data-cursor]");
    c.classList.toggle("big", !!t);
    if (t) lab.textContent = t.dataset.cursor;
    const p = e.target.closest("[data-preview]");
    if (p) { pvi.style.setProperty("--img", `url('${p.dataset.preview}')`); pv.classList.add("on"); }
    else pv.classList.remove("on");
  });
})();

/* Dim sibling rows when hovering a project index */
document.addEventListener("mouseover", (e) => {
  $$(".index").forEach((ix) => ix.classList.toggle("dim", ix.contains(e.target) && !!e.target.closest(".irow")));
});

/* ---------- Page transitions ---------- */
(function transitions() {
  const curtain = $(".curtain");
  const arrived = sessionStorage.getItem("aeva-nav") === "1";
  sessionStorage.removeItem("aeva-nav");
  if (arrived && hasGSAP && !reduce) {
    document.documentElement.classList.add("no-loader");
    gsap.fromTo(curtain, { clipPath: "inset(0% 0% 0% 0%)" }, { clipPath: "inset(0% 0% 100% 0%)", duration: 1.1, ease: "expo.inOut", delay: 0.05 });
  }
  addEventListener("pageshow", (e) => { if (e.persisted && hasGSAP) gsap.set(curtain, { clipPath: "inset(100% 0% 0% 0%)" }); });
  document.addEventListener("click", (e) => {
    const a = e.target.closest("a");
    if (!a || !hasGSAP || reduce) return;
    const href = a.getAttribute("href") || "";
    if (a.target === "_blank" || e.metaKey || e.ctrlKey || e.shiftKey || href.startsWith("#") || href.startsWith("mailto:") || href.startsWith("tel:") || /^https?:/.test(href)) return;
    if (!/\.html(\?|#|$)/.test(href)) return;
    e.preventDefault();
    document.documentElement.classList.remove("menu-open");
    sessionStorage.setItem("aeva-nav", "1");
    gsap.fromTo(curtain, { clipPath: "inset(100% 0% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.9, ease: "expo.inOut", onComplete: () => (location.href = href) });
  });
})();

/* ---------- Text splitting ---------- */
function splitWords(el, cls = "line") {
  const walk = (node) => {
    [...node.childNodes].forEach((n) => {
      if (n.nodeType === 3) {
        const frag = document.createDocumentFragment();
        (n.textContent.match(/[\u2E80-\u9FFF\uF900-\uFAFF\uFF00-\uFFEF\u3000-\u303F]|[^\s\u2E80-\u9FFF\uF900-\uFAFF\uFF00-\uFFEF\u3000-\u303F]+|\s+/g) || []).forEach((part) => {
          if (!part) return;
          if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(" ")); return; }
          const outer = document.createElement("span");
          outer.className = cls;
          outer.style.display = "inline-block";
          const inner = document.createElement("span");
          inner.textContent = part;
          outer.appendChild(inner);
          frag.appendChild(outer);
        });
        n.replaceWith(frag);
      } else if (n.nodeType === 1 && n.tagName !== "BR") walk(n);
    });
  };
  walk(el);
  // Keep closing punctuation on the same line as the character before it
  let prev = null;
  $$(`.${cls} > span`, el).forEach((sp) => {
    if (prev && /^[，。！？：；、）」』”’,.!?:;)]+$/.test(sp.textContent)) {
      prev.textContent += sp.textContent;
      sp.parentElement.remove();
    } else prev = sp;
  });
  return $$(`.${cls} > span`, el);
}

/* ---------- Animations ---------- */
function animate() {
  if (!hasGSAP || reduce) return;
  document.documentElement.classList.add("js");
  gsap.registerPlugin(ScrollTrigger);

  // Split headings
  const heroWords = [];
  $$("[data-split]").forEach((el) => {
    const words = splitWords(el);
    if (el.dataset.split === "hero") { gsap.set(words, { yPercent: 115 }); heroWords.push(words); return; }
    gsap.from(words, { yPercent: 115, duration: 1.3, ease: "expo.out", stagger: 0.035, scrollTrigger: { trigger: el, start: "top 88%" } });
  });

  // Signature writes itself in, left to right
  $$("[data-sign]").forEach((el) => {
    const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: "top 88%" } });
    tl.fromTo($(".sig-wipe", el), { attr: { width: 0 } }, { attr: { width: 350 }, duration: 2.2, ease: "power2.inOut" })
      .fromTo($(".sig-line", el), { strokeDasharray: 1, strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.8, ease: "power2.out" }, "-=0.25")
      .fromTo($(".sig-dot", el), { scale: 0 }, { scale: 1, duration: 0.45, ease: "back.out(3)" }, "-=0.1");
  });

  // Workshop drawings sketch themselves in
  $$("[data-draw]").forEach((svg) => {
    const tl = gsap.timeline({ scrollTrigger: { trigger: svg, start: "top 80%" } });
    tl.to($$(".d", svg), { strokeDashoffset: 0, duration: 1.6, ease: "power2.inOut", stagger: { amount: 2.6, from: "start" } })
      .to($$(".bp-text text", svg), { opacity: 1, duration: 0.8, stagger: 0.08 }, 1.6);
  });

  // Gold rules that draw in on scroll
  $$("[data-rule]").forEach((el) => gsap.fromTo(el, { scaleX: 0 }, { scaleX: 1, duration: 1.8, ease: "expo.inOut", scrollTrigger: { trigger: el, start: "top 92%" } }));

  // Fade-ups
  $$("[data-fade]").forEach((el) => gsap.to(el, { opacity: 1, y: 0, duration: 1.2, ease: "expo.out", scrollTrigger: { trigger: el, start: "top 90%" } }));

  // Clip-path image reveals
  $$(".ph[data-reveal]").forEach((ph) => {
    const tl = gsap.timeline({ scrollTrigger: { trigger: ph, start: "top 85%" } });
    tl.fromTo(ph, { clipPath: "inset(100% 0% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 1.5, ease: "expo.inOut" })
      .from($("i", ph), { scale: 1.35, duration: 1.8, ease: "expo.out" }, 0.2);
  });

  // Parallax inside every photo
  $$(".ph:not(.fit) > i").forEach((i) => {
    gsap.fromTo(i, { yPercent: -7 }, { yPercent: 7, ease: "none", scrollTrigger: { trigger: i.parentElement, start: "top bottom", end: "bottom top", scrub: true } });
  });

  // Free-floating parallax elements
  $$("[data-speed]").forEach((el) => {
    gsap.to(el, { y: () => -parseFloat(el.dataset.speed) * innerHeight * 0.3, ease: "none", scrollTrigger: { trigger: el, start: "top bottom", end: "bottom top", scrub: true, invalidateOnRefresh: true } });
  });

  // Expanding showroom image
  $$(".expand").forEach((sec) => {
    const tl = gsap.timeline({ scrollTrigger: { trigger: sec, start: "top top", end: "+=140%", scrub: 1, pin: true } });
    tl.to($(".ph", sec), { clipPath: "inset(0% 0% 0% 0%)", ease: "none" })
      .from($(".ph i", sec), { scale: 1.25, ease: "none" }, 0)
      .to($(".over", sec), { opacity: 1, ease: "none", duration: 0.35 }, 0.7);
  });

  // Word-by-word scrub statement
  $$("[data-scrub]").forEach((el) => {
    const words = splitWords(el, "wd").map((w) => w.parentElement);
    gsap.to(words, { opacity: 1, stagger: 0.1, ease: "none", scrollTrigger: { trigger: el, start: "top 80%", end: "bottom 45%", scrub: true } });
  });

  // Horizontal featured rail (desktop)
  ScrollTrigger.matchMedia({
    "(min-width: 861px)": () => {
      $$(".hscroll").forEach((sec) => {
        const rail = $(".rail", sec);
        gsap.to(rail, {
          x: () => -(rail.scrollWidth - innerWidth),
          ease: "none",
          scrollTrigger: { trigger: sec, start: "top top", end: () => "+=" + (rail.scrollWidth - innerWidth), scrub: 1, pin: true, invalidateOnRefresh: true }
        });
      });
    }
  });

  // Marquee that reacts to scroll speed
  $$(".marquee .track").forEach((track) => {
    const tw = gsap.to(track, { xPercent: -50, duration: 60, ease: "none", repeat: -1 });
    if (lenis) lenis.on("scroll", ({ velocity }) => gsap.to(tw, { timeScale: 1 + Math.min(Math.abs(velocity) * 0.25, 6), duration: 0.3, overwrite: true }));
  });

  // Intro: loader then hero
  const loader = $(".loader");
  const tag = $("[data-tag]");
  let tagChars = [];
  if (tag) {
    tag.innerHTML = tag.textContent.split(" ").map((w) => `<span class="tw">${w.split("").map((ch) => `<span class="ch" aria-hidden="true">${ch}</span>`).join("")}</span>`).join(`<span class="sp"> </span>`);
    tagChars = $$(".ch", tag);
    gsap.set(tagChars, { opacity: 0, y: 18, filter: "blur(8px)" });
    gsap.set(".tag-rule", { scaleX: 0 });
    // Gentle parallax and fade as you scroll away
    gsap.to(tag, { yPercent: -60, opacity: 0, ease: "none", scrollTrigger: { trigger: tag.closest("section"), start: "top top", end: "bottom top", scrub: true } });
  }
  const playWall = (d = 0) => {
    if (!$(".wall")) return;
    gsap.to(".wall-light", { opacity: 1, duration: 4.5, ease: "power2.inOut", delay: d + 0.6 });
    gsap.to(".wall-light", { x: "-4vw", y: "3vh", rotate: -11, duration: 26, ease: "sine.inOut", yoyo: true, repeat: -1 });
    gsap.from(".wall-plaster", { opacity: 0, duration: 3, delay: d });
    gsap.to(".wall", { opacity: 0, ease: "none", scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true } });
  };
  // t = when the tagline begins, after the room has faded in
  const playHero = (t = 0.15) => {
    playWall(0);
    if (tagChars.length) {
      gsap.to(tagChars, { opacity: 1, y: 0, filter: "blur(0px)", duration: 2, ease: "expo.out", stagger: { each: 0.07, from: "center" }, delay: t });
      gsap.to(".tag-rule", { scaleX: 1, duration: 1.8, ease: "expo.inOut", delay: t + 0.9 });
      // A soft gold shimmer that travels through the letters every few seconds
      gsap.to(tagChars, { color: "#d9b878", textShadow: "0 0 18px rgba(217,184,120,.45)", duration: 0.7, ease: "sine.inOut", yoyo: true, repeat: 1, stagger: { each: 0.07, repeat: -1, repeatDelay: 4 }, delay: t + 2.6 });
      // Slow breathing in the letter spacing
      if (innerWidth > 860) gsap.fromTo(tag, { letterSpacing: "0.62em", paddingLeft: "0.62em" }, { letterSpacing: "0.7em", paddingLeft: "0.7em", duration: 6, ease: "sine.inOut", yoyo: true, repeat: -1, delay: t + 2.4 });
      gsap.from(".hero-min .scroll, .hero-min .socials-mobile", { opacity: 0, duration: 1.5, delay: t + 1.6 });
    }
    heroWords.forEach((w, i) => gsap.to(w, { yPercent: 0, duration: 1.6, ease: "expo.out", stagger: 0.05, delay: 0.1 + i * 0.12 }));
  };
  const seen = sessionStorage.getItem("aeva-seen") === "1";
  const isHome = !!tag;
  if (document.documentElement.classList.contains("no-loader") || !isHome) {
    loader.style.display = "none";
    playHero();
  } else {
    // First arrival: a quiet 0 to 100 count with a hand-drawn line, then the room fades up and the tagline appears
    sessionStorage.setItem("aeva-seen", "1");
    if (lenis) lenis.stop();
    const n = $(".n", loader), fill = $(".fill", loader), c = { v: 0 };
    gsap.set(".site-head, .social-rail, .wa", { opacity: 0 });
    gsap.timeline()
      .from(".ld", { opacity: 0, y: 8, duration: 0.9, ease: "power2.out" }, 0)
      .to(c, { v: 100, duration: 2.6, ease: "power1.inOut", onUpdate: () => { n.textContent = Math.round(c.v); fill.style.strokeDashoffset = 1 - c.v / 100; } }, 0.3)
      .to(".ld", { opacity: 0, y: -6, duration: 0.9, ease: "power2.in" }, 3.1)
      .to(loader, { opacity: 0, duration: 2.4, ease: "power2.inOut", onComplete: () => { loader.style.display = "none"; if (lenis) lenis.start(); } }, 3.6)
      .to(".site-head, .social-rail, .wa", { opacity: 1, duration: 1.6 }, 5.6)
      .add(() => playHero(1.4), 3.6);
  }

  document.fonts && document.fonts.ready.then(() => ScrollTrigger.refresh());
}

// Pages can register extra setup (e.g. rendering projects) before animations run
window.AEVA = { ready: [] };
addEventListener("DOMContentLoaded", () => {
  window.AEVA.ready.forEach((fn) => fn());
  animate();
});
if (!hasGSAP || reduce) { const l = $(".loader"); if (l) l.style.display = "none"; }
