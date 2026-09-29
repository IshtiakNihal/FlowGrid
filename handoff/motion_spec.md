# FlowGrid Motion & Interaction Specification

**Stage 1 Production Delivery · 29 September 2026**  
**Guidance References:** Emil Kowalski Design Engineering & Motion Principles, Delphi Animate Accessibility Guidance, iart Spatial Sequencing.

---

## 1. Motion Principles & Constraints

1. **Purpose-Driven Restraint:** Animations serve spatial orientation, tactile feedback, and structural continuity. Avoid ornamental, gratuitous, or perpetual looping motion.
2. **Snappy Micro-Feedback:** Button presses, card taps, and form focuses execute within **150–200 ms** with `cubic-bezier(0.2, 0.0, 0.2, 1)`. Interactions never delay user action.
3. **Scroll-Linked Storyboard:** The apartment walkthrough is tied directly to scroll progress ($Progress \in [0.0, 1.0]$), rather than an autonomous video timer. Users control their own pacing.
4. **Strict Accessibility Fallbacks:** When `prefers-reduced-motion: reduce` is enabled, all zoom/pan transitions collapse to immediate cuts (0 ms), and the walkthrough converts to a direct still gallery with semantic room jumping.

---

## 2. Complete Interaction Motion Inventory

| Interaction | Trigger & Event | Start -> End State | Affected Elements | Timing & Easing | Interruption & Reversal | Mobile Behavior | Reduced-Motion Alternative |
|---|---|---|---|---|---|---|---|
| **Overview-to-Door Journey** | Scroll progress down from Hero | Bird's-eye 45° cutaway (V01) -> Corridor Dolly (V02) -> Foyer (V03) | Master canvas viewport, camera coordinate | Scroll-linked ($0.0 \to 0.2$ range), scrub-damped | Fully reversible on scroll up | Simplified 2-stage crossfade | Direct click-to-room still gallery |
| **Walkthrough Storyboard Scrub** | Vertical page scroll | Consecutive shot sequence (V03 -> V12) | Main viewport canvas, room indicator badge | Scroll progress ratio ($0.2 \to 0.9$) | Scrub reverse on reverse scroll | Swipeable carousel with thumbnail scrub | Grid of 12 labeled still frames |
| **Header / Mobile Drawer** | Click/Tap hamburger icon | Closed ($x = -100\%$, opacity 0) -> Open ($x = 0\%$, opacity 1) | Drawer container, backdrop scrim (40% pine) | 280 ms, `cubic-bezier(0.16, 1, 0.3, 1)` | Dismiss on scrim tap or Esc key | Full-screen drawer width (320px) | Instant visibility toggle (0 ms) |
| **Project Card -> Detail** | Click project card | Archive card -> Full-width hero detail | Image crop, title container | 320 ms shared element morph | Instant navigation on back | Standard page slide-left | Instant page switch |
| **Consultation Modal Open** | Click primary CTA | Scale 0.96, opacity 0 -> Scale 1.0, opacity 1 | Modal container, backdrop scrim | 250 ms, `cubic-bezier(0.16, 1, 0.3, 1)` | Click outside or Close button to cancel | Bottom-sheet slide-up from $y=100\%$ | Instant popup (0 ms) |
| **Form Submitting State** | Click submit button | Active form fields -> Spinner loader + disabled inputs | Form card, CTA button label | 200 ms fade transition | Submission in flight; lock re-submission | Same | Instant state swap |
| **Form Success Receipt** | Server 200 OK | Submitting -> Success card with checkmark | Success icon, reference number | 300 ms scale-in (`cubic-bezier(0.34, 1.56, 0.64, 1)`) | Click 'Done' / dismiss to close | Bottom sheet update | Instant display |
| **Gallery Thumbnail Select** | Tap thumbnail | Active outline, image switch | Hero gallery viewport, active border | 200 ms crossfade | Click adjacent thumb immediately | Horizontal swipe gesture | Instant picture swap |
| **Language Switcher (BN/EN)**| Click BN/EN pill | Switch language state, retain current view | Text nodes, URL route | Instant route switch | Reversible by clicking back | Same | Instant |

---

## 3. Apartment Walkthrough Storyboard (FG-APT-01)

```
[0.00 - 0.10] V01: Whole-Apartment Roof-Cutaway Overview (Bird's eye, 45° axonometric)
      │       Transition: Camera pitches down towards Entrance North Wall
      ▼
[0.10 - 0.20] V02: Front Door Approach (Corridor landing, eye-level 1.55m, 4B plaque)
      │       Transition: Fluted teak door swings open into foyer
      ▼
[0.20 - 0.30] V03: Foyer Entry Looking into Living Room (Shoe console, slatted screen)
      │       Transition: Camera tracks past oak divider screen into living space
      ▼
[0.30 - 0.40] V04: Living Room Wide (Oatmeal sofa, coffee table, sliding balcony doors)
      │       Transition: Camera pans left toward Balcony 1
      ▼
[0.40 - 0.50] V05: Living Balcony 1 / Verandah (Terracotta tiles, planters, morning sun)
      │       Transition: Camera rotates back inside toward Dining Room
      ▼
[0.50 - 0.60] V06: Dining Room Wide (6-seater teak table, brass pendant, breakfast bar)
      │       Transition: Camera glides toward the architectural alcove
      ▼
[0.60 - 0.70] V07: Dedicated Dining Handwash Basin Niche (Fluted mirror, brass tap)
      │       Transition: Camera turns left into Open Kitchen
      ▼
[0.70 - 0.78] V08: Open Kitchen Working View (Deep pine cabinets, quartz waterfall bar)
      │       Transition: Camera dollies out into central private corridor
      ▼
[0.78 - 0.85] V09: Private Circulation Hallway Junction (Flush oak doors, wall-washers)
      │       Transition: Camera turns into Master Bedroom Suite
      ▼
[0.85 - 0.92] V10: Master Bedroom Suite Wide (King bed, fluted headboard, Balcony 2)
      │       Transition: Camera tracks out onto private balcony
      ▼
[0.92 - 0.96] V11: Master Balcony 2 Sit-Out (Cane armchairs, jasmine planters, Dhaka sun)
      │       Transition: Cut into master en-suite
      ▼
[0.96 - 1.00] V12: Master En-Suite Bathroom (Sage-green fluted tile, fluted shower glass)
              Transition: Tour Complete -> Persistent CTA "Discuss your space"
```

---

## 4. Stage 2 Video Production Manifest (Google Flow Handoff)

> **IMPORTANT STAGE BOUNDARY RULE:**  
> Antigravity Stage 1 finishes with the verified still image masters, camera vectors, and storyboard sequence above. **No video generation was executed in Stage 1.**  
> In Stage 2, Google Flow will consume this exact shot list and camera vector manifest to generate continuous video segments using a dedicated video prompt.
