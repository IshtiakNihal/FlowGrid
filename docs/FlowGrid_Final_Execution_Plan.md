# FlowGrid — Final Execution Plan

Prepared 29 September 2026. Scope: complete the Figma design and design handoff; production development is a separate stage.

## Finish target

Budget **24–36 focused working hours**, approximately **4–6 working days at six productive hours per day**, for one designer using Antigravity. This is a planning estimate, not a guaranteed delivery date or a background countdown. It assumes the current visual direction is retained, Figma editing access works, and business content decisions are returned promptly. Confirm the estimate after the first inventory pass; a wholesale redesign requires a revised estimate.

The immediate goal is a complete, convincing customer journey across the agreed templates. Do not restart the brand, generate additional concept images by default, or expand the page scope.

## Where the work stands

The latest supplied Revision 3.3 archive contains 76 files and passes ZIP integrity checking. Compared with the preceding archive, 19 files changed, seven were added, and 50 stayed identical. This demonstrates progress, not design acceptance.

The supplied native register describes 44 layouts: 11 templates in Bengali and English, each at desktop and mobile sizes. There is specific expanded-layout evidence for 13 of these combinations. Completion of the other 31 is not established by the material reviewed; this does not mean all 31 are broken. Short frames and frame counts alone cannot establish completeness.

Current visible blockers include:

- English archive filter controls are clipped in `phase3_desktop_archive_en.png`.
- The Bengali mobile archive consultation button overlaps the footer in `phase3_mobile_archive_bn.png`.
- Several concept cards and category tabs route to a built-project framework, Services, or Joinery service page instead of the matching concept or filtered archive state.
- Language actions in the supplied readback open Figma **design-editor URLs**, generally targeting a homepage. They do not establish an uninterrupted language change to the corresponding page in the prototype. The report describes different URLs, so the report and evidence also disagree.
- Full visual and interaction coverage of all 44 layouts remains to be demonstrated. The latest report's “awaiting owner visual approval” status is therefore premature.

These findings come from the supplied files and exports. They are not a live inspection of the current cloud Figma file.

## Why the work has dragged on

Corrections have been applied to selected screens and individual audit findings, while the full template and journey checklist remains unfinished. More exports, longer frames, or more wired reactions have sometimes been treated as proof of completion. Different destinations can still be wrong destinations. A successful export can still show clipped controls.

The process needs one authoritative design, one issue list, and one bounded acceptance pass. Repeating the whole audit after every small repair adds delay without closing the full experience.

## Five steps to finish

| Step | Work | Time budget | Required output |
|---|---|---:|---|
| 1. Establish the finish list | Retain the palette and approved typography; inspect the 11-template inventory; settle the studio name and truthful content; identify every incomplete variant. Review home, concept detail and archive together for visual direction. | 2–3 hours | One 44-layout checklist, one route map, one prioritized issue list. |
| 2. Complete the design | Finish each template family across BN/EN and desktop/mobile before moving to the next family. Repair shared components at their source. Improve hierarchy and image composition where screens feel generic. | 12–18 hours | All 44 layouts complete, native and editable, with corresponding content and responsive behavior. |
| 3. Finish journeys and motion | Correct language, archive, card, navigation and consultation behavior. Demonstrate four complete journeys and document reduced-motion behavior. | 4–6 hours | A working Figma review experience; HTML motion evidence clearly separated where needed. |
| 4. Perform one acceptance pass | Inspect every layout once, walk every journey, review Bengali and English copy, check concept disclosures, clipping, focus/contrast intent and responsive states. Fix all blocking and major issues. | 4–6 hours | A completed matrix with evidence and no known blocking or major defects. |
| 5. Package once | Export from the accepted Figma version; update the presentation, asset register, motion notes and handoff together. Check archive contents and links. | 2–3 hours | One versioned handoff package and a concise remaining-limitations note. |

Use Day 1 for the inventory and first complete template families; Days 2–3 for the remaining layouts; Day 4 for journeys; Days 5–6 for acceptance and packaging as needed. These are effort blocks, dependent on the executor's actual availability.

## Exact template scope

Every row needs Bengali desktop, Bengali mobile, English desktop and English mobile. Maintain a separate status for each: To inspect, In progress, Ready for review, or Accepted.

| Template | What constitutes completion |
|---|---|
| Home | Clear positioning, coherent architectural imagery, selected concepts, service/process summary and consultation path. |
| Concept archive | Accurate concept groupings, visible category controls, working filtering, correct card destinations and useful empty state. |
| Concept detail | Consistent imagery and room story, truthful design intent, disclosure, appropriate specifications and return/consultation paths. Reuse this template for matching study content; do not substitute unrelated pages. |
| Built-project framework | A clearly identified internal template until real approved project material exists. Keep it out of customer-facing concept-card destinations. |
| Services | Approved service scope, understandable deliverables and consultation action. Avoid unsupported engineering or certification claims. |
| Joinery service detail | Specific service explanation and credible detail imagery, with boundaries and next step. |
| Process | Clear stages, client inputs and deliverables. No invented timelines or guarantees. |
| Studio | Approved business name, positioning and genuine team/biography information. No fictional staff or credentials. |
| Contact | Approved contact information and an accessible consultation path. Required fields: name, phone, location/area and project type; notes optional. |
| Privacy | Readable layout and clearly identified draft content pending business approval; do not claim legal approval. |
| 404 | Useful return/navigation options, consistent in both languages and sizes. |

## Visual standard: premium, simple and Bangladesh-first

Keep ERA Residence as the primary visual benchmark and Thirdway and Quinta as supporting references. Conduct one focused side-by-side review of composition, image treatment, typography, spacing and motion. Do not reopen broad social-media research unless a specific content gap requires it.

The current warm-paper/deep-pine palette and architectural imagery provide a coherent base. Repeated bordered cards and dense, formal copy still need editorial judgment to achieve the quality requested. Give important rooms and details space; vary image scale for a reason; use concise service language; avoid decorative effects that compete with the work.

Use realistic Dhaka apartment context, believable room proportions and plausible materials. Generated images must remain concept studies. Do not infer built feasibility, material certification, exact area or completed-client status from a render.

Use these disclosures visibly with concept imagery:

- Bengali: **কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়**
- English: **Concept Design · AI Visualization · Not a Built Project**

Keep unapproved addresses, team claims, material guarantees and credentials in internal content notes. Resolve “Interior Studio” versus “Architectural Studio” against the owner's approved business positioning before final export.

## Four journeys that must work

1. **Explore:** Home → archive → choose a category → matching concept detail → back to the archive with a sensible retained state.
2. **Enquire:** Consultation action → form → missing/invalid input state → submitting → clearly identified prototype confirmation → close/reopen. A prototype confirmation is not evidence that a real enquiry was delivered.
3. **Change language:** Switch BN ↔ EN on home, archive and detail while preserving the corresponding page and viewport. Remain in the review experience. If the Figma structure prevents this, organize a dedicated prototype page or equivalent supported structure and document the decision.
4. **Navigate on mobile:** Open drawer → Services/Process/Studio/Contact → close/return → recover from a 404. Check scrolling, overlay dismissal and footer access.

Define triggers, duration, easing, interruption behavior and reduced-motion alternatives for the hero reveal, project transition and overlays. Existing 600 ms hero and 360 ms project timings are starting specifications, not proof of successful motion. Supply a short recording that actually shows the Figma journeys; identify any separate HTML recording as HTML evidence.

## Rules that prevent another revision loop

- **Figma is the design source of truth.** Generate review exports from its accepted version. Retire or clearly mark stale SVG boards instead of maintaining competing masters.
- **Fix shared causes.** Correct sizing, constraints and spacing in components/Auto Layout, then inspect the affected instances. Avoid isolated coordinate patches.
- **Finish by template family.** Complete all four variants of Services, for example, before adding polish to another homepage.
- **Preserve accepted work.** Recheck changed components and affected journeys. Do not rerun unrelated successful checks for every export.
- **Separate evidence from claims.** Label packaged readback, live inspection, static screenshot, and runtime recording accurately. Never report a claim as independently verified merely because it appears in a report.
- **One content decision batch.** Collect unresolved business facts together. Continue layout work using internal annotations; do not invent customer-facing facts.
- **One owner review packet.** Present representative final screens and the four working journeys together. Consolidate feedback into one correction round.
- **Do not count activity as completion.** Frame, file and reaction counts are inventory measurements. Correct behavior and visual quality are acceptance criteria.

## Definition of done

The design is finished when all 44 agreed layouts are covered by the acceptance matrix; the four journeys work; text and components remain editable; customer-facing claims are approved; concept imagery is disclosed; known blocking/major clipping, navigation and responsive defects are closed; and the final deck/exports match the accepted Figma version.

Minor optional refinements can be listed separately without reopening accepted work. Do not promise “zero faults” or “WCAG certified” from this design review. Record what was checked and what remains for production implementation.

## Prompt to give Antigravity

Continue the existing FlowGrid Figma project using this execution plan. Do not restart the brand or build a production website. Keep the agreed 11 templates × BN/EN × desktop/mobile scope. Make Figma the canonical design source.

First produce one complete 44-layout status matrix and route map from the actual file. The latest archive is a baseline, not proof that everything is complete. Fix clipped archive controls, the overlapping mobile archive CTA/footer, incorrect concept/filter destinations and language actions that open editor links. Inspect the remaining variants rather than declaring them complete by frame count.

Complete one template family across all four variants at a time. Preserve accepted design work. Use native text, shared components, sensible Auto Layout and existing tokens. Retain the warm architectural direction while improving image composition, typographic hierarchy and concise Bangladesh-specific copy. Keep all AI concepts disclosed; do not invent clients, projects, credentials, addresses, sizes, dates or technical guarantees.

Demonstrate all four journeys in the actual Figma prototype. Document motion and reduced-motion behavior; keep HTML demonstrations labeled separately. Perform one full acceptance pass, repair blocking and major defects, then export the accepted version once and synchronize the handoff. Report progress as completed template variants and verified journeys, plus exact remaining blockers. Do not claim “complete” or “awaiting approval only” while known functional or visual defects remain.

Budget 24–36 focused hours as an initial estimate, revalidated after inventory. If a tooling limitation blocks a specific action, identify the limitation and the smallest workable alternative; do not silently replace a working prototype interaction with a local file or editor URL.
