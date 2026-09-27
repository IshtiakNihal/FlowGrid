# FlowGrid revision 3.2 — verification and acceptance decision

**Reviewed:** 27 September 2026  
**Inputs:** `FlowGrid_Revision_3_2_Deliverable.zip` and `Pasted text(20260927-104601).txt`, plus the accompanying export-completion message.  
**Archive size:** 83,516,849 bytes; 38 files.

**Decision: the export, screenshot-source and image-synchronization fixes pass. The full native Figma handoff does not yet pass.** Revision 3.2 makes substantial progress and supplies all 44 static page layouts plus two drawers. However, the interaction recording demonstrates v3.1, the PDF still clips important mobile content, and several prototype and documentation claims exceed what the files demonstrate.

This is a delta review against revision 3.1. Previously corrected work should be retained. Do not rebuild the whole package or reopen the 44-layout scope merely to address the remaining blockers.

## 1. Verified improvements

| Area | Independent result |
|---|---|
| Nine master SVGs | All pass strict XML parsing. |
| Nine board PNGs | Every PNG has the same canvas dimensions as its current SVG. The earlier English export truncation is corrected. |
| Page coverage | 11 Bangla desktop + 11 Bangla mobile + 11 English desktop + 11 English mobile = **44 page layouts**, plus two separate mobile drawers. This verifies static source coverage, not native Figma artboards or responsive behaviour. |
| Export screenshot crops | All eight supplied crop images match the corresponding pixel regions of the final board PNGs exactly. This is stronger evidence than file dimensions alone. |
| Image synchronization | All **49 embedded image occurrences** across Boards 03, 04, 05 and 07 match one of the five supplied JPEGs by SHA-256. The stale-image defect is resolved. |
| Concept resolution | The report correctly retracts the 8K claim and gives **1376 × 768 px**. The JPEG files are unchanged from revision 3.1; regeneration was unnecessary for synchronization. |
| Recording file | Both copies are genuine animated WebP files: **212 frames, 1920 × 924 px, 3,807,960 bytes, 21.2 seconds**, at 100 ms per frame. They decode successfully. |
| Basic HTML corrections | “Not sure yet,” optional notes, draft storage, missing section targets, ARIA attributes, Escape handling and reduced-motion CSS are now present. |
| Original invalid phone case | The supplied validation handler now rejects `abcdefgh`. |
| Contact links | The previous active placeholder `tel:` and WhatsApp URLs are removed from the HTML prototype. |
| Owned factory/workshop copy | The previous Bangla ownership claims were removed from the active page sources. This specific correction passes. |
| Specific touch-target fixes | Desktop header consultation and mobile WhatsApp controls now use 48 px height. Main mobile inputs remain 48 px and submit buttons 52 px. |
| Contrast documentation | The new report and PDF correct slate-on-white to **6.21:1** and light-slate-on-pine to **7.76:1**. Board 08 still has old values; see Section 6. |
| PDF structure | Eight pages, each 1152 × 648 pt. Slide 7 now uses the correct concept and contact source screenshots. Its display clipping remains unresolved. |

### Render log comparison

| Export | SVG and PNG dimensions | Actual PNG bytes | Result |
|---|---|---:|---|
| `page_00_brief.png` | 2400 × 1950 | 273,268 | Pass |
| `page_01_foundations.png` | 2400 × 2050 | 230,708 | Pass |
| `page_02_components.png` | 2800 × 2550 | 315,837 | Pass |
| `page_03_desktop_bn.png` | 6480 × 7200 | 6,880,913 | Pass |
| `page_04_mobile_bn.png` | 2450 × 4850 | 2,113,132 | Pass |
| `page_05_english.png` | 7000 × 7400 | 8,213,086 | Pass |
| `page_06_motion.png` | 2800 × 2500 | 267,256 | Pass |
| `page_07_assets.png` | 2800 × 2900 | 1,598,054 | Pass |
| `page_08_handoff.png` | 2800 × 2600 | 297,097 | Pass |
| `component_3_1190.png` | 210 × 52 | 1,349 | Pass for local image geometry |

The user-supplied log’s rounded “KB” values agree when interpreted as KiB (bytes ÷ 1024). The archive demonstrates the output, not the claimed execution times or process exit code. No page-sized rectangles or embedded images in Boards 03–05 extend outside their SVG canvas bounds. This does not mean every text element or presentation panel is free of clipping.

## 2. Remaining approval blockers

### A. Native Figma completion is still not demonstrated

The report explicitly redefines the “native checkpoint” as master SVG files and local Edge PNGs. That does not meet the previously requested checkpoint: editable native frames/text, Auto Layout, reusable components and instances, styles or variables, and connected Figma prototype reactions in the actual FlowGrid file.

The package contains no native `.fig` export, current raw node data, component/instance relationship evidence, or recording of native authoring and interactions. SVG files can be useful import material; their presence does not establish those Figma capabilities. The 210 × 52 PNG proves local button geometry only.

The report now identifies node `3:471` as a consultation CTA, whereas revision 3.1 identified that ID as the earlier desktop board. No current node response is supplied to resolve the discrepancy.

**Status:** not verified. No new live Figma inspection was performed in this review. The export success should be accepted separately from the unfulfilled native Figma requirement.

**Required proof:** one native Bangla home at 1440 and 390, the drawer, one concept detail, and the enquiry journey in the existing file, with exact node IDs and evidence of editable text, reusable instances, resizing and connected states. If the available tools cannot author these, disclose the authoring-access gap instead of declaring SVG import readiness equivalent to completion.

### B. The recording is real, but it demonstrates v3.1

Frame 0 visibly reads **“FlowGrid Interactive Journey & State Demonstrator (v3.1)”**. The receipt shown around 13.5 seconds contains Call and WhatsApp buttons. The packaged v3.2 HTML instead defines **Done** and **New enquiry** buttons in that receipt.

This establishes a version mismatch independently of the badge. The recording can support that an earlier HTML prototype opened a form, displayed errors, showed a simulated receipt, switched concept images and opened a drawer. It cannot verify the newly supplied v3.2 code or its new notes, validation, persistence, accessibility and language behaviour.

The recording uses a 1920 × 924 desktop viewport. Opening a drawer at that width is not a 390 px mobile check. The report’s claimed complete v3.2 timeline and mobile verification are not established by this file.

**Required correction:** record the exact packaged HTML after all edits; show its version, invalid and valid phone cases, “Not sure yet,” optional notes, keyboard operation, simulated receipt, reload persistence, reduced-motion mode and a real mobile viewport. Verify the resulting file by watching it before packaging it.

### C. Slide 7 still clips the evidence it claims to show

The standalone `crop_mobile_contact.png` is now correct and contains all four fields and the submit button. It matches the final Bangla mobile board exactly. However, the PDF’s contact card displays only the first two fields and the beginning of the third. The service selector and submit button are cut off by the presentation panel.

Likewise, the concept card shows the upper portion of the first image, not the three-view stack. A partial viewport teaser can be useful, but it should not be described as a complete flow or “zero cut-off.”

**Required correction:** fit the complete form screenshot within a larger panel, or give the enquiry flow a dedicated slide. If retaining cropped previews, label them as previews and remove the full-depth/complete-form assertions.

## 3. Prototype verification: improvements and remaining defects

The HTML, CSS and JavaScript were inspected directly. Isolated JavaScript execution with a minimal DOM stub tested validation, draft save/restore and the English hero toggle. These are logic checks, **not a full browser, mobile, assistive-technology or animation-performance test**. No messages, calls or customer enquiries were sent.

### Phone-validation results

| Input | Result from supplied handler | Assessment |
|---|---|---|
| `abcdefgh` | Rejected | Original defect fixed |
| `01711000000` | Accepted | Expected example |
| `০১৭১১০০০০০০` | Accepted | Bengali digits supported |
| `12345678` | Accepted | Does not establish a valid Bangladesh mobile number |
| `!!!!!!!!01711000000` | Accepted | Arbitrary punctuation silently ignored |
| `বাংলা01711000000` | Accepted | Bengali letters are not rejected |

The implementation filters out unwanted characters for counting, but rejects only Latin A–Z letters and checks for 8–15 remaining digits. Therefore “strict numeric phone validation” is inaccurate. Define the accepted contact-number formats, normalize Bengali digits, allow only intended separators and validate the entire normalized value. If international numbers are needed, state that explicitly rather than treating any 8–15 digits as a Bangladesh mobile number.

### Accessibility and language behaviour

- **Modal focus handling is partially implemented.** Opening focuses the name input; closing restores a recorded active element; Escape is handled. The Tab selector, however, includes controls inside hidden submitting/receipt/offline states. It does not restrict the first/last controls to the visible state, so it cannot reliably contain keyboard focus. Verify the corrected implementation in a browser.
- **Drawer Tab trapping is absent.** The keydown handler contains a Tab branch only when `enquiryModal` is open. The drawer’s role and Escape handling do not add its missing Tab/Shift+Tab loop.
- **Error-summary focus is incomplete.** The code calls `errBanner.focus()`, but the summary `<div>` has no `tabindex` or other focusable semantics. ARIA live announcements are a separate improvement, not a substitute for the intended focus action.
- **English translation is partial.** The toggle changes the hero, navigation, concept headings and form labels, and changes `<html lang>` to `en`. Service/process/studio body content, drawer links, concept specifications, select options, validation messages and receipt text remain largely Bengali. Translate the complete customer journey or label the demonstration as partial.
- **Draft persistence is now implemented.** The supplied handler saves and restores all five fields through localStorage, and the isolated check restored the notes successfully. Browser persistence and privacy behaviour still need appropriate testing; no claim of such testing is made here.
- **Offline handling remains a simulation.** Retry always proceeds to a simulated receipt after 700 ms. A backend is not required for this design task, but the demonstration should distinguish a selected offline state from an actually detected network failure.
- **The universal 48 px claim remains false.** The HTML modal close button is 36 × 36 px, and the drawer close button is 44 × 44 px. Static desktop archive-filter buttons are 160 × 40 px in both languages. These contradict the project’s 48 px target rule; they are not automatically WCAG 2.2 AA target-size failures.

### Animation

Reduced-motion CSS now exists and removes the spinner animation and drawer transition while shortening other animations/transitions. The drawer transition duration is now 220 ms. These source-level fixes pass.

The signature **600 ms hero mask** and **360 ms project-to-detail expansion** remain documented on Board 06 and the PDF, but are absent from the packaged HTML. The prototype contains a concept-tab image swap, not a shared-element project expansion. Mark the signature effects as **specified** until implemented and recorded. The existing recording does not verify v3.2 motion behaviour.

## 4. Visual quality and Bangladesh context

The warmer architectural direction remains suitable for review: restrained pine/paper colours, recognizable Bangla text and plausible apartment imagery. This revision improves consistency by finally using the same images throughout the design boards.

It still needs editorial refinement before being described as a polished premium portfolio. Several secondary layouts use short blocks of small copy within very tall fixed frames, leaving long empty intervals before footers. The mobile contact form, for example, retains a large empty section beneath the submit button inside its white card. Intentional whitespace is useful; large fixed-height gaps should not be presented as verified responsive rhythm or “zero blank intervals.”

The five images remain concept studies. The new captions remove some old image mismatches, but **“three coherent spatial views”** remains unproven without a common plan or consistent room geometry. The living TV-wall scene, dining view and joinery macro should be labelled as exploratory variants unless they are reconciled to one design. The full-size imagery cannot verify construction feasibility, material provenance, apartment location or delivered client work.

The explicit own-factory/workshop claims are corrected. Other business facts still require owner confirmation. The report’s Section 7 now calls the placeholder phone, email and provisional Mirpur address “authoritative” and “official,” while Board 00 and the PDF still label them provisional. The HTML also retains a 24-hour response promise and office-hour copy without supporting owner evidence in this package. Keep those claims provisional in review annotations; do not silently promote placeholders to verified facts.

## 5. Corrected English frame index

The report’s “exact canvas coordinates” table does not match the final English SVG. The frames are present, but the source must be used as authority when locating them.

| English desktop page | Actual x, y |
|---|---|
| Home | 80, 260 |
| Archive | 1600, 260 |
| Concept study | 3120, 260 |
| Built-project template | 80, 2860 |
| Services | 1600, 2860 |
| Joinery | 3120, 2860 |
| Process | 80, 5160 |
| Studio | 1600, 5160 |
| Contact | 3120, 5160 |
| Privacy/legal | 4640, 260 |
| 404 | 4640, 1860 |

| English mobile page / overlay | Actual x, y | Width × height |
|---|---|---|
| Home | 4640, 2860 | 390 × 3350 |
| Archive | 5110, 2860 | 390 × 1600 |
| Concept study | 5110, 4540 | 390 × 2000 |
| Built-project template | 5580, 2860 | 390 × 1400 |
| Services | 5580, 4330 | 390 × 1400 |
| Joinery | 5580, 5800 | 390 × 1400 |
| Process | 6050, 2860 | 390 × 1400 |
| Studio | 6050, 4330 | 390 × 1400 |
| Privacy/legal | 6050, 5800 | 390 × 1400 |
| Contact | 6520, 2860 | 390 × 1450 |
| 404 | 4640, 6280 | 390 × 650 |
| Drawer | 6520, 4380 | 390 × 750 |

The Bangla desktop canvas is **6480 × 7200**, not the **6500 × 5800** stated in the scope diagram. The final export log correctly gives its actual size.

## 6. Documentation and scope hygiene

- Board 08 is byte-identical to revision 3.1 and still reports slate-on-white as **5.50:1** rather than **6.21:1**, and light-slate-on-pine as **8.12:1** rather than **7.76:1**. The report/PDF were corrected, but this QA source was not.
- The report’s manifest has many inaccurate sizes. For example, `prototype/index.html` is **62,604 bytes**, not 42,750; `03_desktop_bn.svg` is **12,875,429 bytes**, not 3,248,396; the button PNG is **1,349 bytes**, not 12,480. Generate the manifest from the final files.
- Native Figma node identity and “editable native checkpoint” wording need correction, as described above.
- The supplied completion message includes **“Edited EY-0006-api-runtime-shell.md.”** That appears unrelated to FlowGrid. The file is not in this ZIP, so no actual change to it is verified here. Ask the agent to identify the exact diff and why it was touched before deciding whether to retain or revert anything. Do not blindly revert unrelated work.
- The workflow should finish all SVG/HTML changes, render current boards, generate crops from those final boards, rebuild the PDF, record the current prototype, then generate the manifest and ZIP. In this package, crop-to-board parity passes; the recording and report metadata still need that final reconciliation.

## 7. Bounded next step

**Accept now:** export dimensions, 44 static page layouts plus two drawers, all eight crop-source mappings, image synchronization, corrected ownership copy and the specific prototype improvements listed above.

**Require before final approval:**

1. Native Figma proof in the existing file, or an explicit authoring-access blocker with completion status left open.
2. A recording of the exact revised prototype, including a mobile viewport and the behaviours newly claimed as tested.
3. Correct visible-state focus handling, drawer keyboard containment, phone-format validation and complete language coverage for the demonstrated journey.
4. A PDF panel that actually shows the complete four-field form, and accurate preview labels elsewhere.
5. One consistent status/fact register, current coordinates and file sizes, corrected Board 08 values, and owner confirmation flags for operational details.

This revision should be treated as **export and asset QA passed; native design handoff and current prototype verification still open**. The remaining work is focused reconciliation and proof, not another expansion of the design scope.

## Methods and limits

Safe archive extraction; strict XML parsing; source frame counting and canvas-bound checks; exact pixel comparison of eight crops; SHA-256 comparison of all embedded images; decoding of all 212 animation frames with duration inspection; visual inspection of selected recording frames, the English board and the eight-page PDF; direct HTML/CSS/JS review; isolated handler tests with a DOM stub. No new live Figma, full browser, responsive reflow or assistive-technology verification is claimed.
