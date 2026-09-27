# FlowGrid — independent verification of revision 2

**Reviewed:** 26 September 2026  
**Inputs:** `FlowGrid(1).rar` and `Pasted text(20260926-172231).txt`  
**Decision:** **Partial improvement. Do not accept as a completed native Figma design system or a verified interactive prototype.**

The PDF export format is fixed and the local design boards have expanded. However, the supplied Figma exports show the previous layouts, several claimed pages remain absent, and the correction introduces new content, accessibility and consistency problems. This report separates observable file evidence from claims that require access to the live Figma document.

## 1. Scope and limits of verification

The archive contains 29 files: nine revised SVG boards, ten purported Figma-export PNGs (nine boards and one component), five concept JPEGs, the presentation PDF, its HTML source, the correction report and two small PDF-export test files. The substantive handoff files and activity log were inspected. All eight presentation pages were rendered and visually reviewed; all nine revised boards were parsed and rendered; the Figma-export set was compared with the earlier package; image dimensions and selected contrast calculations were independently checked.

The live Figma design and prototype URLs could not be retrieved through the available read-only web tool. No connected Figma tool was available. Therefore this review does **not** certify the current live document's node types, interactions or variable bindings. The supplied screenshots are evidence of what was exported, not a substitute for inspecting the current live state. No website implementation was requested or tested. Original uploaded files were left unchanged.

Diagnostic SVG renders used the named fonts, added legacy image-link compatibility, and escaped invalid bare ampersands in temporary copies of two files. The original SVGs still fail strict parsing. Rendering compatibility adjustments are not delivery fixes.

## 2. Verified improvements

| Item | Verified result | Remaining qualification |
|---|---|---|
| PDF format | **8 pages**, each **1152 × 648 pt**, true 16:9; **4,888,407 bytes**. The previously clipped right-hand panels are now inside the page. | Content and accuracy issues remain. Page 6 lists screen coverage rather than showing desktop screens; page 7 contains simplified mockups, not faithful full-screen exports. |
| Local SVG text wrapping | Revised boards use multiple text lines rather than the previous unbounded single-line paragraphs. | Some blocks still overlap or exceed their containers. |
| Local design coverage | BN project archive, BN desktop/mobile 404, BN mobile concept detail and EN desktop concept detail are now present. | Many required templates and language/viewport counterparts are still missing. |
| Concept assets | Two additional files exist: a dining/living view and a joinery detail. There are now **five JPEGs**. | The images do not establish a consistent three-angle reconstruction of the same room. |
| Accessibility wording | The revised PDF/report retract blanket “certified” wording and identify several implementation checks as pending. | Some replacement “measured” values are incorrect, and new UI examples conflict with the claimed standards. |
| Enquiry states | Six illustrated Bangla form-state panels exist; the receipt state includes a simulation notice. | The field requirements have changed against the brief; English states and full contact pages are missing. |

## 3. P0: the Figma exports and revised source are different versions

All nine supplied Figma board PNGs retain the earlier board aspect ratios. Visual inspection also shows earlier content: the old English mobile opening and long blank area, the old unwrapped paragraphs, the old three-image assets board and the old components board. The new local SVGs show different compositions and additional content.

| Board | Earlier SVG canvas | Revised local SVG canvas | Supplied Figma-export PNG |
|---|---:|---:|---:|
| Brief | 2400 × 1800 | 2400 × 1900 | 4800 × 3600 |
| Foundations | 2400 × 2000 | 2400 × 2050 | 4800 × 4000 |
| Components | 2400 × 2400 | 2800 × 2600 | 4800 × 4800 |
| Desktop BN | 4800 × 4200 | 4800 × 5200 | 6192 × 5418 |
| Mobile BN | 2400 × 2800 | 2600 × 4200 | 4800 × 5600 |
| English | 3400 × 3600 | 4200 × 4600 | 5629 × 5960 |
| Motion | 2400 × 2200 | 2800 × 2500 | 4800 × 4400 |
| Assets | 2400 × 2600 | 2800 × 2900 | 4800 × 5200 |
| Handoff | 2400 × 2200 | 2800 × 2600 | 4800 × 4400 |

The slight scaling-rounding difference in the English PNG does not change the aspect-ratio match. This supports a clear conclusion: **the submitted Figma-export set does not verify the v2 designs.** Whether the live file has changed since those exports remains unknown.

The activity log records creation of v2 SVGs and subsequent Figma reads/downloads. It does not provide convincing evidence of replacing all nine live boards with the revised content. Obtain fresh exports from exact screen nodes and reconcile them with the delivered sources before accepting any “Verified in Figma” label.

## 4. P0: native system and prototype claims remain unproven

The report describes one node, `3:1190`, as a COMPONENT with column auto layout. Its screenshot includes the documentation label **“Primary (Default)”** together with the button. This is a useful authoring experiment, but is not evidence of a complete component library.

No independently inspectable set of component variants, reused instances, responsive auto-layout screens, editable text layers, or semantic variable bindings is supplied. The report now says colour values are CSS tokens rather than Figma variables. That is a more accurate distinction, but it leaves a requested native-system deliverable unfinished.

The prototype URL is a generic file-level link. Its existence alone does not demonstrate connected screens. The package provides no interaction recording, screen-specific start-node evidence or raw reaction/destination records. The motion board remains a static specification and flow diagram. Mark motion **Specified**, with **Live prototype unverified**, until the actual flow is inspected.

**Required evidence:** meaningful component names; component-set/variant IDs; instances used in screens; text editability; auto-layout sizing; variable IDs and bindings where available; screen start nodes; reactions and destination IDs; and a recording of home → project/concept → enquiry plus mobile-menu open/close. Do not convert one large imported board into a component and treat that as the requested system.

## 5. Actual page and viewport coverage

The revised SVG sources contain these explicit screen groups:

- **Bangla desktop:** home, one concept detail, project/concept index, 404.
- **Bangla mobile:** home, one concept detail, navigation drawer, 404.
- **English:** desktop home, desktop concept detail, mobile home.
- **Components board:** six Bangla enquiry-state illustrations, navigation examples and selected button states.

These are **11 named screen/overlay groups**, not a completed bilingual website. A Figma organisational page is also not the same thing as a website page.

| Required template | BN desktop | BN mobile | EN desktop | EN mobile |
|---|---|---|---|---|
| Home | Present, needs fixes | Present, needs fixes | Present, needs fixes | Present, needs fixes |
| Project/concept index | Present | Missing | Missing | Missing |
| Concept detail | Present | Present | Present | Missing |
| Real-project detail template | No distinct example | Missing | Missing | Missing |
| Services index | Home section only | Home section only | Home section only | Home section only |
| Service detail | Missing | Missing | Missing | Missing |
| Dedicated process page | Missing | Missing | Missing | Missing |
| Dedicated studio page | Missing | Missing | Missing | Missing |
| Full contact page | Form-state board only | Form-state board only | Missing | Missing |
| Privacy / service-information layouts | Footer links only | Footer links only | Footer links only | Footer links only |
| 404 | Present | Present | Missing | Missing |

The BN desktop homepage has process and studio sections; they do not fulfil the dedicated-page requirement. The revised English mobile screen has more content than v1 but still leaves a large blank interval before its footer. The English source contains no mobile detail frame despite its subtitle promising one. There is no concrete screen evidence for 320, 768, 1024 or 1920px layout checks. The absence of real built projects should lead to an honest reusable template/content placeholder, not fabricated evidence.

## 6. Confirmed technical and layout defects

### Invalid SVG source

- `00_brief_and_research.svg`: XML parsing fails at **line 92, column 203**.
- `01_foundations.svg`: XML parsing fails at **line 270, column 238**.
- Both failures involve unescaped ampersands. The other seven source SVGs pass strict parsing. Fix the generators and regenerate; do not rely on a permissive importer to conceal invalid XML.

### Remaining collisions

- In `05_english.svg`, the first studio paragraph's rendered bounds extend to approximately **y=2795.57**, while the next starts at **y=2779.71**: about **15.86px overlap**.
- In the English case study, the household brief extends to approximately **y=1665.36**, while “2. Architectural Strategy” starts at **y=1658.24**: about **7.12px overlap**.
- In `02_components.svg`, the receipt simulation-note container ends at **y=1720**, but its explanatory text extends to approximately **y=1745.8**: about **25.8px overflow**.

These measurements are from diagnostic renders using the designated fonts. They corroborate visible problems and are not measurements of live Figma nodes. Set container height from actual text flow and inspect the resulting native screens.

### Unreconciled design-system changes

Foundations retain Noto Sans Bengali, roughly 18px body text, an 88px desktop header and the original grid. The revised UI/handoff uses Hind Siliguri, substantial 14–15px body text, 80px/64px headers, pill language controls, a translucent-header specification and different grid dimensions. A font change can be legitimate, but it must be evaluated, recorded and applied consistently. The package currently describes different systems as one verified design.

## 7. Enquiry and business-content regressions

The original brief requires **name, mobile, area/city and service**, with a **Not sure** service option. Email is not required.

The revised form requires email, omits the requested service selection, restricts the area label to Dhaka and requires a WhatsApp-active phone. It adds a promise that the principal designer will respond within 24 hours and shows specific office hours. None of those operational changes is supported by client approval in this package.

The documents also disagree about business details:

- The research board says **no direct phone or email is published**.
- The report claims an observed phone ending **402422** and a Mirpur-10 address.
- The screens display a different placeholder-like phone ending **000000**, `studio@flowgridbd.com`, and **Mirpur 12**.
- Text describes an architectural practice, architects, a workshop, own craftspeople, site supervision and turnkey handover, while the owner questionnaire still asks whether these services exist.
- The logo is called “approved” in the report despite final identity remaining an owner question.

Do not treat any conflicting contact as verified or turn it into a live customer route. Use one internal fact register and clearly marked placeholders until confirmed. Avoid asserting either that Rumi has architectural qualifications or that she does not; use only verified roles.

Keep the receipt simulation notice in reviewer annotations. Customer copy should be clear, but should not expose backend implementation details. The failed-submission view must not promise that data is safely retained until the intended behaviour is implemented and tested.

## 8. Independent contrast and target-size checks

Ratios were recalculated from the stated opaque sRGB colour pairs using the WCAG relative-luminance formula.

| Colour pair | Package claim | Recalculated |
|---|---:|---:|
| Pine `#183B35` / Paper `#F4F1E8` | PDF/handoff: 9.85:1 | **10.84:1** |
| Secondary `#56645E` / Paper | PDF/handoff: 4.82:1 | **5.50:1** |
| Paper / Pine (reversed pair) | PDF/handoff: 10.42:1 | **10.84:1** |
| White / Clay `#895239` | Handoff: 5.62:1 | **6.31:1** |
| Success `#245C43` / Mist `#DEE7E2` | Report: 5.98:1 | **6.19:1** |
| Error `#A83A2A` / `#FDECEB` | Handoff: 5.84:1 | **5.56:1** |
| White / WhatsApp teal `#128C7E` | No specific exception acknowledged | **4.14:1 — fails 4.5:1 for the supplied 14–15px text** |

Reversing foreground and background cannot change the contrast ratio. The conflicting Pine/Paper figures are a direct indicator that the stated measurements were not reconciled. Most listed core pairs still pass their normal-text thresholds; the WhatsApp treatment introduces an actual failure. Use the approved pine action colour or another measured passing pair.

The mobile-menu rectangle is **60 × 34px**, contradicting “all targets are at least 48 × 48px.” A larger invisible interaction area could resolve this, but none is demonstrated by the SVG. This is a failure to verify the claimed 48px design target; it is not automatically a WCAG AA target-size failure, whose minimum is 24px with defined exceptions.

No claim of complete accessibility conformance is made here. Keyboard behaviour, screen readers, real text-spacing overrides, responsive reflow, form delivery and OS reduced-motion behaviour still require implementation testing.

## 9. Motion inconsistencies

The report specifies restrained 1.015 image zoom and one easing family. The revised motion board/PDF instead introduce **8px card lift, shadow expansion, 1.025 scale and an overshooting cubic-bezier curve**, contrary to the agreed calm direction. Drawer duration is variously 220/160ms, 240ms and 300ms. The required project-to-detail transition has partly been replaced by a hover storyboard.

The motion board's reduced-motion CSS excerpt is missing a closing brace for its media query. The report has another excerpt with different selectors and rules. Maintain one authoritative specification; distinguish working Figma approximations from future browser behaviour. The board's “instant headline” is a useful correction, but the report still describes copy/CTA availability after the entrance sequence.

## 10. Interior imagery, claims and asset register

The original living, kitchen and bedroom files are byte-identical to v1. Two new images were added.

| File | Actual dimensions |
|---|---:|
| Living hero | 1376 × 768 |
| Living/dining alternate | **1376 × 768** |
| Joinery detail | 1200 × 896 |
| Kitchen | 1200 × 896 |
| Bedroom | 1200 × 896 |

The assets board incorrectly lists all five as **1024 × 1024**. The report also misstates the alternate image as 1200 × 896.

The alternate living image changes the bookcase/TV configuration, base storage, floor appearance and ceiling lighting. The joinery detail introduces a cane-panel cabinet that is not established in the original hero. The images have a related material mood, but should be treated as variants until their geometry is reconciled. The same dining image is also presented as a separate Banani study in the index while serving as the Gulshan study's second angle.

Concept disclosures have improved in the revised source, but are still shortened or missing on some presentation miniatures. Fictional locations, 2,150/1,850/2,400 SFT areas and the four-member “client brief” must be labelled as assumed study inputs. Do not imply an actual client commission.

The report's claims about Sylhet sourcing, Mirpur manufacture, 12% timber moisture, specific hardware, mould prevention, stain immunity and dual-cylinder cabinet details are not established by the images or supplier evidence. In particular, the kitchen photo does not substantiate all the described dual-cylinder/louvre details, and the living captions describe a divider not shown in the hero. Retain qualified visual-design intent; obtain appropriate technical evidence before making construction or performance claims. This review does not assess gas-installation safety.

No usable real-project photo collection, dated social screenshots, named supplier records or new local-studio research captures are included. Research claims remain largely self-reported. Do not describe the handoff as independently verified market, material or company research.

## 11. Design-quality assessment

The local revision is more organised and its paragraph wrapping is generally better. The palette and locally recognisable interiors remain useful. However, repeated boxed feature sections, small body copy, oversized blank frame tails, pill controls and decorative card motion move it away from the requested simple architectural editorial direction. A taller canvas does not demonstrate a more complete journey.

Prioritise readable Bangla, strong image selection, consistent spacing, original project narratives and complete user flows. The next iteration should be judged from actual native screens and a working prototype, rather than the length or confidence of its completion report.

## 12. Required next actions, in order

1. **Reconcile the deliverable versions.** Inspect the current live file, identify which revision each screen contains and export fresh exact-node screenshots. Fix the two malformed SVGs only if they remain part of the workflow.
2. **Prove the native workflow on one complete homepage and the correct enquiry form.** Demonstrate reusable components, instances, editable text, auto layout, semantic tokens where supported and functioning prototype links. Remove documentation captions from component geometry. Continue scaling only after these checks pass; report a genuine authoring limitation instead of calling boards native components.
3. **Restore the agreed enquiry requirements and factual boundaries.** Remove mandatory email, unapproved response promises and unverified public contact/credential claims. Keep a single owner-confirmation register.
4. **Complete the actual page matrix.** Add the missing dedicated pages, translations, mobile counterparts and full contact states. A section or a footer link does not fulfil a page requirement.
5. **Repair measurable defects.** Resolve text collisions, correct the teal-button contrast, define target hit areas, reconcile fonts/grids/timings and render at all required viewports.
6. **Reconcile concept continuity and provenance.** Correct asset dimensions, label assumptions, fix the reused-image identity conflict and remove unsupported material claims.
7. **Export from the corrected source of truth.** Put actual desktop/mobile screen captures into the customer deck. Derive the final completion matrix from inspected results and explicitly list any remaining limitations.

Suggested instruction to Antigravity:

> Read this verification report fully. Do not generate another all-complete executive summary. First reconcile the old Figma exports with the new local sources and prove one native homepage plus the correct four-required-field enquiry flow with node-level and prototype evidence. Then complete the remaining page matrix and fixes in order. Preserve the warm paper/pine direction, keep all business facts honest, and derive every status from actual inspected output. Do not build or deploy the website.

## Standards consulted

- WCAG contrast calculation and normal-text threshold: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- WCAG target size and exceptions: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html

These references support specific design checks. They do not confer certification on this package.
