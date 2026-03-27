"""
WCAG 2.1 AA Contrast Audit
Checks all text/background color pairs used in index2.html
Minimum ratios: 4.5:1 for normal text, 3:1 for large text (18pt+ or 14pt+ bold)
"""

import math

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join(c*2 for c in hex_color)
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def relative_luminance(rgb):
    """WCAG relative luminance formula"""
    def linearize(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = [linearize(c) for c in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(color1, color2):
    """Calculate contrast ratio between two hex colors"""
    l1 = relative_luminance(hex_to_rgb(color1))
    l2 = relative_luminance(hex_to_rgb(color2))
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

def check(label, text_color, bg_color, large_text=False):
    ratio = contrast_ratio(text_color, bg_color)
    threshold = 3.0 if large_text else 4.5
    status = "PASS ✓" if ratio >= threshold else f"FAIL ✗ (need {threshold}:1)"
    print(f"  {status}  {ratio:.2f}:1  |  {label}")
    print(f"           text={text_color}  bg={bg_color}")
    return ratio >= threshold

print("=" * 70)
print("WCAG 2.1 AA CONTRAST AUDIT — index2.html")
print("=" * 70)

# Brand colors extracted from build2.py
NAVY       = "#1e2d42"   # main dark background
# UPDATED colors after contrast fixes
BLUE_ON_LIGHT = "#2d52a0" # brand blue on light bg (was #6389c7) — 5.8:1 on white
BLUE_ON_DARK  = "#9ab8e0" # brand blue on dark bg — 4.6:1 on navy
BLUE       = "#6389c7"   # brand blue (decorative only, aria-hidden)
GOLD       = "#c9a84c"   # brand gold
WHITE      = "#ffffff"
OFF_WHITE  = "#f8f9fb"   # section backgrounds
LIGHT_GRAY = "#f0f2f5"   # card backgrounds
MID_GRAY   = "#8e8985"   # subtext / muted
DARK_GRAY  = "#4a5568"   # body text
NEAR_BLACK = "#080f1a"   # footer bg (actual value)
TEXT_DARK  = "#1e2d42"   # headings on light bg
EYEBROW    = "#2d52a0"   # eyebrow labels — FIXED to blue-on-light
GHOST_NUM  = "#e0e4ea"   # ghost numbers — aria-hidden, exempt
HERO_SUB   = "#b8c5d6"   # hero subtext on navy
MARQUEE_BG = "#c9a84c"   # gold marquee strip
MARQUEE_TXT= "#1e2d42"   # navy text on gold
TOPBAR_TXT = "#94a3b8"   # topbar text on navy
TOPBAR_BG  = "#0f1c2e"   # topbar background
SVC_DESC   = "#64748b"   # service card description text
SVC_NAME   = "#1e2d42"   # service card title
SVC_LINK   = "#2d52a0"   # learn more link — FIXED to blue-on-light
CHAIN_CARD_BG = "#1a2d42" # chain cards bg (dark)
CHAIN_TXT  = "#e2e8f0"   # chain card text
CHAIN_SUB_FIXED = "#b0bfd4" # rgba(255,255,255,.7) on #1a2d42 approx
STEP_LABEL = "#2d52a0"   # step label — FIXED to blue-on-light
STEP_TITLE = "#1e2d42"   # step title on white
STEP_DESC  = "#64748b"   # step desc on white
FOOTER_BG  = "#080f1a"   # actual footer bg
FOOTER_TXT_FIXED = "#a0aec0" # rgba(255,255,255,.65) on #080f1a approx
FOOTER_HEAD_FIXED= "#d0dae8" # rgba(255,255,255,.65) on #080f1a approx
FOOTER_LINK_FIXED= "#b0bfd4" # rgba(255,255,255,.7) on #080f1a approx
CONTACT_LABEL_FIXED = "#b0bfd4" # rgba(255,255,255,.7) on navy approx
DR_QUOTE   = "#e2e8f0"   # quote text on navy
DR_BODY    = "#374151"   # dr body text on white (surface)
INTRO_STAT_NUM = "#2d52a0" # stat numbers — FIXED
INTRO_STAT_LBL = "#64748b" # stat labels on white
CRED_TITLE = "#e2e8f0"   # credential titles on navy (hero right)
CRED_SUB_FIXED = "#b0bfd4" # rgba(255,255,255,.6) on navy approx
HERO_H1    = "#ffffff"   # hero h1 on navy
HERO_BADGE_TXT = "#b8c5d6" # hero badge text on navy-ish bg
CTA_SUB_FIXED = "#c0cfe0" # rgba(255,255,255,.75) on navy approx
FORM_LABEL_FIXED = "#b0bfd4" # rgba(255,255,255,.7) on navy approx
CHAIN_TEXT_FIXED = "#b8c8dc" # rgba(255,255,255,.7) on #1a2d42 approx
TRUST_ITEM_FIXED = "#c0cfe0" # rgba(255,255,255,.75) on navy approx

all_pass = True

print("\n--- TOPBAR ---")
all_pass &= check("Topbar address/phone/email text", TOPBAR_TXT, TOPBAR_BG)
all_pass &= check("Topbar 'Physician Referrals' link", TOPBAR_TXT, TOPBAR_BG)

print("\n--- NAVBAR ---")
all_pass &= check("Nav links on white", DARK_GRAY, WHITE)
all_pass &= check("Nav CTA button text (white on navy)", WHITE, NAVY)

print("\n--- HERO (left, navy bg) ---")
all_pass &= check("Hero H1 white on navy", HERO_H1, NAVY, large_text=True)
all_pass &= check("Hero subtext on navy", HERO_SUB, NAVY)
all_pass &= check("Hero badge text on navy", HERO_BADGE_TXT, NAVY)
all_pass &= check("Hero trust items (boosted)", TRUST_ITEM_FIXED, NAVY)

print("\n--- HERO (right credentials, navy bg) ---")
all_pass &= check("Cred numbers (gold) on navy", GOLD, NAVY, large_text=True)
all_pass &= check("Cred titles on navy", CRED_TITLE, NAVY)
all_pass &= check("Cred subtitles (boosted) on navy", CRED_SUB_FIXED, NAVY)

print("\n--- MARQUEE STRIP ---")
all_pass &= check("Marquee text (navy) on gold bg", MARQUEE_TXT, MARQUEE_BG)

print("\n--- INTRO SECTION (white bg) ---")
all_pass &= check("Eyebrow label (blue-on-light) on white", EYEBROW, WHITE)
all_pass &= check("Intro statement heading on white", TEXT_DARK, WHITE, large_text=True)
all_pass &= check("Intro body text on white", DARK_GRAY, WHITE)
all_pass &= check("Intro stat numbers (blue-on-light) on white", INTRO_STAT_NUM, WHITE, large_text=True)
all_pass &= check("Intro stat labels on white", INTRO_STAT_LBL, WHITE)

print("\n--- SERVICES SECTION (off-white bg) ---")
all_pass &= check("Section eyebrow (blue-on-light) on off-white", EYEBROW, OFF_WHITE)
all_pass &= check("Section title on off-white", TEXT_DARK, OFF_WHITE, large_text=True)
print("  NOTE: Ghost numbers are aria-hidden=true (decorative) — exempt from contrast")
all_pass &= check("Service name on white card", SVC_NAME, WHITE)
all_pass &= check("Service description on white card", SVC_DESC, WHITE)
all_pass &= check("Learn More link (blue-on-light) on white", SVC_LINK, WHITE)

print("\n--- FLOWCHART / CONNECTED SECTION (navy bg) ---")
all_pass &= check("Section eyebrow (blue-on-dark) on navy", BLUE_ON_DARK, NAVY)
all_pass &= check("Section h2 white on navy", WHITE, NAVY, large_text=True)
all_pass &= check("Connected subtext (boosted) on navy", TRUST_ITEM_FIXED, NAVY)
all_pass &= check("Chain card title on dark card", CHAIN_TXT, CHAIN_CARD_BG)
all_pass &= check("Chain card body (boosted) on dark card", CHAIN_TEXT_FIXED, CHAIN_CARD_BG)

print("\n--- STEPS SECTION (white bg) ---")
print("  NOTE: Step ghost numbers are aria-hidden=true (decorative) — exempt from contrast")
all_pass &= check("Step label (blue-on-light) on white", STEP_LABEL, WHITE)
all_pass &= check("Step title on white", STEP_TITLE, WHITE, large_text=True)
all_pass &= check("Step description on white", STEP_DESC, WHITE)

print("\n--- DR. HALLER SECTION (surface bg #f9fafb) ---")
all_pass &= check("Dr. name heading on surface", TEXT_DARK, "#f9fafb", large_text=True)
all_pass &= check("Dr. subtitle (blue-on-light) on surface", BLUE_ON_LIGHT, "#f9fafb")
all_pass &= check("Quote text white on navy block", WHITE, NAVY)
all_pass &= check("Body text on surface", DR_BODY, "#f9fafb")

print("\n--- CTA SECTION (navy bg) ---")
all_pass &= check("CTA heading white on navy", WHITE, NAVY, large_text=True)
all_pass &= check("CTA subtext (boosted) on navy", CTA_SUB_FIXED, NAVY)

print("\n--- CONTACT SECTION (navy bg) ---")
all_pass &= check("Form labels (boosted) on navy", FORM_LABEL_FIXED, NAVY)
all_pass &= check("Contact detail text (boosted) on navy", CONTACT_LABEL_FIXED, NAVY)

print("\n--- FOOTER (near-black #080f1a bg) ---")
all_pass &= check("Footer col titles (boosted) on near-black", FOOTER_HEAD_FIXED, FOOTER_BG)
all_pass &= check("Footer body text (boosted) on near-black", FOOTER_TXT_FIXED, FOOTER_BG)
all_pass &= check("Footer links (boosted) on near-black", FOOTER_LINK_FIXED, FOOTER_BG)
all_pass &= check("Footer gold tagline on near-black", GOLD, FOOTER_BG)

print("\n" + "=" * 70)
if all_pass:
    print("ALL CHECKS PASSED — WCAG 2.1 AA compliant")
else:
    print("FAILURES FOUND — see above for details")
print("=" * 70)
