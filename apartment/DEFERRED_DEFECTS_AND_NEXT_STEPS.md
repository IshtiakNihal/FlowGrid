# FlowGrid FG-APT-01 — Deferred Apartment Architecture & Tour Notes

**Status:** Deferred post-website completion (Owner's Revised Delivery Order, 29 September 2026).  
**Context:** Antigravity and Claude Code prioritize delivering the full, responsive, bug-free still-image website first. The connected apartment walkthrough, Google Flow video generation, scroll-scrubbing video animation, and 3D modeling are intentionally isolated and deferred to a dedicated follow-up phase.

---

## 1. Confirmed Architectural & Geometric Defects to Reconcile

### A. Balcony Adjacency & Topology Discrepancies
- **Living Room Balcony (Balcony 1):** In the supplied SVG drawing, Balcony 1 is drawn below the kitchen with its sliding opening spanning across the kitchen's southern boundary. However, the living room is located to the north. In stills V03–V05, the balcony directly connects to the living space. When rebuilding the plan, Balcony 1 must be positioned directly adjacent to the living room.
- **Master Bedroom Balcony (Balcony 2):** In the SVG drawing, Balcony 2 is placed east of the master bathroom, requiring circulation through the bathroom. Master stills V10–V11 instead depict direct private bedroom-to-balcony access. The revised plan must place Balcony 2 directly off the master bedroom.

### B. Kitchen Enclosure vs. Rendered Open Peninsula
- The SVG drawing draws continuous north and east partitions, effectively closing off the kitchen into a four-walled room.
- The 3D concept still (V08) depicts an open culinary workspace with a quartz prep island and wide circulation into dining.
- **Correction:** The architectural CAD/3D model must model an authentic opening with workable island clearance (min. 900mm – 1000mm aisle width).

### C. Door Swings and Internal Circulation
- Door-swing arcs in the current 2D plan overlap solid partition rectangles rather than modeled wall openings.
- The semi-master attached bathroom lacks a clear doorway opening in the drawing.
- Camera V09 (hallway) points east toward a common-bath partition in the drawing, while the image displays an elongated corridor extending forward with doors on both sides.

### D. Scale Consistency & Carpet Area Reconciliations
- The semi-master SVG geometry (approx. 346 × 218 units, ratio ~1.59) conflicts with stated 12.5 × 13.5 ft dimensions (ratio ~0.93 or 1.08 rotated).
- Corridor area (4 × 16 ft = 64 sq ft) was omitted from the 1,222 sq ft room subtotal, yet 1,515 sq ft gross was claimed without reconciled wall thicknesses and shared boundaries.
- **Guideline:** Maintain **"approximately 1,500 sq ft" / "১,৫০০ বর্গফুট"** as the design target until a fully measured 3D blockout reconciles exact internal carpet vs. gross areas.

---

## 2. Walkthrough Stills Inventory & Status

| View | Room / Angle | Resolution | Aspect Ratio | Launch Status | Decision & Reason |
|---|---|---|---|---|---|
| **V01** | Axonometric Cutaway | 1376 × 768 | ~1.792 | **Deferred** | Spatial topology differs from close views; plan cutaway conflict. Held as internal visual reference. |
| **V02** | Unit 4B Doorway / Approach | 1376 × 768 | ~1.792 | **Approved Still** | Attractive fluted teak door with long pull handle and 4B plaque. Usable as entrance concept still. |
| **V03** | Entry Foyer & Screen | 1376 × 768 | ~1.792 | **Approved Still** | Warm timber tones and slatted screen. Usable as foyer / joinery millwork concept still. |
| **V04** | Living to Dining | 1376 × 768 | ~1.792 | **Approved Hero** | Strong, calm living composition with open dining threshold. Primary Hero image for website launch. |
| **V05** | Living Balcony 1 | 1376 × 768 | ~1.792 | **Deferred** | Door opening shown as hinged instead of sliding; flooring pavers differ from V04. Needs continuity fix. |
| **V06** | Dining Room | 1376 × 768 | ~1.792 | **RETIRED** | **Artifact:** Features a foreground handwash basin niche while a second basin niche is visible in the background. Excluded from launch. |
| **V07** | Dining Basin Detail | 1376 × 768 | ~1.792 | **RETIRED** | **Artifact:** Close-up repeats foreground basin niche while background basin remains visible. Excluded from launch. |
| **V08** | Open Kitchen & Island | 1376 × 768 | ~1.792 | **Approved Still** | High-aesthetic culinary working view with dark green cabinetry and quartz island. Deployed on Home Angle 02 and Joinery showcase. |
| **V09** | Private Corridor | 1376 × 768 | ~1.792 | **Deferred** | Corridor camera direction and door positions do not coordinate with 2D plan. Internal reference only. |
| **V10** | Master Bedroom Suite | 1376 × 768 | ~1.792 | **Approved Still** | Rich materiality, fluted timber headboard, warm indirect lighting. Deployed on Home Angle 03 and Archive Study 03. |
| **V11** | Master Balcony Sit-Out | 1376 × 768 | ~1.792 | **Approved Still** | Strong local continuity with V10 (recognizable bedhead and cabinetry). Candidate bedroom/balcony pair. |
| **V12** | Master En-Suite Bathroom | 1376 × 768 | ~1.792 | **Approved Still** | Coherent contemporary bathroom still with floating oak vanity and fluted glass. Usable as bathroom concept still. |

*Note on V13–V16:* Semi-master bedroom, semi-master bath, guest bedroom, and common bath generation is paused. Do not generate or model until the unified 3D spatial blockout is established.

---

## 3. Post-Website Implementation Roadmap: Shared 3D Scene Workflow

When the responsive website handoff is complete and running, the architectural tour will be built cleanly following these principles:

1. **One Fixed 3D Apartment Scene:**
   - Construct a single 3D scene (using Blender or equivalent architectural CAD).
   - Fix all wall boundaries, doorways, windows, ceiling planes, millwork, and furniture coordinates.
   - Maintain fixed materials, textures, and lighting setups across all camera positions.
2. **Camera Rigging & Trajectory:**
   - Position fixed camera targets for each room view.
   - Establish continuous overlapping sightlines from Unit 4B entrance -> Foyer -> Living -> Dining -> Kitchen -> Corridor -> Master Suite -> Master Balcony -> Master Bath.
   - The axonometric cutaway (V01) must be rendered directly from this exact geometry by hiding the ceiling slab and positioning a 45° bird's-eye camera.
3. **Walkthrough Footage & Scroll scrubbing:**
   - Derive smooth camera paths between calibrated viewpoints.
   - Render video frames or seamless WebP sequences.
   - Integrate into the website's designated tour media section with a high-performance scroll-scrubbing controller (using the existing `V04` hero image as the permanent fallback).
