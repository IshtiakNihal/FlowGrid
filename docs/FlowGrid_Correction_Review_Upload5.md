# FlowGrid — Correction Review of Deliverable (5)

**Date:** 29 September 2026, Bangladesh time  
**Verdict:** **PARTIAL PASS. Keep the verified repairs; full design acceptance remains open.**

The clipping and collapsed sections are visibly repaired in the seven updated principal layouts. The enquiry fields are now distinct, the supplied native readback contains actual bindings and instance relationships, and refreshed recordings match their declared identities. This is substantive progress.

However, the report's statement that all twelve findings are resolved is too broad. Remaining issues concern the other templates, incomplete navigation, misleading concept presentation, motion verification, and content consistency. Owner approval is not the only remaining step.

## 1. Package and verification scope

| Check | Result |
|---|---|
| Archive | `FlowGrid_Revision_3_3_Deliverable(5).zip` |
| Bytes | 92,585,533 |
| SHA-256 | `ac2f465384b084282b38a542c1f50de74d097ccea35c62438a7deb89f5c02428` |
| Integrity | 69 entries; ZIP CRC passes |
| Changes from `(4).zip` | 18 changed files, 10 added, 41 identical; no removals |
| Report | Attached report matches archived report |
| Manifest | All 59 listed byte sizes match |
| Syntax | Six packaged `.js` files and the HTML inline script parse successfully; both Python recorder files parse successfully |
| Current HTML SHA-256 | `bd70501d9acc2ef672757b3641b70705453d18a7530be71282f97025b9964403` |
| Runtime/motion identity | Both JSON files identify that exact HTML hash; all three recording hashes and sizes match |
| Recording counts | Enquiry: 65 decoded frames / 178 captured steps; desktop motion: 32 / 49; mobile motion: 36 / 45 |
| Native readback | 98 reaction records; 84 NODE actions and 14 CLOSE actions; no recorded destination marked `NODE_NOT_FOUND` |

I reviewed the supplied files, seven principal layout exports and repaired form exports, compared this archive with the preceding archive, parsed the native readback, inspected repair/recorder code, and decoded the recordings for identity/count checks. The execution log records rerunning both recorders. The new recording files differ from the previous package. Deterministic runtime assertion values remain the same, which is not itself a defect.

I did not rerun the browser journeys or execute authoring scripts. The live Figma URL remained inaccessible through public web retrieval. Native findings below therefore refer to the supplied exports, scripts, and readback, not an independently inspected current cloud session.

## 2. Findings that can be accepted within scope

| Previous finding | Current disposition |
|---|---|
| FG-01 / FG-02: Bengali mobile clipping | **Visible repair passes at the exported 390px width.** The principal text now wraps. This does not independently establish the claimed 360px resize result. |
| FG-03 / FG-04: Bengali desktop collapsed sections | **Visible repair passes at 1440px.** Gallery images, content rows, service cards, and footer now have usable dimensions. |
| FG-05: English homepage and Bengali archive | **The three supplied repaired exports pass the previous collapse defect.** Full 44-layout completion remains unverified. |
| FG-06: Repeated Full Name fields | **Distinct fields and overlap repair pass visually.** The forms show name, phone, location, project type, and optional notes, with a separate close control. |
| FG-07: Unsupported owner approval | **Status corrected.** The report now says “Awaiting Owner Visual Approval.” |
| FG-08: Missing native binding/action evidence | **Evidence improved; journey completion remains partial.** The JSON now includes destination records, variable aliases, and instance-to-main-component IDs. |
| FG-09: Old evidence relabelled | **Refreshed-recording package accepted within supplied-evidence scope.** Hashes/counts match and the log records execution. This is not a fresh independent browser certification. |
| FG-10: Motion evidence | **Identity and frame terminology fixed; verification logic still needs correction.** See section 5. |
| FG-11: Missing repair scripts | **Main correction scripts are included and parse.** They repair existing Figma nodes; they are not a complete standalone reconstruction of the entire file. |
| FG-12: Content/business consistency | **Partly fixed in HTML; still open in Figma and the asset register.** |

Preserve these accepted repairs. Do not repeat the earlier full export/geometry audit unless affected content changes.

## 3. Remaining scope and interaction gaps

### A. Only seven layout records show changed geometry

The current register still lists 44 layouts. Seven have changed dimensions: Bengali home/detail desktop and mobile, English homepage desktop and mobile, and Bengali desktop archive. The other **37 retain their previous short dimensions**, with no new exports establishing their finished state.

Examples still requiring evidence and, where necessary, completion:

| Layout | Node | Registered size | Reactions |
|---|---|---|---|
| Bengali services desktop | `18:1655` | 1440 × 600 | 0 |
| Bengali contact desktop | `18:1780` | 1440 × 600 | 0 |
| English concept detail desktop | `18:1139` | 1440 × 471 | 0 |
| English archive desktop | `18:1102` | 1440 × 595 | 0 |
| Bengali archive mobile | `18:1853` | 390 × 719 | 1 |
| English concept detail mobile | `18:1425` | 390 × 706 | 1 |

Small height or unchanged dimensions alone do not prove incompleteness. But this package does not substantiate full completion of these pages, and current homepage links lead to several of them. Review the actual native contents and complete the intended sections before calling the whole experience finished.

### B. The 98 reactions do not complete the required journeys

The readback now makes specific gaps observable:

- **Language switching:** No language-switch source appears in the supplied reaction list. All destination-bearing actions stay on the source Figma page. The category called `journey3_global_navigation_and_language` contains only two drawer Home links, not Bengali/English switching.
- **Bengali desktop header:** Home has actions for Archive, Services, and Contact, but no actions for the visible Process and Studio links. The wiring script searches for text containing `কার্যপদ্ধতি` and `দর্শন`, while the rebuilt header uses `পদ্ধতি` and `স্টুডিও`.
- **Archive filters:** None of the five visible filter controls appears in the reaction readback.
- **Archive card destinations:** All four cards—Dhanmondi, Gulshan, Banani, and Baridhara—navigate to the same Dhanmondi detail node `18:221`.
- **Return/navigation coverage:** The repaired Bengali desktop detail has only three recorded actions: Archive and two consultation controls. Complete and demonstrate the visible navigation rather than relying on aggregate reaction counts.

Add the missing actions, correct destination/content mappings, and record the actual Figma Present-mode journeys. Figma reactions describe triggers and their actions; an inventory count is not an executed journey test.[1] The readback generator currently exports only the first action from each reaction; export the complete action list when testing multi-action behavior.

## 4. Content regression that must be fixed before customer presentation

The repaired principal screens no longer show the required explicit **AI visualization / unbuilt** disclosure. English uses “CASE STUDY 01 · DHANMONDI, DHAKA”; Bengali uses a short study label. Neither replaces the agreed disclosure. Restore readable labels adjacent to the imagery and on project cards:

- Bengali: **কনসেপ্ট ডিজাইন · AI ভিজ্যুয়ালাইজেশন · বাস্তবায়িত প্রকল্প নয়**
- English: **Concept Design · AI Visualization · Not a Built Project**

The new archive presents four different projects with named neighborhoods, dates, bedrooms, and floor areas. It reuses images that the asset register describes as views/details of one Dhanmondi concept. For example, the dining view becomes a Gulshan penthouse and the same living-room image also appears as a Baridhara residence. No supporting client project records or approved concept briefs are supplied.

Use the real available concept inventory instead. Keep the living, dining, and joinery views together as one concept. Add the existing kitchen and bedroom concepts only if needed. Clearly mark any proposed location, area, material performance, or year as an assumption; remove unsupported claims of completed work. Do not invent projects to fill the archive grid.

Business details also remain inconsistent: HTML now uses Mirpur-10 with provisional labels, while the new Figma exports and repair scripts still say **Banani** without the same qualification. The Bengali archive ends with an English consultation banner. Align these with confirmed information or consistent bilingual placeholders.

The asset register is byte-identical to the previous package and still contains “Nano-Banana / Midjourney v6” attribution and usage-approval claims. Its provenance was not corrected as reported. Use documented sources or mark the unknown fields as unconfirmed.

## 5. Motion evidence: retain the demonstrations, correct the assertions

The new motion files have matching hashes, correct decoded-frame counts, tested HTML identity, and explicit HTML-demo scope. Those improvements are accepted.

However, `scripts/record_phase1_motion_demo.py` writes PASS after capture loops without verifying the claimed animation outcome. Its clearance check uses `document.querySelector('.modal-close')`, but the actual button is `#modalCloseBtn` with class `card-close-btn`. If either queried element is missing, the recorder returns **`{ clearancePx: 16 }`** and still records PASS. The current motion JSON contains this fallback-shaped result.

Fix this targeted issue: select the actual close control, make the intended banner/state visible, fail when required elements are missing, measure both bounds, and assert the clearance. For motion, verify the intended effect/reduced-motion behavior or label a capture as a demonstration rather than a passed measurement. Do not infer animation duration from screenshot-capture elapsed time.

The separate genuine mobile recorder uses actual assertions and provides banner bounds. Its evidence is distinct and should be retained; the defect above does not invalidate every runtime check.

The package still lacks a recording of the corrected native Figma journeys. HTML recordings demonstrate HTML behavior and cannot substitute for that review.

## 6. Exact next steps

1. **Restore truthful concept labels and remove unsupported project facts.** Resolve Banani/Mirpur and language inconsistencies across Figma and HTML.
2. **Complete/check the remaining template inventory.** Start with destinations already linked from the repaired homepages: archive, English detail, services, and contact. Supply native exports and direct node links for each distinct template.
3. **Finish the interactions above.** Include language round-trip, all visible navigation, matching project destinations, filter behavior, and overlay return paths. Fix the existing drawer's narrow close target/long layout and demonstrate reachability on a phone viewport if it remains in use.
4. **Repair the motion recorder and produce a Figma Present demonstration.** Keep valid existing evidence; rerun only the affected checks.
5. **Request one consolidated owner review.** After acceptance, regenerate the final deck and board exports from the approved source. The existing PDF, nine SVG boards, nine board PNGs, drawer PNG, and receipt PNG remain unchanged from the preceding package, so they should not be described as newly synchronized evidence.

The layout repairs are ready to retain. The package as a whole remains **“corrections verified in part; content and complete journeys pending; owner visual approval pending.”**

## Antigravity follow-up

> Keep the seven repaired layouts and corrected distinct enquiry fields. This revision receives a partial pass, not full completion. Restore explicit AI/unbuilt disclosures and remove unsupported project locations, dates, dimensions, and completed-work wording. Keep one concept's views together rather than presenting them as separate client projects. Reconcile Banani/Mirpur and bilingual content. Inspect and finish the remaining 37 layout records where needed. Wire the missing Bengali Process/Studio links, language round-trip, archive filters, correct project destinations, and return paths; provide a recording in Figma Present mode. Fix the motion recorder's `.modal-close` selector and remove its hard-coded 16px success fallback; missing elements must fail. Preserve accepted checks, update only affected evidence, and stop claiming all twelve findings are closed. Present the corrected experience for one owner review before final export synchronization.

## Reference

[1] [Figma Plugin API — reactions](https://developers.figma.com/docs/plugins/api/properties/nodes-reactions/), consulted to interpret triggers, action lists, and navigation evidence. All project-specific findings above derive from the supplied package and previous archive comparison.
