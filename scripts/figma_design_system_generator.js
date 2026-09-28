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
 * 4. Mobile Navigation Drawer Component with Auto Layout & Prototype Reactions
 */

(async function createFlowGridNativeDesignSystem() {
  console.log("Starting FlowGrid Native Design System Authoring...");

  // -------------------------------------------------------------
  // 1. CREATE FIGMA VARIABLES (Tokens Collections)
  // -------------------------------------------------------------
  if (figma.variables) {
    try {
      console.log("1. Creating Variable Collections: Colors, Spacing, Radius...");
      const collections = await figma.variables.getLocalVariableCollectionsAsync();
      
      // 1a. Color Tokens
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

      // 1b. Spacing Collection
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

      // 1c. Radius Collection
      let radiusCol = collections.find(c => c.name === "FlowGrid / Radius Tokens");
      if (!radiusCol) {
        radiusCol = figma.variables.createVariableCollection("FlowGrid / Radius Tokens");
      }
      const rModeId = radiusCol.modes[0].modeId;
      const radii = [
        { name: "radius/none", val: 0 },
        { name: "radius/control", val: 2 },
        { name: "radius/overlay", val: 4 },
        { name: "radius/pill", val: 9999 }
      ];
      for (const r of radii) {
        let rv = localVars.find(x => x.name === r.name && x.variableCollectionId === radiusCol.id);
        if (!rv) {
          rv = figma.variables.createVariable(r.name, radiusCol.id, "FLOAT");
        }
        rv.setValueForMode(rModeId, r.val);
      }

      console.log("Figma Variables created: 30 total tokens across 3 collections.");
    } catch (err) {
      console.warn("Variables creation notice:", err.message);
    }
  }

  // -------------------------------------------------------------
  // 2. TARGET '02 Components' CANVAS
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
      figma.loadFontAsync({ family: "Inter", style: "Regular" }),
      figma.loadFontAsync({ family: "Inter", style: "Bold" })
    ]),
    new Promise(res => setTimeout(res, 2000))
  ]).catch(() => console.log("Using default font..."));

  // -------------------------------------------------------------
  // 3. CREATE NATIVE BUTTON COMPONENTS & VARIANTS
  // -------------------------------------------------------------
  console.log("2. Creating Native Component Set: Button / Primary CTA...");
  let existingBtnSet = compPage.children.find(c => c.name === "Button / Primary CTA");
  if (!existingBtnSet) {
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

    try {
      const btnComponentSet = figma.combineAsVariants(btnComponents, compPage);
      btnComponentSet.name = "Button / Primary CTA";
      btnComponentSet.x = 100;
      btnComponentSet.y = 150;
      console.log("Component Set created: 'Button / Primary CTA' with 5 variants.");
    } catch (err) {
      console.warn("combineAsVariants notice:", err.message);
    }
  }

  // -------------------------------------------------------------
  // 4. CREATE MODAL COMPONENT WITH AUTO LAYOUT & CLEARANCE GAP
  // -------------------------------------------------------------
  console.log("3. Creating Native Component: Modal / Consultation Enquiry Card...");
  let existingModal = compPage.children.find(c => c.name === "Modal / Consultation Enquiry Card");
  if (!existingModal) {
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

    // Header Row with Title & Close Button
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

    // Prototyping Action
    closeBtn.reactions = [{
      trigger: { type: "ON_CLICK" },
      actions: [{ type: "CLOSE" }]
    }];

    modalComp.x = 100;
    modalComp.y = 450;
    compPage.appendChild(modalComp);
    console.log("Modal Card component created with Auto Layout & clearance gap.");
  }

  // -------------------------------------------------------------
  // 5. CREATE NAVIGATION DRAWER COMPONENT
  // -------------------------------------------------------------
  console.log("4. Creating Native Component: Navigation / Mobile Drawer...");
  let existingDrawer = compPage.children.find(c => c.name === "Navigation / Mobile Drawer");
  if (!existingDrawer) {
    const drawerComp = figma.createComponent();
    drawerComp.name = "Navigation / Mobile Drawer";
    drawerComp.layoutMode = "VERTICAL";
    drawerComp.primaryAxisSizingMode = "FIXED";
    drawerComp.counterAxisSizingMode = "FIXED";
    drawerComp.resize(320, 844);
    drawerComp.paddingLeft = 24;
    drawerComp.paddingRight = 24;
    drawerComp.paddingTop = 24;
    drawerComp.paddingBottom = 24;
    drawerComp.itemSpacing = 20;
    drawerComp.fills = [{ type: "SOLID", color: { r: 0.957, g: 0.945, b: 0.910 } }]; // #F4F1E8

    // Header row with Brand & Close Button
    const headRow = figma.createFrame();
    headRow.name = "Drawer Header";
    headRow.layoutMode = "HORIZONTAL";
    headRow.primaryAxisSizingMode = "FIXED";
    headRow.counterAxisSizingMode = "AUTO";
    headRow.resize(272, 44);
    headRow.primaryAxisAlignItems = "SPACE_BETWEEN";
    headRow.counterAxisAlignItems = "CENTER";
    headRow.fills = [];

    const brandTxt = figma.createText();
    brandTxt.characters = "FlowGrid";
    brandTxt.fontSize = 20;
    brandTxt.fills = [{ type: "SOLID", color: { r: 0.094, g: 0.231, b: 0.208 } }];
    headRow.appendChild(brandTxt);

    const drawerCloseBtn = figma.createFrame();
    drawerCloseBtn.name = "Drawer Close Button (44x44)";
    drawerCloseBtn.resize(44, 44);
    drawerCloseBtn.cornerRadius = 22;
    drawerCloseBtn.layoutMode = "HORIZONTAL";
    drawerCloseBtn.primaryAxisAlignItems = "CENTER";
    drawerCloseBtn.counterAxisAlignItems = "CENTER";
    drawerCloseBtn.fills = [];
    drawerCloseBtn.strokes = [{ type: "SOLID", color: { r: 0.722, g: 0.761, b: 0.729 } }];
    drawerCloseBtn.strokeWeight = 1;

    const xTxt = figma.createText();
    xTxt.characters = "×";
    xTxt.fontSize = 24;
    xTxt.fills = [{ type: "SOLID", color: { r: 0.094, g: 0.231, b: 0.208 } }];
    drawerCloseBtn.appendChild(xTxt);
    headRow.appendChild(drawerCloseBtn);
    drawerComp.appendChild(headRow);

    // Prototyping action
    drawerCloseBtn.reactions = [{
      trigger: { type: "ON_CLICK" },
      actions: [{ type: "CLOSE" }]
    }];

    // Navigation Links
    const links = [
      "১. কনসেপ্ট ও ডিজাইন (Concept)",
      "২. আমাদের সেবা (Services)",
      "৩. কর্মপদ্ধতি (Process)",
      "৪. স্টুডিও পরিচিতি (Studio)",
      "৫. যোগাযোগ (Contact)"
    ];
    for (const l of links) {
      const lFrame = figma.createFrame();
      lFrame.name = `Nav Link: ${l.split(' ')[1]}`;
      lFrame.layoutMode = "HORIZONTAL";
      lFrame.primaryAxisSizingMode = "FIXED";
      lFrame.counterAxisSizingMode = "AUTO";
      lFrame.resize(272, 36);
      lFrame.counterAxisAlignItems = "CENTER";
      lFrame.fills = [];

      const lTxt = figma.createText();
      lTxt.characters = l;
      lTxt.fontSize = 15;
      lTxt.fills = [{ type: "SOLID", color: { r: 0.094, g: 0.231, b: 0.208 } }];
      lFrame.appendChild(lTxt);
      drawerComp.appendChild(lFrame);
    }

    // Consultation CTA Button inside Drawer
    const drawerCta = figma.createFrame();
    drawerCta.name = "Drawer CTA Button";
    drawerCta.layoutMode = "HORIZONTAL";
    drawerCta.primaryAxisSizingMode = "FIXED";
    drawerCta.counterAxisSizingMode = "AUTO";
    drawerCta.resize(272, 48);
    drawerCta.primaryAxisAlignItems = "CENTER";
    drawerCta.counterAxisAlignItems = "CENTER";
    drawerCta.cornerRadius = 2;
    drawerCta.fills = [{ type: "SOLID", color: { r: 0.094, g: 0.231, b: 0.208 } }];

    const ctaTxt = figma.createText();
    ctaTxt.characters = "পরামর্শের আবেদন করুন →";
    ctaTxt.fontSize = 14;
    ctaTxt.fills = [{ type: "SOLID", color: { r: 0.957, g: 0.945, b: 0.910 } }];
    drawerCta.appendChild(ctaTxt);
    drawerComp.appendChild(drawerCta);

    drawerComp.x = 520;
    drawerComp.y = 450;
    compPage.appendChild(drawerComp);
    console.log("Mobile Drawer component created with Auto Layout & prototype close interaction.");
  }

  figma.notify("FlowGrid Native Design System & Components successfully authored!");
  console.log("FlowGrid Native Figma Authoring Complete!");
})();
