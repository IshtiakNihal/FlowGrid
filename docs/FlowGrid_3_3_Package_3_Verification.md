# FlowGrid Revision 3.3 — Package (3) Verification

Reviewed: 28 September 2026  
Input: `FlowGrid_Revision_3_3_Deliverable(3).zip` and its supplied execution log

**Verdict: meaningful progress, but not ready for final acceptance.** The package closes the previous mobile-simulator issue and improves focus handling. Its own recording exposes an English mobile overflow, and the report introduces a substantial page-register regression. Native Figma completion remains open.

## Package identity and completed checks

| Check | Result |
|---|---|
| ZIP size | 80,988,398 bytes |
| ZIP entries | 39 files; CRC integrity passed |
| ZIP SHA-256 | `52e444b887311e7c628fa64a20f53149c8e08499ebf46a1d0d7093922ed3c2dd` |
| Changes relative to package (2) | 35 of 39 files byte-identical; HTML, report and two recording copies changed |
| Inline JavaScript | Extracted verbatim; `node --check` passed |
| Phone validation | Actual `validateBDPhone` function isolated; all 13 documented cases passed |
| Report file-size entries | All 29 parsed entries match packaged bytes |
| Recording copies | `prototype/` and `figma_exports/` copies are identical |
| Recording | 78 frames; 390 × 844 pixels; 23.5 seconds; 1,895,678 bytes |
| Recording SHA-256 | `03bd162471ef73f11d07d902eb3296ea8f564c4e89e4ae8f56a3219c982e80dd` |
| Client PDF | Unchanged from package (2); 8 pages, 1152 × 648 points |

The unchanged static assets retain the earlier checks: nine valid SVG boards, nine PNG exports whose dimensions match their boards, 49 embedded image occurrences matching the five supplied concept JPEGs, and eight crops matching their board regions. These are carried forward through byte identity, rather than represented as new visual inspections. The static layout inventory is 44 page layouts plus two drawers.

## Closed or improved in this revision

- The simulator CSS, control and function were removed. The remaining `mobile-sim-active` occurrence is a diagnostic check. Bengali recording frame 63 reports an actual 390 × 844 viewport, a matching mobile media query and `Simulator=false`.
- Focus handling improved in the source. The submitting state is programmatically focusable, and state changes direct focus to the relevant name, Done or retry control. The Tab handler also recovers when the active element is outside the current focusable set.
- The metrics code reads `window.innerWidth`, `window.innerHeight`, the media query, simulator state and active element on load, resize, focus changes and a timer.
- The PDF caption correctly says “All 4 required inputs & 52px CTA visible”.
- The stale 330-frame recording claim is removed. The current recording has 78 frames.
- The 600 ms hero reveal and 360 ms project expansion are now treated as motion specifications, rather than proof of completed native Figma interactions.

These findings support accepting the specific fixes above. They do not establish a complete accessibility audit or prove all runtime assertions.

## 1. English mobile layout exceeds the intended viewport

The supplied recording remains a 390 × 844 image canvas. After switching language, its diagnostic monitor reports a larger layout viewport and the right-hand controls are clipped.

Frame numbers below are zero-based decoded WebP indices.

| Frame | Observation |
|---|---|
| 63 | Bengali; monitor reads 390 × 844 px; simulator false |
| 64 | After switching to English, monitor reads 422 × 914 px |
| 69 | English offline modal right edge and content are clipped |
| 75 | English receipt panel and annotation extend beyond the right edge |
| 77 | Monitor still reads 422 × 914 px; hamburger is clipped at the right edge |

**Assessment:** genuine Bengali mobile evidence is now present, but the English state fails the intended mobile layout. A recording's fixed pixel dimensions alone do not prove its page layout stays within that viewport.

**Likely cause, requiring runtime confirmation:** header flex/minimum-content widths, including the 16 px `.nav-actions` gap, button padding of 12 px 24 px, the 28 px brand and longer English consultation text. This is an inference from the source and recording, not an independently reproduced browser diagnosis.

**Required correction and acceptance check:** at a real 390 × 844 viewport, switch BN → EN → BN. Confirm `innerWidth === 390`; compare document `clientWidth` and `scrollWidth` and remove unintended horizontal overflow. Check the header, drawer, form, offline state and receipt, including every right-edge control. Capture the corrected language transition and relevant states using the existing genuine-mobile method.

See the companion PDF for the Bengali/English evidence frames.

## 2. The page register regressed: 38 of 46 geometries are incorrect

Section 2 of the report was compared with the supplied SVG rectangle geometry, using each row's `(x, y, width, height)` values. Only **8 of 46 entries match**. All master SVGs are byte-identical to package (2), whose register matched all 46 entries.

- Matching rows: **1–6, 39 and 42**.
- Incorrect rows: **7–38, 40–41 and 43–46**.
- Rows extending outside their stated canvas: **40, 41, 43, 44, 45 and 46**.

| Row | Reported value or label | Actual supplied SVG / prior correct register |
|---|---|---|
| 7 | BN Process: 1440 × 1950 | 1440 × 2200 at (3280, 2560) |
| 12 | BN Mobile Home: (60, 260), 390 × 1400 | (80, 260), 390 × 3350 |
| 24 | EN Home: 1440 × 2200 | 1440 × 2500 at (80, 260) |
| 25 | EN Archive: x = 1680 | x = 1600, y = 260; 1440 × 2200 |
| 45 | “EN Mobile Receipt”: (4880, 7610), 390 × 1400 | Reported y exceeds the 7400 px board height; prior corresponding entry is mobile 404 at (4640, 6280), 390 × 650 |
| 46 | EN Drawer: (5350, 7610), 320 × 844 | (6520, 4380), 390 × 750 |

The scope labels also changed without corresponding board changes: Bengali Privacy and 404 entries were renamed to Form Modal and Receipt. This is a documentation error, not evidence that those new layouts were delivered.

**Required correction:** restore package (2)'s correct Section 2 register, or derive a fresh register directly from the actual SVGs. Validate all 46 geometries, canvas bounds and layout labels. Preserve the accepted boards; do not reshape them to fit the incorrect table.

## 3. Cited runtime evidence is absent from the ZIP

The supplied log refers to the following files, but neither is included among the 39 packaged files:

- `docs/genuine_390_verification_assertions.json`
- `scripts/record_genuine_390_mobile.py`

Source inspection and the recording support several improvements. They do not allow every claimed keyboard-loop or system reduced-motion assertion to be inspected or reproduced.

**Required correction:** include the existing assertion JSON and recorder script, identifying the exact tested HTML through a hash or equivalent immutable identity. Include actual outcomes for Tab and Shift+Tab wrapping, Escape, focus return, state transitions and system `prefers-reduced-motion`. Keep system reduced motion separate from any manual toggle test. If an assertion was not run, label it untested.

This is an evidence-packaging gap. It does not require replacing accepted assets or repeating unrelated checks.

## 4. Native Figma remains open / tool-blocked

The report acknowledges this limitation. The package does not establish completed native Auto Layout, reusable components and variants, variables or working Figma prototype flows. SVG boards, PNG exports and a separate HTML prototype are useful deliverables, but do not prove those native Figma requirements are complete.

Keep this item explicitly open until the editable Figma implementation can be inspected. Do not mark the original Figma design brief as fully delivered on the strength of the export package alone.

## Focused next pass

1. Fix the English 390 px overflow and capture BN → EN → BN plus the affected modal/receipt states.
2. Correct Section 2 against the existing SVGs and verify all 46 entries, including names and bounds.
3. Package the already-cited runtime assertion JSON and recording script with tested-source identity.
4. Complete or accurately retain the native Figma blocker, with direct evidence when resolved.

Retain the accepted simulator removal, focus-code changes, valid phone tests, corrected PDF caption and unchanged static assets.

## Review limits

This audit used packaged source, static files, the supplied execution log and decoded recording frames. All 78 frames decoded; selected frames, including the language transition, were inspected. It did not independently execute the browser journey, verify a live Figma node tree or confirm a GitHub push. The earlier browser setup was unavailable; source checks and recorded evidence are identified accordingly. No WCAG certification is issued or implied. Motion timing written in a specification is not, by itself, a demonstrated animation.
