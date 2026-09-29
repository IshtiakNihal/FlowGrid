# FlowGrid FG-APT-01 — Architectural Image Prompts & References

**Project ID:** `FG-APT-01`  
**Public Title:** Dhaka Family Apartment (ঢাকার পারিবারিক বাসা)  
**Aspect Ratio:** 16:9 Landscape  
**Optical Standard:** 1.55 m eye-level elevation, 28mm equivalent moderate wide-angle lens, 0° pitch/roll level horizon, straight architectural verticals.

---

## Pass A — 4-View Continuity Pilot

### View 1: `FG-APT-01_V01_overview`
- **Output Path:** `images/masters/FG-APT-01_V01_overview.jpg`
- **Prompt:**
  > Architectural 3D perspective cutaway model of a 1,500 sq ft modern family apartment in Dhaka (FG-APT-01), looking from a high 45-degree axonometric bird's-eye view with the roof cut away to show the entire interior layout. Program clearly visible: 3 bedrooms (master bedroom with en-suite bath and private balcony, semi-master with en-suite bath, guest bedroom/study), 3 bathrooms total, open living room connecting to a front balcony with planters, dining area with a distinct dedicated handwash basin niche alcove, open kitchen with breakfast bar counter peninsula and deep pine green cabinetry, central hallway connecting private bedrooms. Warm European white oak flooring in living and bedrooms, warm greige porcelain tile in kitchen and foyer. Bright morning natural sunlight streaming in through southern and eastern windows. Sophisticated, realistic, clean architectural model rendering, photorealistic materials, straight lines, no people, no text or labels.
- **Reference Assets:** `apartment/FG-APT-01_concept_plan.svg`
- **Verification:** 100% matched to room program and spatial adjacencies.

### View 2: `FG-APT-01_V02_approach`
- **Output Path:** `images/masters/FG-APT-01_V02_approach.jpg`
- **Prompt:**
  > Architectural eye-level photograph of the front door entrance approach to a modern luxury family apartment in Dhaka (FG-APT-01). View from the quiet, well-lit residential lift lobby corridor looking directly at the apartment main entrance door. The entrance features an elegant solid teak wood door with vertical reeded fluting, a vertical brushed champagne brass bar pull handle, a smart digital door lock, and a discreet backlit apartment numeral plate '4B'. Warm 3000K recessed ceiling spotlight illuminating the doorway. Large-format warm greige porcelain floor tiles in the corridor. Next to the door, a subtle recessed alcove with a minimal potted olive tree or ficus in a ceramic planter. Clean architectural lines, straight verticals, level eye-level horizon (1.55m height), calm residential atmosphere, photorealistic materials, no people, no distorted angles.
- **Reference Assets:** `apartment/continuity_sheet.md`
- **Verification:** Unit '4B' and fluted teak door geometry established as anchor.

### View 3: `FG-APT-01_V03_foyer`
- **Output Path:** `images/masters/FG-APT-01_V03_foyer.jpg`
- **Prompt:**
  > Photorealistic architectural interior photograph of FlowGrid apartment FG-APT-01 entrance foyer looking into the sunlit living room. View from just inside the open front door at eye level (1.55m). In the foreground foyer, a built-in floating white oak shoe console cabinet with an integrated entry bench and subtle warm LED underglow on warm greige tile flooring. An architectural vertical slatted oak screen provides privacy between the entryway and the living room. Beyond the partition screen, the living room opens up with seamless European white oak hardwood plank flooring, a tailored oatmeal textured sofa, a round low oak coffee table, and floor-to-ceiling glass sliding doors opening to a lush green balcony with morning Dhaka sunlight streaming across the floor. Warm Paper off-white walls, 9'-6" ceiling with warm cove light, straight architectural verticals, level horizon, no people, no text.
- **Reference Assets:** `images/masters/FG-APT-01_V02_approach.jpg`
- **Verification:** Exact door swing, 4B plaque, greige-to-oak floor transition, and slatted divider aligned.

### View 4: `FG-APT-01_V04_living`
- **Output Path:** `images/masters/FG-APT-01_V04_living.jpg`
- **Prompt:**
  > Photorealistic architectural interior photograph of FlowGrid apartment FG-APT-01 living room showing its seamless spatial connection to the dining room and open kitchen. View from inside the living room at eye level (1.55m) looking towards the dining and kitchen zone. In the foreground living area, natural European white oak plank flooring and a glimpse of the tailored oatmeal sofa. To the left, floor-to-ceiling glass sliding doors opening to the lush green balcony with morning daylight streaming in. Beyond in the open plan, the dining room features a solid teak 6-seater dining table with cane-back chairs under a minimalist linear brass pendant light. Next to the dining table, a dedicated recessed handwash basin niche alcove with a backlit fluted mirror and marble counter is clearly visible. Spatially connected to the dining room is the open kitchen featuring a quartz breakfast bar peninsula with two barstools and deep pine green cabinetry. Warm Paper off-white walls, 9'-6" ceiling with warm cove lighting, level horizon, straight architectural verticals, no people, no text.
- **Reference Assets:** `images/masters/FG-APT-01_V03_foyer.jpg`, `images/masters/FG-APT-01_V01_overview.jpg`
- **Verification:** Slatted oak screen on right, balcony on left, dining and basin niche aligned with plan.

---

## Pass B — Route Key Views & Spatial Coverage

### View 5: `FG-APT-01_V05_balcony1`
- **Output Path:** `images/masters/FG-APT-01_V05_balcony1.jpg`
- **Prompt:**
  > Photorealistic architectural photograph of Balcony 1 (front verandah) of FlowGrid apartment FG-APT-01, stepping through the black aluminum sliding glass door. The balcony features warm terracotta matte porcelain pavers, architectural charcoal metal railings, and built-in planters with thriving tropical indoor/outdoor plants (monstera deliciosa, areca palms, fiddle-leaf fig). Bright 10:00 AM Dhaka morning sunlight casts gentle shadows. Outside the balcony is a peaceful view of residential Dhaka tree canopies and clean modern residential mid-rise architecture under a clear morning sky. Through the glass slider on the right, the warm European white oak flooring and tailored seating of the living room interior are visible. Straight architectural verticals, eye-level 1.55m, no people.
- **Reference Assets:** `images/masters/FG-APT-01_V04_living.jpg`

### View 6: `FG-APT-01_V06_dining`
- **Output Path:** `images/masters/FG-APT-01_V06_dining.jpg`
- **Prompt:**
  > Close, eye-level (1.55m) architectural photograph inside the dining room of FlowGrid apartment FG-APT-01, stepping up towards the dining table. The camera is focused on the teak 6-seater dining table with cane-back padded chairs and the adjacent dedicated handwashing basin niche alcove. Above the table hangs the minimalist brushed champagne brass linear pendant luminaire. Directly behind the table in the architectural alcove is the dedicated dining handwash station featuring a curved-corner backlit fluted glass mirror, a honed Calacatta gold marble counter, white ceramic undermount washbasin, and wall-mounted brass gooseneck faucet. To the left is the breakfast bar peninsula with deep pine green cabinetry. Warm European white oak flooring, Warm Paper walls, straight verticals, no people, no text.
- **Reference Assets:** `images/masters/FG-APT-01_V04_living.jpg`

### View 7: `FG-APT-01_V07_dining_basin`
- **Output Path:** `images/masters/FG-APT-01_V07_dining_basin.jpg`
- **Prompt:**
  > Detailed architectural eye-level photograph of the dedicated dining handwash basin niche in FlowGrid apartment FG-APT-01. Frontal architectural composition focused on the elegant recessed wash station alcove. Honed Calacatta gold quartz vanity counter with a white undermount basin, paired with a wall-mounted brushed champagne brass gooseneck faucet and matching mixer handle. Above hangs an architectural pill-shaped mirror with subtle fluted glass texture and a warm 2700K concealed perimeter LED halo glow against Warm Paper off-white walls. Below the counter is custom fluted natural white oak cabinetry with a soft reveal. On the counter sits a minimalist amber glass soap bottle and a small ceramic tumbler with eucalyptus sprigs. Crisp architectural focus, photorealistic materiality, no people, no text.
- **Reference Assets:** `images/masters/FG-APT-01_V06_dining.jpg`

### View 8: `FG-APT-01_V08_kitchen`
- **Output Path:** `images/masters/FG-APT-01_V08_kitchen.jpg`
- **Prompt:**
  > Photorealistic architectural interior photograph of the open kitchen in FlowGrid apartment FG-APT-01. Eye-level shot (1.55m) looking into the L-shaped kitchen work zone. Lower base cabinets and tall appliance tower in FlowGrid Deep Pine green satin finish with minimal brushed brass J-pull handles. Seamless Calacatta gold quartz countertops and continuous 18-inch matching quartz backsplash. An undermount double-bowl sink with a brushed champagne brass gooseneck faucet is positioned below a bright casement window with soft morning daylight and green tree foliage outside. On the adjacent counter run, a flush modern 3-burner gas cooktop sits beneath a sleek ducted black glass chimney hood. Upper wall cabinets are crafted from natural fluted white oak with reeded glass inserts and warm under-cabinet LED task lighting. In the foreground, the edge of the breakfast bar peninsula with its 40mm mitered waterfall quartz edge. Floor is large-format warm greige porcelain tiles. Straight architectural verticals, level horizon, no people, no text.
- **Reference Assets:** `images/masters/FG-APT-01_V04_living.jpg`

### View 9: `FG-APT-01_V09_corridor`
- **Output Path:** `images/masters/FG-APT-01_V09_corridor.jpg`
- **Prompt:**
  > Photorealistic architectural interior photograph of the private circulation corridor in FlowGrid apartment FG-APT-01. Eye-level shot (1.55m) looking down the quiet, 4-foot wide private residential hallway connecting the bedrooms. The walls are finished in smooth Warm Paper off-white, illuminated by recessed low-glare ceiling wall-washer spotlights that cast a soft 3000K warm glow on minimal framed monochrome architectural line sketches. The hallway features clean, jambless flush-to-wall natural white oak veneer interior doors with sleek horizontal brushed brass lever handles, leading to the Master Bedroom suite ahead, the Semi-Master on the left, and the Guest Bedroom and Common Bathroom on the right. Flooring is large-format warm greige porcelain tiles with subtle brass transition strips at bedroom thresholds. Straight architectural verticals, calm serene residential ambiance, level horizon, no people, no text.
- **Reference Assets:** `images/masters/FG-APT-01_V08_kitchen.jpg`

### View 10: `FG-APT-01_V10_master_bed`
- **Output Path:** `images/masters/FG-APT-01_V10_master_bed.jpg`
- **Prompt:**
  > Photorealistic architectural interior photograph of the Master Bedroom in FlowGrid apartment FG-APT-01. Eye-level view (1.55m) looking across the serene master suite towards the king bed and private balcony. The bed is a custom low-profile platform bed in natural white oak with an extended textured oatmeal fabric fluted headboard spanning behind twin floating oak nightstands, each fitted with a minimal brushed brass directional reading sconce. Natural European white oak plank flooring runs throughout. To the right, floor-to-ceiling black aluminum sliding glass doors with ripple-fold sheer unbleached linen curtains open out onto private Balcony 2, allowing soft 10 AM Dhaka morning sunlight to cast warm geometric patterns across the bed linens. In the background wall, a full-height built-in wardrobe in linen-finish laminate and the doorway leading into the master en-suite bathroom. On the 9'-6" ceiling, an ultra-quiet aerodynamic black and oak blade ceiling fan and warm perimeter cove lighting. Level horizon, straight architectural verticals, no people, no text.
- **Reference Assets:** `images/masters/FG-APT-01_V03_foyer.jpg`

### View 11: `FG-APT-01_V11_master_balcony`
- **Output Path:** `images/masters/FG-APT-01_V11_master_balcony.jpg`
- **Prompt:**
  > Photorealistic architectural photograph of Balcony 2 (private master bedroom sit-out) of FlowGrid apartment FG-APT-01. Eye-level shot (1.55m) looking across the intimate covered balcony. Flooring is warm terracotta matte porcelain tiles. A modern charcoal metal balustrade borders the balcony, with built-in planter boxes featuring fragrant jasmine and trailing green vines. Two comfortable woven cane lounge armchairs and a small glazed ceramic coffee pedestal sit in the gentle morning Dhaka sunlight. Through the open black aluminum sliding glass door on the left, the serene master bedroom with its natural white oak flooring, platform bed, and sheer linen drapery is visible. Level horizon, straight architectural verticals, quiet residential vista outside, no people.
- **Reference Assets:** `images/masters/FG-APT-01_V10_master_bed.jpg`

### View 12: `FG-APT-01_V12_master_bath`
- **Output Path:** `images/masters/FG-APT-01_V12_master_bath.jpg`
- **Prompt:**
  > Photorealistic architectural interior photograph of the Master En-Suite Bathroom in FlowGrid apartment FG-APT-01. Eye-level shot (1.55m) inside the enclosed private bathroom. Center composition features a floating natural white oak vanity cabinet mounted against a feature wall of vertically fluted sage-green architectural ceramic tiles. Honed white quartz countertop with undermount basin and wall-mounted brushed champagne brass mixer tapware. Above hangs a tall pill-shaped mirror with a warm 2700K concealed perimeter LED halo glow. On the right, a walk-in shower with a 10mm frameless fluted glass partition and a brushed brass rain showerhead, with an illuminated recessed tile niche holding luxury toiletries. On the left wall, a wall-hung toilet with concealed cistern and a brushed brass flush plate. Full bathroom enclosed with matte warm greige limestone porcelain wall and floor tiles. Straight architectural verticals, level horizon, no people, no text, no open view to dining room.
- **Reference Assets:** `images/masters/FG-APT-01_V07_dining_basin.jpg`
