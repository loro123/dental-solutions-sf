# WCAG 2.1 AA Accessibility Audit Report
## Dental Solutions of South Florida
**Audit Date:** March 27, 2026  
**Tool:** axe-core 4.9.1 + custom checks via Playwright  
**Standard:** WCAG 2.1 Level AA  
**Pages Audited:** 9  

## Executive Summary

| Page | axe Violations | axe Incomplete | Custom Issues (Critical) | Custom Issues (Warning) |
|------|---------------|----------------|--------------------------|------------------------|
| ✅ Homepage | 0 | 1 | 0 | 12 |
| ✅ Sleep Apnea | 0 | 1 | 0 | 2 |
| ✅ Tonsils | 0 | 1 | 0 | 2 |
| ✅ Tongue Tie | 0 | 0 | 0 | 2 |
| ✅ NRT | 0 | 0 | 0 | 2 |
| ✅ Snoring | 0 | 1 | 0 | 2 |
| ✅ Adult Airway | 0 | 1 | 0 | 2 |
| ✅ Childrens Airway | 0 | 0 | 0 | 2 |
| ✅ Physician Referral | 0 | 0 | 0 | 2 |
| **TOTAL** | **0** | **5** | **0** | **28** |

---

## Detailed Findings by Page

### Homepage
**URL:** file:///home/ubuntu/dental-modern/index.html  

#### axe-core Incomplete (Needs Manual Review)

**[SERIOUS] color-contrast** — Ensures the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds (122 elements)

#### Custom Checks

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (48x24px, min 44x44px)
  - `A: "Skip to main content"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (66x33px, min 44x44px)
  - `A: "Home"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (132x33px, min 44x44px)
  - `A: "Sleep & Airway"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (217x35px, min 44x44px)
  - `A: "Sleep Apnea & Oral Appliances"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (217x35px, min 44x44px)
  - `A: "Laser Snoring Treatment"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (217x35px, min 44x44px)
  - `A: "Adult Airway Expansion"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (217x35px, min 44x44px)
  - `A: "Nasal Release Therapy"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (115x33px, min 44x44px)
  - `A: "Treatments"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (212x35px, min 44x44px)
  - `A: "Tongue Tie Frenectomy"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (212x35px, min 44x44px)
  - `A: "CO2 Laser Tonsils"`

🟡 **[WARNING] SVG_NO_LABEL** — SVG missing accessible label (aria-label, aria-labelledby, or <title>)
  - `<svg width="100%" viewBox="0 0 1100 580" xmlns="http://www.w3.org/2000/svg" styl`

🟡 **[WARNING] SVG_NO_LABEL** — SVG missing accessible label (aria-label, aria-labelledby, or <title>)
  - `<svg viewBox="0 0 420 1380" xmlns="http://www.w3.org/2000/svg" style="font-famil`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.8) bg=rgba(0, 0, 0, 0) text='Explore Treatments'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='cred-num' color=rgb(201, 168, 76) bg=rgba(0, 0, 0, 0) text='01'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='cred-num' color=rgb(201, 168, 76) bg=rgba(0, 0, 0, 0) text='02'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='cred-num' color=rgb(201, 168, 76) bg=rgba(0, 0, 0, 0) text='03'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='cred-num' color=rgb(201, 168, 76) bg=rgba(0, 0, 0, 0) text='04'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='cred-num' color=rgb(201, 168, 76) bg=rgba(0, 0, 0, 0) text='05'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='intro-stat-num' color=rgb(45, 82, 160) bg=rgba(0, 0, 0, 0) text='Harvard'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='intro-stat-num' color=rgb(45, 82, 160) bg=rgba(0, 0, 0, 0) text='2×'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='intro-stat-num' color=rgb(45, 82, 160) bg=rgba(0, 0, 0, 0) text='CO2'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='intro-stat-num' color=rgb(45, 82, 160) bg=rgba(0, 0, 0, 0) text='0'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='01'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='02'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='03'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='04'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='05'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='06'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='07'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='08'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='01'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='02'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='03'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='04'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='05'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='06'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-link' color=rgb(45, 82, 160) bg=rgba(0, 0, 0, 0) text='Learn more →'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-link' color=rgb(45, 82, 160) bg=rgba(0, 0, 0, 0) text='Learn more →'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-link' color=rgb(45, 82, 160) bg=rgba(0, 0, 0, 0) text='Learn more →'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-link' color=rgb(45, 82, 160) bg=rgba(0, 0, 0, 0) text='Learn more →'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-link' color=rgb(45, 82, 160) bg=rgba(0, 0, 0, 0) text='Learn more →'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-link' color=rgb(45, 82, 160) bg=rgba(0, 0, 0, 0) text='Learn more →'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-link' color=rgb(45, 82, 160) bg=rgba(0, 0, 0, 0) text='Learn more →'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='svc-link' color=rgb(45, 82, 160) bg=rgba(0, 0, 0, 0) text='Learn more →'`

---

### Sleep Apnea
**URL:** file:///home/ubuntu/dental-modern/sleep-apnea.html  

#### axe-core Incomplete (Needs Manual Review)

**[SERIOUS] color-contrast** — Ensures the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds (3 elements)

#### Custom Checks

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (48x24px, min 44x44px)
  - `A: "Skip to main content"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (32x44px, min 44x44px)
  - `A: "Home"`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='1'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='2'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='3'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='4'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='5'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

---

### Tonsils
**URL:** file:///home/ubuntu/dental-modern/tonsils.html  

#### axe-core Incomplete (Needs Manual Review)

**[SERIOUS] color-contrast** — Ensures the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds (4 elements)

#### Custom Checks

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (48x24px, min 44x44px)
  - `A: "Skip to main content"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (32x44px, min 44x44px)
  - `A: "Home"`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='1'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='2'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='3'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='4'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='5'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

---

### Tongue Tie
**URL:** file:///home/ubuntu/dental-modern/tongue-tie.html  

#### Custom Checks

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (48x24px, min 44x44px)
  - `A: "Skip to main content"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (32x44px, min 44x44px)
  - `A: "Home"`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='1'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='2'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='3'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='4'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='5'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

---

### NRT
**URL:** file:///home/ubuntu/dental-modern/nrt.html  

#### Custom Checks

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (48x24px, min 44x44px)
  - `A: "Skip to main content"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (32x44px, min 44x44px)
  - `A: "Home"`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='1'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='2'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='3'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='4'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

---

### Snoring
**URL:** file:///home/ubuntu/dental-modern/snoring.html  

#### axe-core Incomplete (Needs Manual Review)

**[SERIOUS] color-contrast** — Ensures the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds (1 elements)

#### Custom Checks

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (48x24px, min 44x44px)
  - `A: "Skip to main content"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (32x44px, min 44x44px)
  - `A: "Home"`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

---

### Adult Airway
**URL:** file:///home/ubuntu/dental-modern/adult-airway.html  

#### axe-core Incomplete (Needs Manual Review)

**[SERIOUS] color-contrast** — Ensures the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds (1 elements)

#### Custom Checks

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (48x24px, min 44x44px)
  - `A: "Skip to main content"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (32x44px, min 44x44px)
  - `A: "Home"`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='1'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='2'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='3'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='4'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='inner-step-num' color=rgb(107, 130, 154) bg=rgba(0, 0, 0, 0) text='5'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

---

### Childrens Airway
**URL:** file:///home/ubuntu/dental-modern/childrens-airway.html  

#### Custom Checks

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (48x24px, min 44x44px)
  - `A: "Skip to main content"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (32x44px, min 44x44px)
  - `A: "Home"`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

---

### Physician Referral
**URL:** file:///home/ubuntu/dental-modern/physician-referral.html  

#### Custom Checks

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (48x24px, min 44x44px)
  - `A: "Skip to main content"`

🟡 **[WARNING] SMALL_TARGET** — Touch target too small (32x44px, min 44x44px)
  - `A: "Home"`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

🔵 **[INFO] CONTRAST_CHECK** — Manual contrast check needed
  - `class='btn-ghost' color=rgba(255, 255, 255, 0.85) bg=rgba(0, 0, 0, 0) text='Call (305) 447-9199'`

---

## Consolidated Fix List

Issues ranked by severity and frequency across all pages:

### Warning Custom Issues

| Type | Description | Pages Affected |
|------|-------------|----------------|
| SMALL_TARGET | Touch target too small (48x24px, min 44x44px) | Homepage, Sleep Apnea, Tonsils, Tongue Tie, NRT, Snoring, Adult Airway, Childrens Airway, Physician Referral |
| SVG_NO_LABEL | SVG missing accessible label (aria-label, aria-labelledby, or <title>) | Homepage |

---

## WCAG 2.1 AA Criteria Reference

| Criterion | Level | Description |
|-----------|-------|-------------|
| 1.1.1 | A | Non-text Content — all images need alt text |
| 1.3.1 | A | Info and Relationships — structure conveyed through markup |
| 1.4.3 | AA | Contrast (Minimum) — 4.5:1 for normal text, 3:1 for large text |
| 1.4.4 | AA | Resize Text — text resizable up to 200% without loss |
| 1.4.10 | AA | Reflow — content reflows at 320px width |
| 1.4.11 | AA | Non-text Contrast — UI components 3:1 contrast |
| 2.1.1 | A | Keyboard — all functionality via keyboard |
| 2.4.1 | A | Bypass Blocks — skip navigation link |
| 2.4.2 | A | Page Titled — descriptive page titles |
| 2.4.3 | A | Focus Order — logical focus sequence |
| 2.4.7 | AA | Focus Visible — keyboard focus indicator visible |
| 3.1.1 | A | Language of Page — html lang attribute |
| 4.1.1 | A | Parsing — no duplicate IDs, valid markup |
| 4.1.2 | A | Name, Role, Value — all UI components have accessible names |
