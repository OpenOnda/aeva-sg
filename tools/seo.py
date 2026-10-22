#!/usr/bin/env python3
"""SEO build for AEVA.sg. Run from the site root after tools/build_zh.py:
    python3 tools/build_zh.py && python3 tools/seo.py
It generates a static page per design (EN + ZH), writes titles, descriptions,
canonical and language links, social previews and Google structured data into
every page, pre-renders the design lists, labels every photo, and writes
sitemap.xml and robots.txt."""
import html, json, os, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
DOMAIN = "https://aeva.sg"
OG_IMAGE = DOMAIN + "/images/og-image.jpg"
TODAY = "2026-10-22"
WA = "6580405577"
esc = lambda s: html.escape(s, quote=True)

def load(js):
    out = subprocess.check_output(["node", "-e",
        f"const fs=require('fs');process.stdout.write(JSON.stringify(new Function(fs.readFileSync('{js}','utf8')+';return PROJECTS;')()))"])
    return json.loads(out)

DATA = {"en": load("projects.js"), "zh": load("projects-zh.js")}

# ---------- Page metadata ----------
PAGES = {
 "index.html": {
  "en": ("AEVA | Interior Design & Custom Carpentry Singapore",
         "AEVA designs warm, timber-filled Singapore homes and builds every cabinet, bed and reading nook in its own workshop. HDB, condo and landed, with kids in mind."),
  "zh": ("AEVA | 新加坡室内设计与定制木工",
         "AEVA 在新加坡打造温暖的木质家居，每一个柜子、床和阅读角都在自家工坊亲手制作。组屋、公寓与有地住宅，为有孩子的家庭而设计。")},
 "about.html": {
  "en": ("About AEVA | Singapore Interior Design & Carpentry Studio",
         "Meet AEVA, a Singapore interior design studio with its own carpentry workshop. Founded by Alan Tan, a father of two, to build homes made to be handed down."),
  "zh": ("关于 AEVA | 新加坡室内设计与木工工作室",
         "认识 AEVA，一家拥有自家木工坊的新加坡室内设计工作室。由两个孩子的父亲 Alan Tan 创办，打造经得起代代相传的家。")},
 "services.html": {
  "en": ("Carpentry & Interior Design Services Singapore | AEVA",
         "Custom carpentry, kids' rooms, ambient lighting, HDB, condo and landed renovation, and furniture sourcing incl. Taobao. 10-year carpentry warranty."),
  "zh": ("新加坡室内设计服务 | 定制木工、儿童房 | AEVA",
         "定制木工、儿童房与婴儿房、氛围灯光、组屋公寓与有地住宅全屋装修，以及包括淘宝在内的家具采购。木工10年保修。")},
 "designs.html": {
  "en": ("HDB & Condo Interior Design Ideas | AEVA Singapore",
         "AEVA design ideas for Singapore homes: loft beds, nurseries, reading nooks, walnut living rooms, open kitchens and kids' study rooms, all built by hand."),
  "zh": ("组屋与公寓室内设计灵感 | AEVA 新加坡",
         "探索 AEVA 为新加坡家庭打造的设计灵感：阁楼床、婴儿房、阅读角、胡桃木客厅、开放式厨房与儿童书房，全部手工打造。")},
 "contact.html": {
  "en": ("Contact AEVA | Free Interior Design Consultation Singapore",
         "Book a free consultation with AEVA. Visit our showroom at Oxley Bizhub, 65 Ubi Road 1, or WhatsApp +65 8040 5577. We reply within one working day."),
  "zh": ("联系 AEVA | 新加坡免费室内设计咨询",
         "预约 AEVA 免费咨询。欢迎参观我们位于 Oxley Bizhub（65 Ubi Road 1）的展厅，或 WhatsApp +65 8040 5577。我们会在一个工作日内回复。")},
 "coming-soon.html": {"en": ("Coming soon | AEVA", "AEVA's social channels are coming soon."),
                      "zh": ("即将推出 | AEVA", "AEVA 社交媒体频道即将推出。")},
 "thank-you.html": {"en": ("Thank you | AEVA", "Enquiry received."), "zh": ("谢谢 | AEVA", "已收到你的咨询。")},
 "design.html": {"en": ("Design | AEVA", "AEVA design."), "zh": ("设计 | AEVA", "AEVA 设计。")},
 "404.html": {"en": ("Page not found | AEVA", "This page could not be found."), "zh": ("找不到页面 | AEVA", "找不到页面。")},
}
NOINDEX = {"coming-soon.html", "thank-you.html", "design.html", "404.html"}

# ---------- Photo descriptions (used for labels and the image sitemap) ----------
ALT = {"en": {
 "showroom.jpg": "AEVA showroom at Oxley Bizhub with a backlit stone wall, timber shelving and amber pendant lights",
 "home-feature.jpg": "Floating walnut staircase with warm under-step lighting beside a backlit stone feature wall",
 "kids-1.jpg": "Child's bed nook with oak storage steps and warm LED lighting",
 "carpentry-3.jpg": "Built-in walnut study desk with backlit shelves against a stone wall",
 "founder.jpg": "AEVA founder Alan Tan with his wife and two children",
 "about-workshop.jpg": "AEVA carpenter building oak drawers in the carpentry workshop",
 "service-carpentry.jpg": "Carpenter's hands sanding the rounded edge of an oak tabletop",
 "service-kids.jpg": "HDB kids' bedroom with an oak platform bed, storage drawers and a lit toy shelf",
 "service-lighting.jpg": "HDB living room at night with layered warm cove and strip lighting",
 "service-renovation.jpg": "Renovated open-plan HDB living and dining room with light oak carpentry",
 "service-sourcing.jpg": "Styled living and dining corner with a boucle sofa, paper pendant and rattan chairs",
}, "zh": {
 "showroom.jpg": "AEVA 位于 Oxley Bizhub 的展厅，背光石墙、木质层架与琥珀色吊灯",
 "home-feature.jpg": "悬浮胡桃木楼梯，台阶下暖光灯带，旁边是背光石材造型墙",
 "kids-1.jpg": "儿童床铺角落，橡木收纳台阶与暖色LED灯光",
 "carpentry-3.jpg": "嵌入式胡桃木书桌与背光层板，背景为石墙",
 "founder.jpg": "AEVA 创办人 Alan Tan 与妻子和两个孩子",
 "about-workshop.jpg": "AEVA 木工师傅在工坊制作橡木抽屉",
 "service-carpentry.jpg": "木工师傅打磨橡木桌面的圆角",
 "service-kids.jpg": "组屋儿童房，橡木地台床、收纳抽屉与发光玩具层板",
 "service-lighting.jpg": "夜晚的组屋客厅，层次分明的暖色灯槽与灯带",
 "service-renovation.jpg": "翻新后的开放式组屋客厅与餐厅，浅橡木木工",
 "service-sourcing.jpg": "布置好的客厅与餐厅角落，羊羔绒沙发、纸灯与藤编椅",
}}
SHOT = {"en": ["main view", "detail", "detail"], "zh": ["全景", "细节", "细节"]}

def proj_alt(lang, slug, n):
    p = next(x for x in DATA[lang] if x["slug"] == slug)
    return f"{p['title']}, {p['space']}: {SHOT[lang][n-1]}" if lang == "en" else f"{p['title']}（{p['space']}）{SHOT[lang][n-1]}"

def alt_for(lang, path):
    name = path.split("/")[-1]
    m = re.match(r"([a-z-]+)-(\d)\.jpg$", name)
    if "projects/" in path and m:
        return proj_alt(lang, m.group(1), int(m.group(2)))
    return ALT[lang].get(name, "")

def label_images(s, lang):
    def fix(m):
        tag, path = m.group(0), m.group(2)
        if "aria-label" in tag:
            tag = re.sub(r' role="img" aria-label="[^"]*"', "", tag)
        a = alt_for(lang, path)
        return tag.replace("<i ", f'<i role="img" aria-label="{esc(a)}" ', 1) if a else tag
    return re.sub(r"<i (?:role=\"img\" aria-label=\"[^\"]*\" )?style=\"--img:url\('((?:\.\./)?(images/[^']+))'\)\">", fix, s)

# ---------- Structured data ----------
def business(lang):
    return {
     "@context": "https://schema.org", "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
     "@id": DOMAIN + "/#business", "name": "AEVA", "legalName": "AEVA Private Limited",
     "slogan": "Built for generations" if lang == "en" else "为世代而筑",
     "description": PAGES["index.html"][lang][1], "url": DOMAIN + ("/" if lang == "en" else "/zh/"),
     "logo": DOMAIN + "/images/logo.svg", "image": [DOMAIN + "/images/showroom.jpg", OG_IMAGE],
     "telephone": "+65 8040 5577", "email": "inquiries@aeva.sg", "taxID": "202625649E",
     "address": {"@type": "PostalAddress", "streetAddress": "Oxley Bizhub #1, 65 Ubi Road 1, #04-29",
                 "addressLocality": "Singapore", "postalCode": "408729", "addressCountry": "SG"},
     "hasMap": "https://www.google.com/maps/search/?api=1&query=Oxley+Bizhub+65+Ubi+Road+1+Singapore+408729",
     "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "10:00", "closes": "19:00"}],
     "areaServed": {"@type": "Country", "name": "Singapore"},
     "founder": {"@type": "Person", "name": "Alan Tan", "jobTitle": "Founder & CEO"},
     "sameAs": ["https://instagram.com/aevacarpentry"],
     "knowsLanguage": ["en", "zh"],
     "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in (
        ["Custom carpentry", "Kids' rooms and nurseries", "Ambient lighting design", "Full home renovation", "Furniture sourcing"] if lang == "en"
        else ["定制木工", "儿童房与婴儿房", "氛围灯光设计", "全屋装修", "家具采购"])]}

def faq(lang, page_html):
    qs = re.findall(r"<details><summary>(.*?)</summary><p>(.*?)</p></details>", page_html)
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": html.unescape(q),
                            "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a)}} for q, a in qs]}

def crumbs(lang, items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement":
            [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}

def url(lang, page):
    p = "" if page == "index.html" else page
    return f"{DOMAIN}/{p}" if lang == "en" else f"{DOMAIN}/zh/{p}"

# ---------- Head block ----------
HEAD_STRIP = [r'\s*<meta name="description"[^>]*>', r'\s*<meta property="og:[^>]*>', r'\s*<meta name="twitter:[^>]*>',
              r'\s*<link rel="alternate"[^>]*>', r'\s*<link rel="canonical"[^>]*>', r'\s*<meta name="robots"[^>]*>',
              r'\s*<link rel="apple-touch-icon"[^>]*>', r'\s*<script type="application/ld\+json">.*?</script>']

def head(lang, page, title, desc, ld=None, img=OG_IMAGE):
    other = "zh" if lang == "en" else "en"
    tags = [f'<meta name="description" content="{esc(desc)}">']
    if page in NOINDEX:
        tags.append('<meta name="robots" content="noindex, follow">')
    else:
        tags += [f'<link rel="canonical" href="{url(lang, page)}">',
                 f'<link rel="alternate" hreflang="en" href="{url("en", page)}">',
                 f'<link rel="alternate" hreflang="zh-Hans" href="{url("zh", page)}">',
                 f'<link rel="alternate" hreflang="x-default" href="{url("en", page)}">',
                 '<meta property="og:type" content="website">', '<meta property="og:site_name" content="AEVA">',
                 f'<meta property="og:locale" content="{"en_SG" if lang == "en" else "zh_SG"}">',
                 f'<meta property="og:locale:alternate" content="{"zh_SG" if lang == "en" else "en_SG"}">',
                 f'<meta property="og:title" content="{esc(title)}">', f'<meta property="og:description" content="{esc(desc)}">',
                 f'<meta property="og:url" content="{url(lang, page)}">', f'<meta property="og:image" content="{img}">',
                 '<meta name="twitter:card" content="summary_large_image">']
    tags.append(f'<link rel="apple-touch-icon" href="{"" if lang == "en" else "../"}images/apple-touch-icon.png">')
    for block in (ld or []):
        tags.append('<script type="application/ld+json">' + json.dumps(block, ensure_ascii=False) + "</script>")
    return "\n".join(tags)

def apply_head(s, lang, page, title, desc, ld=None, img=OG_IMAGE):
    for pat in HEAD_STRIP:
        s = re.sub(pat, "", s, flags=re.S)
    s = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", s, count=1)
    return s.replace("</title>", "</title>\n" + head(lang, page, title, desc, ld, img), 1)

# ---------- Pre-rendered design lists (the page script re-renders the same markup) ----------
def index_rows(lang):
    return "".join(f'''
      <a class="irow" href="design-{p['slug']}.html">
        <span class="num">0{i+1}</span><h3>{esc(p['title'])}</h3>
        <span class="c">{esc(p['space'])}</span><span class="c">{esc(p['suits'])}</span><span class="c">{esc(p['build'])}</span><span class="go"></span>
      </a>''' for i, p in enumerate(DATA[lang]))

def designs_cards(lang, pre):
    return "".join(f'''
    <a class="fcard" href="design-{p['slug']}.html" data-tags="{' '.join(p['tags'])}" data-cursor="{'View' if lang=='en' else '查看'}">
      <div class="ph" data-reveal><i style="--img:url('{pre}images/projects/{p['slug']}-1.jpg')"></i></div>
      <div class="meta"><h3>{esc(p['title'])}</h3><span class="label">{esc(p['space'])}</span></div>
      <p>{esc(p['summary'])}</p>
    </a>''' for p in DATA[lang])

def designs_rows(lang):
    return "".join(f'''
    <a class="irow" href="design-{p['slug']}.html" data-tags="{' '.join(p['tags'])}">
      <span class="num">0{i+1}</span><h3>{esc(p['title'])}</h3>
      <span class="c">{esc(p['space'])}</span><span class="c">{esc(p['suits'])}</span><span class="c">{esc(p['build'])}</span><span class="go"></span>
    </a>''' for i, p in enumerate(DATA[lang]))

def fill(s, el_id, inner):
    return re.sub(rf'(<(\w+)[^>]*\bid="{el_id}"[^>]*>).*?(</\2>)', lambda m: m.group(1) + inner + m.group(3), s, count=1, flags=re.S)

FACT_LABELS = {"en": ["Space", "Ideal for", "Materials", "Typical build"], "zh": ["空间", "适合", "材料", "一般工期"]}
NAV_NAME = {"en": ("Home", "Designs"), "zh": ("首页", "设计")}

def design_pages(lang):
    base = "" if lang == "en" else "zh/"
    pre = "" if lang == "en" else "../"
    tpl = open(base + "design.html", encoding="utf-8").read()
    P = DATA[lang]
    made = []
    for i, p in enumerate(P):
        n = P[(i + 1) % len(P)]
        s = tpl.replace("<body>", f'<body data-slug="{p["slug"]}">', 1)
        s = fill(s, "p-title", esc(p["title"]))
        s = fill(s, "p-loc", esc(p["space"]))
        s = fill(s, "p-facts", "".join(f"<div><span>{l}</span><b>{esc(v)}</b></div>" for l, v in zip(FACT_LABELS[lang], [p["space"], p["suits"], p["style"], p["build"]])))
        s = fill(s, "p-summary", esc(p["summary"]))
        s = fill(s, "p-story", esc(p["story"]))
        s = fill(s, "p-scope", "".join(f'<li><span class="num">0{k+1}</span>{esc(x)}</li>' for k, x in enumerate(p["scope"])))
        s = fill(s, "p-next-title", esc(n["title"]))
        for k in (1, 2, 3):
            s = re.sub(rf'(<div class="ph"[^>]*id="p-img{k}"><i)(></i>)', rf"\1 style=\"--img:url('{pre}images/projects/{p['slug']}-{k}.jpg')\"\2", s)
        s = re.sub(r'(<a class="next" id="p-next")', rf'\1 href="design-{n["slug"]}.html"', s)
        s = re.sub(r'(<a class="next"[^>]*>\s*<div class="ph"><i)(></i>)', rf"\1 style=\"--img:url('{pre}images/projects/{n['slug']}-1.jpg')\"\2", s)
        msg = (f'Hi AEVA, I like "{p["title"]}" and I\'d like to find out more...' if lang == "en"
               else f"你好 AEVA，我喜欢「{p['title']}」这个设计，想了解更多...")
        s = s.replace('<a href="#" data-wa-design', f'<a href="https://wa.me/{WA}?text={esc(__import__("urllib.parse").parse.quote(msg))}" target="_blank" rel="noopener" data-wa-design', 1)
        page = f"design-{p['slug']}.html"
        title = (f"{p['title']} | {p['space']} | AEVA Singapore" if lang == "en"
                 else f"{p['title']}：{p['space']}设计灵感 | AEVA 新加坡")
        desc = f"{p['summary']} {p['story']}"
        desc = desc[:155].rsplit(" ", 1)[0] + "..." if lang == "en" and len(desc) > 158 else (desc[:80] + "..." if lang == "zh" and len(desc) > 82 else desc)
        ld = [crumbs(lang, [(NAV_NAME[lang][0], url(lang, "index.html")), (NAV_NAME[lang][1], url(lang, "designs.html")), (p["title"], url(lang, page))])]
        s = apply_head(s, lang, page, title, desc, ld, img=f"{DOMAIN}/images/projects/{p['slug']}-1.jpg")
        s = label_images(s, lang)
        open(base + page, "w", encoding="utf-8").write(s)
        made.append(page)
    return made

# ---------- 404 page ----------
def make_404():
    s = open("thank-you.html", encoding="utf-8").read()
    s = s.replace('<span class="label">Enquiry received</span>', '<span class="label">Error 404</span>')
    s = re.sub(r'<h1 data-split="hero">.*?</h1>', '<h1 data-split="hero">This page <em>has moved</em>.</h1>', s, flags=re.S)
    s = re.sub(r'<p class="lead" data-fade>.*?</p>', '<p class="lead" data-fade>The page you were looking for isn\'t here. Have a look at our designs, or head back home.</p>', s, flags=re.S)
    s = s.replace('href="designs.html" class="btn solid">Explore our designs</a>',
                  'href="designs.html" class="btn solid">Explore our designs</a> &nbsp; <a href="index.html" class="btn">Back to home</a>')
    # resolve every relative link from the site root, so the 404 works at any URL depth
    s = s.replace("<head>", '<head>\n<base href="/">', 1)
    open("404.html", "w", encoding="utf-8").write(s)

# ---------- Run ----------
make_404()
sitemap = []
for lang in ("en", "zh"):
    base = "" if lang == "en" else "zh/"
    for page in [p for p in PAGES if os.path.exists(base + p)]:
        if lang == "zh" and page == "404.html":
            continue
        s = open(base + page, encoding="utf-8").read()
        title, desc = PAGES[page][lang]
        ld = []
        if page in ("index.html", "contact.html", "about.html"):
            ld.append(business(lang))
        if page == "services.html":
            ld.append(faq(lang, s))
        if page == "index.html":
            s = fill(s, "index", index_rows(lang))
        if page == "designs.html":
            s = fill(s, "featured", designs_cards(lang, "" if lang == "en" else "../"))
            s = fill(s, "index", designs_rows(lang))
        s = apply_head(s, lang, page, title, desc, ld)
        s = label_images(s, lang)
        open(base + page, "w", encoding="utf-8").write(s)
        if page not in NOINDEX:
            sitemap.append(page)
    for page in design_pages(lang):
        if lang == "en":
            sitemap.append(page)

# sitemap.xml with language pairs and images
def page_images(page):
    s = open(page, encoding="utf-8").read()
    return sorted(set(re.findall(r"--img:url\('(images/[^']+)'\)", s)))

seen, out = set(), []
for page in sitemap:
    if page in seen: continue
    seen.add(page)
    imgs = "".join(f"\n    <image:image><image:loc>{DOMAIN}/{i}</image:loc><image:caption>{esc(alt_for('en', i))}</image:caption></image:image>" for i in page_images(page))
    for lang in ("en", "zh"):
        out.append(f"""  <url>
    <loc>{url(lang, page)}</loc>
    <lastmod>{TODAY}</lastmod>
    <xhtml:link rel="alternate" hreflang="en" href="{url('en', page)}"/>
    <xhtml:link rel="alternate" hreflang="zh-Hans" href="{url('zh', page)}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{url('en', page)}"/>{imgs if lang == 'en' else ''}
  </url>""")
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "\n".join(out) + "\n</urlset>\n")
open("robots.txt", "w").write(f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {DOMAIN}/sitemap.xml\n")
print(f"SEO built: {len(seen)} pages x 2 languages in sitemap")
