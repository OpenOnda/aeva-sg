#!/usr/bin/env python3
"""Builds the Chinese site in /zh from the English pages.
Run from the site root:  python3 tools/build_zh.py
Every English phrase must be found exactly, so if an English page changes,
the script stops and tells you which line needs a new translation."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
os.makedirs("zh", exist_ok=True)

TITLE_SUFFIX = ("AEVA Interior Design Singapore", "AEVA 新加坡室内设计")
NOTO = "&family=Noto+Sans+SC:wght@300;400;500&family=Noto+Serif+SC:wght@300;400;500"

FOUNDER = [
    ('<span class="label gold">A note from Alan</span>', '<span class="label gold">Alan 的话</span>'),
    ("Founder's <em>Message</em>", "创办人<em>寄语</em>"),
    ("Alan at home, with his family", "Alan 与家人"),
    ("I'm a husband and a father of two before I'm anything else. My days begin with little feet running down the corridor and end with bedtime stories in a room I built with my own hands.",
     "在成为设计师之前，我首先是一个丈夫，也是两个孩子的父亲。我的每一天，从走廊里孩子们的小脚步声开始，在我亲手打造的房间里讲完睡前故事后结束。"),
    ("Being a dad taught me what a home really needs. Soft edges, warm light and room to grow. A place where the kids can be loud all day and still fall asleep easily at night. That's what we build at AEVA, properly and by hand, so it lasts long enough to be passed on.",
     "当了爸爸，我才明白一个家真正需要什么：柔和的边角、温暖的灯光，还有成长的空间。一个让孩子白天尽情玩闹，晚上依然能安然入睡的地方。这就是我们在 AEVA 用心、亲手打造的家，经久耐用，足以代代相传。"),
    ("Every family we work with gets the same care I'd give my own, because I know what it feels like to hand over your home and trust someone with it.",
     "每一个与我们合作的家庭，都会得到我对待自己家人一样的用心，因为我明白把家交托给别人是什么感受。"),
    ("Thank you for letting us be part of the place your family calls home. <a href=\"#\" data-wa class=\"inline-link\">Contact me for a free consultation today!</a>",
     "感谢你让我们成为你家庭的一部分。<a href=\"#\" data-wa class=\"inline-link\">立即联系我，预约免费咨询！</a>"),
    ('aria-label="Signed, Alan Tan"', 'aria-label="签名：Alan Tan"'),
    ("Founder &amp; CEO, AEVA", "AEVA 创办人兼首席执行官"),
]

FORM = [
    ("Got a home in mind?<br><span class=\"gold-txt\">Come talk to us</span>", "心中有理想的家？<br><span class=\"gold-txt\">来和我们聊聊</span>"),
    ('<span class="label">Email</span>', '<span class="label">电邮</span>'),
    ('<span class="label">Showroom</span>', '<span class="label">展厅</span>'),
    ('<input type="hidden" name="language" value="English">', '<input type="hidden" name="language" value="中文">'),
    ("Leave blank", "请留空"),
    ("Tell us about your home and family", "告诉我们你的家和家人"),
    ("Who lives there, how old are the kids, what's not working right now?", "家里住着谁？孩子多大了？现在有哪些地方不顺心？"),
    ('<label for="n">Name</label>', '<label for="n">姓名</label>'),
    ('<label for="p">Mobile</label>', '<label for="p">手机号码</label>'),
    ('<label for="e">Email</label>', '<label for="e">电邮</label>'),
    ("I'm happy for AEVA to contact me about my enquiry.", "我同意 AEVA 就我的咨询与我联系。"),
    ("Send message", "发送信息"),
]

PAGES = {
"index.html": [
    ("<title>AEVA | Built for Generations · Interior Design &amp; Carpentry Singapore</title>", "<title>AEVA | 为世代而筑 · 新加坡室内设计与木工</title>"),
    ('content="AEVA is an award-winning Singapore interior design studio with its own carpentry workshop. Warm, timber-filled homes with soft ambient light, designed with children in mind."',
     'content="AEVA 是一家屡获殊荣的新加坡室内设计工作室，拥有自家木工坊。以温暖的木质与柔和的氛围灯光，为有孩子的家庭打造温馨的家。"'),
    ('content="This is AEVA. Built for generations."', 'content="AEVA，为世代而筑。"'),
    ('aria-label="Built for generations">Built for generations</h1>', 'aria-label="为世代而筑">为世代而筑</h1>'),
    ('<span class="scroll"><i></i>Scroll</span>', '<span class="scroll"><i></i>向下滚动</span>'),
    (">Made by hand<", ">匠心手作<"), (">Safe for small hands<", ">呵护孩子的安全设计<"),
    (">Warm ambient lighting<", ">温暖氛围灯光<"), (">Designed to stay with your family<", ">陪伴家人成长的设计<"),
    (">Made to be handed down<", ">值得代代相传<"), (">Award-winning designs<", ">屡获殊荣的设计<"),
    (">100% in-house carpentry<", ">100% 自家木工<"), (">10-year carpentry warranty<", ">木工10年保修<"),
    (">Showroom open daily<", ">展厅每日开放<"), (">Top level client care<", ">贴心周到的客户服务<"),
    ("Warm homes, <em>built by real hands</em>,<br class=\"d-br\"> for the many generations to come.",
     "温暖的家，<em>由真正的双手打造</em>，<br class=\"d-br\">为世世代代而筑。"),
    ("01 &nbsp;·&nbsp; Who we are", "01 &nbsp;·&nbsp; 关于我们"),
    ("We're a Singapore studio of interior designers and carpenters. We design cosy spaces and build every cabinet, bed and reading nook in our own workshop from scratch. No generic house style, no shortcuts. Just homes shaped around the families who live in them, made to be handed down.",
     "我们是一家新加坡的室内设计与木工工作室。我们设计温馨的空间，每一个柜子、每一张床、每一个阅读角，都在自家工坊从零打造。没有千篇一律的风格，也绝不偷工减料。只为住在里面的家人量身打造，经得起代代相传。"),
    ('<span class="label gold">The AEVA spirit</span>', '<span class="label gold">AEVA 精神</span>'),
    ("Rooms that <em>grow up</em> with your children.", "与孩子<em>一起成长</em>的房间。"),
    ("A nursery today, a study corner tomorrow. Rounded edges, soft-close hinges, low-VOC finishes and storage at kid height come standard, and every piece is planned to adapt as your family changes.",
     "今天是婴儿房，明天是书桌角。圆角收边、缓冲铰链、低VOC涂料，以及孩子够得着的收纳都是标配，每一件家具都会随着家庭的变化而调整。"),
    ("\"Our home finally feels warm.<br class=\"q-br\"> The lighting, the timber, all of it.<br class=\"q-br\"> We just love being in it.\"",
     "“家终于有了温暖的感觉。<br class=\"q-br\">灯光、木材，一切都刚刚好。<br class=\"q-br\">我们就是爱待在家里。”"),
    ("02 &nbsp;·&nbsp; What we do", "02 &nbsp;·&nbsp; 我们的服务"),
    ("End to end, <em>under one roof</em>.", "从头到尾，<em>一站式完成</em>。"),
    ("<h3>Custom carpentry</h3><p>Our specialty, made to measure in our own workshop.</p>", "<h3>定制木工</h3><p>我们的专长，在自家工坊量身打造。</p>"),
    ("<h3>Kids' rooms &amp; nurseries</h3><p>Spaces that adapt from cot to teenage years.</p>", "<h3>儿童房与婴儿房</h3><p>从婴儿床到青少年时期都适用的空间。</p>"),
    ("<h3>Ambient lighting</h3><p>Layered, warm light that makes timber glow.</p>", "<h3>氛围灯光</h3><p>层次分明的暖光，让木材焕发光彩。</p>"),
    ("<h3>Full renovation</h3><p>HDB, condo and landed, one team start to finish.</p>", "<h3>全屋装修</h3><p>组屋、公寓与有地住宅，一个团队全程负责。</p>"),
    ("<h3>Furniture sourcing</h3><p>Taobao and beyond, customised to fit your home.</p>", "<h3>家具采购</h3><p>淘宝及更多渠道，按你的家量身定制。</p>"),
    ('class="btn">Our services</a>', 'class="btn">我们的服务</a>'),
    ("03 &nbsp;·&nbsp; Featured designs", "03 &nbsp;·&nbsp; 精选设计"),
    ("Spaces we can <em>build for you</em>.", "我们能<em>为你打造</em>的空间。"),
    ("See all designs <span", "查看全部设计 <span"),
    ("<h3>The Treehouse Loft</h3><span class=\"label\">Shared kids' bedroom</span>", "<h3>树屋阁楼</h3><span class=\"label\">共享儿童房</span>"),
    ("<h3>The Reading Nook</h3><span class=\"label\">Living room &amp; library</span>", "<h3>阅读角</h3><span class=\"label\">客厅与书墙</span>"),
    ("<h3>Walnut &amp; Warmth</h3><span class=\"label\">Living room</span>", "<h3>胡桃木之暖</h3><span class=\"label\">客厅</span>"),
    ("<h3>The Cabin Kitchen</h3><span class=\"label\">Open-concept kitchen</span>", "<h3>原木厨房</h3><span class=\"label\">开放式厨房</span>"),
    ("04 &nbsp;·&nbsp; Design index", "04 &nbsp;·&nbsp; 设计索引"),
    ("Every room, <em>made by hand</em>.", "每个房间，<em>皆由手作</em>。"),
    ("Explore designs <span", "探索设计 <span"),
] + FOUNDER + FORM,

"about.html": [
    ("<title>About | AEVA Interior Design Singapore</title>", "<title>关于我们 | AEVA 新加坡室内设计</title>"),
    ('content="AEVA is a Singapore interior design studio with its own carpentry workshop. Warm, timber-filled homes, built for generations."',
     'content="AEVA 是一家拥有自家木工坊的新加坡室内设计工作室。温暖的木质家居，为世代而筑。"'),
    ('<span class="label">About</span><span class="label">Built for generations</span>', '<span class="label">关于我们</span><span class="label">为世代而筑</span>'),
    ("Made to be <em>handed down</em>.", "经得起<em>代代相传</em>。"),
    ("A home should be warm enough to slow down in, and strong enough to <em>outlast us</em>.", "一个家，应该温暖得让人愿意放慢脚步，也坚固得<em>比我们更长久</em>。"),
    ('<span class="label">Our story</span>', '<span class="label">我们的故事</span>'),
    ("It started with a cot. Our founder built one for their own child in a borrowed corner of a friend's workshop, simple, solid and warm. It's still in the family today. That cot became the idea behind AEVA: design homes around the people who live in them, especially the little ones, and build everything well enough to outlast trends.",
     "一切从一张婴儿床开始。我们的创办人在朋友工坊借来的一角，为自己的孩子亲手做了一张婴儿床，简单、结实又温暖，直到今天仍留在家里。这张婴儿床成了 AEVA 的初心：围绕住在里面的人设计家，尤其是孩子，并把每一件作品做得足够好，经得起时间与潮流的考验。"),
    ('<span class="label">What we stand for</span>', '<span class="label">我们的坚持</span>'),
    ("Three things we <em>never compromise</em> on.", "三件我们<em>绝不妥协</em>的事。"),
    ("<h3>Craft you can feel</h3><p>Run your hand along any AEVA cabinet. No sharp edges, no gaps, no wobble. Our carpenters take pride in the details nobody photographs.</p>",
     "<h3>摸得到的工艺</h3><p>用手摸一摸任何一个 AEVA 柜子：没有尖角，没有缝隙，没有晃动。我们的木工师傅对那些没人拍照的细节同样讲究。</p>"),
    ("<h3>Safe for small hands</h3><p>Rounded corners, soft-close hinges, low-VOC finishes and anchored furniture come standard, never as an upgrade.</p>",
     "<h3>呵护小手的安全</h3><p>圆角、缓冲铰链、低VOC涂料和固定式家具都是标配，从来不是加价选项。</p>"),
    ("<h3>Warmth over trends</h3><p>Timber, linen and soft light never go out of style. We design homes that will still feel right in twenty years.</p>",
     "<h3>温暖胜于潮流</h3><p>木材、亚麻和柔和的灯光永不过时。我们设计的家，二十年后依然恰到好处。</p>"),
    ('<span class="label gold">Our workshop</span>', '<span class="label gold">我们的工坊</span>'),
    ("Why we <em>build it ourselves</em>.", "为什么我们<em>坚持自己做</em>。"),
    ("Most interior firms design the space and pass the carpentry to a subcontractor. We kept it in-house from day one. The person who drew your wardrobe can walk over and check it on the bench, and if anything ever needs fixing, we know exactly how it was made.",
     "大多数室内设计公司负责设计，再把木工交给分包商。我们从第一天起就坚持自己做。画出你衣柜的人，可以直接走到工作台旁检查成品；日后如果需要维修，我们也最清楚它是怎么做的。"),
    ('<span class="label">Recognition</span>', '<span class="label">荣誉</span>'),
    ("Awards <em>&amp; features</em>.", "奖项<em>与报道</em>。"),
    ("<span>Year</span><span>Award name</span><span>Awarding body</span>", "<span>年份</span><span>奖项名称</span><span>颁奖机构</span>"),
    ("<span>Year</span><span>Featured in</span><span>Publication</span>", "<span>年份</span><span>刊登于</span><span>刊物名称</span>"),
    ("Come visit <em>the showroom</em>.", "欢迎<em>参观展厅</em>。"),
    ("See the materials, feel the finishes, meet the people who'll build your home.", "亲眼看看材料，亲手感受质感，认识将为你打造家的团队。"),
    ("Arrange a visit", "预约参观"),
] + FOUNDER,

"services.html": [
    ("<title>Services | AEVA Interior Design Singapore</title>", "<title>服务 | AEVA 新加坡室内设计</title>"),
    ('content="Custom carpentry, kids rooms and nurseries, ambient lighting design and full home renovation for HDB, condo and landed homes in Singapore."',
     'content="为新加坡组屋、公寓与有地住宅提供定制木工、儿童房与婴儿房、氛围灯光设计及全屋装修。"'),
    ('<span class="label">Services</span><span class="label">Designed in our studio · Built in our workshop</span>', '<span class="label">服务</span><span class="label">工作室设计 · 自家工坊打造</span>'),
    ("One team, <em>start to finish</em>.", "一个团队，<em>从头到尾</em>。"),
    ("From first sketch to final screw, the same people design and build your home. That's how we keep the quality high and the timeline honest.",
     "从第一张草图到最后一颗螺丝，设计和打造你家的都是同一班人。这样我们才能确保品质，工期也实实在在。"),
    ("01 &nbsp;·&nbsp; Our specialty", "01 &nbsp;·&nbsp; 我们的专长"),
    ("Custom <em>carpentry</em>", "定制<em>木工</em>"),
    ("Carpentry is the backbone of every AEVA home. Our workshop builds everything to measure, from full-height wardrobes to a single floating shelf, in solid wood and quality plywood with real timber veneers.",
     "木工是每一个 AEVA 家的骨架。我们的工坊按尺寸打造一切，从落地衣柜到一块悬浮层板，选用实木和优质夹板，搭配真木皮。"),
    ("<li>Wardrobes, walk-ins and storage walls</li><li>Kitchen cabinets and islands</li><li>TV consoles, fluted panels and feature walls</li><li>Window seats, benches and reading nooks</li><li>Rounded edges and soft-close hardware as standard</li>",
     "<li>衣柜、步入式衣帽间与收纳墙</li><li>厨房橱柜与中岛</li><li>电视柜、凹槽板与造型墙</li><li>窗台座椅、长凳与阅读角</li><li>圆角收边与缓冲五金为标配</li>"),
    ("02 &nbsp;·&nbsp; For families", "02 &nbsp;·&nbsp; 为家庭而设"),
    ("Kids' rooms <em>&amp; nurseries</em>", "儿童房<em>与婴儿房</em>"),
    ("Children change fast, so their rooms should too. We design nurseries, shared bedrooms and study spaces that adapt from cot to teenage years with as little rework as possible.",
     "孩子长得快，房间也应该跟得上。我们设计的婴儿房、共享卧室和学习空间，从婴儿床到青少年时期都能灵活调整，尽量减少日后翻修。"),
    ("<li>Loft beds, bunk beds and play dens</li><li>Convertible cots, changing tables and desks</li><li>Toy storage at kid height</li><li>Low-VOC paints and child-safe finishes</li>",
     "<li>阁楼床、双层床与游戏小屋</li><li>可转换婴儿床、尿布台与书桌</li><li>孩子够得着的玩具收纳</li><li>低VOC涂料与儿童安全饰面</li>"),
    ("03 &nbsp;·&nbsp; The finishing glow", "03 &nbsp;·&nbsp; 点睛之光"),
    ("Ambient <em>lighting</em>", "氛围<em>灯光</em>"),
    ("Good light is what makes timber come alive. Every project gets a lighting plan that layers warm cove lights, backlit reveals and dimmable fittings, so each room works for homework and for bedtime.",
     "好的灯光让木材活起来。每个项目都附有灯光规划，层层叠加暖色灯槽、背光造型与可调光灯具，让每个房间既适合做功课，也适合睡前时光。"),
    ("<li>Warm 2700K to 3000K throughout</li><li>Cove, cabinet and under-bed strip lighting</li><li>Dimmers and scene control</li><li>Soft night lights for kids' rooms and corridors</li>",
     "<li>全屋2700K至3000K暖光</li><li>灯槽、柜内与床底灯带</li><li>调光器与情景控制</li><li>儿童房与走廊的柔和夜灯</li>"),
    ("04 &nbsp;·&nbsp; Start to finish", "04 &nbsp;·&nbsp; 从头到尾"),
    ("Full <em>renovation</em>", "全屋<em>装修</em>"),
    ("For new BTOs, resale flats, condos and landed homes. We handle design, permits, hacking, wet works, electrical, plumbing and of course the carpentry, with one project lead who answers your WhatsApps.",
     "适用于新预购组屋、转售组屋、公寓和有地住宅。设计、准证、拆除、泥水、电工、水管，当然还有木工，全都由我们负责，并由一位项目负责人亲自回复你的 WhatsApp。"),
    ("<li>HDB BTO and resale</li><li>Condominium makeovers</li><li>Landed home interiors</li><li>Permit applications handled for you</li>",
     "<li>预购组屋与转售组屋</li><li>公寓翻新</li><li>有地住宅室内设计</li><li>代办装修准证</li>"),
    ("05 &nbsp;·&nbsp; The finishing touches", "05 &nbsp;·&nbsp; 画龙点睛"),
    ("Furniture <em>sourcing</em>", "家具<em>采购</em>"),
    ("Beyond carpentry, we help you find and order the loose furniture that completes your home, from sofas and dining sets to lighting and kids' pieces. We source from trusted suppliers and Taobao, check the sizes against your floor plan, and customise finishes and fabrics so every piece fits your space and matches your carpentry.",
     "除了木工，我们也帮你挑选和订购让家更完整的活动家具，从沙发、餐桌椅到灯具和儿童家具。我们从可靠的供应商和淘宝采购，对照你的平面图核对尺寸，并定制饰面和布料，让每件家具都与你的空间和木工完美搭配。"),
    ("<li>Taobao and overseas ordering, handled for you</li><li>Sizes checked against your floor plan before you buy</li><li>Custom fabrics, finishes and dimensions</li><li>Delivery coordinated with your renovation timeline</li><li>Styled to match your carpentry and lighting</li>",
     "<li>淘宝与海外订购，全程代办</li><li>购买前对照平面图核对尺寸</li><li>定制布料、饰面与尺寸</li><li>配合装修进度安排送货</li><li>与木工和灯光风格统一</li>"),
    ('<span class="label">Questions</span>', '<span class="label">常见问题</span>'),
    ("Things parents <em>usually ask</em>.", "家长们<em>常问的问题</em>。"),
    ("<summary>How long does a renovation take?</summary><p>A single kids' room usually takes 3 to 5 weeks from approved design to installation. A full HDB home is typically 8 to 12 weeks, and condos or landed homes 10 to 16 weeks, depending on scope.</p>",
     "<summary>装修需要多长时间？</summary><p>单间儿童房从设计确认到安装，通常需要3至5周。整间组屋一般需要8至12周，公寓或有地住宅则视工程范围需要10至16周。</p>"),
    ("<summary>Is everything really made in your own workshop?</summary><p>Yes. Our carpenters fabricate in our own workshop, so we control the materials, the finish and the schedule. It's also why we can stand behind every piece with a 10-year carpentry warranty.</p>",
     "<summary>所有东西真的都在自家工坊制作吗？</summary><p>是的。我们的木工师傅在自家工坊制作，所以材料、做工和进度都由我们掌控。这也是我们能为每一件作品提供10年木工保修的原因。</p>"),
    ("<summary>What materials do you use for kids' furniture?</summary><p>Solid wood or high-grade plywood with real timber veneer, low-VOC finishes, rounded edges and soft-close hardware. We avoid sharp corners and anything that can trap small fingers.</p>",
     "<summary>儿童家具用什么材料？</summary><p>实木或高级夹板配真木皮、低VOC涂料、圆角收边和缓冲五金。我们避免尖角，以及任何可能夹到小手指的设计。</p>"),
    ("<summary>Can you work with our existing furniture?</summary><p>Of course. We'll plan around the pieces you love and design new carpentry to match.</p>",
     "<summary>可以配合我们现有的家具吗？</summary><p>当然可以。我们会围绕你喜爱的家具来规划，并设计相配的新木工。</p>"),
    ("<summary>Do you handle HDB permits?</summary><p>Yes, permit applications are part of the project.</p>",
     "<summary>你们会代办组屋装修准证吗？</summary><p>会的，准证申请已包含在项目中。</p>"),
    ("<summary>Can you help us order furniture from Taobao?</summary><p>Yes. We'll help you shortlist pieces, check the measurements against your layout, arrange customisation where needed, and coordinate the ordering and delivery so it arrives when your home is ready for it.</p>",
     "<summary>可以帮我们在淘宝订购家具吗？</summary><p>可以。我们会帮你筛选心仪的家具，对照你的空间核对尺寸，需要时安排定制，并协调订购和送货，让家具在你家准备好时准时送达。</p>"),
    ("Not sure where <em>to start?</em>", "不知道<em>从何开始？</em>"),
    ("Send us your floor plan and a few photos. We'll suggest a direction, free.", "把你的平面图和几张照片发给我们，我们免费为你建议设计方向。"),
    ('class="btn solid">Talk to us</a>', 'class="btn solid">联系我们</a>'),
],

"designs.html": [
    ("<title>Designs | AEVA Interior Design Singapore</title>", "<title>设计 | AEVA 新加坡室内设计</title>"),
    ('content="Explore AEVA design concepts: kids\' rooms, nurseries, living rooms, kitchens and studies, all designed and built by hand in our own workshop."',
     'content="探索 AEVA 的设计概念：儿童房、婴儿房、客厅、厨房与书房，全部在自家工坊亲手设计与打造。"'),
    ('<span class="label">Designs</span>', '<span class="label">设计</span>'),
    ("Designs,<br> <em>made to be lived in</em>.", "设计，<br><em>为生活而生</em>。"),
    ("A look at what we can design and build for your family. Every concept can be tailored to your layout, your budget and the way you live.",
     "看看我们能为你的家庭设计和打造什么。每个概念都可以根据你的格局、预算和生活方式量身调整。"),
    ('data-f="all">All</button>', 'data-f="all">全部</button>'),
    ("data-f=\"kids\">Kids' spaces</button>", 'data-f="kids">儿童空间</button>'),
    ('data-f="carpentry">Carpentry</button>', 'data-f="carpentry">木工</button>'),
    ('data-f="hdb">HDB</button>', 'data-f="hdb">组屋</button>'),
    ('data-f="condo">Condo</button>', 'data-f="condo">公寓</button>'),
    ('data-f="landed">Landed</button>', 'data-f="landed">有地住宅</button>'),
    ('data-view="featured">Featured</button>', 'data-view="featured">精选</button>'),
    ('data-view="index">Index</button>', 'data-view="index">索引</button>'),
    ("Like what you see?<br><span class=\"gold-txt\">Let's make it yours</span>", "喜欢吗？<br><span class=\"gold-txt\">让它成为你的家</span>"),
    ('class="btn solid">Start a conversation</a>', 'class="btn solid">开始对话</a>'),
    ('.padStart(2, "0") + " designs";', '.padStart(2, "0") + " 个设计";'),
],

"design.html": [
    ("<title>Design | AEVA Interior Design Singapore</title>", "<title>设计 | AEVA 新加坡室内设计</title>"),
    ('content="An AEVA home: the story, the carpentry and the details."', 'content="AEVA 的设计：理念、木工与细节。"'),
    ('class="link">All designs <span', 'class="link">全部设计 <span'),
    ('<span class="label gold">The idea</span>', '<span class="label gold">设计理念</span>'),
    ("<span class=\"label gold\">What we'd build</span>", '<span class="label gold">我们会打造</span>'),
    ("Want this <span class=\"gold-txt\">in your home?</span>", "想把它<span class=\"gold-txt\">搬进你家吗？</span>"),
    ("WhatsApp us about this design", "就这个设计 WhatsApp 我们"),
    ('<span class="label">Next design</span>', '<span class="label">下一个设计</span>'),
    ("document.title = `${p.title} | AEVA Interior Design Singapore`;", "document.title = `${p.title} | AEVA 新加坡室内设计`;"),
    ("<div><span>Space</span>", "<div><span>空间</span>"),
    ("<div><span>Ideal for</span>", "<div><span>适合</span>"),
    ("<div><span>Materials</span>", "<div><span>材料</span>"),
    ("<div><span>Typical build</span>", "<div><span>一般工期</span>"),
    ("`Hi AEVA, I like \"${p.title}\" and I'd like to find out more...`", "`你好 AEVA，我喜欢「${p.title}」这个设计，想了解更多...`"),
],

"contact.html": [
    ("<title>Contact | AEVA Interior Design Singapore</title>", "<title>联系我们 | AEVA 新加坡室内设计</title>"),
    ('content="Book a free consult with AEVA. Tell us about your home and family and we will get back within one working day."',
     'content="预约 AEVA 免费咨询。告诉我们你的家和家人，我们会在一个工作日内回复。"'),
    ('<span class="label">Contact</span><span class="label">Reply within one working day</span>', '<span class="label">联系我们</span><span class="label">一个工作日内回复</span>'),
    ("Get directions <span", "获取路线 <span"),
    ('<span class="label">Hours</span>', '<span class="label">营业时间</span>'),
    ('<label for="t">Property</label>', '<label for="t">房屋类型</label>'),
    ('<option value="">Choose one</option><option>HDB BTO</option><option>HDB Resale</option><option>Condominium</option><option>Landed</option><option>Commercial</option>',
     '<option value="">请选择</option><option>预购组屋 (BTO)</option><option>转售组屋</option><option>公寓</option><option>有地住宅</option><option>商业空间</option>'),
    ('<label for="s">Scope</label>', '<label for="s">工程范围</label>'),
    ("<option value=\"\">Choose one</option><option>Full home renovation</option><option>Kids' room or nursery</option><option>Carpentry only</option><option>Lighting upgrade</option><option>Furniture sourcing (incl. Taobao)</option><option>Not sure yet</option>",
     '<option value="">请选择</option><option>全屋装修</option><option>儿童房或婴儿房</option><option>只做木工</option><option>灯光升级</option><option>家具采购（包括淘宝）</option><option>还不确定</option>'),
    ('<label for="b">Rough budget</label>', '<label for="b">大概预算</label>'),
    ('<option value="">Choose one</option><option>Below $20k</option><option>$20k to $40k</option><option>$40k to $70k</option><option>$70k to $120k</option><option>Above $120k</option>',
     '<option value="">请选择</option><option>$20k 以下</option><option>$20k 至 $40k</option><option>$40k 至 $70k</option><option>$70k 至 $120k</option><option>$120k 以上</option>'),
] + FORM,

"coming-soon.html": [
    ("<title>Coming soon | AEVA</title>", "<title>即将推出 | AEVA</title>"),
    ('content="AEVA social channels are coming soon."', 'content="AEVA 社交媒体频道即将推出。"'),
    ('<h1 style="margin-top:20px">Coming soon</h1>', '<h1 style="margin-top:20px">即将推出</h1>'),
    ("We're putting the finishing touches on this channel.<br class=\"cs-br\"> In the meantime, come say hello on Instagram.", "我们正在为这个频道做最后的准备。<br class=\"cs-br\">在此期间，欢迎到 Instagram 和我们打招呼。"),
    ("Follow @aevacarpentry", "关注 @aevacarpentry"),
    ('class="btn">Back to home</a>', 'class="btn">返回首页</a>'),
    ('textContent = "AEVA on " + names[k];', 'textContent = "AEVA " + names[k];'),
    ("document.title = `${names[k]} coming soon | AEVA`;", "document.title = `${names[k]} 即将推出 | AEVA`;"),
],

"thank-you.html": [
    ("<title>Thank you | AEVA</title>", "<title>谢谢 | AEVA</title>"),
    ('content="Enquiry received."', 'content="已收到你的咨询。"'),
    ('<span class="label">Enquiry received</span>', '<span class="label">已收到咨询</span>'),
    ("Thank you. <em>We'll be in touch.</em>", "谢谢你。<em>我们会尽快联系你。</em>"),
    ("One of our designers will reply within one working day. In the meantime, have a look around.", "我们的设计师会在一个工作日内回复你。在此期间，欢迎随意看看。"),
    ("Explore our designs", "探索我们的设计"),
],
}

COMMON = [
    ('<html lang="en">', '<html lang="zh-Hans">'),
    ('data-cursor="View"', 'data-cursor="查看"'),
    ('data-cursor="Next"', 'data-cursor="下一个"'),
]

errors = []
for page, pairs in PAGES.items():
    s = open(page, encoding="utf-8").read()
    for en, zh in COMMON + pairs:
        if en not in s:
            if en.startswith('data-cursor'):
                continue
            errors.append(f"{page}: not found -> {en[:90]}")
            continue
        s = s.replace(en, zh)
    s = s.replace(TITLE_SUFFIX[0], TITLE_SUFFIX[1])
    # paths up one level, shared files, Chinese fonts, zh data
    s = s.replace('href="styles.css"', 'href="../styles.css"')
    s = s.replace('src="vendor/', 'src="../vendor/')
    s = s.replace('src="main.js"', 'src="../main.js"')
    s = s.replace('src="projects.js"', 'src="../projects-zh.js"')
    s = re.sub(r'(?<!\.\./)images/', '../images/', s)
    s = s.replace("family=Jost:wght@300;400;500&display=swap", "family=Jost:wght@300;400;500" + NOTO + "&display=swap")
    s = re.sub(r'<link rel="alternate" hreflang="zh" href="zh/[^"]*">', f'<link rel="alternate" hreflang="en" href="../{page}">', s)
    open(os.path.join("zh", page), "w", encoding="utf-8").write(s)

if errors:
    print("\n".join(errors)); sys.exit(1)
print("Chinese pages built:", ", ".join(PAGES))
