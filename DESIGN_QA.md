# SocialCoach Project Page Design QA

Date: 2026-06-07

## Design Direction

Research project page for a technical AI/education audience. The visual system uses a crisp research-product language: neutral paper background, graphite typography, a single teal accent, real EQoach screenshots, restrained glass material, and dense evidence sections for researchers and search/AI retrieval systems.

## Five Optimization Rounds

1. Information architecture
   - Prioritized paper actions, authorship/citation metadata, method, evidence, product demo, and BibTeX.
   - Replaced generic landing-page feature cards with a research reading path.

2. Desktop hero refinement
   - Initial H1 was too long and pushed the first content section below the viewport.
   - Changed the H1 to the brand signal `SocialCoach` and moved the full paper title into supporting copy and metadata.

3. Mobile first-viewport refinement
   - Initial mobile hero was too tall because product visuals consumed vertical layout space.
   - Removed the mobile hero visual from layout flow and kept metrics compact so the next section is visible.

4. Readability and visual polish
   - Fixed desktop H1 word breaking by disabling arbitrary word breaks on the display heading and reducing max display size.
   - Checked button text, metric tiles, visual hierarchy, and line lengths across desktop and mobile.

5. SEO/GEO and rendering QA
   - Added canonical, Open Graph, Twitter Card, citation metadata, JSON-LD, sitemap, robots.txt, manifest, and llms.txt.
   - Verified local HTTP serving, PDF response, image loading, no horizontal overflow, visible next section, and unclipped buttons with Playwright.

6. arXiv header and asset quality update
   - Replaced the conference-style eyebrow with `arXiv preprint`.
   - Added the full paper title and author list at the start of the hero.
   - Re-rendered PDF figures at high DPI, cropped whitespace, and converted all page images to WebP.
   - Rechecked desktop and mobile hero layout after the longer academic title.

7. Academic title readability update
   - Changed the hero structure so the paper title and author list span the page before the content/product split.
   - Removed the narrow-column title treatment that caused excessive line breaks.
   - Verified desktop and mobile screenshots: no horizontal overflow, no clipped buttons, and the title remains quickly scannable.

8. Full-width section heading update
   - Changed major section titles to full-width centered headers before their content blocks.
   - Applied the same treatment to Research contribution, Method, Knowledge corpus, and Evidence.
   - Verified the headings are centered on desktop and mobile instead of being constrained by two-column content layouts.

## Verification Evidence

- Desktop viewport: 1440 x 1100.
- Mobile viewport: 390 x 844.
- All images loaded successfully after scroll inspection.
- Desktop and mobile both expose the next section within the first viewport.
- No horizontal overflow detected.
- No clipped button text detected.
- JSON-LD parsed successfully with `ScholarlyArticle`, `SoftwareSourceCode`, and `FAQPage` graph nodes.
- `llms.txt`, `robots.txt`, `sitemap.xml`, and PDF asset return HTTP 200 locally.
