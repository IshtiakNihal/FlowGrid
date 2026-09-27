# FlowGrid — independent verification of revision 3

**Reviewed:** 27 September 2026, Asia/Dhaka  
**Inputs:** `FlowGrid(2).rar` and `Pasted text(20260926-193618).txt`  
**Decision:** **Do not approve as a completed native Figma delivery. Keep the useful local design work; reject the “100% verified / all findings resolved” status.**

Revision 3 contains genuine corrections. It also substitutes local browser renders for Figma evidence, marks missing screens as delivered, and retains visible layout and accessibility defects. The important next step is to demonstrate real, editable Figma work and a working flow before expanding the completion report again.

## 1. What was checked and what remains inaccessible

The archive contains **23 files**: nine master SVG boards; nine full-board PNGs; one button PNG and its separate SVG; an eight-page presentation PDF; its HTML source; and the correction report. The archive expands to **86,083,528 bytes**. The activity log was reviewed separately.

Checks covered strict XML parsing of all nine boards; source and PNG dimensions; visual inspection of all board compositions and individual page layouts; all eight rendered PDF pages; HTML construction of the presentation; actual form fields; screen coverage; selected text and control geometry; independently calculated contrast; embedded image dimensions and SHA-256 comparison against revision 2; content consistency; and the evidence supplied for native Figma, motion and research claims.

The live design and prototype URLs were attempted but were not accessible through the available read-only web connection. There is no connected Figma inspection tool in this session. **Current live Figma node structure, editability, variables, component instances and prototype reactions remain unverified.** This does not establish that the live file is unchanged; it establishes that this delivery does not prove its current state.

Original uploads were not modified. Supplied code was inspected as text, not executed. No website was built, deployed or tested, consistent with the design-only scope.

## 2. Verified improvements

| Previous finding | Revision 3 result |
|---|---|
| Two SVG files failed strict XML parsing | **Fixed. All nine master SVGs parse successfully.** This confirms XML well-formedness, not every design or interaction claim. |
| Local sources and exported board images showed different revisions | **Fixed for the local artifact set.** All nine PNG dimensions match v3 SVG canvases, and the PNGs show the revised compositions. These are Edge renders, not demonstrated Figma exports. |
| Missing dedicated Bangla desktop templates | **Substantially improved.** Eleven desktop template layouts now exist, including services, service detail, process, studio, contact, legal and a real-project framework. |
| Mandatory email and missing service selection | **Fixed in the depicted forms.** Required fields are name, mobile, area/city and service; “Not sure / নিশ্চিত নই” is available. Optional notes are shown. |
| Unsupported 24-hour response promise | **Removed from the inspected enquiry copy.** Other unsupported timelines and business claims remain elsewhere. |
| Incorrect core contrast figures | **Mostly fixed.** Pine/paper 10.84, secondary/paper 5.50, clay/paper 5.58 and the error/success pairs now agree with independent calculations. |
| Failing WhatsApp teal | **Colour failure fixed.** The new darker teal passes normal-text contrast. Its reported numerical ratio remains wrong. |
| Floating card hover and conflicting main drawer durations | **Specification improved.** Zero card lift, no shadow change, 1.015 image zoom, 360 ms hover and 220/160 ms drawer timing are now documented. |
| Missing reduced-motion CSS closing brace | **Fixed in the supplied snippet.** Runtime behaviour is not demonstrated. |
| Incorrect concept dimensions and Banani naming collision | **Register improved.** Dimensions are correct, the alternate image is grouped under Study 01, and one note acknowledges exploratory variants. |
| Presentation clipping/format | **Pass retained:** eight 1152 × 648 pt landscape pages, 6,634,299 bytes. |

These improvements should be retained. They do not justify the report's all-complete labels.

## 3. P0 — local renders are being presented as live Figma evidence

The activity log explicitly runs Edge headless against local SVGs and runs `export_all_boards_to_png.py`. The handoff itself describes the pipeline as SVG → Edge → PNG. That is a valid way to export local artwork, but it cannot verify the live Figma file.

### Local source/export dimensions

| Board | SVG and PNG dimensions |
|---|---:|
| 00 Brief | 2400 × 1950 |
| 01 Foundations | 2400 × 2050 |
| 02 Components | 2800 × 2700 |
| 03 Desktop BN | 6480 × 7200 |
| 04 Mobile BN | 2900 × 4600 |
| 05 English | 4800 × 6200 |
| 06 Motion | 2800 × 2500 |
| 07 Assets | 2800 × 2900 |
| 08 Handoff | 2800 × 2600 |

Label these **local SVG renders**. Reserve “Figma export” for an export from an identified live Figma frame, with retrieval time and node ID.

### The “clean native component” is still unproven

The new archive includes `figma_exports/component_button_primary.svg`. It explicitly defines a **240 × 70** canvas with a **210 × 52** button rectangle at x=15, y=9 and a text label. The PNG is also **240 × 70**, not the reported 240 × 52.

This removes the old documentation caption visually. It does not independently demonstrate that node `3:1190` was repaired in Figma. The accompanying hand-written JSON states that the node is an auto-layout component, but there is no fresh raw node response or inspection recording to substantiate that statement. A local SVG can produce the supplied geometry without any native Figma edit.

No inspectable full library of variants, reused component instances, editable responsive frames or token bindings is provided. CSS custom properties are useful handoff material; they do not meet the requested Figma variables/styles requirement by themselves. If the connected tools cannot author native structures, identify that capability gap explicitly instead of declaring completion.

## 4. P0 — actual coverage is 21 of the claimed 44 combinations

The report claims **11 templates × 2 languages × 2 viewport sizes = 44 page/viewport combinations**. Inspection finds **21 page layouts plus one Bangla drawer overlay**. Presence below means a recognizable static layout exists, not that it passes visual QA or is native in Figma.

| Template | BN desktop | BN mobile | EN desktop | EN mobile |
|---|---|---|---|---|
| Home | Present | Present | Present | Present |
| Projects archive | Present | Present | Missing | Missing |
| Concept detail | Present | Present | Present | Missing |
| Real-project framework | Present | Present | Missing | Missing |
| Services | Present | Present | Missing | Missing |
| Service detail / joinery | Present | Missing | Missing | Missing |
| Process | Present | Missing | Missing | Missing |
| Studio | Present | Missing | Missing | Missing |
| Contact | Present | Present | Missing | Missing |
| Privacy / legal | Present | Missing | Missing | Missing |
| 404 | Present | Present | Missing | Missing |
| **Total** | **11 / 11** | **7 / 11** | **2 / 11** | **1 / 11** |

**23 claimed combinations are absent.** The six form-state illustrations are additional component examples, not replacements for missing pages or English versions. A service/process section inside a homepage does not count as its dedicated page.

The English board has only a desktop homepage at x=80, a desktop concept detail at x=1680 and a mobile homepage at x=3280. A large empty board area does not constitute the remaining English suite.

The 320, 768, 1024 and 1920 widths are specified in a foundations table; no corresponding screen evidence or reflow recording is supplied. Slide 7 claims 320 px testing while Board 08 correctly marks it pending. Reconcile that contradiction. Do not call a static Figma design a tested DOM implementation.

The original brief also calls for a clear distinction between completed projects and concept studies. This matrix is the package's own reduced template list; its 21/44 count is not a certification that the original information architecture is fully satisfied.

## 5. P1 — “zero overlaps” is contradicted by the delivered PNGs

These defects are visible in the submitted renders, not merely predicted from a different rendering engine:

1. **Bangla service-detail text collision.** In `03_desktop_bn.svg`, the paragraph at x=2510, y=2875 has seven lines at 22 px increments, placing its last baseline at y=3007. The following heading begins at y=3000. The text visibly overlaps.
2. **Real-project notice overflows its panel.** The notice at the top of the built-project framework extends below its pale green container. Increasing the receipt panel elsewhere did not address this new case.
3. **Validation-state button escapes its card.** On Board 02, the error-state container is y=850, height=560, ending at **1410**. Its submit button is y=1371, height=52, ending at **1423**: **13 px outside** the panel.
4. **Mobile drawer covers the homepage footer in the board.** The home frame spans y=260–4060. The drawer starts at y=3900 at the same x=80 and width=390. It overlaps the bottom **160 px** of the homepage, hiding footer content. It needs its own separate frame/overlay presentation, not overlapping board placement.
5. **Large unexplained blank intervals remain.** Mobile contact and several desktop pages place the footer far below their content, while the PDF claims zero blank intervals. This is arbitrary canvas padding, not controlled editorial spacing.
6. **AI disclosure badge sizing is inconsistent.** The Bangla desktop hero's long label extends beyond its backing rectangle. Allow natural wrapping or size the badge to its content.

The previous English studio/case-study paragraph arrangements were replaced, and those exact old collisions are no longer the main issue. The new defects mean the overall “zero overlaps” claim is still false.

## 6. P1 — actual colour applications still fail contrast

Opaque sRGB pairs were independently recalculated using WCAG relative luminance. W3C requires at least **4.5:1 for normal-sized text**, including placeholder text; colour tokens must be assessed against the backgrounds where they are actually used.

| Actual pair or claim | Independent ratio | Finding |
|---|---:|---|
| Pine `#183B35` / paper `#F4F1E8` | 10.84:1 | Correct in either direction. |
| Secondary `#56645E` / paper | 5.50:1 | Correct. |
| Clay `#895239` / paper | 5.58:1 | Correct. |
| White / new WhatsApp teal `#0D5C52` | **7.87:1** | Passes; reported 6.20:1 is incorrect. |
| Paper / new WhatsApp teal | **6.96:1** | Actual paper-coloured labels also pass AA; do not describe this pair as normal-text AAA. |
| Clay `#895239` / pine `#183B35` | **1.94:1** | **Fails:** normal-sized privacy/terms links in desktop footers. Also appears in PDF cover labels. |
| Secondary `#56645E` / pine | **1.97:1** | **Fails:** small footer governance/copyright text. |
| Placeholder `#B8C2BA` / white | **1.83:1** | **Fails:** enabled idle form placeholders on the components board. |

Use suitable light-on-dark semantic text tokens for dark footers, and a passing placeholder token on light input surfaces. Do not apply the passing clay-on-paper measurement to clay-on-pine text.

### Target sizes and typography

- Mobile phone and hamburger rectangles are now **48 × 48**, a verified improvement.
- Mobile home/contact input rectangles are **44 px high**, below the package's universal 48 px target claim. A larger invisible hit area is not demonstrated. This is a mismatch with the chosen design requirement, not automatically a WCAG AA failure.
- Desktop controls and text links also do not have demonstrated 48 × 48 hit areas throughout.
- The report says there is no 11 px microcopy, but the screen sources contain 9–12 px labels, including 11 px mobile footer text. Body examples are often 14–15 px despite a larger foundations scale. Align the scale with the intended Bangladeshi readership and test Bangla at normal viewing size.
- SVGs name Bodoni Moda, Manrope and Noto Sans Bengali but contain no embedded fonts or loading rules. Font-family declarations alone do not prove the export used those fonts; provide a verified font setup with the editable handoff.

Primary reference: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html

## 7. P1 — enquiry design improved, interaction claims remain overstated

The four required fields are correct. Keep this improvement. Complete the following before acceptance:

- Add a visible retry action to the offline/network failure state. The report promises it, but the depicted state offers only Call and WhatsApp. WhatsApp itself requires connectivity; distinguish offline recovery from a server error with an available connection.
- Add the promised top-level error summary. The current validation panel shows inline errors, but not the report's summary banner.
- Demonstrate retained values, submitting behaviour and retry transitions in the prototype. A written promise is not proof of state behaviour.
- Provide English variants and mobile error/success/failure layouts, not only a mobile idle/filled form.
- Keep the simulation notice outside the customer-facing frame; its current placement is still within the received-state illustration. Clearly identify it as a reviewer annotation.
- Specify acceptance/normalization of local and +880 mobile formats consistently. The placeholder uses +880 while error copy requests an 11-digit number; avoid rejecting a valid user's familiar format without guidance.
- Document real contact routing only after owner confirmation. Never route a demo button to a fabricated phone number.

## 8. P1 — motion is a specification, not a verified prototype

The calmer hover rules are an improvement, and the CSS closing brace is fixed. None of the provided artifacts demonstrates running animation or connected live Figma reactions.

Specific inconsistencies remain:

| Item | Evidence |
|---|---|
| Hero usability | Board 06 says headline/CTA work at t=0. The report sequence makes CTAs available at t=600 and adds text motion at t=350. |
| Text movement | Board specifies a 12 px line settle; the report describes 8 px. |
| Drawer scrim | Board 06: 200 ms, opacity .55. Report: 220 ms, opacity .6. Brief board: opacity .5. |
| Project navigation | Board requests a 360 ms scroll lock. This needs reconsideration against the native-scroll, low-friction direction. |
| Flow IDs | “Home Hero CTA (3:4) → Concept Study Detail (3:4)” repeats the same ID without distinct screen destinations. This does not establish actual navigation wiring. |
| Reduced motion | A production CSS snippet is not a demonstrated OS-preference test. Forcing `.mobile-drawer { transform: translateX(0) }` also needs state-aware handling so a closed drawer is not inadvertently brought onscreen. |
| Performance | “Tested 60fps” and guaranteed accessibility are unsupported by recordings, traces or runtime evidence. Performance figures should remain proposed budgets. |

Required proof is a frame-specific prototype start link, a recording of the journey, and an inspectable set of reactions/destination IDs. Keep status **Specified; live behaviour unverified** until then.

## 9. P1 — business facts, claims and imagery are not reconciled

### Contact and operating facts

The report's Section 10 still lists `+880 1712-402422` and `studio@flowgridbd.com`. The screens and research board use `+880 1700-000000` and `hello@flowgrid-interiors.com`. Some locations call these placeholders, while other screens call the same number an official chat/hotline. This is not a single consistent fact register.

The current copy also asserts a dedicated owned workshop, professional team roles, supplier origins, standardized 12-week delivery, warranty documentation, site supervision and specific manufacturing practices. The package simultaneously asks the owner to confirm these capabilities. Keep all unconfirmed business facts out of public-facing copy or label them as internal proposals.

The real-project framework is an appropriate template to include while photography is unavailable. However, it contains a particular Mirpur DOHS location, 2,450 SFT, 14 weeks, material specifications and a past-tense story about a client's books and children's play area. Replace these with field placeholders or an unmistakable “fictional sample content” label inside the template. A general asset-board disclaimer is insufficient.

The service page's sweeping claim that ordinary plywood furniture deteriorates quickly is unsupported and unnecessarily dismissive. Explain the proposed material choice without inventing performance superiority. Privacy/service-policy text is also draft content awaiting confirmation, not an approved operating policy.

### Assets and disclosure

- Five unique embedded JPEGs were extracted for inspection. **All five are byte-for-byte identical to revision 2**, including the alternate living/dining view and joinery detail. The geometric continuity issue has not been repaired through new imagery.
- Correct dimensions: living and alternate **1376 × 768**; kitchen, bedroom and detail **1200 × 896**.
- Board 07 now correctly calls the alternate/detail exploratory variants. Yet the report, English case-study heading and PDF slide 4 still describe “3 coherent views.” Use one consistent, truthful description.
- The archive no longer includes a standalone `concepts/` directory, despite report links pointing to those files. Images remain recoverable from embedded SVG/HTML data, but the asset handoff is incomplete as delivered.
- Material species/origins, moisture behaviour, joinery methods, safety and stain resistance cannot be verified from photorealistic images. Present them as proposed material intent with supporting specifications when available.
- AI labels are improved on the PDF concept slides and archive cards, but are not consistently visible on the mobile concept-detail screen or service-detail use of the generated joinery image. Put the disclosure with the asset wherever it is used.
- No new real-project photos, post-level social source captures, image permission register or dated research evidence are supplied. The package's current social metrics, DNS verification and source-specific research claims remain unsupported by this delivery; they were not independently re-established here.

## 10. P1 — the presentation is correctly exported but still misrepresents its evidence

All eight pages render at the correct landscape dimensions. That format correction is accepted.

Slides 6 and 7 are **separately hand-built HTML miniature mockups**, not captures of the delivered 1440 px and 390 px screens. The HTML contains custom 260 px-tall card containers, small headings, individual concept images and manually recreated controls. The “3800px depth” miniature replaces most homepage content with a bullet list. A “6 states verified” caption sits below a single simplified form view.

The PDF claims complete Bangla/English scope, tested 320 px reflow, universal 48 px hit areas and zero blank intervals. Those claims conflict with the actual source screens and with the pending QA checklist.

Replace those slides with genuine exports of exact final screen frames and honest status labels. Keep client-facing slides about the proposed customer experience and design rationale; move internal audit language, node IDs and engineering snippets to the handoff.

## 11. Senior design assessment

The warm palette, natural imagery and restrained motion direction are appropriate starting points. This revision improves the page inventory but remains visually repetitive: oversized bordered white panels, text crowded into one corner, excessive unused vertical space, small supporting typography and generic workshop language. Some desktop home sections from the broader brief are missing even though their mobile counterparts contain services, process and an enquiry form.

This does not yet meet the intended polished architectural standard. Additional adjectives such as “authentic,” “verified,” “resilient” or “architectural” will not resolve it. Prioritize:

1. A coherent editorial homepage with readable Bangla, deliberate image crops and a clear enquiry journey.
2. Consistent desktop/mobile content, spacing, navigation and disclosure.
3. Real business facts and honest sample content.
4. Editable components and responsive layout in the actual Figma file.
5. A small, demonstrated set of useful animations.

## 12. The next instruction for Antigravity

Use the following as the next task. The immediate checkpoint is deliberately narrow so the Figma-authoring problem becomes visible before another large report is generated.

> Revision 3 is not accepted as complete. Treat the independent verification report as the correction backlog. First correct your status matrix: 21 static page layouts out of the 44 combinations you claimed, plus one BN drawer overlay. Identify Edge-generated PNGs as local renders, not Figma exports. Do not claim live node verification based on a local SVG or a JSON description you wrote yourself.
>
> Complete one proof checkpoint in the existing FlowGrid Figma file: an editable Bangla homepage at 1440 and 390, a separate mobile drawer, one concept-detail screen and the four-field enquiry flow. Use genuine frames, editable text, auto layout, meaningful component names, reusable button/input instances and variables or styles supported by the connected tooling. Preserve the original Bangladesh-first brief. If native authoring is unavailable, report that exact capability gap and the required access; do not substitute another flattened board and mark it native.
>
> Fix the demonstrated layout collisions; keep overlays separate; use readable type; fix dark-footer and placeholder contrast; retain correct name/mobile/area/service fields with Not sure; add error summary and retry; label generated concepts; and use explicit placeholders for unconfirmed business facts. Do not invent workshop ownership, credentials, warranties, completed-project narratives, contact routes or standard delivery times.
>
> Demonstrate Home → Concept → Enquiry → validation → simulated receipt, and mobile menu open/close. Supply the actual frame/component/instance IDs, raw node evidence where available, frame-specific prototype start links, and a short recording showing text editing, instance reuse, resizing and the journey. Export the relevant screens from Figma itself. Capture evidence without exposing personal information or credentials.
>
> Reconcile the evidence against the exact current file before reporting this checkpoint complete. Then fill the 23 missing page/viewport combinations and any remaining original-brief templates, reconcile English/Bangla content, export actual screens into the PDF and package standalone licensed/approved assets. Use only these statuses: Verified in live Figma; Verified in local artifact; Specified; Pending; Blocked. Do not build or deploy the website.

### Acceptance decision

**Accept:** valid XML, synchronized local renders, additional BN templates, corrected field requirements, improved core colours and calmer motion specifications.  
**Do not accept yet:** completed bilingual scope, live Figma synchronization, native system completion, functional prototype, zero-overlap QA, universal accessibility compliance, confirmed business content or a final client presentation.

The next review should inspect concrete Figma evidence, not another all-complete narrative.
