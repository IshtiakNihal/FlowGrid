// Rebuild Consultation Enquiry Modal Master and All 4 Overlays
// Resolves FG-06:
// 1. Master Component: 10:43 on "02 Components"
// 2. Desktop BN: 18:2031 on "03 Desktop — BN"
// 3. Mobile BN: 18:2080 on "04 Mobile — BN"
// 4. Desktop EN: 18:2149 on "05 English"
// 5. Mobile EN: 18:2198 on "05 English"

(async () => {
    console.log("Repairing Consultation Form Modal Master and Overlays...");

    // Fonts
    await figma.loadFontAsync({ family: "Noto Sans Bengali", style: "Regular" });
    await figma.loadFontAsync({ family: "Noto Sans Bengali", style: "Bold" });
    await figma.loadFontAsync({ family: "Inter", style: "Regular" });
    await figma.loadFontAsync({ family: "Inter", style: "Bold" });

    // Variables & Styles
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

    const textFieldSet = figma.getNodeById("21:2599");
    const defaultTextComp = textFieldSet.children.find(c => c.name.includes("Default")) || textFieldSet.children[0];

    const compPage = figma.root.children.find(p => p.name === "02 Components");
    const defaultBtnComp = compPage.children.find(c => c.name === "Button / Primary CTA")?.children[0];

    function createFormField(labelText, placeholderText) {
        const inst = defaultTextComp.createInstance();
        inst.name = "Field / " + labelText.split("(")[0].replace("*", "").trim();
        inst.layoutAlign = "STRETCH";

        const lbl = inst.children.find(c => c.name === "Field Label");
        if (lbl) {
            lbl.characters = labelText;
            lbl.textAutoResize = "HEIGHT";
            lbl.layoutAlign = "STRETCH";
        }
        const box = inst.children.find(c => c.name === "Input Container");
        if (box) {
            box.layoutAlign = "STRETCH";
            const txt = box.children.find(c => c.name === "Input Text");
            if (txt) {
                txt.characters = placeholderText;
                txt.textAutoResize = "WIDTH_AND_HEIGHT";
            }
        }
        return inst;
    }

    function populateModalContent(modalFrame, lang = "BN", isMobile = false) {
        modalFrame.layoutMode = "VERTICAL";
        modalFrame.primaryAxisSizingMode = "AUTO";
        modalFrame.counterAxisSizingMode = "FIXED";
        const pad = isMobile ? 20 : 32;
        modalFrame.paddingLeft = pad;
        modalFrame.paddingRight = pad;
        modalFrame.paddingTop = pad;
        modalFrame.paddingBottom = pad;
        modalFrame.itemSpacing = 16;
        bindFill(modalFrame, 'surface/page');
        bindStroke(modalFrame, 'border/decorative', 1);
        bindCornerRadius(modalFrame, 'radius/modal');

        // Clear existing children
        while (modalFrame.children.length > 0) {
            modalFrame.children[0].remove();
        }

        // 1. Header Bar (Space Between, Title left, 40x40 Close Button right)
        const header = figma.createFrame();
        header.name = "Modal Header Bar";
        header.layoutMode = "HORIZONTAL";
        header.primaryAxisAlignItems = "SPACE_BETWEEN";
        header.counterAxisAlignItems = "CENTER";
        header.fills = [];
        modalFrame.appendChild(header);
        header.layoutAlign = "STRETCH";
        try { header.layoutSizingHorizontal = "FILL"; } catch(e) {}
        header.counterAxisSizingMode = "AUTO";

        const titleTxt = figma.createText();
        titleTxt.name = "Modal Title";
        titleTxt.textStyleId = styleMap[lang === "BN" ? "Typography / Bengali / Section H2" : "Typography / Latin / Card H3"]?.id;
        titleTxt.characters = lang === "BN" ? "স্থানিক পরামর্শের সময়সূচি" : "Schedule Consultation";
        titleTxt.textAutoResize = "HEIGHT";
        bindFill(titleTxt, 'text/primary');
        header.appendChild(titleTxt);
        titleTxt.layoutGrow = 1;

        // Close Button (40x40 touch target with 16px X)
        const closeBtn = figma.createFrame();
        closeBtn.name = "Close Button (X)";
        closeBtn.layoutMode = "HORIZONTAL";
        closeBtn.primaryAxisAlignItems = "CENTER";
        closeBtn.counterAxisAlignItems = "CENTER";
        closeBtn.resize(40, 40);
        bindFill(closeBtn, 'surface/clean');
        bindStroke(closeBtn, 'border/control', 1);
        bindCornerRadius(closeBtn, 'radius/pill');

        const xTxt = figma.createText();
        xTxt.fontName = { family: "Inter", style: "Regular" };
        xTxt.fontSize = 18;
        xTxt.characters = "✕";
        xTxt.textAutoResize = "WIDTH_AND_HEIGHT";
        bindFill(xTxt, 'text/secondary');
        closeBtn.appendChild(xTxt);
        header.appendChild(closeBtn);

        // 2. Subtitle Lead
        const subTxt = figma.createText();
        subTxt.name = "Modal Subtitle";
        subTxt.textStyleId = styleMap[lang === "BN" ? "Typography / Bengali / Body Regular" : "Typography / Latin / Body Regular"]?.id;
        subTxt.characters = lang === "BN" 
            ? "প্রধান স্থপতিদের সাথে সরাসরি স্থানিক পরিকল্পনা আলোচনা। ২৪–৪৮ ঘণ্টার মধ্যে নিশ্চিতকরণ।"
            : "Direct spatial planning discussion with our principal architects. Confirmation within 24–48 hours.";
        subTxt.textAutoResize = "HEIGHT";
        bindFill(subTxt, 'text/secondary');
        modalFrame.appendChild(subTxt);
        subTxt.layoutAlign = "STRETCH";

        // 3. The 5 Distinct Form Fields Contract (FG-06)
        const fields = lang === "BN" ? [
            { label: "আপনার নাম (Full Name) *", placeholder: "যেমন: তানভীর আহমেদ" },
            { label: "ফোন নম্বর (Mobile Number) *", placeholder: "০১৭১১-XXXXXX" },
            { label: "প্রকল্পের অবস্থান (Project Location) *", placeholder: "যেমন: ধানমন্ডি / গুলশান, ঢাকা" },
            { label: "প্রকল্পের ধরন (Project Type) *", placeholder: "আবাসিক অ্যাপার্টমেন্ট / বাণিজ্যিক" },
            { label: "স্থানিক বিবরণ ও বিশেষ চাহিদা (Optional Notes)", placeholder: "প্রকল্পের আয়তন, কক্ষ বিন্যাস বা বিশেষ চাহিদা..." }
        ] : [
            { label: "Full Name *", placeholder: "e.g., Tanvir Ahmed" },
            { label: "Phone Number *", placeholder: "+880 1711-XXXXXX" },
            { label: "Project Location *", placeholder: "e.g., Dhanmondi / Gulshan, Dhaka" },
            { label: "Project Type *", placeholder: "Residential Apartment / Commercial" },
            { label: "Project Notes & Spatial Requirements (Optional)", placeholder: "Project area, layout, or joinery requirements..." }
        ];

        const fieldsStack = figma.createFrame();
        fieldsStack.name = "Form Fields Stack";
        fieldsStack.layoutMode = "VERTICAL";
        fieldsStack.itemSpacing = 12;
        fieldsStack.fills = [];
        modalFrame.appendChild(fieldsStack);
        fieldsStack.layoutAlign = "STRETCH";
        try { fieldsStack.layoutSizingHorizontal = "FILL"; } catch(e) {}
        fieldsStack.counterAxisSizingMode = "AUTO";

        fields.forEach(f => {
            const fieldInst = createFormField(f.label, f.placeholder);
            fieldsStack.appendChild(fieldInst);
            fieldInst.layoutAlign = "STRETCH";
            try { fieldInst.layoutSizingHorizontal = "FILL"; } catch(e) {}
        });

        // 4. Offline Simulation Banner (With explicit 16px clearance, no overlap)
        const offlineBanner = figma.createFrame();
        offlineBanner.name = "Offline Simulation Banner Link";
        offlineBanner.layoutMode = "HORIZONTAL";
        offlineBanner.counterAxisAlignItems = "CENTER";
        offlineBanner.paddingLeft = 14;
        offlineBanner.paddingRight = 14;
        offlineBanner.paddingTop = 10;
        offlineBanner.paddingBottom = 10;
        offlineBanner.itemSpacing = 10;
        bindFill(offlineBanner, 'surface/mist');
        bindStroke(offlineBanner, 'border/decorative', 1);
        bindCornerRadius(offlineBanner, 'radius/control');
        modalFrame.appendChild(offlineBanner);
        offlineBanner.layoutAlign = "STRETCH";
        try { offlineBanner.layoutSizingHorizontal = "FILL"; } catch(e) {}
        offlineBanner.counterAxisSizingMode = "AUTO";

        const offTxt = figma.createText();
        offTxt.textStyleId = styleMap[lang === "BN" ? "Typography / Bengali / Body Small" : "Typography / Latin / Meta Small"]?.id;
        offTxt.characters = lang === "BN" 
            ? "⚡ অফলাইন স্থিতিস্থাপকতা পরীক্ষা করুন (ডেমো মোড)" 
            : "⚡ Test Offline Resilience Simulation (Demo Mode)";
        offTxt.textAutoResize = "HEIGHT";
        bindFill(offTxt, 'accent/clay');
        offlineBanner.appendChild(offTxt);
        offTxt.layoutGrow = 1;

        // 5. Submit CTA Button (full width)
        const submitBtn = defaultBtnComp.createInstance();
        submitBtn.name = "Submit CTA";
        const btnTxt = submitBtn.children.find(c => c.type === "TEXT");
        if (btnTxt) {
            btnTxt.characters = lang === "BN" ? "পরামর্শের আবেদন নিশ্চিত করুন →" : "Confirm Consultation Request →";
        }
        modalFrame.appendChild(submitBtn);
        submitBtn.layoutAlign = "STRETCH";
        try { submitBtn.layoutSizingHorizontal = "FILL"; } catch(e) {}
        submitBtn.resize(modalFrame.width - pad * 2, 52);
    }

    // 1. Master Component 10:43 on "02 Components"
    const masterModal = figma.getNodeById("10:43");
    if (masterModal) {
        masterModal.resize(520, 100);
        populateModalContent(masterModal, "BN", false);
        console.log("Rebuilt Master Component 10:43");
    }

    // 2. Desktop BN Overlay 18:2031
    const desktopBnModal = figma.getNodeById("18:2031");
    if (desktopBnModal) {
        desktopBnModal.resize(560, 100);
        populateModalContent(desktopBnModal, "BN", false);
        console.log("Rebuilt Desktop BN Modal 18:2031");
    }

    // 3. Mobile BN Overlay 18:2080
    const mobileBnModal = figma.getNodeById("18:2080");
    if (mobileBnModal) {
        mobileBnModal.resize(358, 100);
        populateModalContent(mobileBnModal, "BN", true);
        console.log("Rebuilt Mobile BN Modal 18:2080");
    }

    // 4. Desktop EN Overlay 18:2149
    const desktopEnModal = figma.getNodeById("18:2149");
    if (desktopEnModal) {
        desktopEnModal.resize(560, 100);
        populateModalContent(desktopEnModal, "EN", false);
        console.log("Rebuilt Desktop EN Modal 18:2149");
    }

    // 5. Mobile EN Overlay 18:2198
    const mobileEnModal = figma.getNodeById("18:2198");
    if (mobileEnModal) {
        mobileEnModal.resize(358, 100);
        populateModalContent(mobileEnModal, "EN", true);
        console.log("Rebuilt Mobile EN Modal 18:2198");
    }

    return {
        masterModal: masterModal ? { id: masterModal.id, w: masterModal.width, h: masterModal.height } : null,
        desktopBn: desktopBnModal ? { id: desktopBnModal.id, w: desktopBnModal.width, h: desktopBnModal.height } : null,
        mobileBn: mobileBnModal ? { id: mobileBnModal.id, w: mobileBnModal.width, h: mobileBnModal.height } : null,
        desktopEn: desktopEnModal ? { id: desktopEnModal.id, w: desktopEnModal.width, h: desktopEnModal.height } : null,
        mobileEn: mobileEnModal ? { id: mobileEnModal.id, w: mobileEnModal.width, h: mobileEnModal.height } : null
    };
})()
