# FlowGrid — Verification and Completion Plan

Reviewed 28 September 2026 · Revision 3.3, Package 7

**Verdict: the package is intact, and the native Figma generator is a useful starting point. The complete native Figma website and final visual quality are not yet verified.** The next deliverable should be an approved homepage and project detail experience, followed by the remaining editable layouts and connected prototype. Another export-only release will not close these gaps.

The completion target is **zero known blocking defects**, with evidence for each acceptance check. Passing a script or exporting a board cannot establish that a design has no faults.

## 1. What was verified

This review inspected the supplied archive and report, compared them with Package 6, read the new generator, checked its JavaScript syntax, inspected the desktop/mobile homepage crops, and consulted the reference websites and official Figma documentation. It did not execute the generator or modify the cloud file.

| Check | Result | Meaning |
|---|---|---|
| ZIP integrity | Pass: 42 files, no CRC failure | The supplied archive is readable. |
| Change from Package 6 | 40 files byte-identical; one report changed; one script added | The screens, PDF, HTML prototype, recordings, and existing runtime evidence have not changed. |
| Separately supplied report | Matches the report inside the ZIP | There is no discrepancy between those two report copies. |
| Report manifest sizes | 32 listed byte sizes match | This validates listed sizes, not every completion claim. |
| New generator | 16,558 bytes; `node --check` passes | Valid JavaScript syntax; live Figma execution is a separate check. |
| Previous prototype/export checks | Carried forward for unchanged files | This review did not rerun every previous browser test. |
| Native Figma screenshots | The two screenshots mentioned in the execution log are absent from the ZIP | The claimed visual evidence cannot be inspected from this package. |
| Native Figma raw readback | No packaged node/variable readback; the only JSON is the existing HTML runtime evidence | Node IDs in a report are not independent proof of current cloud state. |
| Live Figma and GitHub commit | Public retrieval was unsuccessful | This review cannot independently confirm cloud state or commit `5cfc576`. This does not prove that the reported operations failed. |

Archive identity: `FlowGrid_Revision_3_3_Deliverable(3).zip`, **80,013,463 bytes**.

SHA-256: `0226cde847892b59823ff19ba880fe5e1538fefe99138302f4ee9ce4a18084bb`

The scope contains **11 templates × 2 languages × 2 viewport families = 44 layouts**, plus two drawer overlays. These are not 44 distinct website pages. Imported SVG boards remain useful visual references, but they do not establish native components, editable text, responsive Auto Layout, or complete prototype journeys.

## 2. What the generator actually delivers

The source attempts to create 30 variables in three collections, one primary button component set with five states, a modal component, and a mobile drawer. It does not author the full website.

| Finding from source | Required correction or evidence |
|---|---|
| Components use literal colors, padding, gaps, and radii. The script has no variable binding operations. | Bind reusable values to the variables, then show that changing a token updates a component and a page instance. Figma treats variable creation and binding as separate operations.[4] |
| Only Inter is loaded. No text node receives an explicit `fontName`, Bengali text style, or line-height. Font loading races a two-second timeout. | Await the actual fonts; explicitly apply Noto Sans Bengali and the approved Latin styles. Do not proceed with unconfirmed fonts. Figma requires loaded fonts for text layout changes.[5] |
| The modal contains a title, close control, and error banner. It has no form fields, submit control, or success state. | Complete the native consultation component with the same required fields and states as the approved enquiry design. |
| There are exactly two reactions, both `ON_CLICK → CLOSE`. Links and consultation CTA have no navigation/open action in this script. | Connect actual page instances and overlay flows. A close reaction alone does not demonstrate a working journey. |
| No `createInstance` calls occur. The drawer CTA is a separately drawn frame. | Use native component instances throughout the website; demonstrate main-component-to-instance propagation. |
| Button height is content-driven with no enforced 52px minimum. The drawer CTA also has automatic height and no vertical padding. | Measure rendered interactive targets; apply the approved minimum size and appropriate text wrapping. Do not infer hit-area size from an initial `resize` call. |
| The modal requests automatic vertical sizing but is described as a fixed 366 × 600 component. Its claimed clearance references browser coordinates. | Read actual Figma bounds and measure in a shared coordinate system. Browser geometry is not proof of Figma geometry. |
| Existing named components are skipped. Variable and variant creation errors can be caught while later success messages still appear. | Define safe rerun behavior, update only intended nodes, preserve unrelated work, and issue success only after required readback assertions pass. |

These findings describe the packaged script. The live file could contain additional manual work; that work needs its own evidence. Use **“partial native foundations reported; full experience pending verification”** until that evidence is available.

## 3. Design direction to finish

The current homepage has a coherent warm palette and a clearly labelled concept image. Its desktop hero is text-heavy at the left with a large unused area at the right, followed by an image. On mobile, the Bengali headline/body spacing is tight, a pink telephone emoji conflicts with the visual system, and the philosophy card introduces a generic boxed treatment. These are design judgments based on the packaged crops, not browser accessibility findings.

Use the references to define principles, then approve an original FlowGrid composition:

| Reference | Useful principle | FlowGrid application |
|---|---|---|
| ERA Residence — primary | Architectural storytelling connects imagery, materials, context, and an exploration gallery.[1] | Let one convincing Bangladesh interior establish the experience. Follow with a project story, material details, and a clear enquiry path. |
| Thirdway — secondary | Projects, services, approach, and people support studio credibility.[2] | Explain what FlowGrid does, how it works, and what evidence supports its expertise. |
| Quinta D. Amália — secondary | Residential lifestyle and setting inform the story.[3] | Use a calm sequence and relevant local context, with restrained copy and imagery. |

The retrieved pages support these content observations. They do **not** establish exact animation timings. During design execution, inspect the references visually on desktop and mobile and record the specific interaction being adapted. The motion timings below are proposed FlowGrid values.

The art direction should include deliberate image crops, a clear editorial hierarchy, comfortable Bengali typesetting, consistent icons, and a small number of strong transitions. Avoid repetitive cards, decorative gradients, floating blobs, unnecessary counters, excessive entrance effects, and ornamental text that makes the work harder to understand.

Keep the existing palette as a starting point: Warm Paper `#F4F1E8`, Deep Pine `#183B35`, Surface Mist `#DEE7E2`, and Clay `#895239`. Confirm contrast per actual role. Use Noto Sans Bengali for Bengali and Bodoni Moda selectively for Latin display; do not force Bengali to mimic Latin letterspacing or line-height.

## 4. Completion sequence and gates

Antigravity is the execution owner; the studio owner supplies business facts and approves the visual direction. Each phase produces visible evidence. Only the visual-direction gate and final acceptance require a consolidated owner review; routine fixes should proceed autonomously.

### Phase 1 — Establish the baseline and design four decisive screens

**Work:** Confirm the current native Figma nodes through the available authenticated tooling. Record their actual contents and bindings. Keep existing boards as reference material. In the same phase, visually research the three references and create the Bengali homepage and project/concept detail at **1440px desktop and 390px mobile**.

Use one coherent project story: an overview image, another view of the same space, and a material/joinery detail. Establish a clear first viewport, image rhythm, project metadata, captions, enquiry CTA, and footer. Include a short playable motion draft using this composition.

**Evidence:** Four native screen links, full-page exports, a 20–40 second demonstration, and a compact comparison explaining which reference principle informs each major choice. Supply missing Figma screenshots and raw readback once; do not repeat open-ended API probing.

**Gate:** The owner approves the four-screen direction. If a revision is needed, revise this set before expanding it across the site. If live authoring is blocked, report the exact blocker and continue preparing assets and specifications; do not label static imports as native completion.

### Phase 2 — Complete the native design system and content

**Work:** Bind color, spacing, and radius variables; define bilingual text styles; finish reusable navigation, buttons, links, project modules, image captions, concept labels, form controls, status messages, modal, drawer, and footer. Components must have the states required by their actual use.

The enquiry design needs default, focus, filled, invalid, disabled/submitting, success, and failure/retry presentations where applicable. Preserve the accepted four required enquiry inputs rather than expanding the form without a reason.

Create an asset register recording source, owner/permission, real project versus concept, location, caption, crop, and alt-text intent. Use the owner's supplied FlowGrid social accounts for real work. Keep Rumi's Fashionable House and Onekta Product separate unless an asset's relevance and ownership are explicitly established.

For generated concepts, show plausible Bangladesh apartment proportions, daylight, neighboring context, storage, materials, and consistent room geometry between views. Use Nano-Banana only when it serves the approved composition. Check joinery, door swings, mirrors, fixtures, and light sources visually. A render is not construction validation; technical feasibility and service installations need appropriate professional review.

Label generated work clearly: **“কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়”** and the corresponding English label. Never invent clients, completed projects, testimonials, dimensions, budgets, or delivery promises.

**Evidence:** Component examples, token binding readback, applied text styles, a token-change demonstration on a safe duplicate, and the asset register.

**Gate:** Reusable components behave consistently, Bengali renders correctly, content has traceable provenance, and the native form is complete.

### Phase 3 — Apply the system to the full responsive scope

**Work:** Complete the existing 11-template inventory in Bengali and English: homepage, project archive, concept detail, built-project framework, services, joinery service detail, process, studio, contact, privacy, and 404. Preserve the agreed scope; do not add pages to inflate completion counts.

Build layouts from native text, frames, image fills, Auto Layout, and component instances. Use meaningful layer names and constraints. Adapt content order and crops for mobile instead of shrinking desktop. The built-project framework stays clearly marked as a framework until actual project content exists.

Check the two master widths and resize representative layouts to **360, 768, and 1024px**. Those intermediate checks do not require a second set of every page. Check long Bengali/English labels, project names, navigation, and form errors; resolve overflow and clipping where they occur.

**Evidence:** A frame register linking each language/viewport layout to its native Figma node, plus representative resize screenshots.

**Gate:** All agreed layouts exist and are editable; representative resizing works; no missing copy or assets are disguised as completed customer content.

### Phase 4 — Connect the experience and demonstrate motion

Connect these four journeys in Figma Present mode:

1. Homepage → archive → project/concept detail → enquiry → success.
2. Mobile menu → service → enquiry → failure → retry.
3. Bengali → English → Bengali on corresponding content.
4. Open/close gallery and overlays with clear return paths and usable controls.

Use these starting values only after visual review:

| Motion | Starting target | Completion evidence |
|---|---|---|
| Hero image reveal | 600ms once; small or no text movement | Normal and reduced-motion demonstrations |
| Project/gallery transition | 360ms; preserve orientation | Playable forward/back sequence and mobile controls |
| Menu/overlay | Approximately 220–300ms | Open, close, backdrop, and return behavior |
| Button/link feedback | Approximately 150–180ms | Relevant hover, pressed, and focus appearances |
| Optional section reveal | Approximately 350–500ms, used sparingly | Content remains understandable without the effect |

Do not add scroll hijacking, cursor replacement, forced intro delays, or motion that hides essential information. Provide a static/reduced-motion route with the same content. Figma demonstrates design behavior; keyboard semantics, system motion preferences, and browser behavior belong to the HTML prototype or later implementation checks. Do not represent one as proof of the other.

The existing 600ms hero and 360ms project effects are specifications, not demonstrated features in the unchanged HTML prototype. Update a narrowly scoped motion proof if Figma cannot reproduce an approved effect; do not turn this design task into a production rebuild.

**Evidence:** Direct prototype start links, normal/reduced-motion recordings, and a motion sheet documenting trigger, duration, easing, interruption, and fallback.

**Gate:** All four journeys are complete; no dead ends; every claimed signature animation has visible evidence.

### Phase 5 — Final acceptance and one handoff

Review the approved experience once at normal viewing scale and on a phone-sized viewport. Fix defects, then rerun only the affected checks. Perform one final connected-flow review after fixes.

| Acceptance area | Required result |
|---|---|
| Visual direction | Approved four-screen direction is applied consistently. No unexplained generic cards, icons, or effects. |
| Native Figma | Editable text and image layers; component instances; actual variable bindings; correct text styles and Auto Layout. |
| Responsive/bilingual | No text collisions, clipped controls, accidental horizontal overflow, or incorrect language destinations in tested layouts. |
| Interaction | Four journeys pass. Form states, gallery, navigation, and return paths are represented. |
| Motion | Approved effects are demonstrated, with equivalent reduced-motion content. |
| Content integrity | Real work and concepts clearly distinguished. Business facts and assets have an owner/source. |
| Accessibility | Check all active text/background pairs, visible focus, readable text, target sizes, error communication, and reading-order intent. Record browser keyboard checks separately. A contrast ratio alone is not WCAG certification. |
| Release consistency | Figma, exports, presentation, prototype evidence, and report refer to the same approved revision. |

Classify remaining issues: **blocker** (broken journey, unreadable content, misrepresented work), **major** (responsive/component inconsistency or missing required state), **minor** (cosmetic refinement). Final acceptance requires zero open blockers or majors. Resolve minors or record the owner's explicit acceptance.

The handoff should contain the canonical Figma file and prototype links, native frame/component register, tokens and typography, source/asset register, motion specification, evidence, concise developer notes, and one current presentation/export package. Reconcile stale completion claims in all boards and reports. Label the HTML as a prototype; design approval does not establish a production backend, deployment, or full website compliance.

## 5. Effort, priorities, and stopping rules

A provisional budget for one focused designer/operator is **6–9 working days**, assuming Figma write access is functional, required assets are available, and feedback is consolidated: 1–2 days for the four-screen direction, about 1–2 for native foundations/content, about 2–3 for the remaining layouts, and about 2 for motion and final QA. Re-estimate after Phase 1; this is an effort allowance, not a delivery promise.

The critical dependency is approval of the visual direction. The immediate next review should show the four screens and motion draft, not a new ZIP integrity table.

- Keep one issue list with owner, severity, evidence, and status.
- Reuse accepted evidence for byte-identical artifacts. Retest when a relevant source changes.
- Export only the frames being reviewed during iteration. Regenerate the full package after final design acceptance.
- Report observable outcomes: which screens became native, which journey now works, and which decision needs review.
- Do not use screenshot counts, script exit codes, or board dimensions as a substitute for design acceptance.
- Stop when the acceptance matrix passes and the agreed handoff is complete. Production implementation remains a separate task.

## 6. Next instruction for Antigravity

> Continue from FlowGrid Revision 3.3 Package 7 using this verification plan. First confirm the current native Figma state and preserve the existing approved work. Correct the scope claims: the packaged generator is only a partial foundation. Deliver the Bengali homepage and one coherent project/concept detail at 1440px and 390px as native editable Figma frames, plus a short motion demonstration. Use ERA as the primary architectural storytelling reference, Thirdway for studio credibility, and Quinta for residential atmosphere. Research the references visually before choosing motion; do not invent measured timings. Keep imagery and copy credible for Bangladesh, use real FlowGrid work where available, and clearly label generated concepts. Bind variables, apply the actual Bengali/Latin fonts, and complete the form rather than presenting its shell as finished. Show these four screens for one consolidated visual review before extending the remaining templates. Then follow Phases 2–5 and provide evidence for every completion claim. Do not produce another export-only “complete” release.

## Source notes

Local primary evidence: the supplied Package 7 archive and report, its generator, its homepage exports, and the Package 6 archive used for byte comparison. The prior prototype findings are carried forward only for unchanged artifacts.

1. [ERA Residence](https://www.era-residence.com/) — architectural, material, location, and gallery content.
2. [Thirdway](https://www.thirdway.com/) — studio/project/service/people structure.
3. [Quinta D. Amália](https://www.quintadamalia.com/) — residential context and lifestyle narrative.
4. [Figma: setBoundVariable](https://developers.figma.com/docs/plugins/api/properties/nodes-setboundvariable/) — creating variables does not bind node fields to them.
5. [Figma: Working with Text](https://developers.figma.com/docs/plugins/working-with-text/) — font loading and text styling requirements.

The three user-supplied motion/design skill repositories remain implementation resources. This review does not claim that their instructions were applied by the supplied generator. The execution owner should inspect relevant instructions before adopting them and record the concrete pattern used.
