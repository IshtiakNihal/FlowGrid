// FlowGrid: Complete English Homepages and Bengali Archive
// Resolves FG-05:
// 1. English Homepage — 1440px Desktop (18:1068)
// 2. English Homepage — 390px Mobile (18:1389)
// 3. Bengali Archive — 1440px Desktop (18:1587)

(async () => {
    console.log("Repairing English Homepages and Bengali Archive...");

    // 1. Ensure fonts
    const fonts = [
        { family: "Noto Sans Bengali", style: "Regular" },
        { family: "Noto Sans Bengali", style: "Bold" },
        { family: "Bodoni Moda", style: "Regular" },
        { family: "Bodoni Moda", style: "Bold" },
        { family: "Inter", style: "Regular" },
        { family: "Inter", style: "Bold" }
    ];
    for (const f of fonts) {
        try { await figma.loadFontAsync(f); } catch (e) {}
    }

    // 2. Map tokens & styles
    const cols = figma.variables.getLocalVariableCollections();
    const varMap = {};
    for (const c of cols) {
        for (const vid of c.variableIds) {
            const v = figma.variables.getVariableById(vid);
            if (v) varMap[v.name] = v;
        }
    }
    const styles = figma.getLocalTextStyles();
    const styleMap = {};
    for (const s of styles) styleMap[s.name] = s;

    function bindFill(node, varName) {
        const v = varMap[varName];
        if (!v) return;
        let p = { type: 'SOLID', color: { r: 1, g: 1, b: 1 } };
        p = figma.variables.setBoundVariableForPaint(p, 'color', v);
        node.fills = [p];
    }

    function bindStroke(node, varName, weight = 1) {
        const v = varMap[varName];
        if (!v) return;
        let p = { type: 'SOLID', color: { r: 0, g: 0, b: 0 } };
        p = figma.variables.setBoundVariableForPaint(p, 'color', v);
        node.strokes = [p];
        node.strokeWeight = weight;
    }

    function bindCornerRadius(node, varName) {
        const v = varMap[varName];
        if (!v) return;
        node.setBoundVariable('cornerRadius', v);
    }

    function applyTextStyle(node, styleName, fallbackFamily = "Inter", fallbackSize = 14) {
        const s = styleMap[styleName];
        if (s) {
            node.textStyleId = s.id;
        } else {
            node.fontName = { family: fallbackFamily, style: "Regular" };
            node.fontSize = fallbackSize;
        }
    }

    function createStyledText(text, styleName, fillVar, options = {}) {
        const t = figma.createText();
        applyTextStyle(t, styleName, options.family || "Inter", options.size || 14);
        t.characters = text;
        if (fillVar) bindFill(t, fillVar);
        if (options.align) t.textAlignHorizontal = options.align;
        if (options.hug) {
            t.textAutoResize = "WIDTH_AND_HEIGHT";
        } else {
            t.layoutAlign = "STRETCH";
            t.textAutoResize = "HEIGHT";
        }
        return t;
    }

    function createImageRect(imageHash, w, h, radiusVar = 'radius/none') {
        const rect = figma.createRectangle();
        rect.name = "Architectural Photo";
        rect.resize(w, h);
        rect.fills = [{
            type: 'IMAGE',
            scaleMode: 'FILL',
            imageHash: imageHash
        }];
        if (radiusVar && varMap[radiusVar]) {
            bindCornerRadius(rect, radiusVar);
        }
        return rect;
    }

    // Hashes
    const imgOverviewHash = "9e6c1225ff649790c89d5a011ce12a7bb25d9e9c";
    const imgAltHash = "a50d4991b590cc05dbb7cd34750d69293c60594f";
    const imgJoineryHash = "dcca525e8ca800bc1e178890630b346c99b2a149";

    const compPage = figma.root.children.find(p => p.name === "02 Components");
    const defaultBtnComp = compPage.children.find(c => c.name === "Button / Primary CTA")?.children[0];

    function getBtn(label) {
        const inst = defaultBtnComp.createInstance();
        if (label) {
            const txt = inst.children.find(c => c.type === "TEXT");
            if (txt) txt.characters = label;
        }
        return inst;
    }

    // =========================================================================
    // 1. REPAIR ENGLISH HOMEPAGE — 1440px DESKTOP (Node 18:1068)
    // =========================================================================
    console.log("Rebuilding English Homepage 1440px Desktop (18:1068)...");
    const homeEnDt = figma.getNodeById("18:1068");
    homeEnDt.resize(1440, 100);
    homeEnDt.layoutMode = "VERTICAL";
    homeEnDt.primaryAxisSizingMode = "AUTO";
    homeEnDt.counterAxisSizingMode = "FIXED";
    bindFill(homeEnDt, 'surface/page');

    while (homeEnDt.children.length > 0) {
        homeEnDt.children[0].remove();
    }

    // Header
    const hEnDt = figma.createFrame();
    hEnDt.name = "Header / Global Navigation";
    hEnDt.layoutMode = "HORIZONTAL";
    hEnDt.primaryAxisAlignItems = "SPACE_BETWEEN";
    hEnDt.counterAxisAlignItems = "CENTER";
    hEnDt.paddingLeft = 48;
    hEnDt.paddingRight = 48;
    hEnDt.resize(1440, 88);
    bindFill(hEnDt, 'surface/page');
    bindStroke(hEnDt, 'border/decorative', 1);
    homeEnDt.appendChild(hEnDt);
    hEnDt.layoutAlign = "STRETCH";
    try { hEnDt.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const brandEnDt = figma.createText();
    applyTextStyle(brandEnDt, "Typography / Latin / Brand Display", "Bodoni Moda", 28);
    brandEnDt.characters = "FlowGrid";
    brandEnDt.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(brandEnDt, 'text/primary');
    hEnDt.appendChild(brandEnDt);

    const navLinksEnDt = figma.createFrame();
    navLinksEnDt.name = "Nav Links";
    navLinksEnDt.layoutMode = "HORIZONTAL";
    navLinksEnDt.counterAxisAlignItems = "CENTER";
    navLinksEnDt.itemSpacing = 32;
    navLinksEnDt.fills = [];
    const enLinks = ["Archive", "Services", "Process", "Studio", "Contact"];
    enLinks.forEach(name => {
        const lt = figma.createText();
        applyTextStyle(lt, "Typography / Latin / Body Regular", "Inter", 14);
        lt.characters = name;
        lt.textAutoResize = "WIDTH_AND_HEIGHT";
        bindFill(lt, 'text/primary');
        navLinksEnDt.appendChild(lt);
    });
    hEnDt.appendChild(navLinksEnDt);

    const navActsEnDt = figma.createFrame();
    navActsEnDt.name = "Nav Actions";
    navActsEnDt.layoutMode = "HORIZONTAL";
    navActsEnDt.counterAxisAlignItems = "CENTER";
    navActsEnDt.itemSpacing = 16;
    navActsEnDt.fills = [];

    const langPillEn = figma.createFrame();
    langPillEn.name = "Language Pill";
    langPillEn.layoutMode = "HORIZONTAL";
    langPillEn.paddingLeft = 14;
    langPillEn.paddingRight = 14;
    langPillEn.paddingTop = 6;
    langPillEn.paddingBottom = 6;
    bindFill(langPillEn, 'surface/mist');
    bindCornerRadius(langPillEn, 'radius/pill');
    const langTxtEn = figma.createText();
    applyTextStyle(langTxtEn, "Typography / Bengali / Body Small", "Noto Sans Bengali", 12);
    langTxtEn.characters = "বাংলা";
    langTxtEn.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(langTxtEn, 'text/primary');
    langPillEn.appendChild(langTxtEn);
    navActsEnDt.appendChild(langPillEn);

    const ctaHeadEn = getBtn("Start Consultation");
    ctaHeadEn.name = "Header Consultation CTA";
    navActsEnDt.appendChild(ctaHeadEn);
    hEnDt.appendChild(navActsEnDt);

    // Hero Section
    const heroEnSec = figma.createFrame();
    heroEnSec.name = "Section / Hero Architectural Showcase";
    heroEnSec.layoutMode = "VERTICAL";
    heroEnSec.paddingLeft = 48;
    heroEnSec.paddingRight = 48;
    heroEnSec.paddingTop = 64;
    heroEnSec.paddingBottom = 64;
    heroEnSec.itemSpacing = 32;
    bindFill(heroEnSec, 'surface/page');
    homeEnDt.appendChild(heroEnSec);
    heroEnSec.layoutAlign = "STRETCH";
    try { heroEnSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const heroEnBadge = createStyledText("CASE STUDY 01 · DHANMONDI, DHAKA", "Typography / Latin / Label Bold", 'accent/clay');
    const heroEnTitle = createStyledText("Calm Architectural Interiors for Contemporary Living", "Typography / Latin / Display H1", 'text/primary');
    const heroEnLead = createStyledText(
        "A residential apartment thoughtfully planned around daylight, natural ventilation, and seasoned timber millwork. Engineered specifically for Dhaka's climate and urban rhythm.",
        "Typography / Latin / Body Large",
        'text/secondary'
    );
    heroEnSec.appendChild(heroEnBadge);
    heroEnSec.appendChild(heroEnTitle);
    heroEnSec.appendChild(heroEnLead);

    // Hero Action Buttons
    const heroEnActs = figma.createFrame();
    heroEnActs.name = "Hero Action Buttons";
    heroEnActs.layoutMode = "HORIZONTAL";
    heroEnActs.itemSpacing = 16;
    heroEnActs.fills = [];
    const heroEnCta1 = getBtn("Request Consultation →");
    heroEnActs.appendChild(heroEnCta1);

    const heroEnSecBtn = figma.createFrame();
    heroEnSecBtn.name = "Button / Secondary View Project";
    heroEnSecBtn.layoutMode = "HORIZONTAL";
    heroEnSecBtn.primaryAxisAlignItems = "CENTER";
    heroEnSecBtn.counterAxisAlignItems = "CENTER";
    heroEnSecBtn.paddingLeft = 24;
    heroEnSecBtn.paddingRight = 24;
    heroEnSecBtn.resize(180, 52);
    bindFill(heroEnSecBtn, 'surface/clean');
    bindStroke(heroEnSecBtn, 'border/control', 1);
    bindCornerRadius(heroEnSecBtn, 'radius/control');
    const secBtnEnTxt = figma.createText();
    applyTextStyle(secBtnEnTxt, "Typography / Latin / Body Regular", "Inter", 14);
    secBtnEnTxt.characters = "View Project Detail";
    secBtnEnTxt.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(secBtnEnTxt, 'text/primary');
    heroEnSecBtn.appendChild(secBtnEnTxt);
    heroEnActs.appendChild(heroEnSecBtn);
    heroEnSec.appendChild(heroEnActs);

    const heroEnImg = createImageRect(imgOverviewHash, 1344, 600, 'radius/media');
    heroEnSec.appendChild(heroEnImg);
    heroEnImg.layoutAlign = "STRETCH";
    try { heroEnImg.layoutSizingHorizontal = "FILL"; } catch(e) {}

    // Narrative & Multi-Angle Section
    const narEnSec = figma.createFrame();
    narEnSec.name = "Section / Spatial Sequence & Material Craft";
    narEnSec.layoutMode = "VERTICAL";
    narEnSec.paddingLeft = 48;
    narEnSec.paddingRight = 48;
    narEnSec.paddingTop = 64;
    narEnSec.paddingBottom = 64;
    narEnSec.itemSpacing = 40;
    bindFill(narEnSec, 'surface/page');
    homeEnDt.appendChild(narEnSec);
    narEnSec.layoutAlign = "STRETCH";
    try { narEnSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const narEnHead = figma.createFrame();
    narEnHead.name = "Narrative Header";
    narEnHead.layoutMode = "VERTICAL";
    narEnHead.itemSpacing = 12;
    narEnHead.fills = [];
    narEnSec.appendChild(narEnHead);
    narEnHead.layoutAlign = "STRETCH";
    try { narEnHead.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const narEnBadge = createStyledText("SPATIAL SEQUENCE & MATERIAL CRAFT", "Typography / Latin / Label Bold", 'accent/clay');
    const narEnTitle = createStyledText("Living Comfort, Daylight & Joinery Precision", "Typography / Latin / Section H2", 'text/primary');
    narEnHead.appendChild(narEnBadge);
    narEnHead.appendChild(narEnTitle);

    // 2-Column Gallery Row
    const galEnRow = figma.createFrame();
    galEnRow.name = "Multi-Angle Visual Grid";
    galEnRow.layoutMode = "HORIZONTAL";
    galEnRow.itemSpacing = 24;
    galEnRow.fills = [];
    narEnSec.appendChild(galEnRow);
    galEnRow.layoutAlign = "STRETCH";
    try { galEnRow.layoutSizingHorizontal = "FILL"; } catch(e) {}
    galEnRow.counterAxisSizingMode = "AUTO";

    // Card 1
    const ec1 = figma.createFrame();
    ec1.name = "Angle 02 / Dining Interaction";
    ec1.layoutMode = "VERTICAL";
    ec1.itemSpacing = 16;
    ec1.paddingLeft = 24;
    ec1.paddingRight = 24;
    ec1.paddingTop = 24;
    ec1.paddingBottom = 24;
    bindFill(ec1, 'surface/clean');
    bindStroke(ec1, 'border/decorative', 1);
    bindCornerRadius(ec1, 'radius/control');
    galEnRow.appendChild(ec1);
    ec1.layoutGrow = 1;
    try { ec1.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const ei1 = createImageRect(imgAltHash, 612, 380, 'radius/control');
    ec1.appendChild(ei1);
    ei1.layoutAlign = "STRETCH";
    try { ei1.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const eCap1 = createStyledText("Open Connection: Dining & Balcony", "Typography / Latin / Card H3", 'text/primary');
    const eDesc1 = createStyledText("Balancing natural daylight, layered reflections, and free-flowing spatial transition.", "Typography / Latin / Body Regular", 'text/secondary');
    ec1.appendChild(eCap1);
    ec1.appendChild(eDesc1);

    // Card 2
    const ec2 = figma.createFrame();
    ec2.name = "Angle 03 / Joinery Detail";
    ec2.layoutMode = "VERTICAL";
    ec2.itemSpacing = 16;
    ec2.paddingLeft = 24;
    ec2.paddingRight = 24;
    ec2.paddingTop = 24;
    ec2.paddingBottom = 24;
    bindFill(ec2, 'surface/clean');
    bindStroke(ec2, 'border/decorative', 1);
    bindCornerRadius(ec2, 'radius/control');
    galEnRow.appendChild(ec2);
    ec2.layoutGrow = 1;
    try { ec2.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const ei2 = createImageRect(imgJoineryHash, 612, 380, 'radius/control');
    ec2.appendChild(ei2);
    ei2.layoutAlign = "STRETCH";
    try { ei2.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const eCap2 = createStyledText("Custom Joinery & Precision Craft", "Typography / Latin / Card H3", 'text/primary');
    const eDesc2 = createStyledText("Combining indigenous timber craftsmanship with clean architectural detailing.", "Typography / Latin / Body Regular", 'text/secondary');
    ec2.appendChild(eCap2);
    ec2.appendChild(eDesc2);

    // 4-Card Specs Matrix
    const specEnRow = figma.createFrame();
    specEnRow.name = "Architectural Specifications Matrix";
    specEnRow.layoutMode = "HORIZONTAL";
    specEnRow.itemSpacing = 20;
    specEnRow.fills = [];
    narEnSec.appendChild(specEnRow);
    specEnRow.layoutAlign = "STRETCH";
    try { specEnRow.layoutSizingHorizontal = "FILL"; } catch(e) {}
    specEnRow.counterAxisSizingMode = "AUTO";

    const enSpecs = [
        { label: "Materials & Finishes", val: "Seasoned Mahogany, zero-VOC natural polyurethane, and quartz surfaces." },
        { label: "Architectural Lighting", val: "2700K warm architectural LED cove lighting, 95+ CRI index." },
        { label: "Spatial Dimensions", val: "2,400 sq ft residential layout (3 bedrooms + dedicated studio)." },
        { label: "Design Philosophy", val: "Biophilic balance and climate-responsive contextual materiality." }
    ];

    enSpecs.forEach(sp => {
        const sc = figma.createFrame();
        sc.name = "Spec: " + sp.label;
        sc.layoutMode = "VERTICAL";
        sc.itemSpacing = 8;
        sc.paddingLeft = 20;
        sc.paddingRight = 20;
        sc.paddingTop = 20;
        sc.paddingBottom = 20;
        bindFill(sc, 'surface/clean');
        bindStroke(sc, 'border/decorative', 1);
        bindCornerRadius(sc, 'radius/control');
        specEnRow.appendChild(sc);
        sc.layoutGrow = 1;
        try { sc.layoutSizingHorizontal = "FILL"; } catch(e) {}

        const sTitle = createStyledText(sp.label, "Typography / Latin / Label Bold", 'accent/clay');
        const sVal = createStyledText(sp.val, "Typography / Latin / Body Small", 'text/primary');
        sc.appendChild(sTitle);
        sc.appendChild(sVal);
    });

    // Studio Services Section
    const svcEnSec = figma.createFrame();
    svcEnSec.name = "Section / Studio Services & Practice";
    svcEnSec.layoutMode = "VERTICAL";
    svcEnSec.paddingLeft = 48;
    svcEnSec.paddingRight = 48;
    svcEnSec.paddingTop = 64;
    svcEnSec.paddingBottom = 64;
    svcEnSec.itemSpacing = 40;
    bindFill(svcEnSec, 'surface/page');
    homeEnDt.appendChild(svcEnSec);
    svcEnSec.layoutAlign = "STRETCH";
    try { svcEnSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const svcEnHead = figma.createFrame();
    svcEnHead.name = "Services Header";
    svcEnHead.layoutMode = "VERTICAL";
    svcEnHead.itemSpacing = 12;
    svcEnHead.fills = [];
    svcEnSec.appendChild(svcEnHead);
    svcEnHead.layoutAlign = "STRETCH";
    try { svcEnHead.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const svcEnBadge = createStyledText("PRACTICE AREAS & SERVICES", "Typography / Latin / Label Bold", 'accent/clay');
    const svcEnTitle = createStyledText("Architectural & Interior Design Disciplines", "Typography / Latin / Section H2", 'text/primary');
    svcEnHead.appendChild(svcEnBadge);
    svcEnHead.appendChild(svcEnTitle);

    const svcEnGrid = figma.createFrame();
    svcEnGrid.name = "Services 3-Column Grid";
    svcEnGrid.layoutMode = "HORIZONTAL";
    svcEnGrid.itemSpacing = 24;
    svcEnGrid.fills = [];
    svcEnSec.appendChild(svcEnGrid);
    svcEnGrid.layoutAlign = "STRETCH";
    try { svcEnGrid.layoutSizingHorizontal = "FILL"; } catch(e) {}
    svcEnGrid.counterAxisSizingMode = "AUTO";

    const enSvcCards = [
        { num: "01", title: "Interior Architecture", desc: "Comprehensive space planning, custom wall partitions, architectural cabinetry, and engineered lighting systems." },
        { num: "02", title: "Custom Millwork & Joinery", desc: "Bespoke floor-to-ceiling cabinetry and durable architectural furniture built with seasoned local hardwoods." },
        { num: "03", title: "Space Planning & BOQ", desc: "Transparent market-rate Bill of Quantities, itemized cost estimations, and full-time site supervision." }
    ];

    enSvcCards.forEach(c => {
        const sc = figma.createFrame();
        sc.name = "Service Card " + c.num;
        sc.layoutMode = "VERTICAL";
        sc.itemSpacing = 16;
        sc.paddingLeft = 32;
        sc.paddingRight = 32;
        sc.paddingTop = 32;
        sc.paddingBottom = 32;
        bindFill(sc, 'surface/clean');
        bindStroke(sc, 'border/decorative', 1);
        bindCornerRadius(sc, 'radius/control');
        svcEnGrid.appendChild(sc);
        sc.layoutGrow = 1;
        try { sc.layoutSizingHorizontal = "FILL"; } catch(e) {}

        const numTxt = createStyledText(c.num, "Typography / Latin / Label Bold", 'accent/clay');
        const titTxt = createStyledText(c.title, "Typography / Latin / Card H3", 'text/primary');
        const descTxt = createStyledText(c.desc, "Typography / Latin / Body Regular", 'text/secondary');
        sc.appendChild(numTxt);
        sc.appendChild(titTxt);
        sc.appendChild(descTxt);
    });

    // Consultation Banner
    const consultEnSec = figma.createFrame();
    consultEnSec.name = "Section / Consultation Practice Banner";
    consultEnSec.layoutMode = "VERTICAL";
    consultEnSec.paddingLeft = 48;
    consultEnSec.paddingRight = 48;
    consultEnSec.paddingTop = 48;
    consultEnSec.paddingBottom = 48;
    bindFill(consultEnSec, 'surface/page');
    homeEnDt.appendChild(consultEnSec);
    consultEnSec.layoutAlign = "STRETCH";
    try { consultEnSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const consultEnCard = figma.createFrame();
    consultEnCard.name = "Consultation Card";
    consultEnCard.layoutMode = "HORIZONTAL";
    consultEnCard.primaryAxisAlignItems = "SPACE_BETWEEN";
    consultEnCard.counterAxisAlignItems = "CENTER";
    consultEnCard.paddingLeft = 48;
    consultEnCard.paddingRight = 48;
    consultEnCard.paddingTop = 40;
    consultEnCard.paddingBottom = 40;
    bindFill(consultEnCard, 'surface/mist');
    bindStroke(consultEnCard, 'border/control', 1);
    bindCornerRadius(consultEnCard, 'radius/modal');
    consultEnSec.appendChild(consultEnCard);
    consultEnCard.layoutAlign = "STRETCH";
    try { consultEnCard.layoutSizingHorizontal = "FILL"; } catch(e) {}
    consultEnCard.counterAxisSizingMode = "AUTO";

    const cEnTextWrap = figma.createFrame();
    cEnTextWrap.name = "CTA Text";
    cEnTextWrap.layoutMode = "VERTICAL";
    cEnTextWrap.itemSpacing = 8;
    cEnTextWrap.fills = [];
    consultEnCard.appendChild(cEnTextWrap);
    cEnTextWrap.layoutGrow = 1;
    try { cEnTextWrap.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const cEnTitle = createStyledText("Ready to articulate your spatial vision?", "Typography / Latin / Card H3", 'text/primary');
    const cEnSub = createStyledText("Engage directly with our principal architects in Banani, Dhaka.", "Typography / Latin / Body Regular", 'text/secondary');
    cEnTextWrap.appendChild(cEnTitle);
    cEnTextWrap.appendChild(cEnSub);

    const cEnBtn = getBtn("Request Consultation →");
    cEnBtn.name = "Consultation Action Button";
    consultEnCard.appendChild(cEnBtn);

    // Footer
    const ftEnDt = figma.createFrame();
    ftEnDt.name = "Footer / Colophon";
    ftEnDt.layoutMode = "HORIZONTAL";
    ftEnDt.primaryAxisAlignItems = "SPACE_BETWEEN";
    ftEnDt.counterAxisAlignItems = "CENTER";
    ftEnDt.paddingLeft = 48;
    ftEnDt.paddingRight = 48;
    ftEnDt.paddingTop = 32;
    ftEnDt.paddingBottom = 32;
    bindFill(ftEnDt, 'text/primary');
    homeEnDt.appendChild(ftEnDt);
    ftEnDt.layoutAlign = "STRETCH";
    try { ftEnDt.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const bEnTxt = figma.createText();
    applyTextStyle(bEnTxt, "Typography / Latin / Brand Display", "Bodoni Moda", 20);
    bEnTxt.characters = "FlowGrid Architectural Studio";
    bEnTxt.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(bEnTxt, 'surface/page');
    ftEnDt.appendChild(bEnTxt);

    const cEnTxt = figma.createText();
    applyTextStyle(cEnTxt, "Typography / Latin / Meta Small", "Inter", 12);
    cEnTxt.characters = "© 2026 FlowGrid Architectural Studio. Banani, Dhaka, Bangladesh. All rights reserved.";
    cEnTxt.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(cEnTxt, 'surface/mist');
    ftEnDt.appendChild(cEnTxt);


    // =========================================================================
    // 2. REPAIR ENGLISH HOMEPAGE — 390px MOBILE (Node 18:1389)
    // =========================================================================
    console.log("Rebuilding English Homepage 390px Mobile (18:1389)...");
    const homeEnMb = figma.getNodeById("18:1389");
    homeEnMb.resize(390, 100);
    homeEnMb.layoutMode = "VERTICAL";
    homeEnMb.primaryAxisSizingMode = "AUTO";
    homeEnMb.counterAxisSizingMode = "FIXED";
    bindFill(homeEnMb, 'surface/page');

    while (homeEnMb.children.length > 0) {
        homeEnMb.children[0].remove();
    }

    // Header
    const hEnMb = figma.createFrame();
    hEnMb.name = "Header / Navigation";
    hEnMb.layoutMode = "HORIZONTAL";
    hEnMb.primaryAxisAlignItems = "SPACE_BETWEEN";
    hEnMb.counterAxisAlignItems = "CENTER";
    hEnMb.resize(390, 64);
    hEnMb.paddingLeft = 16;
    hEnMb.paddingRight = 16;
    bindFill(hEnMb, 'surface/page');
    bindStroke(hEnMb, 'border/decorative', 1);
    homeEnMb.appendChild(hEnMb);
    hEnMb.layoutAlign = "STRETCH";
    try { hEnMb.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const bMbLogoEn = figma.createText();
    applyTextStyle(bMbLogoEn, "Typography / Latin / Brand Display", "Bodoni Moda", 24);
    bMbLogoEn.characters = "FlowGrid";
    bMbLogoEn.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(bMbLogoEn, 'text/primary');
    hEnMb.appendChild(bMbLogoEn);

    const burgerEnMb = figma.createFrame();
    burgerEnMb.name = "Hamburger Button";
    burgerEnMb.resize(48, 48);
    burgerEnMb.layoutMode = "HORIZONTAL";
    burgerEnMb.primaryAxisAlignItems = "CENTER";
    burgerEnMb.counterAxisAlignItems = "CENTER";
    bindFill(burgerEnMb, 'surface/clean');
    bindStroke(burgerEnMb, 'border/control', 1);
    bindCornerRadius(burgerEnMb, 'radius/control');
    const burgerEnTxt = figma.createText();
    burgerEnTxt.fontName = { family: "Inter", style: "Bold" };
    burgerEnTxt.fontSize = 20;
    burgerEnTxt.characters = "☰";
    burgerEnTxt.textAutoResize = "WIDTH_AND_HEIGHT";
    bindFill(burgerEnTxt, 'text/primary');
    burgerEnMb.appendChild(burgerEnTxt);
    hEnMb.appendChild(burgerEnMb);

    // Mobile Hero
    const mbHeroEnSec = figma.createFrame();
    mbHeroEnSec.name = "Section / Hero";
    mbHeroEnSec.layoutMode = "VERTICAL";
    mbHeroEnSec.paddingLeft = 16;
    mbHeroEnSec.paddingRight = 16;
    mbHeroEnSec.paddingTop = 24;
    mbHeroEnSec.paddingBottom = 32;
    mbHeroEnSec.itemSpacing = 20;
    bindFill(mbHeroEnSec, 'surface/page');
    homeEnMb.appendChild(mbHeroEnSec);
    mbHeroEnSec.layoutAlign = "STRETCH";
    try { mbHeroEnSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const mbBadgeEn = createStyledText("CASE STUDY 01 · DHANMONDI, DHAKA", "Typography / Latin / Label Bold", 'accent/clay');
    const mbTitleEn = createStyledText("Calm Architectural Interiors for Contemporary Living", "Typography / Latin / Display H1", 'text/primary');
    const mbLeadEn = createStyledText(
        "A residential apartment thoughtfully planned around daylight, natural ventilation, and seasoned timber millwork.",
        "Typography / Latin / Body Large",
        'text/secondary'
    );
    mbHeroEnSec.appendChild(mbBadgeEn);
    mbHeroEnSec.appendChild(mbTitleEn);
    mbHeroEnSec.appendChild(mbLeadEn);

    const mbHeroEnImg = createImageRect(imgOverviewHash, 358, 220, 'radius/control');
    mbHeroEnSec.appendChild(mbHeroEnImg);
    mbHeroEnImg.layoutAlign = "STRETCH";
    try { mbHeroEnImg.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const mbCtaEn = getBtn("Request Consultation →");
    mbHeroEnSec.appendChild(mbCtaEn);
    mbCtaEn.layoutAlign = "STRETCH";

    // Mobile Narrative & Cards
    const mbNarEnSec = figma.createFrame();
    mbNarEnSec.name = "Section / Spatial Sequence";
    mbNarEnSec.layoutMode = "VERTICAL";
    mbNarEnSec.paddingLeft = 16;
    mbNarEnSec.paddingRight = 16;
    mbNarEnSec.paddingTop = 16;
    mbNarEnSec.paddingBottom = 32;
    mbNarEnSec.itemSpacing = 20;
    bindFill(mbNarEnSec, 'surface/page');
    homeEnMb.appendChild(mbNarEnSec);
    mbNarEnSec.layoutAlign = "STRETCH";
    try { mbNarEnSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const mbNarEnHead = createStyledText("Living Comfort & Spatial Layout", "Typography / Latin / Section H2", 'text/primary');
    mbNarEnSec.appendChild(mbNarEnHead);

    // Card 1
    const mbc1En = figma.createFrame();
    mbc1En.name = "Mobile Card / Dining Connection";
    mbc1En.layoutMode = "VERTICAL";
    mbc1En.itemSpacing = 12;
    mbc1En.paddingLeft = 16;
    mbc1En.paddingRight = 16;
    mbc1En.paddingTop = 16;
    mbc1En.paddingBottom = 20;
    bindFill(mbc1En, 'surface/clean');
    bindStroke(mbc1En, 'border/decorative', 1);
    bindCornerRadius(mbc1En, 'radius/control');
    mbNarEnSec.appendChild(mbc1En);
    mbc1En.layoutAlign = "STRETCH";
    try { mbc1En.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const mbi1En = createImageRect(imgAltHash, 326, 200, 'radius/control');
    mbc1En.appendChild(mbi1En);
    mbi1En.layoutAlign = "STRETCH";
    try { mbi1En.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const mbCap1En = createStyledText("Open Connection: Dining & Balcony", "Typography / Latin / Card H3", 'text/primary');
    const mbDesc1En = createStyledText("Balancing natural daylight, layered reflections, and free-flowing spatial transition.", "Typography / Latin / Body Small", 'text/secondary');
    mbc1En.appendChild(mbCap1En);
    mbc1En.appendChild(mbDesc1En);

    // Card 2
    const mbc2En = figma.createFrame();
    mbc2En.name = "Mobile Card / Joinery Detail";
    mbc2En.layoutMode = "VERTICAL";
    mbc2En.itemSpacing = 12;
    mbc2En.paddingLeft = 16;
    mbc2En.paddingRight = 16;
    mbc2En.paddingTop = 16;
    mbc2En.paddingBottom = 20;
    bindFill(mbc2En, 'surface/clean');
    bindStroke(mbc2En, 'border/decorative', 1);
    bindCornerRadius(mbc2En, 'radius/control');
    mbNarEnSec.appendChild(mbc2En);
    mbc2En.layoutAlign = "STRETCH";
    try { mbc2En.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const mbi2En = createImageRect(imgJoineryHash, 326, 200, 'radius/control');
    mbc2En.appendChild(mbi2En);
    mbi2En.layoutAlign = "STRETCH";
    try { mbi2En.layoutSizingHorizontal = "FILL"; } catch(e) {}
    const mbCap2En = createStyledText("Custom Joinery & Precision Craft", "Typography / Latin / Card H3", 'text/primary');
    const mbDesc2En = createStyledText("Combining indigenous timber craftsmanship with clean architectural detailing.", "Typography / Latin / Body Small", 'text/secondary');
    mbc2En.appendChild(mbCap2En);
    mbc2En.appendChild(mbDesc2En);

    // Mobile Services
    const mbSvcEnSec = figma.createFrame();
    mbSvcEnSec.name = "Section / Studio Services";
    mbSvcEnSec.layoutMode = "VERTICAL";
    mbSvcEnSec.paddingLeft = 16;
    mbSvcEnSec.paddingRight = 16;
    mbSvcEnSec.paddingTop = 16;
    mbSvcEnSec.paddingBottom = 32;
    mbSvcEnSec.itemSpacing = 16;
    bindFill(mbSvcEnSec, 'surface/page');
    homeEnMb.appendChild(mbSvcEnSec);
    mbSvcEnSec.layoutAlign = "STRETCH";
    try { mbSvcEnSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const mbSvcEnHead = createStyledText("Studio Practice Areas", "Typography / Latin / Section H2", 'text/primary');
    mbSvcEnSec.appendChild(mbSvcEnHead);

    enSvcCards.forEach(c => {
        const sc = figma.createFrame();
        sc.name = "Service / " + c.title;
        sc.layoutMode = "VERTICAL";
        sc.itemSpacing = 8;
        sc.paddingLeft = 20;
        sc.paddingRight = 20;
        sc.paddingTop = 20;
        sc.paddingBottom = 20;
        bindFill(sc, 'surface/clean');
        bindStroke(sc, 'border/decorative', 1);
        bindCornerRadius(sc, 'radius/control');
        mbSvcEnSec.appendChild(sc);
        sc.layoutAlign = "STRETCH";
        try { sc.layoutSizingHorizontal = "FILL"; } catch(e) {}

        const numTxt = createStyledText(c.num, "Typography / Latin / Label Bold", 'accent/clay');
        const titTxt = createStyledText(c.title, "Typography / Latin / Card H3", 'text/primary');
        const descTxt = createStyledText(c.desc, "Typography / Latin / Body Small", 'text/secondary');
        sc.appendChild(numTxt);
        sc.appendChild(titTxt);
        sc.appendChild(descTxt);
    });

    // Mobile Footer
    const mbFtEn = figma.createFrame();
    mbFtEn.name = "Footer / Colophon";
    mbFtEn.layoutMode = "VERTICAL";
    mbFtEn.paddingLeft = 16;
    mbFtEn.paddingRight = 16;
    mbFtEn.paddingTop = 24;
    mbFtEn.paddingBottom = 24;
    mbFtEn.itemSpacing = 8;
    bindFill(mbFtEn, 'text/primary');
    homeEnMb.appendChild(mbFtEn);
    mbFtEn.layoutAlign = "STRETCH";
    try { mbFtEn.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const mbFtEnTitle = createStyledText("FlowGrid Architectural Studio", "Typography / Latin / Card H3", 'surface/page');
    const mbFtEnCopy = createStyledText("© 2026 FlowGrid Architectural Studio. Banani, Dhaka, Bangladesh.", "Typography / Latin / Body Small", 'surface/mist');
    mbFtEn.appendChild(mbFtEnTitle);
    mbFtEn.appendChild(mbFtEnCopy);


    // =========================================================================
    // 3. REPAIR BENGALI ARCHIVE — 1440px DESKTOP (Node 18:1587)
    // =========================================================================
    console.log("Rebuilding Bengali Concept Archive 1440px Desktop (18:1587)...");
    const arcBnDt = figma.getNodeById("18:1587");
    arcBnDt.resize(1440, 100);
    arcBnDt.layoutMode = "VERTICAL";
    arcBnDt.primaryAxisSizingMode = "AUTO";
    arcBnDt.counterAxisSizingMode = "FIXED";
    bindFill(arcBnDt, 'surface/page');

    while (arcBnDt.children.length > 0) {
        arcBnDt.children[0].remove();
    }

    // Header
    const hArc = hEnDt.clone();
    // Swap lang text back to EN
    const lPill = hArc.findOne(c => c.name === "Language Pill");
    if (lPill) {
        const lt = lPill.children[0];
        if (lt) lt.characters = "EN";
    }
    const ctaArc = hArc.findOne(c => c.name === "Header Consultation CTA");
    if (ctaArc) {
        const ct = ctaArc.findOne(c => c.type === "TEXT");
        if (ct) ct.characters = "পরামর্শ শুরু করুন";
    }
    // Rename links to Bengali
    const nLinks = hArc.findOne(c => c.name === "Nav Links");
    if (nLinks) {
        const bnNav = ["ধারণা সংগ্রহ", "সেবাসমূহ", "পদ্ধতি", "স্টুডিও", "যোগাযোগ"];
        nLinks.children.forEach((c, idx) => {
            if (c.type === "TEXT" && bnNav[idx]) c.characters = bnNav[idx];
        });
    }
    arcBnDt.appendChild(hArc);
    hArc.layoutAlign = "STRETCH";
    try { hArc.layoutSizingHorizontal = "FILL"; } catch(e) {}

    // Archive Hero Header
    const arcHero = figma.createFrame();
    arcHero.name = "Section / Archive Hero";
    arcHero.layoutMode = "VERTICAL";
    arcHero.paddingLeft = 48;
    arcHero.paddingRight = 48;
    arcHero.paddingTop = 64;
    arcHero.paddingBottom = 48;
    arcHero.itemSpacing = 24;
    bindFill(arcHero, 'surface/page');
    arcBnDt.appendChild(arcHero);
    arcHero.layoutAlign = "STRETCH";
    try { arcHero.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const arcBadge = createStyledText("ধারণা সংগ্রহ · ARCHITECTURAL ARCHIVE", "Typography / Bengali / Label Bold", 'accent/clay');
    const arcTitle = createStyledText("স্থায়িত্ব, আলো ও কাঠের স্থাপত্য সমীক্ষা", "Typography / Bengali / Display H1", 'text/primary');
    const arcDesc = createStyledText(
        "ঢাকার পরিবর্তিত আবহাওয়া ও নাগরিক চাহিদার সাথে সঙ্গতি রেখে আমাদের স্টুডিওর নির্বাচিত আবাসিক ও বাণিজ্যিক প্রকল্পের একটি সুবিন্যস্ত স্থানিক দলিল।",
        "Typography / Bengali / Body Large",
        'text/secondary'
    );
    arcHero.appendChild(arcBadge);
    arcHero.appendChild(arcTitle);
    arcHero.appendChild(arcDesc);

    // Filter Chips Row
    const filterRow = figma.createFrame();
    filterRow.name = "Filter Tabs Row";
    filterRow.layoutMode = "HORIZONTAL";
    filterRow.itemSpacing = 12;
    filterRow.fills = [];
    arcHero.appendChild(filterRow);
    filterRow.layoutAlign = "STRETCH";
    try { filterRow.layoutSizingHorizontal = "FILL"; } catch(e) {}
    filterRow.counterAxisSizingMode = "AUTO";

    const filterTabs = [
        { name: "সকল প্রকল্প (০৪)", active: true },
        { name: "আবাসিক ইন্টেরিয়র", active: false },
        { name: "বাণিজ্যিক ও স্টুডিও", active: false },
        { name: "কাস্টম মিলওয়ার্ক", active: false },
        { name: "বায়োফিলিক ব্যালেন্স", active: false }
    ];

    filterTabs.forEach(t => {
        const tab = figma.createFrame();
        tab.name = "Tab / " + t.name;
        tab.layoutMode = "HORIZONTAL";
        tab.primaryAxisAlignItems = "CENTER";
        tab.counterAxisAlignItems = "CENTER";
        tab.paddingLeft = 18;
        tab.paddingRight = 18;
        tab.paddingTop = 10;
        tab.paddingBottom = 10;
        if (t.active) {
            bindFill(tab, 'text/primary');
            bindCornerRadius(tab, 'radius/pill');
        } else {
            bindFill(tab, 'surface/clean');
            bindStroke(tab, 'border/control', 1);
            bindCornerRadius(tab, 'radius/pill');
        }
        const tt = figma.createText();
        applyTextStyle(tt, "Typography / Bengali / Body Small", "Noto Sans Bengali", 13);
        tt.characters = t.name;
        tt.textAutoResize = "WIDTH_AND_HEIGHT";
        bindFill(tt, t.active ? 'surface/page' : 'text/primary');
        tab.appendChild(tt);
        filterRow.appendChild(tab);
    });

    // Archive Projects 2x2 Grid (4 full cards)
    const arcGridSec = figma.createFrame();
    arcGridSec.name = "Section / Archive Project Grid";
    arcGridSec.layoutMode = "VERTICAL";
    arcGridSec.paddingLeft = 48;
    arcGridSec.paddingRight = 48;
    arcGridSec.paddingTop = 16;
    arcGridSec.paddingBottom = 64;
    arcGridSec.itemSpacing = 32;
    bindFill(arcGridSec, 'surface/page');
    arcBnDt.appendChild(arcGridSec);
    arcGridSec.layoutAlign = "STRETCH";
    try { arcGridSec.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const projectCards = [
        {
            num: "প্রকল্প ০১ · ধানমন্ডি",
            title: "ধানমন্ডি রেসিডেনশিয়াল অ্যাপার্টমেন্ট: প্রাকৃতিক আলো ও কাঠের পরিশীলিত বিন্যাস",
            desc: "২,৪০০ বর্গফুটের আবাসিক স্পেস যেখানে মেহগনি ও সেগুন কাঠের মিলওয়ার্কের মাধ্যমে আলো ও বায়ুর অবাধ সঞ্চালন নিশ্চিত করা হয়েছে।",
            imgHash: imgOverviewHash,
            specs: "আবাসিক · ৩ বেডরুম · ২০২৬"
        },
        {
            num: "প্রকল্প ০২ · গুলশান",
            title: "গুলশান পেন্টহাউস: খোলামেলা স্থানিক সংযোগ ও টেরেস গার্ডেন",
            desc: "উন্মুক্ত লিভিং-ডাইনিং বিন্যাস যা সরাসরি সবুজ ব্যালকনির সাথে যুক্ত। ন্যূনতম দেয়াল বিভাজন ও কাস্টম কাঠের শেলফিং।",
            imgHash: imgAltHash,
            specs: "আবাসিক পেন্টহাউস · ৪ বেডরুম · ২০২৫"
        },
        {
            num: "প্রকল্প ০৩ · বনানী",
            title: "বনানী ক্রিয়েটিভ স্টুডিও: আর্কিটেকচারাল জয়েনারি ও অ্যাকোস্টিক ব্যালেন্স",
            desc: "কাজের পরিবেশের জন্য নিখুঁত আলো, শব্দ নিয়ন্ত্রণ এবং টেকসই দেশীয় কাঠের স্টোরেজ ডিজাইনের মেলবন্ধন।",
            imgHash: imgJoineryHash,
            specs: "বাণিজ্যিক স্টুডিও · ১,৮০০ বর্গফুট · ২০২৬"
        },
        {
            num: "প্রকল্প ০৪ · বারিধারা",
            title: "বারিধারা গার্ডেন রেসিডেন্স: বায়োফিলিক আলো ও পরিবেশবান্ধব উপাদান",
            desc: "সিজনড কাঠের ক্যাবিনেটরি, ইনডোর প্ল্যান্ট ইন্টারঅ্যাকশন এবং জিরো-VOC সারফেস ফিনিশের অনন্য সমন্বয়।",
            imgHash: imgOverviewHash,
            specs: "আবাসিক ভিলা · ৩,২০০ বর্গফুট · ২০২৫"
        }
    ];

    // Row 1 (Cards 1 & 2)
    const row1 = figma.createFrame();
    row1.name = "Archive Row 1";
    row1.layoutMode = "HORIZONTAL";
    row1.itemSpacing = 24;
    row1.fills = [];
    arcGridSec.appendChild(row1);
    row1.layoutAlign = "STRETCH";
    try { row1.layoutSizingHorizontal = "FILL"; } catch(e) {}
    row1.counterAxisSizingMode = "AUTO";

    // Row 2 (Cards 3 & 4)
    const row2 = figma.createFrame();
    row2.name = "Archive Row 2";
    row2.layoutMode = "HORIZONTAL";
    row2.itemSpacing = 24;
    row2.fills = [];
    arcGridSec.appendChild(row2);
    row2.layoutAlign = "STRETCH";
    try { row2.layoutSizingHorizontal = "FILL"; } catch(e) {}
    row2.counterAxisSizingMode = "AUTO";

    projectCards.forEach((p, idx) => {
        const targetRow = idx < 2 ? row1 : row2;
        const pc = figma.createFrame();
        pc.name = "Card / " + p.num;
        pc.layoutMode = "VERTICAL";
        pc.itemSpacing = 16;
        pc.paddingLeft = 24;
        pc.paddingRight = 24;
        pc.paddingTop = 24;
        pc.paddingBottom = 24;
        bindFill(pc, 'surface/clean');
        bindStroke(pc, 'border/decorative', 1);
        bindCornerRadius(pc, 'radius/control');
        targetRow.appendChild(pc);
        pc.layoutGrow = 1;
        try { pc.layoutSizingHorizontal = "FILL"; } catch(e) {}

        const pImg = createImageRect(p.imgHash, 612, 360, 'radius/control');
        pc.appendChild(pImg);
        pImg.layoutAlign = "STRETCH";
        try { pImg.layoutSizingHorizontal = "FILL"; } catch(e) {}

        const pBadge = createStyledText(p.num, "Typography / Bengali / Label Bold", 'accent/clay');
        const pTitle = createStyledText(p.title, "Typography / Bengali / Card H3", 'text/primary');
        const pDesc = createStyledText(p.desc, "Typography / Bengali / Body Regular", 'text/secondary');
        const pSpec = createStyledText(p.specs, "Typography / Bengali / Body Small", 'accent/clay');
        pc.appendChild(pBadge);
        pc.appendChild(pTitle);
        pc.appendChild(pDesc);
        pc.appendChild(pSpec);

        const pBtn = getBtn("প্রজেক্ট বিস্তারিত দেখুন →");
        pBtn.layoutAlign = "STRETCH";
        pc.appendChild(pBtn);
    });

    // Archive CTA & Footer
    const arcCta = consultEnSec.clone();
    arcBnDt.appendChild(arcCta);
    arcCta.layoutAlign = "STRETCH";
    try { arcCta.layoutSizingHorizontal = "FILL"; } catch(e) {}

    const arcFt = ftEnDt.clone();
    arcBnDt.appendChild(arcFt);
    arcFt.layoutAlign = "STRETCH";
    try { arcFt.layoutSizingHorizontal = "FILL"; } catch(e) {}

    console.log("Templates rebuilt successfully!");
    return {
        englishDesktop: { id: homeEnDt.id, w: homeEnDt.width, h: homeEnDt.height, children: homeEnDt.children.length },
        englishMobile: { id: homeEnMb.id, w: homeEnMb.width, h: homeEnMb.height, children: homeEnMb.children.length },
        bengaliArchive: { id: arcBnDt.id, w: arcBnDt.width, h: arcBnDt.height, children: arcBnDt.children.length }
    };
})()
