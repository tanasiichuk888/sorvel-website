"""Case studies built from the Figma portfolio file (design-led projects).
Facts only: scope, industry, decisions visible in the design. No invented results."""
import re
W = "WEBSITE_DIR/work/"
SHELL = open(W + "valhalla-capital.html").read()
PHONE = re.search(r'<div class="cs-cover__phone iphone"[^>]*>(.*?)<img', SHELL, re.S).group(1)

def phone(cls, src, alt, par):
    return f'<div class="{cls} iphone" data-parallax="{par}">{PHONE}<img src="{src}" alt="{alt}" loading="lazy" decoding="async"></span></span></span></div>'

def win(src, alt, url="", cls="cs-shot", eager=False):
    u = f'<span class="win__url">{url}</span>' if url else ""
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<div class="vwin {cls}" data-parallax=".03"><div class="win__bar"><i></i><i></i><i></i>{u}</div><img src="{src}" alt="{alt}" width="1600" height="1000" {load}></div>'

PROCESS = [
    ("Brief", "Goals and audience", "We started with who the site is for, what they need to believe and the one action that matters most.", ["Audience and goals", "Content inventory", "Reference review"]),
    ("Structure", "Page flow first", "A section-by-section outline of the homepage, so the story was agreed before any visuals.", ["Section outline", "Messaging hierarchy", "Calls to action"]),
    ("Design", "Desktop and mobile", "The full homepage designed in Figma for desktop and mobile on one set of styles and components.", ["Desktop layout", "Mobile layout", "Components and styles"]),
    ("Handover", "Ready to build", "Organised, named layers and reusable components, so development could start without guesswork.", ["Clean Figma file", "Reusable components", "Build-ready specs"]),
]

C = {
"noir": dict(name="NOIR Properties", short="NOIR", tag="Real estate · Website design", eyebrow="Real estate · Costa Blanca and Costa del Sol · Spain",
  title=["A Spanish property agency", 'that feels <span class="accent">personal</span>.'], url="noirproperties.com",
  lead="NOIR Properties helps international buyers find homes on the Costa Blanca and Costa del Sol, with AI-powered property matching. We designed a website that pairs a confident, editorial look with fast search, real client stories and a direct line to the agents.",
  facts=[("Client", "NOIR Properties"), ("Industry", "Real estate, Spain"), ("Scope", "Website design, desktop and mobile"), ("Tools", "Figma")],
  ch=("The challenge", 'Buying abroad is a leap. <span class="dim">The site has to make it feel safe.</span>'),
  chp=["Most visitors are buying a home in another country, often for the first time. They need to trust the agency before they trust a listing, and they want to start searching straight away.",
       "NOIR also had a story worth telling: a licensed agency with over ten years of local experience and an AI matching approach that sets it apart from listing portals."],
  goals=["Search on the first screen", "Trust signals early on the page", "A personal, human tone"],
  probs=[("Trust from a distance", "Buyers abroad can't walk into the office, so licence, experience and real people had to be visible."), ("Search without friction", "Area, budget and bedrooms needed to be one step away, not buried in a menu."), ("More than a portal", "The agency's AI matching and personal service had to stand out from listing sites.")],
  rows=[("About", "Credentials up front.", "The about block leads with a real photo, ten-plus years of experience and the agency's registration number, then signs off with the broker's name. Trust comes before listings.", "s1", "About section with agency credentials"),
        ("Stories", "A buyer tells it best.", "A client video and pull-quote show what moving to Spain actually felt like, in the buyer's own words, right after the introduction.", "s2", "Client story with video"),
        ("Listings", "Recommended homes, not a wall of ads.", "Property cards with price, location, beds, baths and size, framed as personal recommendations from NOIR rather than search results.", "s3", "Recommended property cards")],
  mob=("The same agency in your pocket.", "Search, client story and listings stack into one clear scroll, with the WhatsApp action always within reach on a phone."),
  dec=[("What's on the first screen?", "A big photo and a slogan.", "The slogan plus a search bar for area, budget and bedrooms, so buyers can start straight away."),
       ("How do you show trust?", "Logos and a generic promise.", "Licence number, years of experience, a named broker and a real client story."),
       ("How do people get in touch?", "A long contact form.", "A direct WhatsApp line, repeated at the end of the page.")],
  out=[("Desktop + mobile", "the full homepage designed for both"), ("Search first", "area, budget and bedrooms on the first screen"), ("Real stories", "client video and quote built into the page"), ("Direct contact", "WhatsApp action repeated through the page")],
  got=["Homepage design, desktop and mobile", "Property search and listing cards", "Client story section", "Blog layout", "Founder message block", "Build-ready Figma file"]),

"skyli": dict(name="Skyli", short="Skyli", tag="Fintech · AI expense tracker", eyebrow="Fintech · AI expense tracking · Pre-launch",
  title=["A money app that finds", 'your <span class="accent">forgotten</span> subscriptions.'], url="skyli.app",
  lead="Skyli is an AI expense tracker that spots forgotten subscriptions and quiet price increases. We designed a pre-launch website that explains the product in seconds, shows it working and turns visitors into waitlist sign-ups.",
  facts=[("Client", "Skyli"), ("Industry", "Fintech, personal finance"), ("Scope", "Pre-launch website, desktop and mobile"), ("Tools", "Figma")],
  ch=("The challenge", 'Selling an app <span class="dim">before it exists.</span>'),
  chp=["Skyli was pre-launch, so the website had one job: make people care about a problem they didn't know they had, then get them on the waitlist.",
       "It also had to earn trust fast. Anything that touches personal finances raises questions about data and bank access, and those answers needed to be on the page, not in a policy."],
  goals=["Make the problem obvious in seconds", "Show the product, not just describe it", "Answer privacy questions openly"],
  probs=[("An invisible problem", "Forgotten subscriptions are easy to ignore until someone shows you the total."), ("No product to try yet", "The site had to show how Skyli works before the app was public."), ("Money means trust", "People are careful about who sees their finances, so privacy had to be part of the pitch.")],
  rows=[("Problem", "Somewhere in your inbox, money is leaking out.", "A dark band names the problem in plain words, with an illustration of the receipts and renewal emails people never open.", "s1", "Problem section"),
        ("Product", "A two-way conversation about money.", "Chat-style product scenes show Skyli asking the questions you forgot to ask, so visitors see the experience instead of reading about it.", "s2", "Conversation product scenes"),
        ("Privacy", "Your data never leaves your control.", "No bank linking and GDPR-first principles get their own section with clear illustrations, turning a worry into a reason to sign up.", "s3", "Privacy section")],
  mob=("Built for the phone it lives on.", "Skyli is a mobile-first product, so the mobile layout leads with the live subscription card and a single waitlist action."),
  dec=[("What does the hero show?", "A phone mockup and a tagline.", "A live subscription list with the monthly total and a 'Skyli suggests' card, so the value is visible at once."),
       ("How do you handle privacy?", "A link to the privacy policy.", "A dedicated section: no bank linking required, data processed on your device, GDPR principles."),
       ("What is the one action?", "Several competing buttons.", "Join the waitlist, repeated with early-access framing.")],
  out=[("Desktop + mobile", "the full landing page designed for both"), ("Waitlist", "one clear action from hero to footer"), ("Product scenes", "chat and dashboard UI shown in context"), ("Privacy first", "trust answers built into the page")],
  got=["Pre-launch landing page", "Product UI scenes for marketing", "Illustration direction", "Mobile layout", "Waitlist flow", "Build-ready Figma file"]),

"open-select": dict(name="Open Select", short="Open Select", tag="Recruitment · B2B website design", eyebrow="Recruitment · Engineering hiring · USA",
  title=["A recruitment firm that", 'speaks <span class="accent">engineer</span>.'], url="openselect.com",
  lead="Open Select builds backend, infrastructure and AI teams for seed to growth-stage startups in the US. We designed a website that leads with the firm's numbers, tells real placement stories and speaks to both founders and engineers.",
  facts=[("Client", "Open Select"), ("Industry", "Technical recruitment, USA"), ("Scope", "Website design, desktop and mobile"), ("Tools", "Figma")],
  ch=("The challenge", 'Every recruiter says they\'re different. <span class="dim">Prove it.</span>'),
  chp=["Founders get messages from recruiters every week, and most sound the same. Open Select needed a site that sounds like it understands engineering and shows evidence instead of adjectives.",
       "The site also serves two audiences: founders hiring their first engineers, and engineers looking for their next role."],
  goals=["Lead with numbers, not claims", "Show real hiring stories", "Separate paths for founders and engineers"],
  probs=[("A crowded category", "Recruitment websites blur together, so the design had to feel closer to a tech product than an agency."), ("Proof over promises", "The firm's time-to-offer and retention figures had to be the headline."), ("Two audiences", "Founders and engineers needed their own clear route through the same site.")],
  rows=[("Proof", "The difference, by the numbers.", "Time to offer, cost per hire, retention and offer acceptance sit side by side as large figures, with what each one means for a founder.", "s1", "Numbers section"),
        ("Roles", "The hires that define a foundation.", "A teal band lists the roles Open Select places, from founding engineers to AI and ML, so founders see their own need named.", "s2", "Hires section"),
        ("People", "A real person behind the search.", "The founder's story and a 'What I actually do' section make the firm feel human and accountable.", "s3", "Founder section")],
  mob=("Clean and fast on a phone.", "A text-first hero, stacked numbers and full-width actions keep the mobile page short and easy to act on."),
  dec=[("What leads the page?", "A photo of a handshake.", "A clear promise and three numbers: days to hire, retention and acceptance rate."),
       ("How do you show experience?", "Client logos.", "Placement stories with the role, the timeline and what changed for the team."),
       ("Who is the site for?", "Everyone at once.", "Founders by default, with a dedicated 'For engineers' section and open roles.")],
  out=[("Desktop + mobile", "the full homepage designed for both"), ("Numbers first", "key hiring metrics as the first proof"), ("Two paths", "founders and engineers each get a route"), ("Founder-led", "a real person at the centre of the story")],
  got=["Homepage design, desktop and mobile", "Metrics and case story blocks", "Open roles section", "Founder profile section", "FAQ layout", "Build-ready Figma file"]),

"copliancy": dict(name="Copliancy", short="Copliancy", tag="SaaS · Compliance platform", eyebrow="B2B SaaS · Compliance and licensing · USA",
  title=["Compliance software", 'that looks <span class="accent">simple</span>.'], url="copliancy.com",
  lead="Copliancy is a web platform that helps businesses manage licences, permits and staff training in one place. We designed a marketing site that puts the real product front and centre and shows exactly which businesses it is built for.",
  facts=[("Client", "Copliancy"), ("Industry", "B2B SaaS, compliance"), ("Scope", "Marketing website, desktop and mobile"), ("Tools", "Figma")],
  ch=("The challenge", 'Compliance is complicated. <span class="dim">The website shouldn\'t be.</span>'),
  chp=["Restaurants, pharmacies, gas stations and liquor stores all deal with licences and renewals, but nobody wants to read about regulation.",
       "Copliancy needed a site that shows the product doing the work, so a busy owner understands it at a glance."],
  goals=["Show the real product UI", "Name the business types it serves", "Keep every section to one idea"],
  probs=[("A dry subject", "Licences and permits are not exciting, so the design had to feel fresh and calm."), ("Many business types", "Each type of business had to see itself on the page."), ("A complex product", "The platform does a lot, and the site had to explain it one feature at a time.")],
  rows=[("Audience", "Built for these businesses.", "Clear icons for restaurants, movie theaters, pharmacies, gas stations, markets and liquor stores, next to a real view of the product.", "s1", "Business types section"),
        ("Licences", "Track applications and renewals.", "A bold green band lists the licence types the platform handles, with layered dashboard screens showing the tracking.", "s2", "Licence tracking section"),
        ("Training", "Staff training in one place.", "Each feature gets its own section with a real screen, so the product explains itself.", "s4", "Training section")],
  mob=("Product screens that still read on a phone.", "Dashboard screens are scaled and layered so they stay legible on mobile, with the start action always visible."),
  dec=[("How do you show the product?", "Abstract illustrations.", "Layered screens from the real platform in every section."),
       ("Who is it for?", "\"Businesses of all kinds.\"", "Named business types with their own icons."),
       ("How is the page paced?", "Long feature lists.", "One feature per section, alternating light and green bands.")],
  out=[("Desktop + mobile", "the full marketing site designed for both"), ("Real UI", "product screens in every section"), ("Clear audience", "six business types named"), ("One idea per band", "a calm, easy-to-scan rhythm")],
  got=["Marketing website design", "Product screen compositions", "Business type icon set", "Mobile layout", "Feature sections", "Build-ready Figma file"]),

"visit-pemba": dict(name="Visit Pemba", short="Visit Pemba", tag="Tourism · Figma + WordPress", eyebrow="Tourism · Pemba Island · Zanzibar, Tanzania",
  title=["An island website", 'as <span class="accent">beautiful</span> as the island.'], url="visitpemba.tz", live="https://visitpemba.tz",
  lead="Visit Pemba is the travel guide for Pemba Island in the Zanzibar archipelago. We designed a website that sells the island through its landscapes, local stories and ready-made itineraries, and makes sending a trip inquiry the natural next step.",
  facts=[("Client", "Visit Pemba"), ("Industry", "Tourism, Tanzania"), ("Scope", "Website design, desktop and mobile, WordPress build"), ("Live site", '<a href="https://visitpemba.tz" target="_blank" rel="noopener">visitpemba.tz ↗</a>')],
  ch=("The challenge", 'Most travellers have <span class="dim">never heard of Pemba.</span>'),
  chp=["Pemba sits next to Zanzibar but gets a fraction of the visitors. The website had to introduce the island, make people want to go and help them plan a trip.",
       "It also had to reflect what makes Pemba different: untouched nature, a living Swahili culture and responsible tourism."],
  goals=["Sell the island visually", "Make planning easy", "Turn interest into trip inquiries"],
  probs=[("An unknown destination", "The site had to answer 'why Pemba?' within the first screen."), ("Many kinds of traveller", "Divers, families, culture lovers and honeymooners all needed a way in."), ("From dream to plan", "Inspiration had to lead to itineraries and a simple inquiry form.")],
  rows=[("Stories", "Stories that make the island unforgettable.", "Arched photo cards for clove farms, coral reefs, seaweed farmers and traditional dhows, inspired by Swahili doorways.", "s1", "Stories section"),
        ("Discovery", "Find your kind of Pemba.", "Filter tabs for marine, nature, culture, community and wellness experiences, each with duration and price.", "s2", "Experience finder"),
        ("Planning", "Ready-made itineraries.", "Two- and four-day plans with clear durations, so visitors can picture the whole trip and ask for it.", "s3", "Itineraries section")],
  mob=("Made for planning on a phone.", "Big imagery, swipeable cards and a short inquiry form, because most travellers plan on mobile."),
  dec=[("How do you introduce the island?", "A slideshow of beaches.", "A full-bleed aerial shot with four facts: dive sites, community focus, flight time and no mass tourism."),
       ("How do people explore?", "A long list of tours.", "Experience tabs by interest, then ready-made itineraries."),
       ("What does it feel like?", "Generic resort turquoise.", "Deep teal, warm sand and an editorial serif, with arches taken from local architecture.")],
  out=[("Desktop + mobile", "every page designed for both"), ("Live on WordPress", "built and launched at visitpemba.tz"), ("Itineraries", "ready-made trips that lead to inquiries"), ("Local identity", "Swahili arches and island colours")],
  got=["Website design, desktop and mobile", "Experience finder", "Itinerary pages", "Trip inquiry form", "WordPress build", "Design system in Figma"]),

"agentur": dict(name="KI-Agentur", short="KI-Agentur", tag="AI agency · Website design (DE)", eyebrow="AI automation · Agency · Austria and Germany",
  title=["An AI agency that", 'explains <span class="accent">AI agents</span> plainly.'], url="ki-agentur.wien",
  lead="A Vienna-based agency that builds custom AI agents and n8n automations for small and mid-sized businesses. We designed a German-language website that explains what an AI agent does, why it matters now and how working together looks, step by step.",
  facts=[("Client", "KI-Agentur, Vienna"), ("Industry", "AI automation"), ("Scope", "Website design in German, desktop and mobile"), ("Tools", "Figma")],
  ch=("The challenge", 'Everyone talks about AI. <span class="dim">Few explain what it does for your business.</span>'),
  chp=["Business owners hear about AI agents every day but rarely see what one would actually do in their company. The site had to make it concrete.",
       "The audience is German-speaking SMEs, so the tone had to be clear, precise and trustworthy, with data protection addressed early."],
  goals=["Explain AI agents in plain German", "Show the value with one clear chart", "Make the first consultation the obvious step"],
  probs=[("Abstract technology", "AI agents are hard to picture, so each one needed a job title and a list of tasks."), ("Healthy scepticism", "German-speaking businesses expect GDPR compliance and local partners."), ("A clear process", "Buyers needed to see the steps from analysis to support before booking a call.")],
  rows=[("Why now", "Why you should act now.", "A single growth chart compares companies with and without AI agents, making the case in one look.", "s1", "Why now chart section"),
        ("Agents", "Our AI agents for your company.", "Six agents on a dark band, each with a role, the tasks it takes over and the benefit, from content to sales.", "s2", "AI agents section"),
        ("Process", "Four steps to your AI agents.", "A vertical timeline from process analysis to training and support, with the tools used at each step.", "s3", "Process timeline")],
  mob=("Clear on every screen.", "Short paragraphs, stacked agent cards and a sticky consultation button keep the German copy readable on mobile."),
  dec=[("How do you explain an AI agent?", "Futuristic robot imagery.", "Agents named like team members, with the tasks they take over."),
       ("How do you address concerns?", "Small print in the footer.", "GDPR compliance and local partnership right under the hero."),
       ("What is the next step?", "\"Contact us.\"", "A free first consultation, repeated after each section.")],
  out=[("Desktop + mobile", "the full homepage designed for both"), ("German-first", "copy and layout designed for German"), ("Six agents", "each with a role and tasks"), ("Four steps", "a clear process from analysis to support")],
  got=["Homepage design, desktop and mobile", "AI agent cards", "Process timeline", "FAQ and contact sections", "Tech partner logo strip", "Build-ready Figma file"]),

"mutmachbuch": dict(name="Mutmachbuch", short="Mutmachbuch", tag="E-commerce · Shopify store design", eyebrow="E-commerce · Personalised children's books · Germany",
  title=["A bookshop where", 'every child is the <span class="accent">hero</span>.'], url="mutmachbuch.com", live="https://mutmachbuch.com",
  lead="Mutmachbuch creates personalised children's books that build confidence, with the child as the main character. We designed a Shopify store that feels as warm and magical as the books, while making personalising and ordering a book quick and clear.",
  facts=[("Client", "Mutmachbuch"), ("Industry", "E-commerce, children's books"), ("Scope", "Shopify store design, desktop and mobile"), ("Live site", '<a href="https://mutmachbuch.com" target="_blank" rel="noopener">mutmachbuch.com ↗</a>')],
  ch=("The challenge", 'Parents buy a feeling. <span class="dim">The store has to sell it.</span>'),
  chp=["A personalised book is a gift with a purpose: helping a child feel brave and capable. The store needed to show that story, not just a product grid.",
       "Personalisation also adds steps, so the path from choosing a book to ordering it had to stay simple."],
  goals=["Make the books the star", "Explain personalisation in four steps", "Show why the books help children grow"],
  probs=[("A gift, not a product", "Parents need to see the emotional value, not just the price."), ("Personalisation feels complex", "Choosing, personalising and adding a dedication had to feel easy."), ("Trust for a new brand", "Reviews, real authors and 'no AI texts' needed to be visible.")],
  rows=[("Collections", "Books for girls, boys and occasions.", "Large illustrated collection cards let parents start from who the book is for.", "s1", "Book collections"),
        ("Bestsellers", "Bestsellers with clear prices.", "Product cards with badges, sale prices and the occasion, ready for quick comparison.", "s2", "Bestseller cards"),
        ("Bundles", "Complete packages as gifts.", "Bundle cards for girls and boys list everything included, making a bigger gift an easy choice.", "s3", "Gift bundles")],
  mob=("Magic on a small screen.", "Covers, headline and the main action fit in the first screen, with the trust points right below."),
  dec=[("What leads the store?", "A product grid.", "The promise, 'Make your child the hero', with real book covers and two clear actions."),
       ("How is personalisation explained?", "A long FAQ.", "Four illustrated steps: choose, personalise, add a dedication, give."),
       ("How do you build trust?", "A review badge in the footer.", "Trustpilot rating under the hero, real authors and 'no AI texts' as checkmarks.")],
  out=[("Desktop + mobile", "the full store designed for both"), ("Live on Shopify", "launched at mutmachbuch.com"), ("Four steps", "personalisation explained at a glance"), ("Gift bundles", "packages designed for bigger orders")],
  got=["Shopify store design", "Homepage, desktop and mobile", "Collection and product cards", "Bundle sections", "Review and FAQ blocks", "Newsletter section"]),

"wehike": dict(name="WeHike", short="WeHike", tag="Travel · Website design", eyebrow="Travel · Guided hiking tours · Spain",
  title=["Guided hikes", 'you can <span class="accent">book</span> in a minute.'], url="wehike.ro",
  lead="WeHike runs guided hiking trips across Spain, from the Pyrenees to the Sierra Nevada. We designed a website that sparks the urge to go, then shows dates, difficulty and price on every trip so booking is one step away.",
  facts=[("Client", "WeHike"), ("Industry", "Travel, guided tours"), ("Scope", "Website design, desktop and mobile"), ("Tools", "Figma")],
  ch=("The challenge", 'Inspiration is easy. <span class="dim">Booking is where people drop off.</span>'),
  chp=["Hiking sites usually have beautiful photos and unclear details. WeHike wanted visitors to see the trips, dates and difficulty straight away.",
       "The audience ranges from beginners to experienced hikers, so every trip needed a clear level."],
  goals=["Search from the first screen", "Dates, level and price on every trip", "Show the guides' care and safety"],
  probs=[("Pretty but unclear", "Many tour sites hide the practical details behind extra clicks."), ("Mixed experience levels", "Beginners and experienced hikers needed to find the right trip fast."), ("Safety matters", "People want to know who is guiding them and how safe it is.")],
  rows=[("Trips", "Next trips at a glance.", "Trip cards show the place, price, dates and level, with availability badges like 'Few spots left' and 'Sold out'.", "s1", "Next trips cards"),
        ("Explore", "Explore by type of trip.", "A photo mosaic splits trips into mountain, advanced, coastal, Spain and family adventures, each with a trip count.", "s2", "Explore trip types"),
        ("Why us", "Local guides, custom routes, safety.", "Three clear reasons to book with WeHike, each with its own icon.", "s4", "Why choose us")],
  mob=("Ready for the trail.", "The search bar and trip cards come first on mobile, with booking buttons sized for a thumb."),
  dec=[("What's on the first screen?", "A slideshow and a slogan.", "A headline, a search bar and a real trail photo."),
       ("What does a trip card show?", "A photo and 'Learn more'.", "Price, dates, level, availability and two actions: details or book."),
       ("How do you show trust?", "Stock testimonials.", "Named reviews with the trip and date they took part in.")],
  out=[("Desktop + mobile", "the full homepage designed for both"), ("Bookable cards", "price, dates and level on every trip"), ("Trip types", "five ways to explore"), ("Clear levels", "from beginner to advanced")],
  got=["Homepage design, desktop and mobile", "Trip search", "Trip and category cards", "Testimonials section", "Blog layout", "Build-ready Figma file"]),
}

def page(slug, d):
    img = f"../img/work/{slug}/"
    t = "\n".join(f'          <span class="line"><span class="line__in">{x}</span></span>' for x in d["title"])
    facts = "\n".join(f'          <div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in d["facts"])
    goals = "".join(f"<li>{g}</li>" for g in d["goals"])
    probs = "\n".join(f'          <article data-reveal><h3>{a}</h3><p>{b}</p></article>' for a, b in d["probs"])
    phases = "\n".join(f'          <div class="cs-phase"><p class="cs-phase__when">{w}</p><h3>{h}</h3><p>{p}</p><ul>{"".join(f"<li>{x}</li>" for x in li)}</ul></div>' for w, h, p, li in PROCESS)
    rows = "\n".join(f'''        <article class="cs-row{" cs-row--flip" if i % 2 else ""}">
          <div class="cs-row__text" data-reveal><p class="eyebrow">{e}</p><h3>{h}</h3><p>{p}</p></div>
          <div class="cs-stage" data-reveal>{win(img + f + ".webp", a)}</div>
        </article>''' for i, (e, h, p, f, a) in enumerate(d["rows"]))
    dec = "\n".join(f'''          <div class="cs-dec__row" data-reveal>
            <h3 class="cs-dec__q">{q}</h3>
            <div class="cs-dec__col cs-dec__no"><span class="cs-dec__lbl">The usual answer</span><p>{n}</p></div>
            <div class="cs-dec__col cs-dec__yes"><span class="cs-dec__lbl">What we did</span><p>{y}</p></div>
          </div>''' for q, n, y in d["dec"])
    out = "\n".join(f'          <div data-reveal><b>{a}</b><span>{b}</span></div>' for a, b in d["out"])
    got = "".join(f"<li>{x}</li>" for x in d["got"])
    reel = "".join(f'<img src="{img}{f}.webp" alt="" loading="lazy" width="1600" height="1000">' for f in ["s1", "s2", "s3", "s4", "hero"] * 2)
    mh, mp = d["mob"]
    main = f'''<main class="cs cs--vh">
    <div class="cs-progress" aria-hidden="true"><i></i></div>
    <!-- ============ CASE HERO ============ -->
    <section class="cs-hero">
      <canvas class="hero__dots" aria-hidden="true"></canvas>
      <div class="wrap">
        <nav class="cs-crumbs" data-intro><a href="../work.html">Work</a><span>/</span><span>{d["name"]}</span></nav>
        <p class="eyebrow" data-intro>{d["eyebrow"]}</p>
        <h1 class="cs-title">
{t}
        </h1>
        <p class="cs-lead" data-intro>{d["lead"]}</p>
        <dl class="cs-facts" data-intro>
{facts}
        </dl>
      </div>
      <div class="wrap cs-cover" data-intro>
        {phone("cs-cover__phone", img + "m-hero.webp", "", "-.1")}
        {win(img + "hero.webp", d["name"] + " homepage", d["url"], "cs-win", eager=True)}
      </div>
    </section>

    <!-- ============ CHALLENGE ============ -->
    <section data-chapter="Challenge" class="sec cs-brief">
      <div class="wrap cs-split">
        <div data-reveal><p class="eyebrow">{d["ch"][0]}</p><h2 class="h2">{d["ch"][1]}</h2></div>
        <div class="cs-text" data-reveal>
          {"".join(f"<p>{x}</p>" for x in d["chp"])}
          <ul class="cs-goals">{goals}</ul>
        </div>
      </div>
      <div class="wrap">
        <div class="cs-problems">
{probs}
        </div>
      </div>
    </section>

    <!-- ============ HOW WE WORKED ============ -->
    <section data-chapter="Process" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head sec__head--row" data-reveal>
          <div><p class="eyebrow">How we worked</p><h2 class="h2">Structure first, <span class="dim">then the pixels.</span></h2></div>
          <p class="sec__lead">The same four steps on every project, so the client signs off the story before the design and the design before the build.</p>
        </header>
        <div class="cs-process" data-reveal>
{phases}
        </div>
      </div>
    </section>

    <!-- ============ FIGMA ============ -->
    <section data-chapter="System" class="sec cs-figma">
      <div class="wrap">
        <header class="sec__head sec__head--row" data-reveal>
          <div><p class="eyebrow">Design first</p><h2 class="h2">Every section, <span class="dim">desktop and mobile.</span></h2></div>
          <p class="sec__lead">The full page designed in Figma for both breakpoints on one set of styles and components, so the build had a clear blueprint.</p>
        </header>
        <div class="figma figma--solo" data-reveal>
          <div class="vwin figma__canvas" data-parallax=".03"><div class="win__bar"><i></i><i></i><i></i><span class="win__url">Figma · {d["name"]}</span></div><img src="{img}figma.webp" alt="Figma canvas with the {d["name"]} desktop and mobile designs" width="1600" height="1113" loading="lazy" decoding="async"></div>
        </div>
      </div>
    </section>

    <!-- ============ DETAILS ============ -->
    <section data-chapter="Details" class="sec cs-story">
      <div class="wrap">
{rows}
      </div>
    </section>

    <!-- ============ MOBILE ============ -->
    <section class="sec cs-duo">
      <div class="wrap cs-duo__grid">
        <div class="cs-duo__code" data-reveal>
          <p class="eyebrow">Mobile</p>
          <h3>{mh}</h3>
          <p>{mp}</p>
          {win(img + "hero.webp", d["name"] + " desktop homepage")}
        </div>
        <div class="cs-phones cs-phones--solo" data-reveal>
          {phone("cs-phone", img + "m-hero.webp", d["name"] + " mobile homepage", ".08")}
        </div>
      </div>
    </section>

    <!-- ============ REEL ============ -->
    <section class="cs-reel" aria-hidden="true">
      <div class="cs-reel__track">{reel}</div>
    </section>

    <!-- ============ KEY DECISIONS ============ -->
    <section data-chapter="Decisions" class="sec cs-chapter">
      <div class="wrap">
        <header class="sec__head" data-reveal><p class="eyebrow">Key decisions</p><h2 class="h2">Small choices <span class="dim">that shape the page.</span></h2></header>
        <div class="cs-dec">
{dec}
        </div>
      </div>
    </section>

    <!-- ============ RESULT ============ -->
    <section data-chapter="Result" class="sec cs-result">
      <div class="wrap">
        <header class="sec__head" data-reveal><p class="eyebrow">What was delivered</p><h2 class="h2">Designed, <span class="dim">ready to ship.</span></h2></header>
        <div class="cs-outcomes">
{out}
        </div>
        <div class="cs-got" data-reveal>
          <h3>What {d["short"]} <br>walked away with</h3>
          <ul>{got}</ul>
        </div>
      </div>
    </section>

    <!-- ============ MORE WORK ============ -->
    <!-- ============ NEXT ============ -->'''
    s = SHELL
    nxt = s.index("    <!-- ============ NEXT ============ -->")
    a = s.index("<main")
    s = s[:a] + main + s[nxt + len("    <!-- ============ NEXT ============ -->"):]
    title = f'{d["name"]} case study | {d["tag"]} | Sorvel'
    s = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{d["lead"][:155].rsplit(" ", 1)[0]}…"', s, count=1)
    s = s.replace("<!-- ============ MORE WORK ============ -->\n    <!-- ============ NEXT ============ -->",
                  "<!-- ============ MORE WORK ============ -->\n    <!-- ============ NEXT ============ -->", 1)
    open(W + slug + ".html", "w").write(s)
    print("case", slug)

for k, v in C.items():
    page(k, v)
