# FlowGrid revision 3.1 — independent verification

**Review date:** 27 September 2026  
**Verdict:** Do not approve as a completed Figma design handoff. Accept the verified local improvements as work in progress.

This review covers `FlowGrid_Revision_3_1_Deliverable.zip` and the supplied activity log. It compares the contents with revision 3 and the requested native Figma proof checkpoint. The archive contains 38 files, including nine master SVG boards, nine corresponding board PNGs, an eight-page PDF, five standalone concept JPEGs, an HTML prototype, and two copies of the claimed interaction recording.

The design direction remains usable: warm paper, deep pine, restrained framing, Bengali typography, architectural imagery and a short enquiry form. The problem is completion and evidence integrity. The delivery report repeatedly marks work verified when its own files contradict those claims.

## 1. Findings that determine approval

| Priority | Finding | Evidence and practical consequence |
|---|---|---|
| P0 | The interaction recording is a placeholder still | Both `prototype/prototype_enquiry_journey.webp` and its `figma_exports` copy are 11,418-byte, 960 × 960, single-frame WebP files. They display **“Generating recording…”**. No enquiry journey, timing, focus behaviour or mobile interaction is recorded. |
| P0 | Native Figma completion remains unproven | The report itself says the live file retains earlier v1 layouts and that these PNGs were rendered locally in Edge. The archive contains no inspectable native Figma file, raw node response, verified component/instance relationships or connected Figma prototype evidence. The HTML demonstration does not satisfy the previous native Figma checkpoint. |
| P0 | Source, export and presentation versions disagree | Boards 03, 04 and 05 embed only the old revision 3 images. All 39 image occurrences across those boards use old asset bytes. Board 07 uses the five new JPEGs, and the HTML points to those new files. The English PNG also excludes an entire column of source screens. |
| P1 | The corrected completion count is still wrong | Actual source: **35 page layouts plus two drawer overlays**, not 38 page layouts plus one overlay. English mobile has home and archive only; its concept, contact and 404 screens are absent. Against the original 44 page combinations, nine are missing. |
| P1 | The PDF misidentifies mobile screenshots | Slide 7’s “Mobile 3-view detail” shows the built-project placeholder. Its “4-field enquiry & contact” preview shows blank space and a footer, without a form. These are actual image crops, but incorrect ones. |
| P1 | Prototype behaviour contradicts the report | No focus trapping, Escape handler, reduced-motion query, language-switch action or complete navigation. Phone validation checks length only. “Not sure yet” is missing. Offline retry always produces a timed simulated receipt. |
| P1 | Unsupported operational claims remain in customer copy | Bangla desktop services, process and studio copy still claim an owned factory/workshop. The report says these were removed. Contact links use an unverified placeholder number. |

P0 means an approval blocker. P1 means a substantial correction is required before handoff. These priorities assess this design delivery, not production security severity.

## 2. What is genuinely improved

- All nine master SVGs pass strict XML parsing.
- Bangla mobile expands to 11 page layouts, and English desktop expands to 11. These are source-layout counts, not acceptance of their usability or native editability.
- Five new standalone concept JPEGs are supplied. Their bytes differ from the previous assets.
- The button PNG is now exactly **210 × 52 px**, matching its revised standalone SVG. This verifies local geometry only.
- Footer colours are substantially improved. Soft mist on deep pine measures **9.69:1**; light slate on deep pine measures **7.76:1**. Both pass the normal-text contrast threshold.
- The main mobile form inputs are now 48 px high. The main submit control is 52 px high.
- The desktop real-project notice contains its text. The error-state card now contains its submit button and includes an error summary.
- The separate Bangla drawer no longer covers the home footer. The service paragraph and following heading no longer visibly overlap, although spacing remains tight and the source is not the four-line paragraph described in the report.
- The PDF has eight correctly proportioned 16:9 pages, each **1152 × 648 pt**. Desktop preview panels use actual supplied crops. Mobile panels also use supplied crops, but two are wrong.
- The HTML contains a real four-required-field form, tab-switching logic, loading/receipt states, error display and a drawer toggle. It openly labels its success response as simulated. It is useful as a limited demonstration, without proving a complete accessible experience.
- The handoff now admits that local PNGs are not live Figma exports. That clarification is welcome, but the overall “verified completion” claim remains unsupported.

## 3. Correct scope and export accounting

### Page coverage in the SVG source

| Language / viewport | Source page layouts | Drawer overlays | Remaining page combinations |
|---|---:|---:|---:|
| Bangla desktop, 1440 px | 11 | 0 | 0 |
| Bangla mobile, 390 px | 11 | 1 | 0 |
| English desktop, 1440 px | 11 | 0 | 0 |
| English mobile, 390 px | 2 | 1 | 9 |
| **Total** | **35 / 44** | **2** | **9** |

The 11 page types are home, projects archive, concept study, built-project template, services, joinery service detail, process, studio, contact, privacy/legal and 404. English mobile includes home and archive. An enquiry section inside the home page is not a separate contact-page layout, and a drawer is not a 404 page.

No supplied 320, 768, 1024 or 1920 px visual evidence establishes the claimed responsive checks. Fixed-coordinate SVG boards also do not demonstrate responsive reflow or Figma Auto Layout. The activity log describes actions, but cannot replace missing outputs.

### Actual frame coordinates

These coordinates refer to the SVG source, not proof that the corresponding PNG is current.

| Bangla mobile layout | Source x, y | Width × height |
|---|---|---|
| Home | 80, 260 | 390 × 3350 |
| Archive | 550, 260 | 390 × 1600 |
| Concept study | 550, 1920 | 390 × 2000 |
| Built-project template | 1020, 260 | 390 × 1400 |
| Services | 1020, 1720 | 390 × 1400 |
| Joinery | 1020, 3180 | 390 × 1400 |
| Process | 1490, 260 | 390 × 1400 |
| Studio | 1490, 1720 | 390 × 1400 |
| Privacy | 1490, 3180 | 390 × 1400 |
| Contact | 1960, 260 | 390 × 1450 |
| 404 | 1960, 1730 | 390 × 650 |
| Drawer | 1960, 2420 | 390 × 750 |

The report incorrectly places the concept at 1020,260 and contact at 1020,2560, among other errors. Its screenshot index should not be used to crop or locate the revised frames.

English mobile home, archive and drawer begin at **4880,2860**, **5350,2860** and **5820,2860** respectively. English desktop legal and 404 also begin at x=4880. All are beyond the supplied English PNG’s 4800 px width.

### Board dimensions

| Board | SVG canvas | Supplied PNG | Result |
|---|---|---|---|
| 00 Brief | 2400 × 1950 | 2400 × 1950 | Dimension match |
| 01 Foundations | 2400 × 2050 | 2400 × 2050 | Dimension match |
| 02 Components | 2800 × 2550 | 2800 × 2700 | 150 px extra PNG height |
| 03 Bangla desktop | 6480 × 7200 | 6480 × 7200 | Dimension match |
| 04 Bangla mobile | 2450 × 4850 | 2900 × 4600 | Canvas extents differ |
| 05 English | 6400 × 7300 | 4800 × 6200 | Right-hand screens absent; lower layouts truncated |
| 06 Motion | 2800 × 2500 | 2800 × 2500 | Dimension match; source and PNG unchanged from revision 3 |
| 07 Assets | 2800 × 2900 | 2800 × 2900 | Dimension match; new imagery present |
| 08 Handoff | 2800 × 2600 | 2800 × 2600 | Dimension match |

A dimension match alone does not prove visual parity. The report’s universal “1:1 canvas scale / exact pixel parity” assertion is false. In particular, the English source’s bottom row extends to y=7150 while the PNG ends at y=6200. Re-export each current board at its actual bounds and inspect the resulting images before updating the PDF.

## 4. Prototype verification

### Test boundary

The HTML/CSS/JavaScript was inspected directly. An isolated JavaScript test used a minimal DOM stub to exercise the supplied handlers. This verifies those branches only; it is **not** a browser, assistive-technology, responsive-layout or performance test. A local browser executable was unavailable. No calls, WhatsApp messages or enquiries were sent.

### Results

| Check | Result |
|---|---|
| Submit empty form | Pass at logic level: the summary and all four field error classes activate. |
| Select second concept angle | Pass at logic level: image path changes to `concept_01_living_alt.jpg`. |
| Required form fields | Name, phone, area and project type are present; email is not required. |
| “Not sure yet” service option | Fail: absent from the HTML select, although specified in the static designs. |
| Optional project notes | Absent from the HTML, although present in the component specification. |
| Phone validation | Fail: `abcdefgh` is accepted because the test is only non-empty and length ≥8. The handler advances through submitting to receipt. |
| Offline retry | Demonstration only: retry always transitions to receipt after 700 ms; no connection test or simulated failure branch. |
| Draft preservation claim | No local/session storage or equivalent persistence. Values can remain in the live DOM, but the UI’s device-saved-draft assurance is unsupported across refresh/closure. |
| Modal focus handling | No focus movement, focus trap, focus restoration, Escape handler, dialog semantics or inert background handling. The report specifically claims a clean focus trap. |
| Error announcements | No `aria-invalid`, error description linkage or live-region announcement of the summary/receipt. |
| Main navigation | `#services`, `#process` and `#studio` have no target elements. |
| Language switch | Button exists, but no handler changes language or navigates to the English experience. |
| Reduced motion | No `prefers-reduced-motion` query in this HTML. An infinite 0.8 s spinner and CSS transitions remain defined. |
| Signature motion | No implemented 600 ms hero mask or 360 ms shared-element project expansion. Drawer CSS is **250 ms**, while the board/report specify **220 ms**. |
| Contact actions | Active `tel:+8801700000000` and `https://wa.me/8801700000000` links point to an unverified placeholder number. Do not expose these as genuine customer contact channels. |
| Submitted “recording” | Fail: a non-animated placeholder image, duplicated in two folders. |

The simulated success notice is appropriately explicit. A backend is not required to approve a design prototype. What is required is a faithful, honestly labelled demonstration of the intended journey, including invalid input, uncertain service selection, error recovery, keyboard behaviour and the agreed motion fallback.

The current prototype also places implementation commentary in customer-facing areas: “0px Architectural Radii” in the concept specification and contrast ratios in the footer/drawer. Move such notes to reviewer annotations. They do not help a homeowner choose an interior designer.

## 5. Accessibility and typography

### Independent colour calculations

Calculated from the submitted opaque sRGB hex values using the WCAG relative-luminance formula. The ratio belongs to the exact foreground/background pair; changing the background changes the result.

| Foreground | Background | Calculated | Delivery report | Assessment |
|---|---|---:|---:|---|
| Pine `#183B35` | Paper `#F4F1E8` | 10.84:1 | 10.84:1 | Correct |
| Slate `#56645E` | Paper `#F4F1E8` | 5.50:1 | 5.50:1 | Correct |
| Slate `#56645E` | White `#FFFFFF` | **6.21:1** | 5.50:1 | Report uses the paper ratio for white |
| Clay `#895239` | Paper `#F4F1E8` | 5.58:1 | 5.58:1 | Correct |
| Mist `#DEE7E2` | Pine `#183B35` | 9.69:1 | 9.69:1 | Correct; footer improvement |
| Light slate `#C4D1CA` | Pine `#183B35` | **7.76:1** | 8.12:1 | Report incorrect; still passes |
| Error `#9B302B` | Paper `#F4F1E8` | 6.52:1 | 6.52:1 | Correct |
| Success `#245C43` | Mist `#DEE7E2` | 6.19:1 | 6.19:1 | Correct |
| Teal `#0D5C52` | White `#FFFFFF` | 7.87:1 | 7.87:1 | Correct |
| Teal `#0D5C52` | Paper `#F4F1E8` | 6.96:1 | 6.96:1 | Correct |

These are improvements, not whole-experience WCAG certification. The W3C normal-text contrast threshold is 4.5:1; keyboard operation, focus, semantics, error identification and reflow need separate evaluation.

The universal 48 × 48 claim is still false. For example, the Bangla mobile contact WhatsApp control is a **320 × 44 px** rectangle at x=1995, y=1030. English desktop header consultation buttons are 44 px high. This violates the project’s stated 48 px minimum; a 44 px control does not automatically violate WCAG 2.2 AA target-size requirements. Do not conflate the two standards.

The Bangla mobile SVG still includes many 12–13 px text elements and 10–11 px labels. Small text alone is not an automatic WCAG failure, but this is below the intended comfortable reading treatment. Inspect real Bengali rendering at 100% on a phone, especially form labels, disclosure text and metadata. A board overview cannot establish that quality.

## 6. Images, realism and Bangladesh context

### Asset consistency

SHA-256 comparison establishes that every embedded image in Boards 03, 04 and 05 matches an old revision 3 asset. None matches the five new JPEGs. Board 07 embeds the new assets. This is an actual version mismatch, not a visual judgement about similarity.

| New standalone file | Dimensions | SHA-256 prefix |
|---|---|---|
| `concept_01_living_dhaka.jpg` | 1376 × 768 | `08e0b1f21db2789da` |
| `concept_01_living_alt.jpg` | 1376 × 768 | `8bfda450a7514508` |
| `concept_01_joinery_detail.jpg` | 1376 × 768 | `c76b0f2a5838bdc9` |
| `concept_02_kitchen_dhaka.jpg` | 1376 × 768 | `34eb1b7ea8875b7d` |
| `concept_03_bedroom_dhaka.jpg` | 1376 × 768 | `b8e982b6cf29a56d` |

The files are approximately 1.06 megapixels each. They are **not 8K**, despite the deliverables table’s “16:9 / 8K” label. The resolution is also slightly different from exact 16:9.

### Design judgement

The new images are convincing at presentation size and show plausible urban apartment cues: balconies, nearby buildings, plants, compact cooking space and timber furnishings. That is progress. They remain generated concept images; they do not establish a real Dhaka site, actual construction, material provenance or the studio’s delivered work.

“Three coherent spatial views” is still too strong. The living scene uses a slatted TV wall; the dining view shows a materially different living arrangement, and the macro joinery image does not visibly establish the same assembly. No common floor plan, fixed camera positions or dimensional model ties them together. Treat them as exploratory variants until continuity is checked against a single layout.

Some captions describe the older imagery: the new hero is called a bookcase study in the PDF, while it shows a TV feature wall; the new macro is captioned as a cane detail without visible cane; the bedroom is described as a work/study alcove without clearly showing that feature. An LPG cylinder niche cannot be verified from the kitchen image alone. Update claims to what is actually visible, or supply the missing plan/detail.

To meet the anti-AI-slop goal, prioritize a consistent room plan, believable furniture clearances, actual apartment constraints and material details that can be explained. Repeated teak slats, warm cove lighting and greenery alone do not make the portfolio distinctive. Use verified real project photographs when available, retain AI/unbuilt labels for concepts, and keep source/rights records. The ZIP does not contain independent evidence of the claimed social-media research or permission to reuse third-party photography.

### Operational claims still needing correction

Bangla desktop copy includes **“নিজস্ব কারখানায়”** in services and process, and **“আমাদের নিজস্ব কাঠের ওয়ার্কশপে”** in the studio section. These mean work in the studio’s own factory/workshop. They contradict the report’s assertion that owned-factory claims were removed. Warranty certificates and fixed workflow durations also remain in the copy without owner evidence in this package.

The single fact register labels the phone/email as placeholders and the address as provisional. Customer-facing screens present those values as ordinary contact facts. Keep owner confirmation status visible in review annotations and disable external actions until real details are supplied. Do not invent opening hours, credentials, factory ownership, warranty terms or guaranteed completion schedules.

## 7. Figma and evidence boundary

The live URL was attempted during this audit, but it did not return inspectable file contents. No Figma connector was available in this session. Therefore this review does **not** independently assert what is currently in the live file. The report’s statement that it remains at v1 is its own admission, not a fresh node-tree verification by this reviewer.

The archive cannot establish editable Figma text, Auto Layout, component variants and instances, variable bindings, responsive constraints or working prototype reactions. SVG text and rectangles do not automatically become that design system. Embedded JPEGs also remain raster content. “100% vector fidelity / clean layer naming” should not be treated as proof of native quality.

Distinguish three statuses in the next report:

1. **Specified:** documented behaviour or intended token.
2. **Implemented in a named artifact:** present in the actual SVG, HTML or native Figma file.
3. **Verified:** independently inspected in that artifact, with the exact evidence supplied.

Only the third status supports completion. Tool limitations can explain missing native work, but do not convert it into completed work.

## 8. Required next delivery

Do not produce another broad “everything verified” deck first. Complete the previously requested narrow native Figma checkpoint:

1. In the actual FlowGrid file, create an editable Bangla home at 1440 and 390, a separate drawer, one concept detail and the four-required-field enquiry journey. Use real components/instances, Auto Layout and bound styles/variables where intended.
2. Provide precise frame and component node IDs, raw inspectable node data or a native `.fig` export, and a playable recording showing text editing, instance reuse, resizing and the connected journey. Check that the recording plays before packaging it.
3. Show valid input, invalid input, “Not sure yet,” submission/loading, clearly simulated receipt, error/retry and keyboard/focus behaviour. Specify or demonstrate the reduced-motion path accurately for the prototype tool being used.
4. Use one approved asset set throughout boards, prototype and PDF. Reconcile captions and operational facts, and preserve truthful AI/unbuilt disclosures.
5. Re-export current boards at their actual bounds. Correct the mobile screenshot mapping and inspect every PDF page at readable size. Remove 8K, focus-trap, responsiveness and completion claims until their evidence exists.
6. Correct scope to 35/44 local page layouts plus two drawers, or deliver the missing nine English mobile pages before claiming full coverage.

If native authoring remains unavailable, report that precise capability gap and request the necessary Figma authoring access. A local SVG/HTML package can be delivered as an intermediate design study, but should not be accepted as completion of the requested native Figma work.

## Verification methods and references

- Archive inventory and safe extraction; strict XML parsing; SVG frame and text inspection.
- PNG/WebP dimensions and frame-count inspection; visual review of supplied board crops and all eight rendered PDF pages.
- SHA-256 comparison of standalone and embedded image bytes against revision 3.
- Independent opaque-sRGB contrast calculations.
- Direct HTML/CSS/JS inspection and isolated handler execution with a DOM stub. No full browser or assistive-technology test is claimed.
- [W3C: Understanding Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
- [W3C ARIA Authoring Practices: Modal Dialog Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).

**Approval decision:** retain the genuine improvements, correct the demonstrably false evidence claims, and require native Figma proof before accepting completion.
