import sys, json, re; sys.path.insert(0, "SOURCE_DIR/site")
from common import *

S = "https://sorvel.agency"
G = [
("Platforms", [
 ("webflow", "Webflow", "A visual website builder with built-in hosting and a CMS. Designers build real HTML and CSS without writing code, and marketing teams edit content without a developer. Best for content-rich marketing sites.", "services/webflow-agency.html"),
 ("framer", "Framer", "A website builder that works like a design tool. It is fast for launch sites and motion-rich pages, with a simpler CMS than Webflow.", "blog/webflow-vs-framer.html"),
 ("wordpress", "WordPress", "An open-source content management system that runs about two in five websites. Very flexible through themes and plugins, but hosting, updates and security are the owner's job.", "blog/webflow-vs-wordpress.html"),
 ("cms", "CMS (content management system)", "The part of a website where content lives as structured items, such as blog posts, case studies or team members, so editors can add pages without touching the design.", ""),
 ("headless-cms", "Headless CMS", "A CMS that stores content only and sends it to a separately built front end through an API. Flexible for large products, but it needs developers for most changes.", ""),
 ("no-code", "No-code website", "A website built in a visual tool like Webflow or Framer instead of hand-written code. It is still real, fast, indexable HTML, and the team can edit it without developers.", ""),
]),
("SEO and migrations", [
 ("migration", "Website migration", "Moving a website from one platform to another, for example from WordPress to Webflow, while keeping content, URLs, links and search rankings.", "services/wordpress-to-webflow-migration.html"),
 ("redirect-301", "301 redirect", "A permanent redirect from an old URL to a new one. It passes most of the old page's ranking power to the new page, which is why every changed URL needs one after a migration.", "blog/migrate-wordpress-to-webflow-without-losing-seo.html"),
 ("redirect-map", "Redirect map", "A list that pairs every old URL with its closest new URL. It is the single most important document in a migration that keeps traffic.", "blog/migrate-wordpress-to-webflow-without-losing-seo.html"),
 ("core-web-vitals", "Core Web Vitals", "Google's three page-experience metrics, measured on real visitors: LCP (how fast the main content shows, good under 2.5 s), INP (how fast the page reacts to taps and clicks, good under 200 ms) and CLS (how much the layout jumps, good under 0.1).", ""),
 ("schema", "Structured data (schema)", "Hidden code that tells search engines and AI assistants exactly what a page is about: a company, a service, an article, an FAQ or a price. It helps pages earn rich results and get cited.", ""),
 ("aeo", "AEO (answer engine optimisation)", "Writing and structuring pages so AI assistants like ChatGPT, Claude and Perplexity can understand, quote and recommend them. Clear answers, definitions, comparisons and structured data matter most.", ""),
 ("llms-txt", "llms.txt", "A plain text file at the root of a website that summarises who the business is and links to its key pages, written for AI assistants to read.", ""),
 ("canonical", "Canonical URL", "A tag that tells search engines which version of a page is the main one, so duplicates do not compete with each other in results.", ""),
]),
("Design", [
 ("ui-ux", "UI/UX design", "UX design decides how a website or product works: structure, flows and what the user needs at each step. UI design decides how it looks: layout, type, colour and components.", "services/product-design.html"),
 ("design-system", "Design system", "A shared set of components, styles and rules, kept in Figma and in code, so every new page or screen looks consistent and is quick to build.", "services/product-design.html"),
 ("figma", "Figma", "The browser-based design tool most teams use to design websites and apps, share them for feedback and hand them to developers.", ""),
 ("wireframe", "Wireframe", "A simple, grey layout of a page that shows structure and content order before visual design starts.", ""),
 ("landing-page", "Landing page", "A single page built for one goal, usually sign-ups or enquiries from ads or a launch. It has one message and one main action.", "services/landing-pages.html"),
 ("cro", "CRO (conversion rate optimisation)", "Improving a website so more visitors take the action you want, by testing headlines, layouts, forms and offers against real data.", "services/landing-pages.html"),
 ("brand-identity", "Brand identity", "The visual system of a company: logo, colours, typography, imagery and the rules for using them across the website and materials.", "services/brand-identity.html"),
]),
("Pricing and process", [
 ("fixed-price", "Fixed-price project", "A project with scope, timeline and price agreed in writing before work starts, so the cost does not change unless the scope does.", "pricing.html"),
 ("design-retainer", "Design retainer", "A monthly plan for ongoing design and development work, with tasks taken from a shared backlog instead of quoted one by one.", "pricing.html"),
 ("ux-audit", "UX audit", "A review of a website or product against usability and conversion best practice, ending in a ranked list of fixes.", "pricing.html"),
 ("discovery", "Discovery", "The first step of a project, where goals, audience, content and technical needs are collected so the scope and price are accurate.", "process.html"),
]),
]

def main():
    p = ""
    toc = "".join(f'<a href="#{c.lower().replace(" ", "-")}">{c}</a>' for c, _ in G)
    body_parts, terms = [], []
    for cat, items in G:
        body_parts.append(f'          <h2 id="{cat.lower().replace(" ", "-")}">{cat}</h2>')
        for tid, name, d, link in items:
            more = f' <a href="{p}{link}">Read more</a>' if link else ""
            body_parts.append(f'          <h3 id="{tid}">{name}</h3>\n          <p>{d}{more}</p>')
            terms.append({"@type": "DefinedTerm", "@id": f"{S}/glossary#{tid}", "name": name, "description": d, "url": f"{S}/glossary#{tid}", "inDefinedTermSet": f"{S}/glossary#set"})
    ld = {"@context": "https://schema.org", "@type": "DefinedTermSet", "@id": f"{S}/glossary#set", "name": "Website design and development glossary", "url": f"{S}/glossary", "hasDefinedTerm": terms}
    body = hero("<span>Glossary</span>", "Glossary", ['Website terms,', '<span class="accent">plainly</span> explained.'],
                "Short, plain definitions of the words that come up when you plan, design, build or move a website.", p=p)
    body += f'''
    <section class="sec post-sec">
      <div class="wrap legal post">
        <nav class="legal__toc post__toc" aria-label="Sections"><p>Sections</p>{toc}</nav>
        <article class="legal__body post__body">
{chr(10).join(body_parts)}
        </article>
      </div>
      <script type="application/ld+json">{json.dumps(ld)}</script>
    </section>
'''
    body += cta(p)
    page("glossary.html", "Website Design Glossary: Webflow, SEO, Migration and UX Terms | Sorvel",
         "Plain definitions of website design and development terms: Webflow, Framer, CMS, 301 redirects, Core Web Vitals, AEO, design systems, CRO and more.", "", body, p, dock=False)

if __name__ == "__main__":
    main()
