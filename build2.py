import base64

# Read logos
with open('/home/ubuntu/dental-modern/logo.png', 'rb') as f:
    logo_uri = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

with open('/home/ubuntu/dental-modern/logo_transparent.png', 'rb') as f:
    logo_transparent_uri = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

# Read flowchart SVG
with open('/tmp/flowchart_orig.svg', 'r') as f:
    flowchart_svg = f.read().strip()

# Mobile flowchart SVG
from mobile_svg import MOBILE_SVG
mobile_flowchart_svg = MOBILE_SVG

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dental Solutions of South Florida — Airway Dentistry</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&family=DM+Serif+Display:ital@0;1&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
/* ============================================================
   RESET & BASE
   ============================================================ */
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
html{{scroll-behavior:smooth;font-size:16px;}}
body{{
  font-family:"DM Sans",system-ui,sans-serif;
  background:#fafaf8;
  color:#111;
  -webkit-font-smoothing:antialiased;
  overflow-x:hidden;
}}

/* ============================================================
   DESIGN TOKENS
   ============================================================ */
:root{{
  --blue:#6389c7;          /* brand blue — decorative only */
  --blue-on-light:#2d52a0; /* AA on white: 5.8:1 */
  --blue-on-dark:#9ab8e0;  /* AA on navy: 4.6:1 */
  --blue-dk:#3a5a9e;
  --blue-lt:#e8eef8;
  --gold:#c9a84c;
  --gold-on-dark:#d4b86a;  /* slightly lighter gold for dark bg text */
  --gold-lt:#fdf5e0;
  --navy:#0f1e33;
  --navy-mid:#1e3050;
  --ink:#111827;
  --body:#374151;
  --muted:#6b7280;
  --border:#e5e7eb;
  --surface:#f9fafb;
  --white:#ffffff;
  --green:#1a6b4a;
  --green-lt:#e6f4ed;
  --max-w:1800px;
  --gutter:72px;
}}

/* ============================================================
   LAYOUT UTILITIES
   ============================================================ */
.wrap{{max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter);}}
.eyebrow{{
  font-family:"Space Grotesk",sans-serif;
  font-size:11px;font-weight:600;
  letter-spacing:.18em;text-transform:uppercase;
  color:var(--blue-on-light); /* #2d52a0 — 5.8:1 on white */
}}
.eyebrow--gold{{color:var(--gold);}}
.eyebrow--white{{color:#b8c9e0;}} /* 4.8:1 on navy */

/* ============================================================
   TOPBAR
   ============================================================ */
.topbar{{
  background:var(--navy);
  padding:10px 0;
  border-bottom:1px solid rgba(255,255,255,.06);
}}
.topbar .wrap{{
  display:flex;justify-content:space-between;align-items:center;
}}
.topbar-info{{
  font-size:12px;color:rgba(255,255,255,.8); /* boosted: ~9:1 on navy */
  display:flex;align-items:center;gap:20px;
}}
.topbar-info span{{display:flex;align-items:center;gap:6px;}}
.topbar-info svg{{opacity:.7;}}
.topbar-right{{display:flex;align-items:center;gap:24px;}}
.topbar-link{{
  font-size:12px;color:rgba(255,255,255,.8); /* boosted: ~9:1 on navy */
  text-decoration:none;transition:color .2s;
}}
.topbar-link:hover{{color:#fff;}}
.topbar-btn{{
  background:var(--gold);color:var(--navy);
  font-family:"Space Grotesk",sans-serif;
  font-size:11px;font-weight:700;letter-spacing:.1em;
  text-transform:uppercase;padding:7px 20px;
  border-radius:100px;border:none;cursor:pointer;
  transition:background .2s,transform .15s;
}}
.topbar-btn:hover{{background:#dbb95a;transform:translateY(-1px);}}

/* ============================================================
   NAV
   ============================================================ */
.nav{{
  background:rgba(255,255,255,.97);
  backdrop-filter:blur(12px);
  border-bottom:1px solid var(--border);
  position:sticky;top:0;z-index:200;
}}
.nav .wrap{{
  display:flex;align-items:center;justify-content:space-between;
  height:100px;gap:32px;
}}
.nav-logo{{height:80px;width:auto;display:block;flex-shrink:0;}}
.nav-links{{display:flex;align-items:center;gap:0;}}
.nav-links a{{
  font-family:"Space Grotesk",sans-serif;
  font-size:13px;font-weight:500;
  color:var(--muted);text-decoration:none;
  padding:8px 15px;border-radius:8px;
  transition:color .15s,background .15s;
  white-space:nowrap;
}}
.nav-links a:hover,.nav-links a.active{{color:var(--ink);background:#f3f4f6;}}
.nav-cta{{
  background:var(--navy);color:#fff;
  font-family:"Space Grotesk",sans-serif;
  font-size:13px;font-weight:600;letter-spacing:.02em;
  padding:10px 24px;border-radius:100px;border:none;cursor:pointer;
  transition:background .2s,transform .15s;white-space:nowrap;
  flex-shrink:0;
}}
.nav-cta:hover{{background:var(--blue-dk);transform:translateY(-1px);}}
.nav-item{{position:relative;display:flex;align-items:center;}}
.nav-link-dd{{font-family:"Space Grotesk",sans-serif;font-size:13px;font-weight:500;color:var(--muted);text-decoration:none;padding:8px 15px;border-radius:8px;transition:color .15s,background .15s;white-space:nowrap;cursor:pointer;display:flex;align-items:center;gap:5px;}}
.nav-link-dd::after{{content:'';display:inline-block;width:6px;height:6px;border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:rotate(45deg) translateY(-2px);transition:transform .2s;flex-shrink:0;}}
.nav-item:hover>.nav-link-dd::after{{transform:rotate(-135deg) translateY(-2px);}}
.nav-link-dd:hover,.nav-item:hover>.nav-link-dd{{color:var(--ink);background:#f3f4f6;}}
.nav-dropdown{{position:absolute;top:calc(100% + 8px);left:0;min-width:230px;background:#fff;border:1px solid #e5e7eb;border-radius:12px;box-shadow:0 12px 40px rgba(0,0,0,.12);padding:8px;opacity:0;visibility:hidden;transform:translateY(-6px);transition:opacity .18s,transform .18s,visibility .18s;z-index:300;}}
.nav-item:hover>.nav-dropdown{{opacity:1;visibility:visible;transform:translateY(0);}}
.nav-dropdown a{{display:block;padding:9px 14px;font-size:13px;font-weight:500;font-family:"Space Grotesk",sans-serif;color:#1e2d42;border-radius:8px;transition:background .15s,color .15s;white-space:nowrap;}}
.nav-dropdown a:hover{{background:rgba(45,82,160,.07);color:#2d52a0;}}
.nav-hamburger{{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:6px;border:none;background:none;}}
.nav-hamburger span{{display:block;width:22px;height:2px;background:var(--navy);border-radius:2px;transition:all .25s;}}
.nav-hamburger.open span:nth-child(1){{transform:translateY(7px) rotate(45deg);}}
.nav-hamburger.open span:nth-child(2){{opacity:0;}}
.nav-hamburger.open span:nth-child(3){{transform:translateY(-7px) rotate(-45deg);}}
.nav-mobile{{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:#fff;z-index:500;overflow-y:auto;padding:24px 20px 40px;flex-direction:column;}}
.nav-mobile.open{{display:flex;}}
.nav-mobile-header{{display:flex;align-items:center;justify-content:space-between;margin-bottom:32px;}}
.nav-mobile-close{{font-size:28px;background:none;border:none;cursor:pointer;color:var(--navy);line-height:1;}}
.nav-mobile a{{display:block;font-size:17px;font-weight:600;color:var(--navy);padding:14px 0;border-bottom:1px solid #e5e7eb;text-decoration:none;}}
.nav-mobile a:hover{{color:#2d52a0;}}
.nav-mobile .mob-section-label{{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#6b7280;padding:20px 0 8px;border-bottom:none;display:block;}}
.nav-mobile .mob-sub{{font-size:15px;font-weight:500;padding:10px 0 10px 16px;color:#1e2d42;}}

/* ============================================================
   HERO — FULL BLEED SPLIT
   ============================================================ */
.hero{{
  background:var(--navy);
  min-height:92vh;
  display:grid;
  grid-template-columns:1fr 1fr;
  position:relative;
  overflow:hidden;
}}
/* Decorative circles */
.hero::before{{
  content:"";
  position:absolute;
  width:700px;height:700px;
  border-radius:50%;
  background:radial-gradient(circle,rgba(99,137,199,.18) 0%,transparent 70%);
  top:-200px;left:-150px;
  pointer-events:none;
}}
.hero::after{{
  content:"";
  position:absolute;
  width:500px;height:500px;
  border-radius:50%;
  background:radial-gradient(circle,rgba(201,168,76,.12) 0%,transparent 70%);
  bottom:-100px;right:300px;
  pointer-events:none;
}}
.hero-left{{
  padding:100px var(--gutter) 100px;
  display:flex;flex-direction:column;justify-content:center;
  position:relative;z-index:2;
}}
.hero-badge{{
  display:inline-flex;align-items:center;gap:8px;
  background:rgba(99,137,199,.15);
  border:1px solid rgba(99,137,199,.3);
  border-radius:100px;
  padding:6px 16px;
  font-family:"Space Grotesk",sans-serif;
  font-size:11px;font-weight:600;letter-spacing:.1em;
  color:rgba(255,255,255,.7);
  text-transform:uppercase;
  margin-bottom:36px;
  width:fit-content;
}}
.hero-badge::before{{
  content:"";
  width:6px;height:6px;border-radius:50%;
  background:var(--gold);
  flex-shrink:0;
}}
.hero-h1{{
  font-family:"DM Serif Display",serif;
  font-size:clamp(52px,5.5vw,88px);
  line-height:1.0;
  color:#fff;
  margin-bottom:28px;
  letter-spacing:-.02em;
}}
.hero-h1 em{{
  font-style:italic;
  color:var(--blue-on-dark); /* #9ab8e0 — 4.6:1 on navy */
}}
.hero-h1 strong{{
  font-style:normal;
  color:var(--gold);
}}
.hero-sub{{
  font-size:17px;line-height:1.7;
  color:rgba(255,255,255,.6);
  max-width:520px;
  margin-bottom:44px;
}}
.hero-actions{{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:48px;}}
.btn-primary{{
  background:var(--gold);color:var(--navy);
  font-family:"Space Grotesk",sans-serif;
  font-size:14px;font-weight:700;letter-spacing:.04em;
  padding:15px 32px;border-radius:100px;border:none;cursor:pointer;
  transition:background .2s,transform .15s,box-shadow .2s;
}}
.btn-primary:hover{{background:#dbb95a;transform:translateY(-2px);box-shadow:0 8px 24px rgba(201,168,76,.35);}}
.btn-ghost{{
  background:transparent;color:rgba(255,255,255,.8);
  font-family:"Space Grotesk",sans-serif;
  font-size:14px;font-weight:600;letter-spacing:.04em;
  padding:15px 32px;border-radius:100px;
  border:1.5px solid rgba(255,255,255,.25);cursor:pointer;
  transition:border-color .2s,color .2s,background .2s;
}}
.btn-ghost:hover{{border-color:rgba(255,255,255,.6);color:#fff;background:rgba(255,255,255,.07);}}
.hero-trust{{
  display:flex;flex-direction:column;gap:10px;
}}
.trust-item{{
  display:flex;align-items:center;gap:10px;
  font-size:13px;color:rgba(255,255,255,.75); /* boosted to ~7:1 on navy */
}}
.trust-dot{{
  width:18px;height:18px;border-radius:50%;
  background:rgba(99,137,199,.25);
  border:1.5px solid rgba(99,137,199,.5);
  display:flex;align-items:center;justify-content:center;
  flex-shrink:0;
  font-size:9px;color:var(--blue);
  font-weight:700;
}}

/* HERO RIGHT — credential wall */
.hero-right{{
  background:rgba(255,255,255,.04);
  border-left:1px solid rgba(255,255,255,.07);
  display:flex;flex-direction:column;justify-content:center;
  padding:80px 64px 80px 72px;
  position:relative;z-index:2;
  gap:0;
}}
.hero-right-label{{
  font-family:"Space Grotesk",sans-serif;
  font-size:10px;font-weight:600;letter-spacing:.2em;
  text-transform:uppercase;color:rgba(255,255,255,.55); /* boosted to ~4.8:1 on navy */
  margin-bottom:32px;
}}
.cred-item{{
  padding:22px 0;
  border-bottom:1px solid rgba(255,255,255,.07);
  display:flex;align-items:flex-start;gap:18px;
}}
.cred-item:last-child{{border-bottom:none;}}
.cred-num{{
  font-family:"DM Serif Display",serif;
  font-size:28px;color:var(--gold);
  line-height:1;flex-shrink:0;width:32px;
  opacity:.7;
}}
.cred-body{{}}
.cred-title{{
  font-family:"Space Grotesk",sans-serif;
  font-size:15px;font-weight:600;color:#fff;
  margin-bottom:3px;
}}
.cred-sub{{font-size:12px;color:rgba(255,255,255,.6);line-height:1.5;}} /* boosted to ~5.2:1 on navy */

/* ============================================================
   MARQUEE STRIP
   ============================================================ */
.marquee-strip{{
  background:var(--gold);
  padding:14px 0;
  overflow:hidden;
  white-space:nowrap;
}}
.marquee-track{{
  display:inline-flex;gap:0;
  animation:marquee 30s linear infinite;
}}
.marquee-item{{
  font-family:"Space Grotesk",sans-serif;
  font-size:12px;font-weight:700;letter-spacing:.12em;
  text-transform:uppercase;color:var(--navy);
  padding:0 36px;
  display:inline-flex;align-items:center;gap:12px;
}}
.marquee-item::after{{
  content:"✦";font-size:8px;opacity:.5;
}}
@keyframes marquee{{
  from{{transform:translateX(0);}}
  to{{transform:translateX(-50%);}}
}}

/* ============================================================
   INTRO STATEMENT
   ============================================================ */
.intro-section{{
  padding:120px 0;
  background:#fff;
}}
.intro-inner{{
  max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter);
  display:grid;grid-template-columns:1fr 1fr;gap:96px;align-items:center;
}}
.intro-left{{}}
.intro-statement{{
  font-family:"DM Serif Display",serif;
  font-size:clamp(36px,3.5vw,56px);
  line-height:1.15;
  color:var(--ink);
  letter-spacing:-.02em;
  margin-bottom:0;
}}
.intro-statement em{{
  font-style:italic;color:var(--blue-on-light); /* #2d52a0 — 5.8:1 on white */
}}
.intro-right{{}}
.intro-text{{
  font-size:17px;line-height:1.8;color:var(--body);
  margin-bottom:32px;
}}
.intro-divider{{
  width:48px;height:3px;
  background:linear-gradient(to right,var(--gold),transparent);
  margin-bottom:32px;
  border-radius:2px;
}}
.intro-stats{{
  display:grid;grid-template-columns:1fr 1fr;gap:24px;
  margin-top:40px;
}}
.intro-stat{{
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:16px;
  padding:24px;
}}
.intro-stat-num{{
  font-family:"DM Serif Display",serif;
  font-size:32px;color:var(--blue-on-light); /* #2d52a0 — 5.8:1 on white */
  line-height:1;margin-bottom:6px;
}}
.intro-stat-label{{font-size:13px;color:var(--muted);line-height:1.4;}}

/* ============================================================
   SERVICES — LARGE CARD GRID
   ============================================================ */
.services-section{{
  padding:120px 0;
  background:var(--surface);
}}
.section-header{{margin-bottom:64px;}}
.section-title{{
  font-family:"DM Serif Display",serif;
  font-size:clamp(32px,3vw,48px);
  color:var(--ink);
  letter-spacing:-.02em;
  margin-top:12px;
  line-height:1.15;
}}
.section-title em{{font-style:italic;color:var(--blue-on-light);}} /* #2d52a0 — 5.8:1 */
.services-grid{{
  display:grid;
  grid-template-columns:repeat(4,1fr);
  gap:2px;
  background:var(--border);
  border-radius:20px;
  overflow:hidden;
}}
.svc-card{{
  background:#fff;
  padding:36px 32px 32px;
  display:flex;flex-direction:column;
  gap:0;
  transition:background .2s;
  position:relative;
  overflow:hidden;
}}
.svc-card::before{{
  content:"";
  position:absolute;
  top:0;left:0;right:0;
  height:3px;
  background:var(--accent-color,var(--blue));
  transform:scaleX(0);
  transform-origin:left;
  transition:transform .3s ease;
}}
.svc-card:hover{{background:#fafbff;}}
.svc-card:hover::before{{transform:scaleX(1);}}
.svc-num{{
  font-family:"DM Serif Display",serif;
  font-size:48px;color:var(--border);
  line-height:1;margin-bottom:20px;
  font-weight:400;
}}
.svc-icon-wrap{{
  width:48px;height:48px;border-radius:14px;
  display:flex;align-items:center;justify-content:center;
  font-size:22px;margin-bottom:20px;
  flex-shrink:0;
}}
.svc-name{{
  font-family:"Space Grotesk",sans-serif;
  font-size:16px;font-weight:600;color:var(--ink);
  margin-bottom:10px;line-height:1.3;
}}
.svc-desc{{
  font-size:14px;line-height:1.65;color:var(--muted);
  flex:1;margin-bottom:20px;
}}
.svc-link{{
  font-family:"Space Grotesk",sans-serif;
  font-size:12px;font-weight:600;letter-spacing:.06em;
  text-transform:uppercase;color:var(--blue-on-light); /* #2d52a0 — 5.8:1 on white */
  text-decoration:none;
  display:inline-flex;align-items:center;gap:6px;
  transition:gap .2s,color .2s;
}}
.svc-link:hover{{gap:10px;color:var(--blue-dk);}}

/* ============================================================
   FLOWCHART SECTION — KEPT AS-IS, RESTYLED CONTAINER
   ============================================================ */
.connected-section{{
  padding:120px 0;
  background:var(--navy);
  position:relative;
  overflow:hidden;
}}
.connected-section::before{{
  content:"";
  position:absolute;
  width:800px;height:800px;border-radius:50%;
  background:radial-gradient(circle,rgba(99,137,199,.08) 0%,transparent 70%);
  top:-200px;right:-200px;pointer-events:none;
}}
.connected-section .wrap{{position:relative;z-index:2;}}
.connected-header{{
  display:grid;grid-template-columns:1fr 1fr;gap:64px;
  align-items:end;margin-bottom:72px;
}}
.connected-h2{{
  font-family:"DM Serif Display",serif;
  font-size:clamp(40px,4vw,64px);
  color:#fff;line-height:1.05;
  letter-spacing:-.02em;
}}
.connected-h2 em{{font-style:italic;color:var(--blue-on-dark);}} /* #9ab8e0 — 4.6:1 on navy */
.connected-sub{{
  font-size:17px;line-height:1.75;
  color:rgba(255,255,255,.75); /* boosted to ~7:1 on navy */
  align-self:end;
}}
.flowchart-container{{
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.1);
  border-radius:24px;
  padding:48px;
  margin-bottom:48px;
  overflow-x:auto;
}}
.diagram-wrapper{{width:100%;}}
.diagram-desktop,.diagram-mobile{{width:100%;}}
.diagram-desktop svg,.diagram-mobile svg{{width:100%;height:auto;display:block;}}
.diagram-desktop{{display:block;}}
.diagram-mobile{{display:none;}}
@media(max-width:768px){{
  .diagram-desktop{{display:none;}}
  .diagram-mobile{{display:block;}}
  .flowchart-container{{padding:20px;}}
}}
.chain-grid{{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:16px;
  margin-top:48px;
}}
.chain-card{{
  background:rgba(255,255,255,.05);
  border:1px solid rgba(255,255,255,.1);
  border-radius:16px;
  padding:28px;
  transition:background .2s,border-color .2s;
}}
.chain-card:hover{{
  background:rgba(255,255,255,.08);
  border-color:rgba(255,255,255,.2);
}}
.chain-card-icon{{font-size:24px;margin-bottom:12px;}}
.chain-card-title{{
  font-family:"Space Grotesk",sans-serif;
  font-size:15px;font-weight:600;color:#fff;
  margin-bottom:10px;line-height:1.3;
}}
.chain-card-text{{
  font-size:14px;line-height:1.65;
  color:rgba(255,255,255,.7); /* boosted to ~5.8:1 on dark card */
}}

/* ============================================================
   BREAK THE CHAIN — NUMBERED STEPS
   ============================================================ */
.break-section{{
  padding:120px 0;
  background:#fff;
}}
.break-intro{{
  display:grid;grid-template-columns:1fr 1fr;gap:64px;
  align-items:center;margin-bottom:80px;
}}
.break-h2{{
  font-family:"DM Serif Display",serif;
  font-size:clamp(36px,3.5vw,54px);
  color:var(--ink);line-height:1.1;
  letter-spacing:-.02em;
}}
.break-h2 em{{font-style:italic;color:var(--blue-on-light);}} /* #2d52a0 — 5.8:1 on white */
.break-desc{{
  font-size:17px;line-height:1.75;color:var(--body);
}}
.steps-track{{
  display:grid;
  grid-template-columns:repeat(3,1fr);
  gap:2px;
  background:var(--border);
  border-radius:24px;
  overflow:hidden;
}}
.step-card{{
  background:#fff;
  padding:40px 36px;
  position:relative;
  transition:background .2s;
}}
.step-card:hover{{background:#fafbff;}}
.step-num{{
  font-family:"DM Serif Display",serif;
  font-size:64px;color:var(--border);
  line-height:1;margin-bottom:20px;
  font-weight:400;
  transition:color .2s;
}}
.step-card:hover .step-num{{color:var(--blue-lt);}}
.step-label{{
  font-family:"Space Grotesk",sans-serif;
  font-size:10px;font-weight:700;letter-spacing:.15em;
  text-transform:uppercase;color:var(--blue-on-light); /* #2d52a0 — 5.8:1 on white */
  margin-bottom:8px;
}}
.step-title{{
  font-family:"DM Serif Display",serif;
  font-size:22px;color:var(--ink);
  margin-bottom:12px;line-height:1.2;
}}
.step-text{{
  font-size:14px;line-height:1.65;color:var(--muted);
  margin-bottom:20px;
}}
.step-tools{{display:flex;flex-direction:column;gap:6px;}}
.step-tool{{
  font-size:13px;color:var(--body);
  display:flex;align-items:flex-start;gap:8px;
  line-height:1.4;
}}
.step-tool::before{{
  content:"→";
  color:var(--blue-on-light);font-size:12px; /* #2d52a0 — 5.8:1 on white */
  flex-shrink:0;margin-top:1px;
}}

/* ============================================================
   DR HALLER — EDITORIAL LAYOUT
   ============================================================ */
.dr-section{{
  padding:120px 0;
  background:var(--surface);
}}
.dr-inner{{
  max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter);
  display:grid;grid-template-columns:420px 1fr;gap:96px;align-items:start;
}}
.dr-photo-block{{
  position:sticky;top:100px;
}}
.dr-photo{{
  background:linear-gradient(135deg,var(--blue-lt) 0%,var(--blue) 100%);
  border-radius:24px;
  aspect-ratio:3/4;
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  margin-bottom:24px;
  position:relative;
  overflow:hidden;
}}
.dr-photo::before{{
  content:"";
  position:absolute;inset:0;
  background:radial-gradient(circle at 30% 30%,rgba(255,255,255,.15),transparent 60%);
}}
.dr-initials{{
  font-family:"DM Serif Display",serif;
  font-size:80px;color:rgba(255,255,255,.3);
  line-height:1;
}}
.dr-photo-note{{
  font-size:11px;color:rgba(255,255,255,.4);
  position:absolute;bottom:16px;
  font-style:italic;
}}
.dr-cred-block{{
  background:#fff;
  border:1px solid var(--border);
  border-radius:16px;
  padding:24px;
}}
.dr-cred-label{{
  font-family:"Space Grotesk",sans-serif;
  font-size:10px;font-weight:700;letter-spacing:.15em;
  text-transform:uppercase;color:var(--muted);
  margin-bottom:14px;
}}
.dr-cred-list{{
  font-size:13px;line-height:2;color:var(--body);
}}
.dr-content{{}}
.dr-eyebrow{{margin-bottom:16px;}}
.dr-name{{
  font-family:"DM Serif Display",serif;
  font-size:clamp(40px,4vw,60px);
  color:var(--ink);line-height:1.05;
  letter-spacing:-.02em;margin-bottom:8px;
}}
.dr-title-line{{
  font-size:15px;color:var(--blue-on-light); /* #2d52a0 — 5.8:1 on white */
  font-weight:500;margin-bottom:40px;
}}
.dr-quote-block{{
  background:var(--navy);
  border-radius:20px;
  padding:40px 44px;
  margin-bottom:36px;
  position:relative;
}}
.dr-quote-mark{{
  font-family:"DM Serif Display",serif;
  font-size:80px;color:var(--gold);
  line-height:.7;
  opacity:.4;
  position:absolute;top:24px;left:36px;
}}
.dr-quote{{
  font-family:"DM Serif Display",serif;
  font-size:clamp(18px,2vw,24px);
  font-style:italic;
  color:#fff;
  line-height:1.6;
  position:relative;z-index:1;
}}
.dr-bio{{
  font-size:16px;line-height:1.8;color:var(--body);
  margin-bottom:36px;
}}
.dr-badges{{
  display:flex;flex-wrap:wrap;gap:8px;
}}
.dr-badge{{
  background:var(--blue-lt);
  border:1px solid rgba(99,137,199,.25);
  color:var(--blue-dk);
  font-family:"Space Grotesk",sans-serif;
  font-size:12px;font-weight:600;
  padding:6px 14px;border-radius:100px;
}}

/* ============================================================
   CTA BANNER
   ============================================================ */
.cta-section{{
  background:var(--navy);
  padding:100px 0;
  position:relative;overflow:hidden;
}}
.cta-section::before{{
  content:"";
  position:absolute;
  width:600px;height:600px;border-radius:50%;
  background:radial-gradient(circle,rgba(201,168,76,.12) 0%,transparent 70%);
  top:-200px;right:-100px;pointer-events:none;
}}
.cta-inner{{
  max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter);
  display:grid;grid-template-columns:1fr auto;gap:80px;align-items:center;
  position:relative;z-index:2;
}}
.cta-h2{{
  font-family:"DM Serif Display",serif;
  font-size:clamp(36px,4vw,60px);
  color:#fff;line-height:1.1;
  letter-spacing:-.02em;margin-bottom:16px;
}}
.cta-h2 span{{color:var(--gold);font-style:italic;}}
.cta-sub{{
  font-size:15px;line-height:1.7;
  color:rgba(255,255,255,.75); /* boosted to ~7:1 on navy */
  max-width:560px;
}}
.cta-buttons{{
  display:flex;flex-direction:column;gap:12px;
  align-items:stretch;min-width:220px;
}}
.btn-gold{{
  background:var(--gold);color:var(--navy);
  font-family:"Space Grotesk",sans-serif;
  font-size:14px;font-weight:700;letter-spacing:.04em;
  padding:16px 32px;border-radius:100px;border:none;cursor:pointer;
  transition:background .2s,transform .15s;text-align:center;
  white-space:nowrap;
}}
.btn-gold:hover{{background:#dbb95a;transform:translateY(-2px);}}
.btn-outline-white{{
  background:transparent;color:rgba(255,255,255,.9); /* boosted to ~13:1 on navy */
  font-family:"Space Grotesk",sans-serif;
  font-size:14px;font-weight:600;letter-spacing:.04em;
  padding:16px 32px;border-radius:100px;
  border:1.5px solid rgba(255,255,255,.5);cursor:pointer;
  transition:border-color .2s,color .2s;text-align:center;
  white-space:nowrap;
}}
.btn-outline-white:hover{{border-color:rgba(255,255,255,.5);color:#fff;}}

/* ============================================================
   TESTIMONIALS — LARGE FORMAT
   ============================================================ */
.test-section{{
  padding:120px 0;
  background:#fff;
}}
.test-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:24px;
  margin-top:0;
}}
.test-card{{
  background:var(--surface);
  border:1px solid var(--border);
  border-radius:20px;
  padding:40px 36px;
  display:flex;flex-direction:column;
  gap:0;
  transition:transform .2s,box-shadow .2s;
}}
.test-card:hover{{
  transform:translateY(-4px);
  box-shadow:0 20px 48px rgba(0,0,0,.08);
}}
.test-stars{{
  font-size:16px;color:var(--gold);
  letter-spacing:2px;margin-bottom:20px;
}}
.test-quote{{
  font-family:"DM Serif Display",serif;
  font-size:18px;font-style:italic;
  color:var(--ink);line-height:1.6;
  flex:1;margin-bottom:28px;
}}
.test-divider{{
  width:32px;height:2px;
  background:var(--border);
  margin-bottom:24px;
}}
.test-row{{display:flex;align-items:center;gap:14px;}}
.test-avatar{{
  width:44px;height:44px;border-radius:50%;
  background:var(--navy);
  display:flex;align-items:center;justify-content:center;
  font-family:"Space Grotesk",sans-serif;
  font-size:13px;font-weight:700;color:#fff;
  flex-shrink:0;
}}
.test-author{{
  font-family:"Space Grotesk",sans-serif;
  font-size:14px;font-weight:600;color:var(--ink);
}}
.test-type{{font-size:12px;color:var(--muted);margin-top:2px;}}

/* ============================================================
   BOOKS
   ============================================================ */
.books-section{{
  padding:80px 0 120px;
  background:var(--surface);
}}
.books-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:24px;
}}
.book-card{{
  background:#fff;
  border:1px solid var(--border);
  border-radius:16px;
  padding:28px;
  display:flex;gap:20px;align-items:flex-start;
  transition:transform .2s,box-shadow .2s;
}}
.book-card:hover{{
  transform:translateY(-3px);
  box-shadow:0 12px 32px rgba(0,0,0,.07);
}}
.book-cover{{
  width:52px;height:68px;border-radius:6px;
  display:flex;align-items:center;justify-content:center;
  font-size:24px;flex-shrink:0;
}}
.book-title{{
  font-family:"Space Grotesk",sans-serif;
  font-size:15px;font-weight:600;color:var(--ink);
  margin-bottom:4px;line-height:1.3;
}}
.book-author{{font-size:13px;color:var(--blue-on-light);margin-bottom:8px;font-weight:500;}} /* #2d52a0 — 5.8:1 on white */
.book-desc{{font-size:13px;color:var(--muted);line-height:1.5;}}

/* ============================================================
   CONTACT
   ============================================================ */
.contact-section{{
  padding:120px 0;
  background:var(--navy);
  position:relative;overflow:hidden;
}}
.contact-section::before{{
  content:"";
  position:absolute;
  width:500px;height:500px;border-radius:50%;
  background:radial-gradient(circle,rgba(99,137,199,.1) 0%,transparent 70%);
  bottom:-100px;left:-100px;pointer-events:none;
}}
.contact-inner{{
  max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter);
  display:grid;grid-template-columns:1fr 1fr;gap:96px;
  position:relative;z-index:2;
}}
.contact-h2{{
  font-family:"DM Serif Display",serif;
  font-size:clamp(32px,3vw,48px);
  color:#fff;margin-bottom:40px;
  letter-spacing:-.02em;line-height:1.1;
}}
.form-row{{margin-bottom:20px;}}
.form-label{{
  display:block;
  font-family:"Space Grotesk",sans-serif;
  font-size:11px;font-weight:600;letter-spacing:.1em;
  text-transform:uppercase;color:rgba(255,255,255,.7); /* boosted to ~6:1 on navy */
  margin-bottom:8px;
}}
.form-input{{
  width:100%;
  background:rgba(255,255,255,.07);
  border:1.5px solid rgba(255,255,255,.12);
  border-radius:12px;
  padding:14px 18px;
  font-family:"DM Sans",sans-serif;
  font-size:15px;color:#fff;
  outline:none;
  transition:border-color .2s,background .2s;
  -webkit-appearance:none;
}}
.form-input::placeholder{{color:rgba(255,255,255,.25);}}
.form-input:focus{{
  border-color:var(--blue);
  background:rgba(99,137,199,.1);
}}
.form-input option{{background:var(--navy);color:#fff;}}
.form-submit{{
  width:100%;
  background:var(--gold);color:var(--navy);
  font-family:"Space Grotesk",sans-serif;
  font-size:14px;font-weight:700;letter-spacing:.06em;
  text-transform:uppercase;
  padding:16px 32px;border-radius:100px;border:none;cursor:pointer;
  margin-top:8px;
  transition:background .2s,transform .15s;
}}
.form-submit:hover{{background:#dbb95a;transform:translateY(-2px);}}
.form-note{{
  font-size:12px;color:rgba(255,255,255,.6); /* boosted to ~5.2:1 on navy */
  line-height:1.6;margin-top:16px;font-style:italic;
}}
.contact-info-side{{}}
.contact-info-h{{
  font-family:"DM Serif Display",serif;
  font-size:clamp(32px,3vw,48px);
  color:#fff;margin-bottom:40px;
  letter-spacing:-.02em;line-height:1.1;
}}
.contact-detail{{
  display:flex;align-items:flex-start;gap:16px;
  padding:20px 0;
  border-bottom:1px solid rgba(255,255,255,.07);
}}
.contact-detail:last-of-type{{border-bottom:none;}}
.contact-icon-wrap{{
  width:40px;height:40px;border-radius:10px;
  background:rgba(255,255,255,.07);
  display:flex;align-items:center;justify-content:center;
  font-size:16px;flex-shrink:0;
}}
.contact-dt{{
  font-family:"Space Grotesk",sans-serif;
  font-size:15px;font-weight:600;color:#fff;
  margin-bottom:3px;
}}
.contact-ds{{font-size:13px;color:rgba(255,255,255,.65);}} /* boosted to ~5.5:1 on navy */
.map-ph{{
  margin-top:32px;
  background:rgba(255,255,255,.05);
  border:1.5px dashed rgba(255,255,255,.12);
  border-radius:16px;height:160px;
  display:flex;align-items:center;justify-content:center;
  font-size:13px;color:rgba(255,255,255,.55); /* boosted — decorative placeholder */
  font-style:italic;
}}

/* ============================================================
   FOOTER
   ============================================================ */
.footer{{
  background:#080f1a;
  padding:72px 0 0;
}}
.footer-inner{{
  max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter) 56px;
  display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:56px;
}}
.footer-logo{{height:50px;width:auto;margin-bottom:16px;filter:brightness(0) invert(1);}}
.footer-tagline{{
  font-family:"DM Serif Display",serif;
  font-size:14px;font-style:italic;
  color:var(--gold);margin-bottom:20px;
}}
.footer-contact-info{{
  font-size:13px;color:rgba(255,255,255,.65); /* boosted to ~5.5:1 on #080f1a */
  line-height:2.2;
}}
.footer-col-title{{
  font-family:"Space Grotesk",sans-serif;
  font-size:10px;font-weight:700;letter-spacing:.18em;
  text-transform:uppercase;color:rgba(255,255,255,.65); /* boosted to ~5.5:1 on #080f1a */
  margin-bottom:20px;
}}
.footer-link{{
  display:block;font-size:14px;
  color:rgba(255,255,255,.7); /* boosted to ~6:1 on #080f1a */
  text-decoration:none;margin-bottom:10px;
  transition:color .15s;
}}
.footer-link:hover{{color:#fff;}}
.footer-bottom{{
  border-top:1px solid rgba(255,255,255,.06);
}}
.footer-bottom-inner{{
  max-width:var(--max-w);margin:0 auto;padding:20px var(--gutter);
  display:flex;justify-content:space-between;
  font-size:12px;color:rgba(255,255,255,.55); /* boosted to ~4.6:1 on #080f1a */
}}

/* ============================================================
   RESPONSIVE
   ============================================================ */
@media(max-width:1400px){{
  :root{{--gutter:48px;}}
  .hero{{grid-template-columns:1fr 1fr;}}
  .services-grid{{grid-template-columns:repeat(4,1fr);}}
  .steps-track{{grid-template-columns:repeat(3,1fr);}}
}}
@media(max-width:1100px){{
  :root{{--gutter:32px;}}
  .hero{{grid-template-columns:1fr;min-height:auto;}}
  .hero-right{{display:none;}}
  .intro-inner{{grid-template-columns:1fr;gap:48px;}}
  .services-grid{{grid-template-columns:repeat(2,1fr);}}
  .connected-header{{grid-template-columns:1fr;gap:24px;}}
  .chain-grid{{grid-template-columns:repeat(2,1fr);}}
  .break-intro{{grid-template-columns:1fr;gap:32px;}}
  .steps-track{{grid-template-columns:repeat(2,1fr);}}
  .dr-inner{{grid-template-columns:1fr;gap:48px;}}
  .dr-photo-block{{position:static;}}
  .cta-inner{{grid-template-columns:1fr;gap:40px;}}
  .contact-inner{{grid-template-columns:1fr;gap:56px;}}
  .footer-inner{{grid-template-columns:1fr 1fr;}}
  .test-grid{{grid-template-columns:1fr;}}
  .books-grid{{grid-template-columns:1fr;}}
}}
/* ============================================================
   TABLET — 769px to 1024px
   ============================================================ */
@media(min-width:769px) and (max-width:1024px){{
  :root{{--gutter:32px;}}

  /* Hero: single column, tighter padding */
  .hero{{grid-template-columns:1fr;min-height:auto;}}
  .hero-right{{display:none;}}
  .hero-left{{padding:72px var(--gutter);}}
  .hero-h1{{font-size:clamp(44px,7vw,64px);}}

  /* Intro: single column */
  .intro-inner{{grid-template-columns:1fr;gap:40px;}}
  .intro-stats{{grid-template-columns:repeat(4,1fr);}}

  /* Services: 2-column grid */
  .services-grid{{grid-template-columns:repeat(2,1fr);}}

  /* Flowchart header: single column */
  .connected-header{{grid-template-columns:1fr;gap:20px;}}
  .connected-section{{padding:80px 0;}}
  .flowchart-container{{padding:28px;}}

  /* Chain cards: 2-column (not 3) */
  .chain-grid{{grid-template-columns:repeat(2,1fr);}}

  /* Steps: 2-column */
  .break-intro{{grid-template-columns:1fr;gap:28px;}}
  .steps-track{{grid-template-columns:repeat(2,1fr);}}
  .step-card{{padding:28px 24px;}}
  .step-num{{font-size:48px;}}

  /* Dr. Haller: single column */
  .dr-inner{{grid-template-columns:1fr;gap:40px;}}
  .dr-photo-block{{position:static;max-width:400px;}}
  .dr-photo{{aspect-ratio:4/3;}}

  /* CTA: single column */
  .cta-inner{{grid-template-columns:1fr;gap:32px;}}
  .cta-buttons{{flex-direction:row;justify-content:flex-start;}}

  /* Contact: single column */
  .contact-inner{{grid-template-columns:1fr;gap:48px;}}

  /* Testimonials: 1-column */
  .test-grid{{grid-template-columns:1fr 1fr;}}

  /* Books: 2-column */
  .books-grid{{grid-template-columns:repeat(2,1fr);}}

  /* Footer: 2-column */
  .footer-inner{{grid-template-columns:1fr 1fr;gap:40px;}}

  /* Nav: show hamburger hint, keep logo visible */
  .nav-logo{{height:68px;}}
  .nav .wrap{{height:88px;}}
}}

@media(max-width:768px){{
  :root{{--gutter:20px;}}
  .topbar-info,.topbar-right .topbar-link,.topbar-btn{{display:none;}}
  .nav-links{{display:none;}}
  .nav-hamburger{{display:flex;}}
  .nav-cta{{display:none;}}
  .nav-logo{{height:60px;}}
  .hero-badge--hide-mobile{{display:none;}}
  .hero-left{{padding:60px var(--gutter);}}
  .services-grid{{
    grid-template-columns:1fr;
    gap:0;
    border-radius:16px;
  }}
  .svc-card{{
    padding:20px 20px;
    flex-direction:row;
    align-items:flex-start;
    gap:14px;
    flex-wrap:nowrap;
  }}
  .svc-num{{display:none;}}
  .svc-icon-wrap{{
    width:40px;height:40px;
    border-radius:10px;
    font-size:18px;
    flex-shrink:0;
    margin-bottom:0;
  }}
  .svc-card-body{{
    flex:1;
    min-width:0;
  }}
  .svc-name{{font-size:15px;margin-bottom:6px;}}
  .svc-desc{{font-size:13px;margin-bottom:10px;}}
  .steps-track{{grid-template-columns:1fr;}}
  .chain-grid{{grid-template-columns:1fr;}}
  .footer-inner{{grid-template-columns:1fr;}}
  .intro-stats{{grid-template-columns:1fr;}}
}}
</style>
</head>
<body>

<!-- TOPBAR -->
<div class="topbar">
  <div class="wrap">
    <div class="topbar-info">
      <span>📍 348 Alhambra Circle, Coral Gables</span>
      <span>📞 (305) 447-9199</span>
      <span>✉ dentistry@lesliehallerdmd.com</span>
    </div>
    <div class="topbar-right">
      <a href="#" class="topbar-link">Physician Referrals</a>
    </div>
  </div>
</div>

<!-- NAV -->
<nav class="nav">
  <div class="wrap">
    <img src="{logo_uri}" alt="Dental Solutions of South Florida" class="nav-logo">
    <div class="nav-links">
      <a href="index.html" class="active">Home</a>
      <div class="nav-item">
        <a href="sleep-apnea.html" class="nav-link-dd">Sleep &amp; Airway</a>
        <div class="nav-dropdown">
          <a href="sleep-apnea.html">Sleep Apnea &amp; Oral Appliances</a>
          <a href="snoring.html">Laser Snoring Treatment</a>
          <a href="adult-airway.html">Adult Airway Expansion</a>
          <a href="nrt.html">Nasal Release Therapy</a>
        </div>
      </div>
      <div class="nav-item">
        <a href="tonsils.html" class="nav-link-dd">Treatments</a>
        <div class="nav-dropdown">
          <a href="tongue-tie.html">Tongue Tie Frenectomy</a>
          <a href="tonsils.html">CO2 Laser Tonsils</a>
          <a href="adult-airway.html">Epigenetic Arch Expansion</a>
          <a href="nrt.html">Nasal Release Therapy</a>
        </div>
      </div>
      <div class="nav-item">
        <a href="childrens-airway.html" class="nav-link-dd">Children</a>
        <div class="nav-dropdown">
          <a href="childrens-airway.html">Children&#39;s Airway &amp; Orthodontics</a>
          <a href="tongue-tie.html">Tongue Tie (Infants &amp; Children)</a>
          <a href="tonsils.html">CO2 Laser Tonsils</a>
        </div>
      </div>
      <div class="nav-item">
        <a href="#dr-haller" class="nav-link-dd">About</a>
        <div class="nav-dropdown">
          <a href="#dr-haller">Dr. Leslie Haller</a>
          <a href="#philosophy">Our Philosophy</a>
          <a href="physician-referral.html">For Physicians</a>
        </div>
      </div>
      <a href="physician-referral.html">Physicians</a>
      <a href="#contact">Contact</a>
    </div>
    <button class="nav-hamburger" aria-label="Open menu" onclick="document.getElementById('navMobile').classList.toggle('open');this.classList.toggle('open')">
      <span></span><span></span><span></span>
    </button>
    <button class="nav-cta">Book Appointment</button>
  </div>
</nav>
<!-- MOBILE NAV DRAWER -->
<div class="nav-mobile" id="navMobile">
  <div class="nav-mobile-header">
    <img src="{logo_uri}" alt="Dental Solutions of South Florida" style="height:52px">
    <button class="nav-mobile-close" onclick="document.getElementById('navMobile').classList.remove('open');document.querySelector('.nav-hamburger').classList.remove('open')">&times;</button>
  </div>
  <a href="index.html">Home</a>
  <span class="mob-section-label">Sleep &amp; Airway</span>
  <a href="sleep-apnea.html" class="mob-sub">Sleep Apnea &amp; Oral Appliances</a>
  <a href="snoring.html" class="mob-sub">Laser Snoring Treatment</a>
  <a href="adult-airway.html" class="mob-sub">Adult Airway Expansion</a>
  <a href="nrt.html" class="mob-sub">Nasal Release Therapy</a>
  <span class="mob-section-label">Treatments</span>
  <a href="tongue-tie.html" class="mob-sub">Tongue Tie Frenectomy</a>
  <a href="tonsils.html" class="mob-sub">CO2 Laser Tonsils</a>
  <a href="adult-airway.html" class="mob-sub">Epigenetic Arch Expansion</a>
  <span class="mob-section-label">Children</span>
  <a href="childrens-airway.html" class="mob-sub">Children&#39;s Airway &amp; Orthodontics</a>
  <a href="tongue-tie.html" class="mob-sub">Tongue Tie (Infants &amp; Children)</a>
  <span class="mob-section-label">About</span>
  <a href="#dr-haller" class="mob-sub">Dr. Leslie Haller</a>
  <a href="physician-referral.html" class="mob-sub">For Physicians</a>
  <a href="physician-referral.html">Physician Referrals</a>
  <a href="#contact">Contact</a>
  <a href="#contact" style="margin-top:24px;background:var(--navy);color:white;text-align:center;border-radius:50px;padding:16px 24px;display:block">Book Appointment</a>
</div>

<!-- HERO -->
<section class="hero">
  <div class="hero-left">
    <div class="hero-badge hero-badge--hide-mobile">Harvard-Trained &middot; Board Certified &middot; Coral Gables, FL</div>
    <h1 class="hero-h1">
      Breathe Better.<br>
      <em>Sleep Better.</em><br>
      <strong>Live Better.</strong>
    </h1>
    <p class="hero-sub">
      Most practices treat symptoms. We treat the anatomy. Through epigenetic remodeling, guided jaw development, and targeted airway therapies, Dr. Haller helps patients of all ages breathe better, sleep better, and live better &mdash; without surgery.
    </p>
    <div class="hero-actions">
      <button class="btn-primary">Book a Consultation &rarr;</button>
      <button class="btn-ghost">Explore Treatments</button>
    </div>
    <div class="hero-trust">
      <div class="trust-item"><div class="trust-dot">✓</div>Board Certified Laser Dentist (ALD)</div>
      <div class="trust-item"><div class="trust-dot">✓</div>Board Certified in Dental Sleep Medicine (ASBA)</div>
      <div class="trust-item"><div class="trust-dot">✓</div>Published Researcher &mdash; Journal of Rare Disorders</div>
    </div>
  </div>
  <div class="hero-right">
    <div class="hero-right-label">Why patients choose us</div>
    <div class="cred-item">
      <div class="cred-num">01</div>
      <div class="cred-body">
        <div class="cred-title">Harvard School of Dental Medicine</div>
        <div class="cred-sub">Dr. Haller trained at one of the world's premier dental institutions</div>
      </div>
    </div>
    <div class="cred-item">
      <div class="cred-num">02</div>
      <div class="cred-body">
        <div class="cred-title">Board Certified Laser Dentist (ALD)</div>
        <div class="cred-sub">Advanced CO2 laser for tongue ties, tonsils, and soft tissue procedures</div>
      </div>
    </div>
    <div class="cred-item">
      <div class="cred-num">03</div>
      <div class="cred-body">
        <div class="cred-title">Board Certified in Dental Sleep Medicine</div>
        <div class="cred-sub">ASBA certified — custom oral appliances as a CPAP alternative</div>
      </div>
    </div>
    <div class="cred-item">
      <div class="cred-num">04</div>
      <div class="cred-body">
        <div class="cred-title">Epigenetic Airway Remodeling</div>
        <div class="cred-sub">Vivos, Homeoblock, Start Thriving Appliance&reg; — permanent structural change without surgery</div>
      </div>
    </div>
    <div class="cred-item">
      <div class="cred-num">05</div>
      <div class="cred-body">
        <div class="cred-title">Children's Airway &amp; Orthodontics</div>
        <div class="cred-sub">Healthy Start, functional appliances, and early intervention to prevent lifetime airway problems</div>
      </div>
    </div>
  </div>
</section>

<!-- MARQUEE -->
<div class="marquee-strip" aria-hidden="true">
  <div class="marquee-track">
    <span class="marquee-item">Harvard DMD</span>
    <span class="marquee-item">Board Certified Laser Dentist</span>
    <span class="marquee-item">Dental Sleep Medicine</span>
    <span class="marquee-item">Epigenetic Airway Remodeling</span>
    <span class="marquee-item">CO2 Laser Specialist</span>
    <span class="marquee-item">Vivos Provider</span>
    <span class="marquee-item">Homeoblock Certified</span>
    <span class="marquee-item">Children's Airway Care</span>
    <span class="marquee-item">Tongue Tie Release</span>
    <span class="marquee-item">Coral Gables, FL</span>
    <!-- duplicate for seamless loop -->
    <span class="marquee-item">Harvard DMD</span>
    <span class="marquee-item">Board Certified Laser Dentist</span>
    <span class="marquee-item">Dental Sleep Medicine</span>
    <span class="marquee-item">Epigenetic Airway Remodeling</span>
    <span class="marquee-item">CO2 Laser Specialist</span>
    <span class="marquee-item">Vivos Provider</span>
    <span class="marquee-item">Homeoblock Certified</span>
    <span class="marquee-item">Children's Airway Care</span>
    <span class="marquee-item">Tongue Tie Release</span>
    <span class="marquee-item">Coral Gables, FL</span>
  </div>
</div>

<!-- INTRO STATEMENT -->
<section class="intro-section">
  <div class="intro-inner">
    <div class="intro-left">
      <div class="eyebrow" style="margin-bottom:20px;">A different kind of dental practice</div>
      <p class="intro-statement">
        Most practices treat<br>
        <em>symptoms.</em><br>
        We treat the<br>
        anatomy.
      </p>
    </div>
    <div class="intro-right">
      <div class="intro-divider"></div>
      <p class="intro-text">
        Through epigenetic remodeling, guided jaw development, and targeted airway therapies, Dr. Haller helps patients of all ages breathe better, sleep better, and live better &mdash; without surgery.
      </p>
      <p class="intro-text" style="margin-bottom:0;">
        Tongue tie, mouth breathing, enlarged tonsils, poor sleep, and systemic disease aren&rsquo;t separate problems. They form a chain &mdash; and we treat the root.
      </p>
      <div class="intro-stats">
        <div class="intro-stat">
          <div class="intro-stat-num">Harvard</div>
          <div class="intro-stat-label">School of Dental Medicine graduate</div>
        </div>
        <div class="intro-stat">
          <div class="intro-stat-num">2×</div>
          <div class="intro-stat-label">Board certified — laser &amp; sleep medicine</div>
        </div>
        <div class="intro-stat">
          <div class="intro-stat-num">CO2</div>
          <div class="intro-stat-label">Laser specialist — 15-min procedures</div>
        </div>
        <div class="intro-stat">
          <div class="intro-stat-num">0</div>
          <div class="intro-stat-label">Surgeries needed for most treatments</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="services-section">
  <div class="wrap">
    <div class="section-header">
      <div class="eyebrow">What we treat</div>
      <h2 class="section-title">Airway-focused services<br>for adults <em>&amp;</em> children</h2>
    </div>
    <div class="services-grid">
      <div class="svc-card" style="--accent-color:linear-gradient(to right,#1a6b4a,#4a9a7a);">
        <div class="svc-num" aria-hidden="true">01</div>
        <div class="svc-icon-wrap" style="background:#e8f5ee;">🌙</div>
        <div class="svc-card-body">
          <div class="svc-name">Sleep Apnea &amp; Oral Appliances</div>
          <div class="svc-desc">Custom mandibular advancement devices (MAD) for diagnosed sleep apnea. A comfortable, effective CPAP alternative covered by medical insurance.</div>
          <a class="svc-link" href="#">Learn more <span>→</span></a>
        </div>
      </div>
      <div class="svc-card" style="--accent-color:linear-gradient(to right,#6389c7,#8aaad8);">
        <div class="svc-num" aria-hidden="true">02</div>
        <div class="svc-icon-wrap" style="background:#eef3fb;">💎</div>
        <div class="svc-card-body">
          <div class="svc-name">CO2 Laser Tonsil Treatment</div>
          <div class="svc-desc">Laser decontamination shrinks enlarged tonsils without surgery. No hospital, no general anesthesia, no recovery time. Results in 4&ndash;6 sessions.</div>
          <a class="svc-link" href="#">Learn more <span>→</span></a>
        </div>
      </div>
      <div class="svc-card" style="--accent-color:linear-gradient(to right,#c9a84c,#e0bc5a);">
        <div class="svc-num" aria-hidden="true">03</div>
        <div class="svc-icon-wrap" style="background:#fdf6e3;">💅</div>
        <div class="svc-card-body">
          <div class="svc-name">Tongue Tie Release (Frenectomy)</div>
          <div class="svc-desc">CO2 laser frenectomy for infants, children, and adults. Minimal discomfort, rapid healing, and paired with myofunctional therapy for lasting results.</div>
          <a class="svc-link" href="#">Learn more <span>→</span></a>
        </div>
      </div>
      <div class="svc-card" style="--accent-color:linear-gradient(to right,#6a3ab5,#9a6ad5);">
        <div class="svc-num" aria-hidden="true">04</div>
        <div class="svc-icon-wrap" style="background:#f5f0fb;">🤚</div>
        <div class="svc-card-body">
          <div class="svc-name">Airway Expansion (Epigenetic)</div>
          <div class="svc-desc">Epigenetic appliances create permanent structural change &mdash; widening dental arches and nasal passages. Vivos, Homeoblock, Start Thriving Appliance&reg;.</div>
          <a class="svc-link" href="#">Learn more <span>→</span></a>
        </div>
      </div>
      <div class="svc-card" style="--accent-color:linear-gradient(to right,#1a6a7a,#2a9aaa);">
        <div class="svc-num" aria-hidden="true">05</div>
        <div class="svc-icon-wrap" style="background:#e8fafd;">👃</div>
        <div class="svc-card-body">
          <div class="svc-name">Nasal Release Therapy (NRT)</div>
          <div class="svc-desc">Opens the nasal airway to enable nasal breathing. Combined with SONU headband, mouth tape, and nasal sprays for a complete breathing protocol.</div>
          <a class="svc-link" href="#">Learn more <span>→</span></a>
        </div>
      </div>
      <div class="svc-card" style="--accent-color:linear-gradient(to right,#c97a4a,#e09a6a);">
        <div class="svc-num" aria-hidden="true">06</div>
        <div class="svc-icon-wrap" style="background:#fdf0e8;">😤</div>
        <div class="svc-card-body">
          <div class="svc-name">Snoring Laser Treatment</div>
          <div class="svc-desc">Fractional ablative laser therapy tightens soft palate tissue to reduce snoring. Non-surgical, no downtime, effective in 3 sessions.</div>
          <a class="svc-link" href="#">Learn more <span>→</span></a>
        </div>
      </div>
      <div class="svc-card" style="--accent-color:linear-gradient(to right,#2d6a54,#4a9a7a);">
        <div class="svc-num" aria-hidden="true">07</div>
        <div class="svc-icon-wrap" style="background:#e8f5ee;">🤚</div>
        <div class="svc-card-body">
          <div class="svc-name">Children's Airway &amp; Orthodontics</div>
          <div class="svc-desc">Healthy Start and functional appliances guide jaw development in children. Early intervention prevents a lifetime of airway problems.</div>
          <a class="svc-link" href="#">Learn more <span>→</span></a>
        </div>
      </div>
      <div class="svc-card" style="--accent-color:linear-gradient(to right,#2d5fa3,#5a87c3);">
        <div class="svc-num" aria-hidden="true">08</div>
        <div class="svc-icon-wrap" style="background:#eef3fb;">📋</div>
        <div class="svc-card-body">
          <div class="svc-name">Physician Referral Program</div>
          <div class="svc-desc">We work closely with ENTs, pediatricians, sleep physicians, and myofunctional therapists. Detailed reports and collaborative care for every patient.</div>
          <a class="svc-link" href="#">Learn more <span>→</span></a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CONNECTED / FLOWCHART — KEPT AS-IS -->
<section class="connected-section">
  <div class="wrap">
    <div class="connected-header">
      <div>
        <div class="eyebrow eyebrow--white" style="margin-bottom:20px;">The bigger picture</div>
        <h2 class="connected-h2">Everything is <em>connected.</em></h2>
      </div>
      <p class="connected-sub">
        Tongue tie, mouth breathing, enlarged tonsils, poor sleep, and systemic disease aren&rsquo;t separate problems. They form a chain &mdash; and we treat the root.
      </p>
    </div>
    <div class="flowchart-container">
      <div class="diagram-wrapper">
        <div class="diagram-desktop">
          {flowchart_svg}
        </div>
        <div class="diagram-mobile">
          {mobile_flowchart_svg}
        </div>
      </div>
    </div>
    <div class="chain-grid">
      <div class="chain-card">
        <div class="chain-card-icon">💅</div>
        <div class="chain-card-title">Tongue tie &rarr; mouth breathing</div>
        <div class="chain-card-text">A restricted tongue can&rsquo;t rest on the roof of the mouth. It sits low, forcing mouth breathing &mdash; and sending unfiltered, bacteria-laden air directly to the tonsils.</div>
      </div>
      <div class="chain-card">
        <div class="chain-card-icon">😮</div>
        <div class="chain-card-title">Mouth breathing &rarr; enlarged tonsils</div>
        <div class="chain-card-text">The nose filters, humidifies, and cleans air before it reaches the tonsils. Mouth breathing bypasses all of this &mdash; delivering dirty air full of bacteria directly to tonsil tissue.</div>
      </div>
      <div class="chain-card">
        <div class="chain-card-icon">🔄</div>
        <div class="chain-card-title">Enlarged tonsils &rarr; more mouth breathing</div>
        <div class="chain-card-text">Once tonsils enlarge, they obstruct the airway further &mdash; forcing even more mouth breathing. A self-reinforcing cycle that worsens over time without treatment.</div>
      </div>
      <div class="chain-card">
        <div class="chain-card-icon">🪨</div>
        <div class="chain-card-title">Forward head posture &rarr; neck &amp; shoulder pain</div>
        <div class="chain-card-text">Mouth breathing shifts the head forward to open the airway. Over time this causes forward head posture, neck strain, and chronic shoulder pain.</div>
      </div>
      <div class="chain-card">
        <div class="chain-card-icon">💤</div>
        <div class="chain-card-title">Poor sleep &rarr; whole-body consequences</div>
        <div class="chain-card-text">Narrowed airway &rarr; snoring, apnea, low oxygen. Every night of disrupted sleep compounds over years: ADHD-like symptoms, fatigue, brain fog, mood disorders, cardiovascular risk.</div>
      </div>
      <div class="chain-card" style="background:rgba(201,168,76,.12);border-color:rgba(201,168,76,.3);">
        <div class="chain-card-icon">🔗</div>
        <div class="chain-card-title" style="color:var(--gold);">Fix the root &mdash; fix everything</div>
        <div class="chain-card-text">Because everything is connected, treating the root cause ripples through the chain. Better tongue posture &rarr; nasal breathing &rarr; smaller tonsils &rarr; better sleep &rarr; healthier life.</div>
      </div>
    </div>
  </div>
</section>

<!-- BREAK THE CHAIN — STEPS -->
<section class="break-section">
  <div class="wrap">
    <div class="break-intro">
      <div>
        <div class="eyebrow" style="margin-bottom:20px;">Breaking the cycle</div>
        <h2 class="break-h2">Treating the root &mdash;<br><em>not just the symptom</em></h2>
      </div>
      <p class="break-desc">
        Because everything is connected, we follow a systematic protocol that addresses each link in the chain &mdash; from tongue tie release through airway expansion and long-term maintenance.
      </p>
    </div>
    <div class="steps-track">
      <div class="step-card">
        <div class="step-num" aria-hidden="true">01</div>
        <div class="step-label">Find the origin</div>
        <div class="step-title">Is there a tongue tie?</div>
        <div class="step-text">A restricted tongue is often where the chain begins. Releasing it allows the tongue to rest on the palate.</div>
        <div class="step-tools">
          <div class="step-tool">CO2 laser frenectomy</div>
          <div class="step-tool">Myofunctional therapy</div>
        </div>
      </div>
      <div class="step-card">
        <div class="step-num" aria-hidden="true">02</div>
        <div class="step-label">Stop mouth breathing</div>
        <div class="step-title">Open the nasal airway</div>
        <div class="step-text">Patients can&rsquo;t nasal breathe if they can&rsquo;t breathe through their nose.</div>
        <div class="step-tools">
          <div class="step-tool">Nasal Release Therapy (NRT)</div>
          <div class="step-tool">SONU headband (15 min morning + before bed)</div>
          <div class="step-tool">Nasal sprays &middot; Mouth tape at night</div>
        </div>
      </div>
      <div class="step-card">
        <div class="step-num" aria-hidden="true">03</div>
        <div class="step-label">Treat the tonsils</div>
        <div class="step-title">Shrink tonsils &amp; prevent recurrence</div>
        <div class="step-text">Laser decontamination shrinks tonsils. But if mouth breathing continues, they may enlarge again.</div>
        <div class="step-tools">
          <div class="step-tool">CO2 laser tonsil decontamination</div>
          <div class="step-tool">Nasal breathing to prevent recurrence</div>
        </div>
      </div>
      <div class="step-card">
        <div class="step-num" aria-hidden="true">04</div>
        <div class="step-label">Expand the airway</div>
        <div class="step-title">Grow a permanently larger airway</div>
        <div class="step-text">Epigenetic appliances create permanent structural change &mdash; widening the dental arches and nasal passages without surgery.</div>
        <div class="step-tools">
          <div class="step-tool">Epigenetic arch remodeling &mdash; multiple systems</div>
          <div class="step-tool">Healthy Start &middot; Functional appliances (children)</div>
        </div>
      </div>
      <div class="step-card">
        <div class="step-num" aria-hidden="true">05</div>
        <div class="step-label">Address sleep</div>
        <div class="step-title">Restore restorative sleep</div>
        <div class="step-text">MAD devices and snoring laser bridge the gap while expansion is underway.</div>
        <div class="step-tools">
          <div class="step-tool">Custom MAD device for diagnosed sleep apnea</div>
          <div class="step-tool">Snoring laser (fractional ablative therapy)</div>
        </div>
      </div>
      <div class="step-card">
        <div class="step-num" aria-hidden="true">06</div>
        <div class="step-label">Reinforce &amp; maintain</div>
        <div class="step-title">Make it stick for life</div>
        <div class="step-text">Myofunctional therapy retrains tongue, face, and throat muscles.</div>
        <div class="step-tools">
          <div class="step-tool">Myofunctional therapy referral</div>
          <div class="step-tool">Nasal breathing habit reinforcement</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- DR HALLER -->
<section class="dr-section">
  <div class="dr-inner">
    <div class="dr-photo-block">
      <div class="dr-photo">
        <div class="dr-initials">LH</div>
        <div class="dr-photo-note">Photo from current site</div>
      </div>
      <div class="dr-cred-block">
        <div class="dr-cred-label">Credentials</div>
        <div class="dr-cred-list">
          Harvard DMD<br>
          Board Certified Laser Dentist (ALD)<br>
          Board Certified Dental Sleep Medicine (ASBA)<br>
          Certified AMD (Dr. Liao)<br>
          Homeoblock certified<br>
          Vivos provider<br>
          Pediatric orthodontics (Dr. Ramirez)<br>
          ALD &middot; ICAP &middot; AADSM &middot; ASBA &middot; AAGO &middot; AHS
        </div>
      </div>
    </div>
    <div class="dr-content">
      <div class="eyebrow dr-eyebrow">Meet Dr. Haller</div>
      <div class="dr-name">Leslie Haller, DMD</div>
      <div class="dr-title-line">Airway Dentist &middot; CO2 Laser Specialist &middot; Coral Gables, FL</div>
      <div class="dr-quote-block">
        <div class="dr-quote-mark">&ldquo;</div>
        <div class="dr-quote">Along with releasing tongue ties, airway remodeling is the most satisfying work of my life. I have had patients tell me their tinnitus went away, that they could smell their wife&rsquo;s perfume for the first time, that their child finally slept through the night.</div>
      </div>
      <p class="dr-bio">Dr. Haller graduated from Harvard School of Dental Medicine and is board certified in laser dentistry (ALD) and dental sleep medicine (ASBA). She has trained extensively with the leading innovators in airway dentistry, including Dr. Felix Liao (Start Thriving Appliance&reg; / Holistic Mouth Solutions), Vivos Therapeutics, Dr. Theodore Belfor (Homeoblock), Dr. German Ramirez, Dr. Miraglia, Dr. Boyd, and others through AHS Airway Health Solutions. She completed pediatric orthodontic training with Dr. German Ramirez.</p>
      <div class="dr-badges">
        <span class="dr-badge">Harvard DMD</span>
        <span class="dr-badge">CO2 Laser Certified</span>
        <span class="dr-badge">Vivos Provider</span>
        <span class="dr-badge">Homeoblock Certified</span>
        <span class="dr-badge">AMD Certified</span>
        <span class="dr-badge">Pediatric Orthodontics</span>
        <span class="dr-badge">ASBA Board Certified</span>
        <span class="dr-badge">Journal of Rare Disorders</span>
      </div>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="cta-section">
  <div class="cta-inner">
    <div>
      <div class="eyebrow eyebrow--gold" style="margin-bottom:20px;">Ready to breathe better?</div>
      <h2 class="cta-h2">Your airway is the<br><span>root cause.</span><br>Let&rsquo;s fix it &mdash; for good.</h2>
      <p class="cta-sub">Our practice is fee-for-service. We provide a Letter of Medical Necessity and insurance codes for you to submit to your insurance company for potential reimbursement.</p>
    </div>
    <div class="cta-buttons">
      <button class="btn-gold">Book a Consultation</button>
      <button class="btn-outline-white">For Physicians</button>
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<section class="test-section">
  <div class="wrap">
    <div class="section-header">
      <div class="eyebrow">Patient stories</div>
      <h2 class="section-title">What our patients say</h2>
    </div>
    <div class="test-grid">
      <div class="test-card">
        <div class="test-stars">★★★★★</div>
        <div class="test-quote">&ldquo;My son&rsquo;s tonsils were Grade 3 and his pediatrician wanted a surgical referral. After 4 laser sessions with Dr. Haller, they&rsquo;re barely visible. No surgery, no hospital, no recovery time.&rdquo;</div>
        <div class="test-divider"></div>
        <div class="test-row">
          <div class="test-avatar">MT</div>
          <div>
            <div class="test-author">Maria T.</div>
            <div class="test-type">Tonsil Laser Treatment &middot; Parent</div>
          </div>
        </div>
      </div>
      <div class="test-card">
        <div class="test-stars">★★★★★</div>
        <div class="test-quote">&ldquo;I tried CPAP for two years and couldn&rsquo;t tolerate it. Dr. Haller made me a custom oral appliance and I sleep through the night for the first time in a decade.&rdquo;</div>
        <div class="test-divider"></div>
        <div class="test-row">
          <div class="test-avatar">RM</div>
          <div>
            <div class="test-author">Robert M.</div>
            <div class="test-type">Sleep Apnea &middot; Oral Appliance</div>
          </div>
        </div>
      </div>
      <div class="test-card">
        <div class="test-stars">★★★★★</div>
        <div class="test-quote">&ldquo;My infant had a posterior tongue tie nobody else caught. The CO2 laser release took 15 minutes and transformed her ability to nurse. Dr. Haller literally changed our lives.&rdquo;</div>
        <div class="test-divider"></div>
        <div class="test-row">
          <div class="test-avatar">JK</div>
          <div>
            <div class="test-author">Jennifer K.</div>
            <div class="test-type">Infant Tongue Tie &middot; Mother</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- BOOKS -->
<section class="books-section">
  <div class="wrap">
    <div class="section-header">
      <div class="eyebrow">Recommended reading</div>
      <h2 class="section-title">Understand the problem &mdash; and the solution</h2>
    </div>
    <div class="books-grid">
      <div class="book-card">
        <div class="book-cover" style="background:#dce8f5;">📘</div>
        <div>
          <div class="book-title">Breath: The New Science of a Lost Art</div>
          <div class="book-author">James Nestor</div>
          <div class="book-desc">How the way we breathe affects our health &mdash; and how to fix it.</div>
        </div>
      </div>
      <div class="book-card">
        <div class="book-cover" style="background:#e8f5ee;">📗</div>
        <div>
          <div class="book-title">Six-Foot Tiger in a Three-Foot Cage</div>
          <div class="book-author">Dr. Felix Liao</div>
          <div class="book-desc">How an underdeveloped jaw is the hidden cause of sleep apnea, TMJ, and chronic pain.</div>
        </div>
      </div>
      <div class="book-card">
        <div class="book-cover" style="background:#f5f0e8;">📙</div>
        <div>
          <div class="book-title">Licensed to Thrive</div>
          <div class="book-author">Dr. Felix Liao</div>
          <div class="book-desc">Dr. Liao&rsquo;s newest book on the Holistic Mouth Solutions framework.</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section class="contact-section">
  <div class="contact-inner">
    <div>
      <h2 class="contact-h2">Request an<br>appointment</h2>
      <div class="form-row">
        <label class="form-label">Your name</label>
        <input class="form-input" placeholder="Full name" type="text">
      </div>
      <div class="form-row">
        <label class="form-label">Phone or email</label>
        <input class="form-input" placeholder="Best way to reach you" type="text">
      </div>
      <div class="form-row">
        <label class="form-label">Patient age group</label>
        <select class="form-input">
          <option>Adult (18+)</option>
          <option>Child / Teen</option>
          <option>Infant</option>
        </select>
      </div>
      <div class="form-row">
        <label class="form-label">I&rsquo;m interested in&hellip;</label>
        <select class="form-input">
          <option>Sleep Apnea / Oral Appliance</option>
          <option>CO2 Laser Tonsil Treatment</option>
          <option>Tongue Tie Release</option>
          <option>Children&rsquo;s Airway / Orthodontics</option>
          <option>Nasal Release Therapy (NRT)</option>
          <option>Snoring Laser Treatment</option>
          <option>Adult Airway Expansion</option>
        </select>
      </div>
      <button class="form-submit">Send Request &rarr;</button>
      <p class="form-note">Our practice is fee-for-service. We provide a Letter of Medical Necessity and insurance codes for you to submit to your insurance company for potential reimbursement.</p>
    </div>
    <div class="contact-info-side">
      <h2 class="contact-info-h">Find us</h2>
      <div class="contact-detail">
        <div class="contact-icon-wrap">📍</div>
        <div>
          <div class="contact-dt">348 Alhambra Circle</div>
          <div class="contact-ds">Coral Gables, Florida 33134</div>
        </div>
      </div>
      <div class="contact-detail">
        <div class="contact-icon-wrap">📞</div>
        <div>
          <div class="contact-dt">(305) 447-9199</div>
          <div class="contact-ds">Call or text anytime</div>
        </div>
      </div>
      <div class="contact-detail">
        <div class="contact-icon-wrap">✉</div>
        <div>
          <div class="contact-dt">dentistry@lesliehallerdmd.com</div>
          <div class="contact-ds">We respond within one business day</div>
        </div>
      </div>
      <div class="contact-detail">
        <div class="contact-icon-wrap">🕐</div>
        <div>
          <div class="contact-dt">Mon &ndash; Fri, 9am &ndash; 5pm</div>
          <div class="contact-ds">Contact us to schedule</div>
        </div>
      </div>
      <div class="map-ph">Google Map embed goes here</div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer class="footer">
  <div class="footer-inner">
    <div>
      <img src="{logo_transparent_uri}" alt="Dental Solutions of South Florida" class="footer-logo">
      <div class="footer-tagline">Breathe Better. Sleep Better. Live Better.</div>
      <div class="footer-contact-info">
        348 Alhambra Circle<br>
        Coral Gables, FL 33134<br>
        (305) 447-9199<br>
        dentistry@lesliehallerdmd.com
      </div>
    </div>
    <div>
      <div class="footer-col-title">Treatments</div>
      <a class="footer-link" href="#">Tongue Tie Release</a>
      <a class="footer-link" href="#">Sleep Apnea</a>
      <a class="footer-link" href="#">CO2 Laser Tonsils</a>
      <a class="footer-link" href="#">Airway Expansion</a>
      <a class="footer-link" href="#">Children&rsquo;s Airway</a>
      <a class="footer-link" href="#">Snoring Laser</a>
      <a class="footer-link" href="#">NRT</a>
    </div>
    <div>
      <div class="footer-col-title">About</div>
      <a class="footer-link" href="#">Dr. Leslie Haller</a>
      <a class="footer-link" href="#">Our Philosophy</a>
      <a class="footer-link" href="#">For Physicians</a>
      <a class="footer-link" href="#">Research</a>
      <a class="footer-link" href="#">Patient Stories</a>
    </div>
    <div>
      <div class="footer-col-title">Contact</div>
      <a class="footer-link" href="#">Request Appointment</a>
      <a class="footer-link" href="#">Physician Referral</a>
      <a class="footer-link" href="#">Directions</a>
      <a class="footer-link" href="#">Patient Portal</a>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="footer-bottom-inner">
      <span>&copy; 2025 Dental Solutions of South Florida &middot; Leslie Haller, DMD</span>
      <span>Privacy Policy &middot; Terms of Use &middot; Accessibility</span>
    </div>
  </div>
</footer>

</body>
</html>'''

with open('/home/ubuntu/dental-modern/index2.html', 'w') as f:
    f.write(html)

print(f"Written: {len(html):,} chars, {html.count(chr(10))} lines")
