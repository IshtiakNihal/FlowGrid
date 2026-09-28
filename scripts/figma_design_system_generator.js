/**
 * FlowGrid Design System — Native Figma Authoring Script
 * 
 * Target: Figma Plugin Console / Scripter Plugin / Dev Mode Console
 * File: eMRunQ80brYYvuTWkufV2o
 * 
 * Automates:
 * 1. Design Token Variables (Color, Spacing, Radius Collections)
 * 2. Button Component Set with Auto Layout & Variants (Default, Hover, Focus, Disabled, Submitting)
 * 3. Consultation Form Modal Component with Auto Layout & >=8px Close Button Clearance
 * 4. Interactive Prototype Connections & Interaction Triggers
 */

(async function createFlowGridNativeDesignSystem() {
  console.log("Starting FlowGrid Native Design System Authoring...");

  // -------------------------------------------------------------
  // 1. CREATE FIGMA VARIABLES (Tokens Collection)
  // -------------------------------------------------------------
  if (figma.variables) {
    try {
      console.log("Creating Variables Collection: FlowGrid Tokens...");
      const collections = await figma.variables.getLocalVariableCollectionsAsync();
      let colorCol = collections.find(c => c.name === "FlowGrid / Color Tokens");
      if (!colorCol) {
        colorCol = figma.variables.createVariableCollection("FlowGrid / Color Tokens");
      }
      const modeId = colorCol.modes[0].modeId;

      const colorTokens = [
        { name: "surface/page", r: 0.957, g: 0.945, b: 0.910 },      // #F4F1E8
        { name: "surface/clean", r: 1.0, g: 1.0, b: 1.0 },          // #FFFFFF
        { name: "surface/mist", r: 0.871, g: 0.906, b: 0.886 },      // #DEE7E2
        { name: "text/primary", r: 0.094, g: 0.231, b: 0.208 },      // #183B35
        { name: "text/secondary", r: 0.337, g: 0.392, b: 0.369 },    // #56645E
        { name: "action/primary", r: 0.094, g: 0.231, b: 0.208 },    // #183B35
        { name: "action/hover", r: 0.063, g: 0.169, b: 0.149 },      // #102B26
        { name: "accent/clay", r: 0.537, g: 0.322, b: 0.224 },       // #895239
        { name: "border/decorative", r: 0.722, g: 0.761, b: 0.729 }, // #B8C2BA
        { name: "border/control", r: 0.443, g: 0.506, b: 0.471 },    // #718178
        { name: "focus", r: 0.537, g: 0.322, b: 0.224 },             // #895239
        { name: "status/error", r: 0.608, g: 0.188, b: 0.169 },      // #9B302B
        { name: "status/success", r: 0.141, g: 0.361, b: 0.263 },    // #245C43
        { name: "status/error-bg", r: 0.992, g: 0.949, b: 0.949 },   // #FDF2F2
        { name: "status/success-bg", r: 0.922, g: 0.961, b: 0.941 }  // #EBF5F0
      ];

      const localVars = await figma.variables.getLocalVariablesAsync();
      for (const token of colorTokens) {
        let v = localVars.find(x => x.name === token.name && x.variableCollectionId === colorCol.id);
        if (!v) {
          v = figma.variables.createVariable(token.name, colorCol.id, "COLOR");
        }
        v.setValueForMode(modeId, { r: token.r, g: token.g, b: token.b, a: 1 });
      }

      // Spacing Collection
      let spaceCol = collections.find(c => c.name === "FlowGrid / Spatial Spacing");
      if (!spaceCol) {
        spaceCol = figma.variables.createVariableCollection("FlowGrid / Spatial Spacing");
      }
      const spaceModeId = spaceCol.modes[0].modeId;
      const spacingValues = [4, 8, 12, 16, 24, 32, 48, 64, 80, 96, 128];
      for (const s of spacingValues) {
        let sv = localVars.find(x => x.name === `space/${s}` && x.variableCollectionId === spaceCol.id);
        if (!sv) {
          sv = figma.variables.createVariable(`space/${s}`, spaceCol.id, "FLOAT");
        }
        sv.setValueForMode(spaceModeId, s);
      }

      console.log("Figma Variables created successfully!");
    } catch (err) {
      console.warn("Variables creation notice:", err.message);
    }
  }

  // -------------------------------------------------------------
  // 2. NAVIGATE TO '02 Components' CANVAS
  // -------------------------------------------------------------
  let compPage = figma.root.children.find(p => p.name === "02 Components");
  if (!compPage) {
    compPage = figma.createPage();
    compPage.name = "02 Components";
  }
  figma.currentPage = compPage;

  // Load Fonts
  await Promise.race([
    Promise.all([
      figma.loadFontAsync({ family: "Manrope", style: "Bold" }),
      figma.loadFontAsync({ family: "Manrope", style: "Regular" }),
      figma.loadFontAsync({ family: "Noto Sans Bengali", style: "Bold" }),
      figma.loadFontAsync({ family: "Noto Sans Bengali", style: "Regular" })
    ]),
    new Promise(res => setTimeout(res, 3000))
  ]).catch(() => console.log("Proceeding with available fonts..."));

  // -------------------------------------------------------------
  // 3. CREATE NATIVE BUTTON COMPONENTS & VARIANTS
  // -------------------------------------------------------------
  console.log("Creating Native Component Set: Button / Primary CTA...");

  const states = [
    { name: "Default", bg: { r: 0.094, g: 0.231, b: 0.208 }, text: "পরামর্শের আবেদন করুন →", textColor: { r: 0.957, g: 0.945, b: 0.910 }, border: null },
    { name: "Hover", bg: { r: 0.063, g: 0.169, b: 0.149 }, text: "পরামর্শের আবেদন করুন →", textColor: { r: 1.0, g: 1.0, b: 1.0 }, border: null },
    { name: "Focus", bg: { r: 0.094, g: 0.231, b: 0.208 }, text: "পরামর্শের আবেদন করুন →", textColor: { r: 0.957, g: 0.945, b: 0.910 }, border: { r: 0.537, g: 0.322, b: 0.224 } },
    { name: "Disabled", bg: { r: 0.722, g: 0.761, b: 0.729 }, text: "পরামর্শের আবেদন করুন →", textColor: { r: 0.337, g: 0.392, b: 0.369 }, border: null },
    { name: "Submitting", bg: { r: 0.094, g: 0.231, b: 0.208 }, text: "অনুরোধ পাঠানো হচ্ছে...", textColor: { r: 0.957, g: 0.945, b: 0.910 }, border: null }
  ];

  const btnComponents = [];
  let posX = 100;

  for (const st of states) {
    const comp = figma.createComponent();
    comp.name = `State=${st.name}`;
    comp.layoutMode = "HORIZONTAL";
    comp.primaryAxisSizingMode = "AUTO";
    comp.counterAxisSizingMode = "AUTO";
    comp.primaryAxisAlignItems = "CENTER";
    comp.counterAxisAlignItems = "CENTER";
    comp.paddingLeft = 24;
    comp.paddingRight = 24;
    comp.paddingTop = 14;
    comp.paddingBottom = 14;
    comp.itemSpacing = 8;
    comp.cornerRadius = 2;

    comp.fills = [{ type: "SOLID", color: st.bg }];
    if (st.border) {
      comp.strokes = [{ type: "SOLID", color: st.border }];
      comp.strokeWeight = 2;
    }

    const txt = figma.createText();
    txt.characters = st.text;
    txt.fontSize = 15;
    txt.fills = [{ type: "SOLID", color: st.textColor }];
    comp.appendChild(txt);

    comp.x = posX;
    comp.y = 200;
    posX += 260;
    btnComponents.push(comp);
  }

  // Combine into Component Set
  let btnComponentSet = null;
  try {
    btnComponentSet = figma.combineAsVariants(btnComponents, compPage);
    btnComponentSet.name = "Button / Primary CTA";
    btnComponentSet.x = 100;
    btnComponentSet.y = 150;
    console.log("Component Set created: 'Button / Primary CTA' with 5 variants!");
  } catch (err) {
    console.warn("combineAsVariants notice:", err.message);
  }

  // -------------------------------------------------------------
  // 4. CREATE MODAL COMPONENT WITH AUTO LAYOUT & CLEARANCE GAP
  // -------------------------------------------------------------
  console.log("Creating Native Component: Consultation Modal Card...");
  const modalComp = figma.createComponent();
  modalComp.name = "Modal / Consultation Enquiry Card";
  modalComp.layoutMode = "VERTICAL";
  modalComp.primaryAxisSizingMode = "AUTO";
  modalComp.counterAxisSizingMode = "FIXED";
  modalComp.resize(366, 600);
  modalComp.paddingLeft = 16;
  modalComp.paddingRight = 16;
  modalComp.paddingTop = 24;
  modalComp.paddingBottom = 24;
  modalComp.itemSpacing = 16;
  modalComp.cornerRadius = 4;
  modalComp.fills = [{ type: "SOLID", color: { r: 1.0, g: 1.0, b: 1.0 } }];
  modalComp.strokes = [{ type: "SOLID", color: { r: 0.722, g: 0.761, b: 0.729 } }];
  modalComp.strokeWeight = 1;

  // Header Frame with Title & Close Button
  const headerFrame = figma.createFrame();
  headerFrame.name = "Header Row";
  headerFrame.layoutMode = "HORIZONTAL";
  headerFrame.primaryAxisSizingMode = "FIXED";
  headerFrame.counterAxisSizingMode = "AUTO";
  headerFrame.resize(334, 48);
  headerFrame.primaryAxisAlignItems = "SPACE_BETWEEN";
  headerFrame.counterAxisAlignItems = "CENTER";
  headerFrame.fills = [];

  const titleTxt = figma.createText();
  titleTxt.characters = "পরামর্শের আবেদন করুন";
  titleTxt.fontSize = 20;
  titleTxt.fills = [{ type: "SOLID", color: { r: 0.094, g: 0.231, b: 0.208 } }];
  headerFrame.appendChild(titleTxt);

  const closeBtn = figma.createFrame();
  closeBtn.name = "Close Button (48x48)";
  closeBtn.resize(48, 48);
  closeBtn.cornerRadius = 24;
  closeBtn.layoutMode = "HORIZONTAL";
  closeBtn.primaryAxisAlignItems = "CENTER";
  closeBtn.counterAxisAlignItems = "CENTER";
  closeBtn.fills = [];
  closeBtn.strokes = [{ type: "SOLID", color: { r: 0.722, g: 0.761, b: 0.729 } }];
  closeBtn.strokeWeight = 1;

  const closeTxt = figma.createText();
  closeTxt.characters = "×";
  closeTxt.fontSize = 22;
  closeTxt.fills = [{ type: "SOLID", color: { r: 0.094, g: 0.231, b: 0.208 } }];
  closeBtn.appendChild(closeTxt);
  headerFrame.appendChild(closeBtn);
  modalComp.appendChild(headerFrame);

  // Top Error Summary Banner (with >=8px right clearance gap)
  const errBanner = figma.createFrame();
  errBanner.name = "Error Summary Banner (Gap >= 8px)";
  errBanner.layoutMode = "HORIZONTAL";
  errBanner.primaryAxisSizingMode = "FIXED";
  errBanner.counterAxisSizingMode = "AUTO";
  errBanner.resize(266, 40); // 334 - 68px = 266px width, reserving positive 16px clearance
  errBanner.paddingLeft = 12;
  errBanner.paddingRight = 12;
  errBanner.paddingTop = 8;
  errBanner.paddingBottom = 8;
  errBanner.itemSpacing = 8;
  errBanner.cornerRadius = 2;
  errBanner.fills = [{ type: "SOLID", color: { r: 0.992, g: 0.949, b: 0.949 } }];
  errBanner.strokes = [{ type: "SOLID", color: { r: 0.608, g: 0.188, b: 0.169 } }];
  errBanner.strokeWeight = 1.5;

  const errTxt = figma.createText();
  errTxt.characters = "⚠️ চিহ্নিত ক্ষেত্রগুলো পূরণ করুন";
  errTxt.fontSize = 13;
  errTxt.fills = [{ type: "SOLID", color: { r: 0.608, g: 0.188, b: 0.169 } }];
  errBanner.appendChild(errTxt);
  modalComp.appendChild(errBanner);

  modalComp.x = 100;
  modalComp.y = 450;
  console.log("Modal Card component created with Auto Layout & clearance gap!");

  // -------------------------------------------------------------
  // 5. PROTOTYPE INTERACTION CONNECTIONS
  // -------------------------------------------------------------
  console.log("Configuring Prototype Default Interactions...");
  try {
    closeBtn.reactions = [
      {
        trigger: { type: "ON_CLICK" },
        actions: [{ type: "CLOSE" }]
      }
    ];
    console.log("Prototyping noodle added to Close Button (ON_CLICK -> CLOSE)!");
  } catch (err) {
    console.warn("Prototyping reactions notice:", err.message);
  }

  figma.notify("FlowGrid Native Design System & Components successfully authored!");
  console.log("FlowGrid Native Figma Authoring Complete!");
})();
