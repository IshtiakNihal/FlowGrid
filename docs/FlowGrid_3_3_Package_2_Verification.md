# FlowGrid 3.3 — Package (2) Verification

**Reviewed:** 28 September 2026, Bangladesh time  
**Input:** `FlowGrid_Revision_3_3_Deliverable(2).zip`  
**Verdict:** PDF wording and New enquiry focus handling improved as requested. Real mobile viewport testing and native Figma completion remain open. The statement that all four findings are resolved is unsupported.

## Package checks

| Check | Result |
|---|---|
| ZIP size | 82,079,142 bytes; matches release claim |
| File count | 39; matches release claim |
| SHA-256 | `297cc0addf7f25cd3506b16514bf7fde7bfaa18390ad97ce489991a0e2828305`; exact match |
| ZIP integrity | CRC check passed for every archived file |
| JavaScript syntax | Main script extracted from this ZIP passes `node --check` |
| Phone validation | Actual packaged function passes all 13 documented inputs |
| Report manifest | All 29 parsed file-size entries match the packaged bytes |
| Recording | Both copies identical; 186 decodable frames, 1783 × 997px, 18.6 seconds, 3,002,420 bytes |
| Previous static work | 34 of 39 files are byte-identical to package (1); all master SVGs, board PNGs, concepts and crops retain their earlier verification results |

Five files changed: the HTML, the report, the PDF and the two recording copies. Original deliverables were left unchanged.

## Findings matrix

| Finding | Evidence in this package | Decision |
|---|---|---|
| PDF falsely claimed a visible header; report claimed optional notes in the crop | Rendered PDF slide 7 now says “All 4 required inputs & 52px CTA visible.” Report explicitly excludes the header and optional notes from the crop. | **Closed** |
| New enquiry returned to the form without explicit focus restoration | `showState('stateForm')` and `resetForm()` now focus `inputName`. Recording frame 155 shows a cleared form with the name input visibly outlined. | **Specific correction accepted from source + supplied recording** |
| Genuine 390px mobile viewport evidence missing | Added a CSS body-width simulator, then manually overrode grid/navigation/drawer styles. Browser viewport was not established as 390px. | **Still open** |
| Native Figma components, Auto Layout, variables and prototype flows unverified | Report still labels native Figma OPEN / TOOL-BLOCKED. No new native-file evidence supplied. | **Still open** |
| Complete keyboard and reduced-motion runtime checks | Existing focus trap remains; new manual reduced-motion toggle and system media-query CSS are present. Evidence does not establish complete keyboard or system-preference behavior. | **Partially addressed** |

## Why the simulator does not close mobile verification

At HTML lines 856–857, `.mobile-sim-active` sets the body to `max-width: 390px`. `toggleMobileSimulator()` at line 1640 only toggles that class. This changes the content width without changing `window.innerWidth` or triggering viewport media queries.

The simulator separately forces stacked grids and hides navigation with `!important`, and places the drawer with `right: calc(50% - 195px)`. Those rules can make a desktop page resemble a mobile layout even when the actual mobile breakpoint behavior is wrong.

The recording confirms a narrow simulated layout and drawer in frames 15–40. It then returns to the desktop layout before the enquiry journey. Frame 155 demonstrates focus styling on a desktop modal. These are useful demonstrations, but they do not establish the requested real mobile form and navigation behavior.

**Required evidence:** use the browser's actual viewport at 390 × 844px, with the simulator class disabled. Record the following values alongside the journey:

```javascript
window.innerWidth === 390
matchMedia('(max-width: 900px)').matches === true
document.documentElement.classList.contains('mobile-sim-active') === false
```

Then show the hamburger, drawer, enquiry fields, invalid input, valid submission, receipt and New enquiry in Bengali and English at that viewport. Do not add more simulator-specific CSS to satisfy this check.

## Keyboard and motion: retain the improvement, finish the evidence

The specific New enquiry focus fix is accepted at the evidence level stated above. Full keyboard acceptance is broader. The source still gives no explicit focus destination for `stateSubmitting`, and its Tab handler only wraps when focus already equals the first or last control. Check submitting, receipt, New enquiry, Edit Form, Escape and focus restoration through keyboard input. Capture actual focus assertions where applicable, including `document.activeElement.id === 'inputName'` after New enquiry.

The manual reduced-motion toggle and the `prefers-reduced-motion` rules are present. Test the browser/system preference separately, confirm that the media query matches, and check the affected transitions and spinner. A manual class toggle alone does not verify the system preference path.

The named 600ms hero reveal and 360ms project expansion remain specified rather than implemented in this prototype. Preserve that distinction in the handoff.

## Small documentation correction

The report's conclusion still says **330 frames**, although this recording has **186**. Correct that stale count and replace “all four resolved” with the actual per-item statuses above. Native Figma being explicitly open is incompatible with blanket final acceptance.

## Review limits and next action

This review checked the uploaded archive, source, validator, file comparisons, PDF rendering and supplied recording. All recording frames were decoded; selected frames were visually inspected. No independent browser execution, live Figma inspection, accessibility certification or GitHub push verification is claimed.

Keep the accepted design boards, corrected PDF and phone validator. Complete actual viewport and keyboard/motion checks, then finish and inspect native Figma. The immediate correction is to the verification method and remaining native deliverable; the accepted static layouts do not require regeneration.
