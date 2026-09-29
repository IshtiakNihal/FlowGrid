# FlowGrid — Stage 1 Audit & Website-First Corrections

**Reviewed:** 29 September 2026  
**Inputs:** `FlowGrid_Stage1_Final_Deliverable.zip` and `Pasted text(9).txt`  
**Decision:** Do not accept the package as a completed design or a coherent apartment walkthrough. Retain useful assets, finish the website experience first, then develop the apartment tour separately.

## 1. The owner's revised delivery order

This direction supersedes the earlier requirement to complete the apartment image sequence before moving to website implementation.

1. **Antigravity finishes the website's Figma design and usable still-image handoff.** Fix the visible defects and content issues below. Use selected, reviewed concept stills. The full apartment tour is not a dependency.
2. **Claude Code builds the complete responsive website.** Include Bengali/English pages, navigation, galleries, working enquiry delivery, accessibility, mobile behaviour and restrained ordinary interface motion. Claude may improve weak compositions while preserving the approved identity and truthful content.
3. **After the website is complete, resolve the apartment architecture.** Establish one measured concept plan and one consistent spatial model, then derive connected camera views.
4. **Produce the walkthrough footage and integrate its scroll effect.** Reuse a prepared media section with a still fallback. Do not redesign or block the whole website around unfinished footage.

“Website first” includes ordinary menu, gallery, hover, focus and section-transition design. The deferred item is the cinematic apartment walkthrough and its scroll-controlled playback.

## 2. What was actually checked

The ZIP contains **129 files, 63,519,274 bytes**, and passes CRC integrity checking. SHA-256:

`8f2118c89759d0f7b30be87cafa738112b1957930ca933fff414bfcc02c42918`

The review covered the file inventory, reports, all four CSVs, apartment plan SVG and PNG, continuity and camera specifications, actual image prompts, all 12 apartment masters at their supplied size, logo comparison/assets, the 42 available template exports in contact sheets and selected screens at readable scale. Exports were compared by hash with `FlowGrid_Revision_3_3_Deliverable(7).zip`.

This is a review of supplied files. The live Figma editor and prototype were not independently operated here. A supplied assertion or execution command is not equivalent to an observed live result. No claim is made that every live Figma node retains the same defect as its packaged export.

| Area | Finding |
|---|---|
| Package integrity | Pass: archive opens correctly |
| Logo assets | Useful progress: source, vectors, transparent PNGs and comparison provided |
| Logo integration into website | Not established; reviewed website exports still use the earlier wordmark |
| Apartment plan | Fails spatial coordination and documented scale consistency |
| Apartment image continuity | Fails as one connected apartment; several stills remain useful individually |
| Apartment coverage | 12 images supplied; semi-master, its bath, guest room and common bath images missing |
| Website layout coverage | 44 main layouts listed; 42 separate screen exports found |
| Website visual finish | Visible blank/clipped controls, missing imagery and inconsistent headers remain |
| Copy/disclosure cleanup | Contradicted by supplied customer-facing exports |
| Prototype evidence | More mapping supplied, but incomplete and internally contradictory |
| Readiness | Targeted website correction pass needed; apartment video deferred |

## 3. Apartment architecture: confirmed defects

### A. The balconies connect to the wrong rooms in the plan

The plan labels Balcony 1 as a living-room balcony, but draws it immediately below the kitchen. Its cyan slider lies across the kitchen's bottom wall. The living room is farther north. This is not the direct living-to-balcony relationship required by the brief or shown in V03–V05.

Balcony 2 is drawn to the east of the master bathroom. The indicated opening is on the bathroom's outer wall, with the bathroom between the master bedroom and balcony. V10–V11 instead show direct bedroom-to-balcony access. The drawing and photographs cannot both describe the same arrangement.

**Later correction:** place the balconies directly beside the living and master bedroom respectively, or deliberately revise the whole plan while preserving direct access. Update all dependent views from that same geometry.

### B. The kitchen is labelled open, but its plan boundaries close it off

The SVG draws continuous north and east kitchen partitions; the outer west and south boundaries complete its enclosure. It does not show a clear interior opening into dining. The render shows a broad connection and peninsula arrangement. This is a topology conflict, not a colour or styling issue.

**Later correction:** draw an actual opening and workable peninsula, then check the aisle and approach with furniture in place.

### C. Doors and circulation are not resolved

Door-swing symbols are drawn over unbroken wall rectangles instead of consistently formed openings. The semi-master attached bathroom has no connecting doorway drawn. The guest-room door symbol sits on its boundary with the semi-master area, rather than a clearly connected shared hall opening. The private circulation camera V09 points east toward the common-bath zone in the drawing, while its image presents a long hallway extending forward with doors on both sides.

These issues mean the current drawing cannot support the claimed walking route. A list of room names and arrows does not establish a traversable apartment.

### D. “Scaled CAD plan” and the area claim are unsupported by the geometry

The drawing is an editable SVG diagram, but its rectangles do not consistently match their labelled proportions. For example, the semi-master internal zone is approximately 346 × 218 SVG units, a ratio of about **1.59**, while its stated 12.5 × 13.5 ft dimensions imply about **0.93**, or **1.08** when rotated. A single consistent scale cannot produce both.

The listed room groups total 1,222 sq ft, which is then used as the entire interior carpet area. Yet the continuity sheet separately specifies a **4 × 16 ft corridor = 64 sq ft** without clearly accounting for it in that total. Do not simply add 64 and publish a new number: boundaries and possible overlapping allocations must first be resolved.

Keep “approximately 1,500 sq ft” as an internal design target until measured areas reconcile. The claimed 1,515 sq ft figure is not verified by the supplied drawing.

### E. The plan export itself is cut off

The PNG includes horizontal and vertical browser scrollbars and truncates the lower content. The SVG declares a 1440 × 1140 canvas, while the supplied PNG is 2100 × 1650 and captures a viewport with overflow. This contradicts a clean, complete architectural export.

## 4. Review of every generated view

All 12 JPEG masters are **1376 × 768**, not the **1920 × 1080** recorded in the manifest. Their aspect ratio is approximately **1.792**, close to but not exactly 16:9. Preview files do not establish higher-resolution masters.

“Candidate still” below means visually useful for a separate concept presentation after editorial review. It does not mean a real completed project or proof that the image fits the apartment plan.

| View | Specific observation | Decision |
|---|---|---|
| **V01 — Overview** | Its walls, kitchen arrangement, openings and room relationships do not reconcile with the SVG plan. The cutaway has a different spatial arrangement from the close views; the kitchen/bar and dining-basin forms also change. | Reject as the authoritative apartment overview. Keep only as internal visual inspiration. |
| **V02 — Entrance** | Attractive doorway with fluted timber, long pull handle, digital lock and 4B plaque. No coordinated building landing or threshold geometry connects it to the cutaway. | Candidate entrance still; not a verified route start. |
| **V03 — Foyer** | Shares the timber and warm-light theme, but introduces an additional FG-APT-01 sign on the door and its own console/screen arrangement. The V02 landing-to-V03 threshold has no demonstrated matching camera connection. The balcony straight ahead conflicts with the supplied plan. | Candidate foyer still after removing unwanted embedded project text; hold for tour. |
| **V04 — Living to dining** | A useful interior composition with one dining basin and two bar stools. It establishes a layout different from the plan. The balcony floor appears grey here, while V05 uses terracotta. | Strong candidate standalone concept view; not approved as plan-accurate. |
| **V05 — Balcony 1** | The foreground glass door is visibly hinged open, whereas the neighbouring views and specification describe a sliding system. Flooring changes from V04. The visible openings are not coordinated with the plan. | Requires continuity correction before joining to V04. |
| **V06 — Dining** | Shows a large handwash niche in the right foreground while another basin/mirror niche remains behind the dining table. The foreground kitchen counter adds a further inconsistent spatial arrangement. | Reject from the public set until the duplicated fixture/layout is corrected. |
| **V07 — Dining basin** | The close-up repeats the same problem: the foreground basin remains while another basin/mirror niche is visible in the dining background. | Reject as a truthful detail of one dining basin. Do not solve it by claiming a second basin was intended. |
| **V08 — Kitchen** | Visually usable in isolation. Its sink is on the back window wall and hob on the right run; the plan puts them along the same left run. Cabinet fronts, upper cabinetry and peninsula treatment also differ from other views. | Candidate kitchen concept still; hold as part of this apartment. |
| **V09 — Corridor** | A credible corridor image by itself, but door positions and forward route do not match the plan's camera marker and adjacency. Its doorway arrangement cannot be used to connect the bedrooms reliably. | Internal reference only until the actual hall is modelled. |
| **V10 — Master bedroom** | Strong material and lighting presentation. Direct balcony access conflicts with the plan's bathroom occupying that side. The freestanding headboard/wardrobe/bathroom circulation also needs a measured check. | Candidate bedroom concept; no full-apartment continuity approval. |
| **V11 — Master balcony** | The strongest local continuity with V10: the headboard, bed, fan and cabinetry are recognisably related. That does not resolve the larger plan conflict. | Preserve as a promising bedroom/balcony pair, pending measured geometry. |
| **V12 — Master bathroom** | Coherent-looking bathroom still. Its window, fixture layout and connection to the bedroom are not established by a usable plan or matching threshold view. The prompt asks for an undermount basin while the image shows a vessel basin. | Candidate bathroom concept; update the material/fixture record and verify later. |

V13 semi-master, V14 semi-master bathroom, V15 guest room and V16 common bathroom are absent. The report says their exact prompts were preserved, but `images/prompts.md` ends at V12. The camera-route document contains short descriptions for later views and D01–D06, not a completed set of detailed generation prompts.

The quota pause explains missing files. It does not establish that the existing images passed geometric review. The repeated “100% matched” and “100% alignment” statements should be withdrawn.

## 5. Why the sequence does not feel like photographs of one apartment

The prompts repeatedly describe a style and a desired room. Their reference lists do not provide a verifiable chain from one measured spatial model to every image. There is no shared 3D scene/blockout in the package. A prompt can preserve wood colour while changing the room behind it.

For the later walkthrough, use **one fixed apartment scene with several cameras**. Keep walls, openings, furniture, lights and materials fixed. Move only the camera for each view. Render the roof-cutaway from that same scene using a controlled visibility setup. Use matching reference views for any image enhancement and reject edits that move architecture.

Blender is one free option; its documented camera view displays the scene from the active camera. This is a practical workflow recommendation, not a claim that Antigravity has already built a model or that modelling is effortless. Sources: [Blender](https://www.blender.org/about/) and [camera-view documentation](https://docs.blender.org/manual/en/5.3/editors/3dview/navigate/camera_view.html).

Later acceptance requires fixed wall/opening IDs, a furniture schedule, camera coordinates/direction, matching overlapping views, and explicit returns from branch rooms. A matching first and last image alone will not prove that the intermediate video follows the apartment.

**Do not start this modelling or regeneration cycle as a prerequisite for finishing the website now.**

## 6. Website and handoff defects that matter now

### W1 — Actual customer screens still contradict the cleanup claim

`phase3_desktop_home_en.png`, `phase3_mobile_home_en.png`, `phase3_desktop_detail_en.png` and the reviewed Bengali home export still show the old disclosure text. Examples include “AI Visualization” and “Not a Built Project.” The same reviewed screens retain the older FlowGrid wordmark rather than the supplied identity.

The homepage still uses previous imagery and a previous 2,400 sq ft concept description. It is not the newly described FG-APT-01 homepage. A new design-system document does not update these screens automatically.

Compared with the preceding ZIP, **39 export files are byte-identical, four changed and 38 are newly included**. The four changed files are the Brief, Foundations, Assets and Handoff boards. The unchanged files include homepage/detail exports, major language boards and prototype recordings. This explains why the package still displays superseded content; it does not establish whether every live frame is equally stale.

**Fix:** update the actual public frames and component instances, then regenerate exports from that state. Verify customer screens, not just internal boards.

### W2 — Visible interface defects remain

- English desktop homepage: primary green CTA areas lack visible labels, including the header action, hero action and bottom enquiry action.
- English mobile homepage: its primary green button has no visible label.
- English mobile 404: both recovery buttons visibly clip their text; footer content also runs beyond the edge.
- English mobile contact: the submit control meets the footer without adequate clearance and is visibly cut at the lower edge; placeholder contact details remain public.
- Desktop services/joinery: header content occupies only part of the desktop width; logo/navigation collide, and control sizes do not form a consistent header.
- English detail: the expected hero image is reduced to a thin strip before the next heading.
- Joinery: a very large empty media region precedes specification cards. A mostly blank frame is not a finished portfolio detail page.
- Mobile studio/services/process: excessive fixed blank space, tall buttons and repeated cards make the layouts feel like expanded templates rather than carefully composed pages.

These examples directly contradict “zero visible clipping” and “all layouts complete.” Fix the shared component and responsive sizing causes, then inspect affected instances.

### W3 — Public copy is overly technical and includes unsupported claims

The visible screens contain location placeholders, a dummy phone number, inconsistent Dhanmondi/Banani/Mirpur references and claims about architects, workshops, material performance or certification without supporting business information in this package.

The mobile studio even includes an “Authenticity & Credentials Policy” paragraph explaining that FlowGrid does not invent staff. This is internal production commentary, not useful customer-facing content.

Replace these with short, natural descriptions of the confirmed service. Use only **Concept Design / কনসেপ্ট ডিজাইন** for the project category. Keep unconfirmed contact/business details on an internal dependency list. Preserve verified owner details already available; do not ask for them again unnecessarily.

### W4 — Missing layouts and incomplete prototype evidence

The register contains **44 main template layouts**, plus overlays, one generic board row and 46 flow/review frames. It contains 109 rows in total, not 109 website pages.

Only **42 individual main screen exports** are supplied: 22 desktop and 20 mobile. Separate Bengali and English mobile privacy exports are missing. The register has no export-path field, so it does not reconcile each frame to its image.

The route CSV has **357 rows**: 323 NODE, 10 URL and 24 CLOSE actions. All 357 are stamped with the same “Native In-Canvas Transition Verified” result, even the URL actions, whose destinations are recorded only as `N/A`. It therefore cannot prove that editor links have been removed.

The map also retains legacy archive routes into the internal built-project framework:

- Bengali archive source `23:503` → `18:1624`.
- English archive source `23:579` → `18:1160`.

There are **191 entries labelled with Flow / source frames and 166 other entries**. Thus, the 357 total is not evidence of 357 new Page 06 reactions. The actual intended four start journeys need a short current screen recording and correct destination mapping. Remove obsolete public routes or clearly separate retired frames from the active design.

No fresh raw node/interaction readback or dedicated current `evidence/` folder is supplied. The previously packaged walkthrough recordings are unchanged. No working website/backend is established by this ZIP.

### W5 — CSV data is malformed

Unquoted commas split fields across columns:

- `images/asset_manifest.csv`: V01 row.
- `handoff/copy_bn_en.csv`: `hero.subline` and `project.area` rows.

This can put Bengali text into an English field and corrupt area labels. Re-export using a CSV writer with proper quoting and parse it once to confirm every row has the same columns. Correct actual image dimensions and add stable placement/crop records.

## 7. The next bounded completion pass

| Order | Work | Evidence needed to move on |
|---|---|---|
| 1 | Choose the public still-image set and freeze launch scope | Clear asset list; no defective duplicated-basin images, no claim that unrelated views form one apartment |
| 2 | Fix logo, public copy, header/buttons and responsive layout | Corrected BN/EN desktop/mobile Home → Archive → Detail → Contact shown at readable scale |
| 3 | Apply fixes to remaining templates and active prototype routes | All 44 layouts accounted for, including internal-only built templates; four valid start journeys |
| 4 | Export and hand off the current state | 44 matching screen exports, correct CSVs, short fresh recordings and a concise real dependency list |
| 5 | Claude builds the functioning website using stills | Responsive pages, working forms, navigation, accessibility and ordinary motion verified in browser |
| Later | Correct the apartment model, render matching views, make footage and add scroll playback | Separate architecture/continuity and media performance review |

The website should retain the intended sophistication of the reference direction without depending on a cinematic opening. Prioritize image quality, restrained layouts, readable type and convincing project presentation. Adding video will not correct blank buttons, inaccurate copy or a weak mobile composition.

## 8. Ready-to-send Antigravity correction instruction

Read this audit and treat the following as the latest owner direction. Continue the existing FlowGrid project and preserve useful work. The immediate goal is a finished website design and a reliable handoff to Claude Code.

**Change the sequence:** finish Figma for a complete still-image website first; Claude will then build the website. The apartment walkthrough, Google Flow footage and cinematic scroll effect are deferred until afterward. Do not spend time or credits completing V13–V16, detail renders, video or a 3D model during this website correction pass.

1. Review the actual live public frames against the defects in Sections 6–7. Do not rely on the current all-PASS report. Retire or clearly mark obsolete frames so active work has one identifiable source.
2. Integrate the supplied FlowGrid identity into real headers and footers. Preserve the useful reconstructed assets. Check small-size legibility; confirm the vector tagline/font renders as intended.
3. Remove superseded production-disclosure phrases from all customer-facing screens and exports. Use Concept Design / কনসেপ্ট ডিজাইন with ordinary portfolio copy. Remove internal honesty policies, public placeholder details and unsupported business claims. Keep missing owner facts in one internal list.
4. Select a small, attractive still-image set. V04 and selected individual room views may be candidates; V10/V11 are a promising local pair. Do not use V06/V07 with duplicated basins, or publish the defective plan/cutaway as an accurate apartment. Do not present inconsistent rooms as a connected tour or as separate completed client commissions. Room-scale concept presentation is acceptable.
5. Finish one strong BN/EN desktop/mobile Home → Archive → Concept Detail → Contact journey first. Use ERA as the primary creative reference, Thirdway for studio/project clarity and Quinta for residential atmosphere. Improve composition and image hierarchy rather than adding more generic cards.
6. Fix the actual component/layout causes: blank CTA labels, clipped 404 controls, partial-width headers, contact/footer overlap, missing detail imagery, oversized empty regions and inconsistent button heights. Use responsive Auto Layout and native reusable components. Keep Bengali text natural and readable.
7. Complete the remaining template variants. Preserve the agreed 44-layout coverage; keep built-project frameworks internal. Provide the missing mobile privacy exports. Map every accepted layout node to its current export filename.
8. Correct active prototype destinations. Record actual URL targets where external actions are intended. Remove unintended links to internal frameworks/editor pages. Test the four current start journeys and language switching; provide a short fresh recording. Do not use reaction counts as the completion criterion.
9. Keep normal menu, gallery, focus, hover and restrained reveal motion. Design the future tour as an optional media section with a still fallback. There must be no empty “video coming soon” gap or dependency on missing footage in the launch design.
10. Correct CSV quoting, image dimensions and placement mappings. Export after edits finish. Exclude superseded reports/recordings from final evidence or label them historical. Report what was actually observed and any remaining blocker.

Deliver the corrected Figma file, four prototype links, selected web-ready stills, all matching layout exports, component/motion guidance, a usable content/asset manifest and one concise handoff for Claude. Do not issue another completion claim without showing the corrected screens.

Keep the current apartment material in a deferred folder with the defects from Sections 3–4. Later, it must be rebuilt from one coherent measured plan and fixed scene before we resume connected imagery and video.

## 9. Reference sources consulted

- [ERA Residence](https://www.era-residence.com/) — retained primary reference; this review does not claim to have independently watched its current browser animation.
- [Thirdway](https://www.thirdway.com/) — project, service and studio reference.
- [Blender official overview](https://www.blender.org/about/) — free/open-source option for the later shared apartment scene.
- [Blender camera-view documentation](https://docs.blender.org/manual/en/5.3/editors/3dview/navigate/camera_view.html) — scene viewed from the active camera.

The audit findings themselves come from the user's supplied ZIP, its images, SVG geometry, CSVs and execution log.
