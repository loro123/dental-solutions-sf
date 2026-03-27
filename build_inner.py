"""
Build all inner pages for Dental Solutions of South Florida.
Shares the same design system as index2.html (build2.py).
"""
import base64, os

# ── Assets ──────────────────────────────────────────────────────────────────
with open('/home/ubuntu/dental-modern/logo.png', 'rb') as f:
    LOGO = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()
with open('/home/ubuntu/dental-modern/logo_transparent.png', 'rb') as f:
    LOGO_T = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

# ── Shared CSS ───────────────────────────────────────────────────────────────
SHARED_CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600;700&display=swap');
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --navy:#0d1f35;
  --navy2:#1e2d42;
  --blue:#2d52a0;
  --blue-light:#9ab8e0;
  --gold:#c9a84c;
  --gold2:#a8893e;
  --green:#1D9E75;
  --white:#ffffff;
  --off-white:#f8f7f4;
  --gray:#6b7280;
  --gray-light:#e5e7eb;
  --text:#1a1a2e;
  --gutter:64px;
  --max:1800px;
  --radius:16px;
}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;color:var(--text);background:var(--white);-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}

/* ── TOPBAR ── */
.topbar{background:var(--navy);padding:10px var(--gutter);display:flex;align-items:center;justify-content:space-between;gap:16px}
.topbar-info{display:flex;align-items:center;gap:24px;flex-wrap:wrap}
.topbar-item{display:flex;align-items:center;gap:6px;font-size:13px;color:rgba(255,255,255,.82);font-weight:400}
.topbar-item svg{opacity:.7;flex-shrink:0}
.topbar-right{display:flex;align-items:center;gap:20px}
.topbar-link{font-size:13px;color:rgba(255,255,255,.82);font-weight:500;letter-spacing:.3px;transition:color .2s}
.topbar-link:hover{color:var(--gold)}

/* ── NAV ── */
.nav{background:var(--white);border-bottom:1px solid var(--gray-light);position:sticky;top:0;z-index:200;box-shadow:0 1px 12px rgba(0,0,0,.06)}
.nav .wrap{max-width:var(--max);margin:0 auto;padding:0 var(--gutter);height:100px;display:flex;align-items:center;justify-content:space-between;gap:32px}
.nav-logo{height:80px;width:auto;object-fit:contain}
.nav-links{display:flex;align-items:center;gap:2px;flex:1;justify-content:center}
/* plain links */
.nav-link{font-size:14px;font-weight:500;color:var(--navy2);padding:8px 14px;border-radius:8px;transition:all .2s;white-space:nowrap;display:block}
.nav-link:hover,.nav-link.active{background:rgba(45,82,160,.08);color:var(--blue)}
/* dropdown parent */
.nav-item{position:relative;display:flex;align-items:center}
.nav-item>.nav-link{display:flex;align-items:center;gap:5px;cursor:pointer}
.nav-item>.nav-link::after{content:'';display:inline-block;width:7px;height:7px;border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:rotate(45deg) translateY(-2px);transition:transform .2s;flex-shrink:0}
.nav-item:hover>.nav-link::after,.nav-item.open>.nav-link::after{transform:rotate(-135deg) translateY(-2px)}
/* dropdown panel */
.nav-dropdown{position:absolute;top:calc(100% + 8px);left:0;min-width:220px;background:var(--white);border:1px solid var(--gray-light);border-radius:12px;box-shadow:0 12px 40px rgba(0,0,0,.12);padding:8px;opacity:0;visibility:hidden;transform:translateY(-6px);transition:opacity .18s,transform .18s,visibility .18s;z-index:300}
.nav-item:hover>.nav-dropdown,.nav-item.open>.nav-dropdown{opacity:1;visibility:visible;transform:translateY(0)}
.nav-dropdown a{display:block;padding:9px 14px;font-size:13.5px;font-weight:500;color:var(--navy2);border-radius:8px;transition:background .15s,color .15s;white-space:nowrap}
.nav-dropdown a:hover{background:rgba(45,82,160,.07);color:var(--blue)}
.nav-dropdown .dd-divider{height:1px;background:var(--gray-light);margin:6px 0}
/* hamburger */
.nav-hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:6px;border:none;background:none}
.nav-hamburger span{display:block;width:22px;height:2px;background:var(--navy);border-radius:2px;transition:all .25s}
.nav-hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.nav-hamburger.open span:nth-child(2){opacity:0}
.nav-hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
/* mobile drawer */
.nav-mobile{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:var(--white);z-index:500;overflow-y:auto;padding:24px var(--gutter) 40px;flex-direction:column}
.nav-mobile.open{display:flex}
.nav-mobile-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:32px}
.nav-mobile-close{font-size:28px;background:none;border:none;cursor:pointer;color:var(--navy);line-height:1}
.nav-mobile a{display:block;font-size:17px;font-weight:600;color:var(--navy);padding:14px 0;border-bottom:1px solid var(--gray-light)}
.nav-mobile a:hover{color:var(--blue)}
.nav-mobile .mob-section-label{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--gray);padding:20px 0 8px;border-bottom:none}
.nav-mobile .mob-sub{font-size:15px;font-weight:500;padding:10px 0 10px 16px;color:var(--navy2)}
.nav-cta{background:var(--navy2);color:var(--white)!important;padding:12px 24px!important;border-radius:50px!important;font-weight:600!important;transition:background .2s!important;white-space:nowrap;flex-shrink:0}
.nav-cta:hover{background:var(--blue)!important}

/* ── PAGE HERO (inner pages) ── */
.page-hero{background:linear-gradient(135deg,var(--navy) 0%,var(--navy2) 60%,#1a3a5c 100%);padding:80px var(--gutter) 72px;position:relative;overflow:hidden}
.page-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 60% 80% at 70% 50%,rgba(45,82,160,.18) 0%,transparent 70%)}
.page-hero-inner{max-width:var(--max);margin:0 auto;position:relative;z-index:1}
.page-hero-eyebrow{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:50px;padding:6px 16px;font-size:12px;font-weight:600;letter-spacing:1.5px;color:var(--gold);text-transform:uppercase;margin-bottom:24px}
.page-hero h1{font-family:'DM Serif Display',serif;font-size:clamp(40px,5vw,72px);color:var(--white);line-height:1.1;margin-bottom:20px;max-width:900px}
.page-hero h1 em{font-style:italic;color:var(--blue-light)}
.page-hero h1 strong{color:var(--gold)}
.page-hero-sub{font-size:clamp(16px,1.5vw,20px);color:rgba(255,255,255,.78);line-height:1.7;max-width:700px;margin-bottom:36px}
.page-hero-badges{display:flex;flex-wrap:wrap;gap:12px}
.hero-badge{display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:50px;padding:8px 18px;font-size:13px;color:rgba(255,255,255,.85);font-weight:500}
.hero-badge-dot{width:6px;height:6px;border-radius:50%;background:var(--green);flex-shrink:0}

/* ── WRAP ── */
.wrap{max-width:var(--max);margin:0 auto;padding:0 var(--gutter)}

/* ── SECTION TITLES ── */
.section-eyebrow{font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--blue);margin-bottom:12px}
.section-title{font-family:'DM Serif Display',serif;font-size:clamp(32px,3.5vw,52px);line-height:1.15;color:var(--navy);margin-bottom:16px}
.section-title em{font-style:italic;color:var(--blue)}
.section-title strong{color:var(--gold)}
.section-sub{font-size:17px;color:var(--gray);line-height:1.7;max-width:680px}

/* ── CONTENT SECTIONS ── */
.section{padding:96px 0}
.section-alt{background:var(--off-white)}
.section-dark{background:var(--navy);color:var(--white)}
.section-dark .section-eyebrow{color:var(--blue-light)}
.section-dark .section-title{color:var(--white)}
.section-dark .section-sub{color:rgba(255,255,255,.72)}

/* ── CARDS ── */
.card-grid{display:grid;gap:24px}
.card-grid-2{grid-template-columns:repeat(2,1fr)}
.card-grid-3{grid-template-columns:repeat(3,1fr)}
.card-grid-4{grid-template-columns:repeat(4,1fr)}
.card{background:var(--white);border-radius:var(--radius);padding:36px 32px;box-shadow:0 2px 16px rgba(0,0,0,.06);border:1px solid var(--gray-light);transition:transform .25s,box-shadow .25s;position:relative;overflow:hidden}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--blue);border-radius:var(--radius) var(--radius) 0 0}
.card:hover{transform:translateY(-4px);box-shadow:0 8px 32px rgba(0,0,0,.1)}
.card-icon{font-size:32px;margin-bottom:16px}
.card-title{font-family:'DM Serif Display',serif;font-size:22px;color:var(--navy);margin-bottom:10px}
.card-body{font-size:15px;color:var(--gray);line-height:1.7}
.card-dark{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);color:var(--white)}
.card-dark::before{background:var(--gold)}
.card-dark .card-title{color:var(--white)}
.card-dark .card-body{color:rgba(255,255,255,.72)}

/* ── TWO-COLUMN LAYOUT ── */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start}
.two-col-60{grid-template-columns:3fr 2fr}
.two-col-40{grid-template-columns:2fr 3fr}

/* ── PROSE ── */
.prose h2{font-family:'DM Serif Display',serif;font-size:clamp(26px,2.5vw,38px);color:var(--navy);margin:40px 0 16px;line-height:1.2}
.prose h3{font-family:'DM Serif Display',serif;font-size:22px;color:var(--navy);margin:28px 0 10px}
.prose p{font-size:16px;color:#374151;line-height:1.8;margin-bottom:16px}
.prose ul,.prose ol{margin:16px 0 16px 24px}
.prose li{font-size:16px;color:#374151;line-height:1.7;margin-bottom:8px}
.prose strong{color:var(--navy);font-weight:600}
.prose-dark p,.prose-dark li{color:rgba(255,255,255,.8)}
.prose-dark h2,.prose-dark h3{color:var(--white)}

/* ── STEPS ── */
.steps-list{display:flex;flex-direction:column;gap:0}
.step-item{display:grid;grid-template-columns:64px 1fr;gap:24px;padding:32px 0;border-bottom:1px solid var(--gray-light);align-items:start}
.step-item:last-child{border-bottom:none}
.step-num-circle{width:56px;height:56px;border-radius:50%;background:var(--navy);color:var(--white);display:flex;align-items:center;justify-content:center;font-family:'DM Serif Display',serif;font-size:22px;flex-shrink:0}
.step-content h3{font-family:'DM Serif Display',serif;font-size:22px;color:var(--navy);margin-bottom:8px}
.step-content p{font-size:15px;color:var(--gray);line-height:1.7}
.step-content ul{margin:10px 0 0 20px}
.step-content li{font-size:14px;color:var(--gray);line-height:1.6;margin-bottom:4px}

/* ── SYMPTOM LIST ── */
.symptom-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.symptom-item{display:flex;align-items:flex-start;gap:10px;padding:14px 16px;background:var(--off-white);border-radius:10px;font-size:14px;color:var(--navy2);font-weight:500;line-height:1.4}
.symptom-dot{width:8px;height:8px;border-radius:50%;background:var(--blue);flex-shrink:0;margin-top:4px}
.symptom-grid-dark .symptom-item{background:rgba(255,255,255,.07);color:rgba(255,255,255,.85)}
.symptom-grid-dark .symptom-dot{background:var(--gold)}

/* ── CALLOUT BOX ── */
.callout{border-left:4px solid var(--gold);background:rgba(201,168,76,.08);padding:24px 28px;border-radius:0 12px 12px 0;margin:32px 0}
.callout-icon{font-size:20px;margin-bottom:8px}
.callout-title{font-weight:700;color:var(--navy);margin-bottom:6px;font-size:16px}
.callout-body{font-size:15px;color:#374151;line-height:1.7}
.callout-dark{border-left-color:var(--gold);background:rgba(201,168,76,.1)}
.callout-dark .callout-title{color:var(--white)}
.callout-dark .callout-body{color:rgba(255,255,255,.78)}

/* ── COMPARISON TABLE ── */
.compare-table{width:100%;border-collapse:collapse;font-size:15px}
.compare-table th{background:var(--navy);color:var(--white);padding:14px 20px;text-align:left;font-weight:600;font-size:13px;letter-spacing:.5px}
.compare-table td{padding:14px 20px;border-bottom:1px solid var(--gray-light);color:#374151;line-height:1.5}
.compare-table tr:nth-child(even) td{background:var(--off-white)}
.compare-table .check{color:var(--green);font-weight:700}
.compare-table .cross{color:#ef4444;font-weight:700}

/* ── QUOTE ── */
.blockquote{border-left:4px solid var(--blue);padding:24px 32px;background:var(--off-white);border-radius:0 12px 12px 0;margin:32px 0}
.blockquote-text{font-family:'DM Serif Display',serif;font-size:22px;color:var(--navy);line-height:1.5;font-style:italic;margin-bottom:12px}
.blockquote-attr{font-size:13px;color:var(--gray);font-weight:600;letter-spacing:.5px;text-transform:uppercase}
.blockquote-dark{background:rgba(255,255,255,.05);border-left-color:var(--gold)}
.blockquote-dark .blockquote-text{color:var(--white)}
.blockquote-dark .blockquote-attr{color:var(--gold)}

/* ── CTA STRIP ── */
.cta-strip{background:var(--navy);padding:80px var(--gutter);text-align:center;position:relative;overflow:hidden}
.cta-strip::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 50% 80% at 50% 50%,rgba(201,168,76,.12) 0%,transparent 70%)}
.cta-strip-inner{max-width:700px;margin:0 auto;position:relative;z-index:1}
.cta-strip h2{font-family:'DM Serif Display',serif;font-size:clamp(32px,3.5vw,48px);color:var(--white);margin-bottom:16px;line-height:1.2}
.cta-strip p{font-size:18px;color:rgba(255,255,255,.72);margin-bottom:36px;line-height:1.6}
.cta-buttons{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:8px;padding:16px 32px;border-radius:50px;font-size:15px;font-weight:600;cursor:pointer;border:none;transition:all .25s;text-decoration:none}
.btn-gold{background:var(--gold);color:var(--navy)}
.btn-gold:hover{background:var(--gold2);transform:translateY(-2px)}
.btn-outline{background:transparent;color:var(--white);border:2px solid rgba(255,255,255,.3)}
.btn-outline:hover{border-color:var(--white);background:rgba(255,255,255,.08)}
.btn-navy{background:var(--navy);color:var(--white)}
.btn-navy:hover{background:var(--blue)}

/* ── FOOTER ── */
.footer{background:#0a0f1a;padding:72px var(--gutter) 40px}
.footer-inner{max-width:var(--max);margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:60px;margin-bottom:56px}
.footer-brand p{font-size:14px;color:rgba(255,255,255,.55);line-height:1.7;margin-top:16px;max-width:280px}
.footer-logo{height:60px;width:auto;object-fit:contain;filter:brightness(0) invert(1);opacity:.85}
.footer-col h4{font-size:12px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:rgba(255,255,255,.4);margin-bottom:20px}
.footer-col a{display:block;font-size:14px;color:rgba(255,255,255,.65);margin-bottom:10px;transition:color .2s}
.footer-col a:hover{color:var(--gold)}
.footer-bottom{max-width:var(--max);margin:0 auto;padding-top:32px;border-top:1px solid rgba(255,255,255,.08);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}
.footer-copy{font-size:13px;color:rgba(255,255,255,.35)}
.footer-links{display:flex;gap:20px}
.footer-links a{font-size:13px;color:rgba(255,255,255,.35);transition:color .2s}
.footer-links a:hover{color:rgba(255,255,255,.7)}

/* ── BREADCRUMB ── */
.breadcrumb{background:var(--off-white);padding:14px var(--gutter);border-bottom:1px solid var(--gray-light)}
.breadcrumb-inner{max-width:var(--max);margin:0 auto;display:flex;align-items:center;gap:8px;font-size:13px;color:var(--gray)}
.breadcrumb a{color:var(--blue);font-weight:500}
.breadcrumb a:hover{text-decoration:underline}
.breadcrumb-sep{color:var(--gray-light)}

/* ── SIDEBAR LAYOUT ── */
.sidebar-layout{display:grid;grid-template-columns:1fr 320px;gap:64px;align-items:start}
.sticky-sidebar{position:sticky;top:120px}
.sidebar-card{background:var(--off-white);border-radius:var(--radius);padding:32px;border:1px solid var(--gray-light);margin-bottom:24px}
.sidebar-card h3{font-family:'DM Serif Display',serif;font-size:20px;color:var(--navy);margin-bottom:16px}
.sidebar-cta{background:var(--navy);border-radius:var(--radius);padding:32px;text-align:center}
.sidebar-cta h3{font-family:'DM Serif Display',serif;font-size:22px;color:var(--white);margin-bottom:12px}
.sidebar-cta p{font-size:14px;color:rgba(255,255,255,.7);margin-bottom:20px;line-height:1.6}
.sidebar-cta .btn{width:100%;justify-content:center;margin-bottom:10px}

/* ── PROCESS TIMELINE ── */
.timeline{position:relative;padding-left:48px}
.timeline::before{content:'';position:absolute;left:20px;top:8px;bottom:8px;width:2px;background:var(--gray-light)}
.timeline-item{position:relative;margin-bottom:40px}
.timeline-dot{position:absolute;left:-36px;top:4px;width:32px;height:32px;border-radius:50%;background:var(--navy);color:var(--white);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;z-index:1}
.timeline-item h3{font-family:'DM Serif Display',serif;font-size:20px;color:var(--navy);margin-bottom:8px}
.timeline-item p{font-size:15px;color:var(--gray);line-height:1.7}
.timeline-item ul{margin:8px 0 0 20px}
.timeline-item li{font-size:14px;color:var(--gray);line-height:1.6;margin-bottom:4px}

/* ── STAT BADGES ── */
.stat-row{display:flex;gap:24px;flex-wrap:wrap;margin:32px 0}
.stat-badge{background:var(--navy);color:var(--white);border-radius:12px;padding:20px 28px;text-align:center;min-width:140px}
.stat-badge-num{font-family:'DM Serif Display',serif;font-size:36px;color:var(--gold);line-height:1}
.stat-badge-label{font-size:12px;color:rgba(255,255,255,.65);margin-top:4px;line-height:1.3}

/* ── TABLET ── */
@media(min-width:769px) and (max-width:1024px){
  :root{--gutter:32px}
  .two-col,.two-col-60,.two-col-40{grid-template-columns:1fr;gap:40px}
  .card-grid-3,.card-grid-4{grid-template-columns:repeat(2,1fr)}
  .sidebar-layout{grid-template-columns:1fr;gap:40px}
  .sticky-sidebar{position:static}
  .footer-inner{grid-template-columns:1fr 1fr;gap:40px}
  .symptom-grid{grid-template-columns:repeat(2,1fr)}
  .nav-logo{height:68px}
  .nav .wrap{height:88px}
  .topbar-info{gap:16px}
}

/* ── MOBILE ── */
@media(max-width:768px){
  :root{--gutter:20px}
  .topbar{padding:10px var(--gutter)}
  .topbar-info{display:none}
  .topbar-right .topbar-link{display:none}
  .nav .wrap{height:72px}
  .nav-logo{height:52px}
  .nav-links{display:none}
  .nav-hamburger{display:flex}
  .nav-cta{display:none}
  .page-hero{padding:56px var(--gutter) 48px}
  .section{padding:60px 0}
  .two-col,.two-col-60,.two-col-40{grid-template-columns:1fr;gap:32px}
  .card-grid-2,.card-grid-3,.card-grid-4{grid-template-columns:1fr}
  .sidebar-layout{grid-template-columns:1fr;gap:32px}
  .sticky-sidebar{position:static}
  .footer-inner{grid-template-columns:1fr;gap:32px}
  .footer-bottom{flex-direction:column;text-align:center}
  .symptom-grid{grid-template-columns:1fr}
  .step-item{grid-template-columns:48px 1fr;gap:16px}
  .cta-strip{padding:60px var(--gutter)}
  .breadcrumb{padding:12px var(--gutter)}
  .stat-row{gap:12px}
  .stat-badge{min-width:100px;padding:16px 20px}
}
"""

# ── Nav HTML ─────────────────────────────────────────────────────────────────
def nav_html(active=''):
    def is_active(label):
        return 'active' if label.lower() in active.lower() else ''
    home_cls = is_active('home')
    about_cls = is_active('about')
    phys_cls = is_active('physician')
    contact_cls = is_active('contact')
    sleep_cls = is_active('sleep') or is_active('snoring') or is_active('adult airway')
    treat_cls = is_active('tonsil') or is_active('tongue') or is_active('nrt') or is_active('nasal')
    child_cls = is_active('children')
    return f"""<div class="topbar">
  <div class="topbar-info">
    <span class="topbar-item"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>348 Alhambra Circle, Coral Gables</span>
    <span class="topbar-item"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 01.22 1.22 2 2 0 012.22 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.09a16 16 0 006 6l.66-.66a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>(305) 447-9199</span>
    <span class="topbar-item"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>dentistry@lesliehallerdmd.com</span>
  </div>
  <div class="topbar-right">
    <a href="physician-referral.html" class="topbar-link">Physician Referrals</a>
  </div>
</div>
<nav class="nav">
  <div class="wrap">
    <a href="index.html"><img src="{LOGO}" alt="Dental Solutions of South Florida" class="nav-logo"></a>
    <div class="nav-links">
      <a href="index.html" class="nav-link {home_cls}">Home</a>
      <div class="nav-item">
        <a href="sleep-apnea.html" class="nav-link {sleep_cls}">Sleep &amp; Airway</a>
        <div class="nav-dropdown">
          <a href="sleep-apnea.html">Sleep Apnea &amp; Oral Appliances</a>
          <a href="snoring.html">Laser Snoring Treatment</a>
          <a href="adult-airway.html">Adult Airway Expansion</a>
          <a href="nrt.html">Nasal Release Therapy</a>
        </div>
      </div>
      <div class="nav-item">
        <a href="tonsils.html" class="nav-link {treat_cls}">Treatments</a>
        <div class="nav-dropdown">
          <a href="tongue-tie.html">Tongue Tie Frenectomy</a>
          <a href="tonsils.html">CO2 Laser Tonsils</a>
          <a href="adult-airway.html">Epigenetic Arch Expansion</a>
          <a href="nrt.html">Nasal Release Therapy</a>
        </div>
      </div>
      <div class="nav-item">
        <a href="childrens-airway.html" class="nav-link {child_cls}">Children</a>
        <div class="nav-dropdown">
          <a href="childrens-airway.html">Children&#39;s Airway &amp; Orthodontics</a>
          <a href="tongue-tie.html">Tongue Tie (Infants &amp; Children)</a>
          <a href="tonsils.html">CO2 Laser Tonsils</a>
        </div>
      </div>
      <div class="nav-item">
        <a href="#" class="nav-link {about_cls}">About</a>
        <div class="nav-dropdown">
          <a href="index.html#dr-haller">Dr. Leslie Haller</a>
          <a href="index.html#philosophy">Our Philosophy</a>
          <a href="physician-referral.html">For Physicians</a>
        </div>
      </div>
      <a href="physician-referral.html" class="nav-link {phys_cls}">Physicians</a>
      <a href="index.html#contact" class="nav-link {contact_cls}">Contact</a>
    </div>
    <button class="nav-hamburger" aria-label="Open menu" onclick="document.getElementById('navMobile').classList.toggle('open');this.classList.toggle('open')">
      <span></span><span></span><span></span>
    </button>
    <a href="index.html#contact" class="btn btn-navy nav-cta">Book Appointment</a>
  </div>
</nav>
<!-- MOBILE NAV DRAWER -->
<div class="nav-mobile" id="navMobile">
  <div class="nav-mobile-header">
    <img src="{LOGO}" alt="Dental Solutions of South Florida" style="height:52px">
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
  <a href="index.html#dr-haller" class="mob-sub">Dr. Leslie Haller</a>
  <a href="physician-referral.html" class="mob-sub">For Physicians</a>
  <a href="physician-referral.html">Physician Referrals</a>
  <a href="index.html#contact">Contact</a>
  <a href="index.html#contact" style="margin-top:24px;background:var(--navy);color:white;text-align:center;border-radius:50px;padding:16px 24px">Book Appointment</a>
</div>"""

# ── Footer HTML ───────────────────────────────────────────────────────────────
FOOTER_HTML = f"""
<footer class="footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <img src="{LOGO_T}" alt="Dental Solutions of South Florida" class="footer-logo" style="height:56px;filter:none;opacity:1">
      <p>Airway-focused dental care for adults and children. Harvard-trained. Board certified in laser dentistry and dental sleep medicine.</p>
      <p style="margin-top:12px;font-size:13px;color:rgba(255,255,255,.4)">348 Alhambra Circle · Coral Gables, FL 33134<br>(305) 447-9199 · dentistry@lesliehallerdmd.com</p>
    </div>
    <div class="footer-col">
      <h4>Sleep &amp; Airway</h4>
      <a href="sleep-apnea.html">Sleep Apnea</a>
      <a href="snoring.html">Snoring Laser Treatment</a>
      <a href="adult-airway.html">Adult Airway Expansion</a>
      <a href="nrt.html">Nasal Release Therapy</a>
    </div>
    <div class="footer-col">
      <h4>Treatments</h4>
      <a href="tongue-tie.html">Tongue Tie Frenectomy</a>
      <a href="tonsils.html">CO2 Laser Tonsils</a>
      <a href="childrens-airway.html">Children's Airway</a>
      <a href="physician-referral.html">Physician Referrals</a>
    </div>
    <div class="footer-col">
      <h4>Practice</h4>
      <a href="about.html">About Dr. Haller</a>
      <a href="physician-referral.html">For Physicians</a>
      <a href="index.html#contact">Request Appointment</a>
      <a href="index.html#contact">Contact</a>
    </div>
  </div>
  <div class="footer-bottom">
    <p class="footer-copy">© 2025 Dental Solutions of South Florida · Leslie Haller, DMD · 348 Alhambra Circle, Coral Gables, FL 33134</p>
    <div class="footer-links">
      <a href="#">Privacy Policy</a>
      <a href="#">Accessibility</a>
    </div>
  </div>
</footer>"""

# ── Page wrapper ──────────────────────────────────────────────────────────────
def page(title, meta_desc, active, breadcrumb_label, body_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<style>{SHARED_CSS}</style>
</head>
<body>
{nav_html(active)}
<nav class="breadcrumb" aria-label="Breadcrumb">
  <div class="breadcrumb-inner">
    <a href="index.html">Home</a>
    <span class="breadcrumb-sep">›</span>
    <span>{breadcrumb_label}</span>
  </div>
</nav>
{body_html}
{FOOTER_HTML}
</body>
</html>"""


# ════════════════════════════════════════════════════════════════════════════
# PAGE BUILDERS
# ════════════════════════════════════════════════════════════════════════════

def build_sleep_apnea():
    body = """
<section class="page-hero">
  <div class="page-hero-inner">
    <div class="page-hero-eyebrow"><span class="hero-badge-dot"></span>Sleep Apnea Treatment</div>
    <h1>A CPAP Alternative<br>That <em>Actually</em> Works</h1>
    <p class="page-hero-sub">Custom oral appliances for diagnosed sleep apnea. Covered by medical insurance. No mask, no machine, no noise — just better sleep.</p>
    <div class="page-hero-badges">
      <span class="hero-badge"><span class="hero-badge-dot"></span>Medical Insurance Accepted</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>Board Certified in Dental Sleep Medicine</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>CPAP Intolerant? We Can Help</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sidebar-layout">
      <div class="prose">
        <p class="section-eyebrow">What Is Sleep Apnea?</p>
        <h2>Your airway collapses while you sleep</h2>
        <p>Obstructive sleep apnea (OSA) occurs when the soft tissues of the throat relax during sleep and partially or completely block the airway. Each blockage is an "apnea event" — your brain jolts you partially awake to restore breathing. This can happen hundreds of times per night, fragmenting sleep and starving the body of oxygen.</p>
        <p>Most patients have no idea it's happening. Their partner hears the snoring and gasping. They just feel exhausted, foggy, and unwell — often for years before a diagnosis.</p>

        <div class="callout">
          <div class="callout-icon">⚠️</div>
          <div class="callout-title">Untreated sleep apnea is a serious medical condition</div>
          <div class="callout-body">Untreated OSA is associated with significantly elevated risk of hypertension, stroke, heart attack, type 2 diabetes, depression, and motor vehicle accidents. It is not just snoring.</div>
        </div>

        <h2>Symptoms of sleep apnea</h2>
        <div class="symptom-grid" style="margin:20px 0">
          <div class="symptom-item"><span class="symptom-dot"></span>Loud or chronic snoring</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Gasping or choking during sleep</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Witnessed apneas (partner reports you stop breathing)</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Waking unrefreshed despite 7–8 hours</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Excessive daytime sleepiness</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Falling asleep at inappropriate times</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Morning headaches</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Dry mouth or sore throat on waking</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Bruxism (teeth grinding)</div>
          <div class="symptom-item"><span class="symptom-dot"></span>TMJ pain or jaw clicking</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Frequent nighttime urination</div>
          <div class="symptom-item"><span class="symptom-dot"></span>High blood pressure resistant to medication</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Chronic neck or shoulder pain</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Brain fog, poor concentration</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Mood swings, irritability</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Depression or anxiety</div>
          <div class="symptom-item"><span class="symptom-dot"></span>ADHD-like symptoms</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Acid reflux at night</div>
        </div>

        <h2>The MAD device — how it works</h2>
        <p>A mandibular advancement device (MAD) is a custom-fitted oral appliance worn during sleep. It holds the lower jaw slightly forward, which keeps the airway open and prevents the soft tissue collapse that causes apnea events.</p>
        <p>Unlike CPAP, a MAD is silent, portable, and requires no mask, hose, or electricity. Most patients adapt within 1–2 weeks. For mild to moderate OSA, MAD therapy achieves outcomes comparable to CPAP — and dramatically higher compliance rates.</p>

        <div class="card-grid card-grid-2" style="margin:28px 0">
          <div class="card" style="--card-accent:#2d52a0">
            <div class="card-icon">😷</div>
            <div class="card-title">CPAP</div>
            <div class="card-body">Pressurized air via mask. Highly effective but ~50% of patients are non-compliant within 1 year due to discomfort, noise, and inconvenience.</div>
          </div>
          <div class="card" style="border-top-color:var(--green)">
            <div class="card-icon">😴</div>
            <div class="card-title">MAD Device</div>
            <div class="card-body">Custom oral appliance. Silent, portable, no mask. Comparable efficacy for mild–moderate OSA. 80%+ long-term compliance. Covered by medical insurance.</div>
          </div>
        </div>

        <h2>Insurance coverage</h2>
        <p>MAD therapy for diagnosed sleep apnea is billable to <strong>medical insurance</strong> — not dental insurance. Most major medical plans, including Medicare, cover oral appliance therapy when a sleep study confirms the diagnosis. Dr. Haller's team handles the insurance coordination.</p>
        <p>A sleep study (polysomnography or home sleep test) is required before treatment. If you don't have one, we can refer you to a sleep physician.</p>

        <h2>The bigger picture — structural solutions</h2>
        <p>For patients who want a permanent solution rather than a nightly appliance, <strong>epigenetic arch expansion</strong> widens the dental arch and nasal passages — creating a structurally larger airway. This is the only treatment that addresses the anatomical root cause of sleep apnea rather than managing symptoms.</p>
        <p>Dr. Haller has trained extensively with the leading innovators in this field and uses multiple appliance systems tailored to each patient's anatomy and goals.</p>
      </div>

      <div class="sticky-sidebar">
        <div class="sidebar-cta">
          <h3>Ready to sleep better?</h3>
          <p>Book a consultation with Dr. Haller. We'll review your sleep study, evaluate your airway, and recommend the right treatment.</p>
          <a href="index.html#contact" class="btn btn-gold">Book a Consultation</a>
          <a href="tel:3054479199" class="btn btn-outline" style="color:rgba(255,255,255,.8)">Call (305) 447-9199</a>
        </div>
        <div class="sidebar-card">
          <h3>Do you have a sleep study?</h3>
          <p style="font-size:14px;color:var(--gray);line-height:1.6;margin-bottom:12px">A diagnosis is required before we can fabricate a MAD device. If you don't have a sleep study, we can refer you to a sleep physician in our network.</p>
          <a href="index.html#contact" class="btn btn-navy" style="font-size:14px;padding:12px 20px">Get a Referral</a>
        </div>
        <div class="sidebar-card">
          <h3>Related treatments</h3>
          <a href="snoring.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ Laser Snoring Treatment</a>
          <a href="adult-airway.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ Epigenetic Airway Expansion</a>
          <a href="nrt.html" style="display:block;color:var(--blue);font-size:14px;font-weight:500">→ Nasal Release Therapy</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="cta-strip-inner">
    <h2>Stop managing sleep apnea.<br><em>Treat it.</em></h2>
    <p>Custom oral appliances, epigenetic expansion, and a physician who connects the dots. Covered by medical insurance.</p>
    <div class="cta-buttons">
      <a href="index.html#contact" class="btn btn-gold">Book a Consultation →</a>
      <a href="physician-referral.html" class="btn btn-outline">For Physicians</a>
    </div>
  </div>
</section>"""
    return page(
        "Sleep Apnea Treatment — CPAP Alternative — Dental Solutions of South Florida",
        "Custom oral appliances for diagnosed sleep apnea. Covered by medical insurance. Board certified dental sleep medicine in Coral Gables, FL.",
        "Sleep & Airway", "Sleep Apnea & Oral Appliances", body)


def build_tonsils():
    body = """
<section class="page-hero">
  <div class="page-hero-inner">
    <div class="page-hero-eyebrow"><span class="hero-badge-dot"></span>CO2 Laser Treatment</div>
    <h1>Try Laser<br>Before <strong>Surgery</strong></h1>
    <p class="page-hero-sub">Non-surgical tonsil reduction via fractional CO2 laser. Eliminates chronic bacterial biofilm. Tonsils measurably shrink within days — no hospital, no anesthesia, no recovery time.</p>
    <div class="page-hero-badges">
      <span class="hero-badge"><span class="hero-badge-dot"></span>No Surgery Required</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>10–15 Min Per Session</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>Well-Tolerated by Children</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sidebar-layout">
      <div class="prose">
        <p class="section-eyebrow">Why Tonsils Enlarge</p>
        <h2>The real cause is chronic bacterial biofilm</h2>
        <p>Enlarged tonsils are almost always the result of chronic bacterial colonization — not a single acute infection. Here's the chain:</p>
        <div class="steps-list" style="margin:24px 0">
          <div class="step-item">
            <div class="step-num-circle">1</div>
            <div class="step-content"><h3>Mouth breathing is the underlying cause</h3><p>The nose filters, humidifies, and cleans air before it reaches the tonsils. Mouth breathing bypasses all of this — delivering unfiltered, bacteria-laden air directly to tonsil tissue.</p></div>
          </div>
          <div class="step-item">
            <div class="step-num-circle">2</div>
            <div class="step-content"><h3>Bacteria form a protective biofilm</h3><p>Once established, bacteria form a biofilm deep in tonsillar crypts that is shielded from antibiotics. This is why antibiotics provide temporary relief but tonsils keep enlarging.</p></div>
          </div>
          <div class="step-item">
            <div class="step-num-circle">3</div>
            <div class="step-content"><h3>Chronic immune response keeps tonsils swollen</h3><p>The body's ongoing immune response to the biofilm maintains chronic inflammation — keeping tonsil tissue permanently enlarged.</p></div>
          </div>
          <div class="step-item">
            <div class="step-num-circle">4</div>
            <div class="step-content"><h3>Result: narrowed airway and disrupted sleep</h3><p>Enlarged tonsils obstruct the airway, causing snoring, sleep apnea, ADHD-like symptoms, halitosis, and chronic fatigue.</p></div>
          </div>
        </div>

        <div class="callout">
          <div class="callout-icon">⚠️</div>
          <div class="callout-title">Treating tonsils without addressing mouth breathing is like bailing a boat without plugging the hole</div>
          <div class="callout-body">If mouth breathing continues after treatment, tonsils are likely to enlarge again. Laser decontamination is most effective when combined with a plan to restore nasal breathing.</div>
        </div>

        <h2>How the CO2 laser works</h2>
        <p>Dr. Haller uses a specialized CO2 laser attachment designed specifically for tonsillar crypts. Here's what happens at each session:</p>
        <div class="card-grid card-grid-2" style="margin:20px 0">
          <div class="card"><div class="card-icon">🔬</div><div class="card-title">Eliminates biofilm</div><div class="card-body">Photobiomodulation eliminates chronic bacterial biofilm at the source — deep in tonsillar crypts where antibiotics can't reach.</div></div>
          <div class="card"><div class="card-icon">🩸</div><div class="card-title">Reduces engorgement</div><div class="card-body">Thermal energy reduces vascular engorgement and stimulates lymphatic drainage — tonsils measurably shrink as chronic inflammation resolves.</div></div>
          <div class="card"><div class="card-icon">⏱️</div><div class="card-title">10–15 minutes total</div><div class="card-body">Sessions are brief. Most patients — including children — feel mild warmth at most. No topical anesthetic needed in most cases.</div></div>
          <div class="card"><div class="card-icon">🏫</div><div class="card-title">Same-day return</div><div class="card-body">No hospital, no recovery time. Patients return to school or work immediately after each session.</div></div>
        </div>

        <h2>Symptoms that respond to laser treatment</h2>
        <div class="symptom-grid" style="margin:20px 0">
          <div class="symptom-item"><span class="symptom-dot"></span>Persistent bad breath despite good oral hygiene</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Visible white or yellow spots on tonsils</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Foreign body sensation or throat tightness</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Metallic taste in the mouth</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Chronic sore throat or difficulty swallowing</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Recurrent coughing or choking sensation</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Snoring or sleep-disordered breathing</div>
          <div class="symptom-item"><span class="symptom-dot"></span>ADHD-like symptoms in children</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Restless sleep, bedwetting</div>
        </div>

        <h2>Tonsil grading scale</h2>
        <p>Tonsil size is graded 1–4 based on how much of the airway the tonsils occupy. Dr. Haller photographs tonsils at every visit to track objective reduction.</p>
        <table class="compare-table" style="margin:20px 0">
          <thead><tr><th>Grade</th><th>Description</th><th>Airway Obstruction</th><th>Laser Recommendation</th></tr></thead>
          <tbody>
            <tr><td><strong>Grade 1</strong></td><td>Tonsils visible but within the pillars</td><td>&lt;25%</td><td>Monitor &amp; maintain nasal breathing</td></tr>
            <tr><td><strong>Grade 2</strong></td><td>Tonsils extend to edge of pillars</td><td>25–50%</td><td class="check">✓ Highly effective</td></tr>
            <tr><td><strong>Grade 3</strong></td><td>Tonsils extend past pillars toward midline</td><td>50–75%</td><td class="check">✓ Effective — try before surgery</td></tr>
            <tr><td><strong>Grade 4</strong></td><td>"Kissing tonsils" — meet at midline</td><td>&gt;75%</td><td>Surgical consult likely indicated</td></tr>
          </tbody>
        </table>

        <h2>What to expect — step by step</h2>
        <div class="timeline">
          <div class="timeline-item"><div class="timeline-dot">1</div><h3>Initial evaluation &amp; grading</h3><p>Dr. Haller photographs and grades tonsils using standardized intraoral imaging. She also evaluates airway anatomy, jaw development, tongue posture, and signs of sleep-disordered breathing.</p></div>
          <div class="timeline-item"><div class="timeline-dot">2</div><h3>Treatment planning</h3><p>A customized protocol is created based on tonsil grade, bacterial load, age, and the patient's airway goals. Co-existing issues may be addressed in parallel.</p></div>
          <div class="timeline-item"><div class="timeline-dot">3</div><h3>CO2 laser treatment sessions</h3><p>The specialized tonsillar laser attachment is applied to each tonsil for a few minutes per session. Most patients feel mild warmth at most. Sessions are 10–15 minutes total.</p></div>
          <div class="timeline-item"><div class="timeline-dot">4</div><h3>Progress monitoring</h3><p>Tonsils are photographed and graded at every visit. Families can see measurable reduction within days. A typical full course is 3–6 sessions spaced 1–2 weeks apart.</p></div>
        </div>
      </div>

      <div class="sticky-sidebar">
        <div class="sidebar-cta">
          <h3>Try laser before surgery</h3>
          <p>Book an evaluation with Dr. Haller. We'll grade your tonsils, review your airway, and create a treatment plan.</p>
          <a href="index.html#contact" class="btn btn-gold">Book Evaluation</a>
          <a href="tel:3054479199" class="btn btn-outline" style="color:rgba(255,255,255,.8)">Call (305) 447-9199</a>
        </div>
        <div class="sidebar-card">
          <h3>When surgery may still be needed</h3>
          <ul style="font-size:14px;color:var(--gray);line-height:1.7;padding-left:16px">
            <li>Grade 4 ("kissing") tonsils from the outset</li>
            <li>Airway obstruction causing oxygen desaturation</li>
            <li>No measurable reduction after full laser course</li>
            <li>Recurrent peritonsillar abscess history</li>
          </ul>
          <p style="font-size:13px;color:var(--gray);margin-top:12px">We coordinate directly with your ENT throughout the process.</p>
        </div>
        <div class="sidebar-card">
          <h3>Related treatments</h3>
          <a href="tongue-tie.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ Tongue Tie Release</a>
          <a href="nrt.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ Nasal Release Therapy</a>
          <a href="adult-airway.html" style="display:block;color:var(--blue);font-size:14px;font-weight:500">→ Airway Expansion</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="cta-strip-inner">
    <h2>Don't rush to surgery.<br><em>Try laser first.</em></h2>
    <p>Non-surgical tonsil reduction. No hospital, no anesthesia, no recovery time. Results visible within days.</p>
    <div class="cta-buttons">
      <a href="index.html#contact" class="btn btn-gold">Book an Evaluation →</a>
      <a href="physician-referral.html" class="btn btn-outline">For Physicians</a>
    </div>
  </div>
</section>"""
    return page(
        "Tonsil Decontamination — Try Laser Before Surgery — Dental Solutions of South Florida",
        "Non-surgical CO2 laser tonsil reduction in Coral Gables, FL. No hospital, no anesthesia. Tonsils measurably shrink within days.",
        "Treatments", "CO2 Laser Tonsil Treatment", body)


def build_tongue_tie():
    body = """
<section class="page-hero">
  <div class="page-hero-inner">
    <div class="page-hero-eyebrow"><span class="hero-badge-dot"></span>CO2 Laser Frenectomy</div>
    <h1>Tongue Tie Release<br>for <em>Infants, Children</em><br>&amp; Adults</h1>
    <p class="page-hero-sub">CO2 laser frenectomy with minimal discomfort and rapid healing. Safe from 2 days old. No sutures, no bleeding, no general anesthesia for infants.</p>
    <div class="page-hero-badges">
      <span class="hero-badge"><span class="hero-badge-dot"></span>Safe from 2 Days Old</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>No Sutures or Bleeding</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>Hundreds of Releases Performed</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sidebar-layout">
      <div class="prose">
        <p class="section-eyebrow">Understanding Tongue Tie</p>
        <h2>When the tongue can't do its job</h2>
        <p>A tongue tie (ankyloglossia) occurs when the lingual frenulum — the band of tissue connecting the tongue to the floor of the mouth — is too short, too thick, or too tightly attached. This restricts tongue movement and affects everything from infant feeding to adult airway health.</p>
        <p>The tongue is designed to rest on the roof of the mouth (the palate). When it can't — because of a tie — it sits low in the mouth, forcing mouth breathing and setting off a chain of downstream effects: jaw underdevelopment, enlarged tonsils, disrupted sleep, and systemic health consequences.</p>

        <div class="callout">
          <div class="callout-icon">⚠️</div>
          <div class="callout-title">Posterior tongue ties are frequently missed</div>
          <div class="callout-body">Many tongue ties are not visible to the naked eye. A posterior tie is submucosal — it can only be identified by palpation and functional assessment. Dr. Haller evaluates for both anterior and posterior ties at every consultation.</div>
        </div>

        <h2>Symptoms by age group</h2>

        <h3>🍼 Infants</h3>
        <div class="symptom-grid" style="margin:16px 0 28px">
          <div class="symptom-item"><span class="symptom-dot"></span>Difficulty latching or maintaining latch</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Clicking or smacking sounds while nursing</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Excessive fussiness, colic, reflux from swallowed air</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Poor weight gain despite frequent feeding</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Falling asleep at breast from exhaustion</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Milk dribbling from corners of mouth</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Snoring or restless, unsettled sleep</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Reluctance to sleep on back</div>
        </div>

        <h3>👩 Nursing Mothers</h3>
        <div class="symptom-grid" style="margin:16px 0 28px">
          <div class="symptom-item"><span class="symptom-dot"></span>Severe nipple pain during or after nursing</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Cracked, creased, or blistered nipples</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Plugged ducts or mastitis from poor milk drainage</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Feeling like baby never gets enough</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Considering stopping breastfeeding due to pain</div>
        </div>

        <h3>🧒 Children &amp; Adults</h3>
        <div class="symptom-grid" style="margin:16px 0 28px">
          <div class="symptom-item"><span class="symptom-dot"></span>Mouth breathing</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Narrow palate or crowded teeth</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Speech difficulties (especially "l", "r", "t", "d")</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Snoring or sleep apnea</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Difficulty swallowing certain foods</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Neck and shoulder tension</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Forward head posture</div>
          <div class="symptom-item"><span class="symptom-dot"></span>TMJ pain or jaw clicking</div>
        </div>

        <h2>The CO2 laser procedure</h2>
        <p>Dr. Haller performs tongue tie releases using a CO2 laser — the gold standard for frenectomy. The laser vaporizes the restricted tissue with precision, causing minimal bleeding and dramatically reducing healing time compared to scissors or scalpel.</p>

        <div class="card-grid card-grid-2" style="margin:20px 0">
          <div class="card"><div class="card-icon">👶</div><div class="card-title">Infants (2 days+)</div><div class="card-body">No sutures, no bleeding, no general anesthesia. The procedure takes under 2 minutes. Most infants nurse immediately afterward. Topical anesthetic is applied.</div></div>
          <div class="card"><div class="card-icon">🧒</div><div class="card-title">Children</div><div class="card-body">Local anesthetic is used. The procedure is brief and well-tolerated. Children typically return to school the same day. Post-release stretches are provided.</div></div>
          <div class="card"><div class="card-icon">👤</div><div class="card-title">Adults</div><div class="card-body">Local anesthetic. Minimal discomfort during and after. Paired with myofunctional therapy for lasting functional results. Most patients notice immediate improvement in tongue mobility.</div></div>
          <div class="card"><div class="card-icon">🔄</div><div class="card-title">Myofunctional Therapy</div><div class="card-body">For children and adults, myofunctional therapy retrains tongue, face, and throat muscles after release — ensuring the tongue learns to rest and function correctly.</div></div>
        </div>

        <h2>After the release — what to expect</h2>
        <div class="timeline">
          <div class="timeline-item"><div class="timeline-dot">1</div><h3>Post-release stretches</h3><p>Stretching exercises are provided at the visit — every 4 hours for one week, then three times daily for three weeks. This prevents reattachment and ensures full range of motion.</p></div>
          <div class="timeline-item"><div class="timeline-dot">2</div><h3>Pain management</h3><p>Dr. Haller provides coconut oil with a hint of clove oil for pain relief. Breast milk popsicles can also help soothe the site in infants.</p></div>
          <div class="timeline-item"><div class="timeline-dot">3</div><h3>The healing site</h3><p>The diamond-shaped white scab is normal and healthy — not infection. It resolves within 2–3 weeks as the tissue heals from the inside out.</p></div>
          <div class="timeline-item"><div class="timeline-dot">4</div><h3>Myofunctional therapy</h3><p>Not required for infants — post-release stretches are sufficient. Recommended for children and adults to maximize functional outcomes.</p></div>
        </div>
      </div>

      <div class="sticky-sidebar">
        <div class="sidebar-cta">
          <h3>Is it a tongue tie?</h3>
          <p>Book a consultation with Dr. Haller. She evaluates for both anterior and posterior ties — including the submucosal ties that are frequently missed.</p>
          <a href="index.html#contact" class="btn btn-gold">Book Evaluation</a>
          <a href="tel:3054479199" class="btn btn-outline" style="color:rgba(255,255,255,.8)">Call (305) 447-9199</a>
        </div>
        <div class="sidebar-card">
          <h3>We coordinate with</h3>
          <ul style="font-size:14px;color:var(--gray);line-height:1.8;padding-left:16px">
            <li>Lactation consultants</li>
            <li>Myofunctional therapists</li>
            <li>Pediatric speech therapists</li>
            <li>ENTs and pediatricians</li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>Related treatments</h3>
          <a href="tonsils.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ CO2 Laser Tonsil Treatment</a>
          <a href="childrens-airway.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ Children's Airway</a>
          <a href="adult-airway.html" style="display:block;color:var(--blue);font-size:14px;font-weight:500">→ Airway Expansion</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="cta-strip-inner">
    <h2>Tongue tie affects more than<br><em>you might think.</em></h2>
    <p>From infant feeding to adult sleep apnea — a restricted tongue is often where the chain begins. Let's evaluate it.</p>
    <div class="cta-buttons">
      <a href="index.html#contact" class="btn btn-gold">Book an Evaluation →</a>
      <a href="physician-referral.html" class="btn btn-outline">Refer a Patient</a>
    </div>
  </div>
</section>"""
    return page(
        "Tongue Tie Frenectomy — Infants, Children & Adults — Dental Solutions of South Florida",
        "CO2 laser tongue tie release for infants, children, and adults in Coral Gables, FL. Safe from 2 days old. No sutures, no bleeding.",
        "Treatments", "Tongue Tie Release (Frenectomy)", body)


def build_nrt():
    body = """
<section class="page-hero">
  <div class="page-hero-inner">
    <div class="page-hero-eyebrow"><span class="hero-badge-dot"></span>Nasal Release Therapy</div>
    <h1>Open the Airway<br>from the <em>Inside</em></h1>
    <p class="page-hero-sub">Balloon-assisted cranial restriction release through the nasal passage. Particularly effective for patients with chronic nasal obstruction, head or facial trauma history, or difficult birth.</p>
    <div class="page-hero-badges">
      <span class="hero-badge"><span class="hero-badge-dot"></span>Non-Surgical</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>6–8 Sessions</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>Cumulative Results</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sidebar-layout">
      <div class="prose">
        <p class="section-eyebrow">What Is NRT?</p>
        <h2>Releasing cranial restrictions through the nasal passage</h2>
        <p>Nasal Release Therapy (NRT) is a specialized technique that uses a small balloon inserted into the nasal passage to release restrictions in the sphenopalatine ganglion and surrounding cranial structures. The balloon is briefly inflated, creating a gentle mobilization of the cranial bones and nasal structures.</p>
        <p>NRT is particularly effective for patients who have not responded to conventional nasal treatments — including those with a history of head or facial trauma, difficult birth (forceps, vacuum, prolonged labor), or chronic nasal obstruction that persists despite medication.</p>

        <h2>Who benefits from NRT?</h2>
        <div class="card-grid card-grid-2" style="margin:20px 0">
          <div class="card"><div class="card-icon">🤕</div><div class="card-title">Head or facial trauma</div><div class="card-body">Accidents, sports injuries, or falls that affected the skull, face, or nasal structures can create restrictions that NRT helps release.</div></div>
          <div class="card"><div class="card-icon">👶</div><div class="card-title">Difficult birth history</div><div class="card-body">Forceps delivery, vacuum extraction, or prolonged labor can create cranial compressions that persist into childhood and adulthood.</div></div>
          <div class="card"><div class="card-icon">👃</div><div class="card-title">Chronic nasal obstruction</div><div class="card-body">Patients who can't breathe through their nose despite medication, nasal sprays, or previous procedures often respond well to NRT.</div></div>
          <div class="card"><div class="card-icon">😴</div><div class="card-title">Sleep-disordered breathing</div><div class="card-body">When nasal obstruction is contributing to mouth breathing and sleep apnea, restoring the nasal airway is a critical upstream fix.</div></div>
          <div class="card"><div class="card-icon">🤧</div><div class="card-title">Chronic sinusitis</div><div class="card-body">Structural restrictions can contribute to chronic sinus drainage problems. NRT addresses the structural component that medications alone cannot.</div></div>
          <div class="card"><div class="card-icon">🧠</div><div class="card-title">Brain fog &amp; fatigue</div><div class="card-body">Chronic nasal obstruction reduces oxygen delivery and disrupts sleep. Patients often report significant improvements in energy and mental clarity after NRT.</div></div>
        </div>

        <h2>The NRT protocol</h2>
        <div class="timeline">
          <div class="timeline-item"><div class="timeline-dot">1</div><h3>Initial evaluation</h3><p>Dr. Haller evaluates nasal airway patency, reviews history of trauma or difficult birth, and assesses the full airway picture including tongue posture, jaw development, and sleep quality.</p></div>
          <div class="timeline-item"><div class="timeline-dot">2</div><h3>Treatment sessions (6–8)</h3><p>A small balloon is inserted into the nasal passage and briefly inflated. The sensation is unusual but brief — most patients describe it as pressure rather than pain. Sessions are spaced approximately one week apart.</p></div>
          <div class="timeline-item"><div class="timeline-dot">3</div><h3>Cumulative results</h3><p>NRT produces cumulative results — each session builds on the last. Most patients notice improvement in nasal airflow within the first 2–3 sessions. Full results are typically seen after the complete course.</p></div>
          <div class="timeline-item"><div class="timeline-dot">4</div><h3>Integrated airway protocol</h3><p>NRT is most effective when combined with the full airway protocol: SONU headband (15 min morning + before bed), nasal sprays, and mouth taping at night once nasal breathing is established.</p></div>
        </div>

        <div class="callout">
          <div class="callout-icon">💡</div>
          <div class="callout-title">NRT is one piece of the airway puzzle</div>
          <div class="callout-body">Opening the nasal airway is necessary but not always sufficient. Dr. Haller evaluates the full chain — tongue tie, jaw development, tonsils, and sleep — to ensure NRT is part of a complete treatment plan rather than a standalone intervention.</div>
        </div>

        <h2>What patients report</h2>
        <div class="card-grid card-grid-3" style="margin:20px 0">
          <div class="card"><div class="card-icon">😮‍💨</div><div class="card-title">"I can breathe through my nose for the first time"</div><div class="card-body">Many patients have been mouth breathers for so long they forgot what nasal breathing feels like.</div></div>
          <div class="card"><div class="card-icon">💤</div><div class="card-title">Better sleep quality</div><div class="card-body">Restoring nasal breathing often dramatically improves sleep — even before other airway interventions are complete.</div></div>
          <div class="card"><div class="card-icon">🧠</div><div class="card-title">Clearer thinking</div><div class="card-body">Patients frequently report reduced brain fog and improved mental clarity within the first few sessions.</div></div>
        </div>
      </div>

      <div class="sticky-sidebar">
        <div class="sidebar-cta">
          <h3>Can't breathe through your nose?</h3>
          <p>Book a consultation with Dr. Haller to evaluate whether NRT is appropriate for your situation.</p>
          <a href="index.html#contact" class="btn btn-gold">Book Consultation</a>
          <a href="tel:3054479199" class="btn btn-outline" style="color:rgba(255,255,255,.8)">Call (305) 447-9199</a>
        </div>
        <div class="sidebar-card">
          <h3>The full nasal breathing protocol</h3>
          <ul style="font-size:14px;color:var(--gray);line-height:1.8;padding-left:16px">
            <li>NRT (6–8 sessions)</li>
            <li>SONU headband — 15 min morning + before bed</li>
            <li>Nasal sprays as indicated</li>
            <li>Mouth tape at night (once nasal breathing established)</li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>Related treatments</h3>
          <a href="tongue-tie.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ Tongue Tie Release</a>
          <a href="adult-airway.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ Airway Expansion</a>
          <a href="sleep-apnea.html" style="display:block;color:var(--blue);font-size:14px;font-weight:500">→ Sleep Apnea Treatment</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="cta-strip-inner">
    <h2>Nasal breathing is<br><em>the foundation of everything.</em></h2>
    <p>You can't sleep well, think clearly, or breathe properly if your nasal airway is obstructed. Let's fix it.</p>
    <div class="cta-buttons">
      <a href="index.html#contact" class="btn btn-gold">Book a Consultation →</a>
      <a href="physician-referral.html" class="btn btn-outline">Refer a Patient</a>
    </div>
  </div>
</section>"""
    return page(
        "Nasal Release Therapy (NRT) — Coral Gables, FL — Dental Solutions of South Florida",
        "Balloon-assisted nasal release therapy for chronic nasal obstruction, head trauma, and difficult birth history. Non-surgical, cumulative results.",
        "Treatments", "Nasal Release Therapy (NRT)", body)


def build_snoring():
    body = """
<section class="page-hero">
  <div class="page-hero-inner">
    <div class="page-hero-eyebrow"><span class="hero-badge-dot"></span>Laser Snoring Treatment</div>
    <h1>Stop Snoring.<br><em>No Surgery.</em><br>No Downtime.</h1>
    <p class="page-hero-sub">Fractional ablative CO2 laser therapy tightens soft palate tissue to reduce snoring. Non-surgical, virtually painless, effective in 3 sessions.</p>
    <div class="page-hero-badges">
      <span class="hero-badge"><span class="hero-badge-dot"></span>No Surgery Required</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>5–10 Min Per Session</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>Results in 1–5 Days</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sidebar-layout">
      <div class="prose">
        <p class="section-eyebrow">Why People Snore</p>
        <h2>Snoring is a structural problem</h2>
        <p>Snoring occurs when airflow causes vibration of relaxed soft tissues in the throat. The louder and more frequent the snoring, the more significant the airway obstruction. Common structural causes include:</p>
        <div class="symptom-grid" style="margin:20px 0 32px">
          <div class="symptom-item"><span class="symptom-dot"></span>Lax or elongated soft palate — the most common cause</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Enlarged tonsils — often caused by chronic mouth breathing</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Tongue falling backward during sleep</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Nasal obstruction — forces mouth breathing</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Low tongue posture from tongue tie</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Underdeveloped jaws — smaller airway</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Weight gain — increases tissue around the airway</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Alcohol and sedatives — relax throat muscles further</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Age — tissue naturally loses tone over time</div>
        </div>

        <div class="callout">
          <div class="callout-icon">⚠️</div>
          <div class="callout-title">Snoring can be a sign of sleep apnea</div>
          <div class="callout-body">Not all snorers have sleep apnea — but all sleep apnea patients snore. If you snore, Dr. Haller will evaluate whether a sleep study is warranted before or alongside laser treatment.</div>
        </div>

        <h2>How the laser works</h2>
        <p>Dr. Haller uses a fractional ablative CO2 laser to treat the soft palate — the primary source of snoring vibration in most patients. Here's how it compares to other approaches:</p>

        <table class="compare-table" style="margin:20px 0">
          <thead><tr><th>Treatment</th><th>How It Works</th><th>Pain</th><th>Downtime</th><th>Effectiveness</th></tr></thead>
          <tbody>
            <tr><td><strong>CO2 Laser (Dr. Haller)</strong></td><td>Fractional laser creates microinjuries → new collagen → tissue tightens</td><td class="check">✓ Mild warmth only</td><td class="check">✓ None</td><td class="check">✓ Effective in 3 sessions</td></tr>
            <tr><td>Radiofrequency (Snoreplasty)</td><td>RF energy heats tissue → scar tissue forms → stiffens palate</td><td>Moderate</td><td>1–2 days</td><td>Variable</td></tr>
            <tr><td>UPPP Surgery</td><td>Surgical removal of excess tissue</td><td class="cross">✗ Significant</td><td class="cross">✗ 2–3 weeks</td><td>Variable, irreversible</td></tr>
            <tr><td>Microneedling (skin)</td><td>Tiny needles create microinjuries → collagen → skin tightens</td><td>Moderate</td><td>Days</td><td>Skin only</td></tr>
          </tbody>
        </table>

        <h2>What to expect</h2>
        <div class="timeline">
          <div class="timeline-item"><div class="timeline-dot">1</div><h3>Evaluation</h3><p>Dr. Haller evaluates the source of snoring — soft palate, tongue position, tonsil size, nasal patency — and determines whether laser treatment alone is appropriate or whether other interventions should be combined.</p></div>
          <div class="timeline-item"><div class="timeline-dot">2</div><h3>Treatment sessions (typically 3)</h3><p>The fractional CO2 laser is applied to the soft palate for 5–10 minutes. Most patients feel mild warmth at most — no topical anesthetic is required. You return to normal activity immediately.</p></div>
          <div class="timeline-item"><div class="timeline-dot">3</div><h3>Results</h3><p>New collagen production begins immediately. Most patients and their partners notice improvement within 1–5 days of the first session. Results continue to improve over 4–6 weeks as collagen remodeling completes.</p></div>
          <div class="timeline-item"><div class="timeline-dot">4</div><h3>Maintenance</h3><p>A single maintenance session every 12–18 months is typically sufficient to maintain results. If snoring recurs, it usually responds quickly to a repeat session.</p></div>
        </div>

        <h2>Addressing the root cause</h2>
        <p>Laser snoring treatment is highly effective — but it treats the symptom, not the anatomy. For patients who want a permanent structural solution, <strong>epigenetic arch expansion</strong> widens the dental arch and nasal passages, creating a structurally larger airway that reduces snoring at the source.</p>
        <p>Dr. Haller will discuss which approach — or combination of approaches — is right for your anatomy and goals.</p>
      </div>

      <div class="sticky-sidebar">
        <div class="sidebar-cta">
          <h3>Stop snoring tonight</h3>
          <p>Book a consultation with Dr. Haller. We'll identify the source of your snoring and recommend the right treatment.</p>
          <a href="index.html#contact" class="btn btn-gold">Book Consultation</a>
          <a href="tel:3054479199" class="btn btn-outline" style="color:rgba(255,255,255,.8)">Call (305) 447-9199</a>
        </div>
        <div class="sidebar-card">
          <h3>Quick facts</h3>
          <ul style="font-size:14px;color:var(--gray);line-height:1.9;padding-left:16px">
            <li>5–10 min per session</li>
            <li>Typically 3 sessions</li>
            <li>No anesthesia required</li>
            <li>No downtime</li>
            <li>Results in 1–5 days</li>
            <li>Maintenance every 12–18 months</li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>Related treatments</h3>
          <a href="sleep-apnea.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ Sleep Apnea Treatment</a>
          <a href="tonsils.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ CO2 Laser Tonsils</a>
          <a href="adult-airway.html" style="display:block;color:var(--blue);font-size:14px;font-weight:500">→ Airway Expansion</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="cta-strip-inner">
    <h2>Your partner will<br><em>thank you.</em></h2>
    <p>Non-surgical laser snoring treatment. 5–10 minutes. No downtime. Results in days.</p>
    <div class="cta-buttons">
      <a href="index.html#contact" class="btn btn-gold">Book a Consultation →</a>
      <a href="sleep-apnea.html" class="btn btn-outline">Sleep Apnea Treatment</a>
    </div>
  </div>
</section>"""
    return page(
        "Laser Snoring Treatment — No Surgery, No Downtime — Dental Solutions of South Florida",
        "Fractional CO2 laser snoring treatment in Coral Gables, FL. Non-surgical, no downtime, results in 1–5 days. Effective in 3 sessions.",
        "Sleep & Airway", "Laser Snoring Treatment", body)


def build_adult_airway():
    body = """
<section class="page-hero">
  <div class="page-hero-inner">
    <div class="page-hero-eyebrow"><span class="hero-badge-dot"></span>Epigenetic Airway Remodeling</div>
    <h1>Grow a Permanently<br><em>Larger Airway</em><br>Without Surgery</h1>
    <p class="page-hero-sub">Epigenetic appliances create permanent structural change — widening the dental arch and nasal passages. The only treatment that addresses the anatomical root cause of airway obstruction.</p>
    <div class="page-hero-badges">
      <span class="hero-badge"><span class="hero-badge-dot"></span>Permanent Structural Change</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>No Surgery Required</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>Trained with Leading Innovators</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sidebar-layout">
      <div class="prose">
        <p class="section-eyebrow">The Root Cause</p>
        <h2>Most airway problems are structural</h2>
        <p>Snoring, sleep apnea, mouth breathing, and chronic nasal obstruction are symptoms. The underlying cause in most patients is a structurally narrow airway — the result of underdeveloped dental arches and nasal passages.</p>
        <p>This underdevelopment happens early in life: tongue tie prevents proper tongue posture, soft foods reduce the chewing forces that stimulate jaw growth, and mouth breathing allows the palate to narrow rather than widen. The result is a smaller airway that causes problems for decades.</p>
        <p>Epigenetic arch expansion reverses this. By applying gentle, sustained forces to the dental arch, the appliances stimulate bone remodeling — widening the arch and the nasal passages above it. The change is permanent because it's structural, not muscular.</p>

        <div class="stat-row">
          <div class="stat-badge"><div class="stat-badge-num">12–24</div><div class="stat-badge-label">months typical treatment</div></div>
          <div class="stat-badge"><div class="stat-badge-num">0</div><div class="stat-badge-label">surgeries required</div></div>
          <div class="stat-badge"><div class="stat-badge-num">∞</div><div class="stat-badge-label">permanent results</div></div>
        </div>

        <h2>Appliance systems Dr. Haller uses</h2>
        <div class="card-grid card-grid-2" style="margin:20px 0">
          <div class="card"><div class="card-icon">🦷</div><div class="card-title">Vivos System</div><div class="card-body">FDA-cleared epigenetic arch expansion system. Removable appliance worn primarily at night. Clinically validated for adults with sleep apnea and airway restriction.</div></div>
          <div class="card"><div class="card-icon">🔄</div><div class="card-title">Homeoblock</div><div class="card-body">Developed by Dr. Theodore Belfor. Uses the body's own neuromuscular signals to stimulate arch development. Particularly effective for facial development and nasal breathing.</div></div>
          <div class="card"><div class="card-icon">🌱</div><div class="card-title">Start Thriving Appliance®</div><div class="card-body">Developed by Dr. Felix Liao (AMD — Airway Mouth Doctor). Addresses the full airway picture including jaw posture, tongue function, and nasal breathing.</div></div>
          <div class="card"><div class="card-icon">👶</div><div class="card-title">Healthy Start (Children)</div><div class="card-body">Functional appliance system for children. Guides jaw development during the growth years when the most change is possible. "Fix before six" is our standard.</div></div>
        </div>

        <h2>Who is a candidate?</h2>
        <p>Epigenetic expansion is appropriate for adults and children with:</p>
        <div class="symptom-grid" style="margin:20px 0 28px">
          <div class="symptom-item"><span class="symptom-dot"></span>Diagnosed sleep apnea (mild to moderate)</div>
          <div class="symptom-item"><span class="symptom-dot"></span>CPAP intolerance</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Chronic mouth breathing</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Narrow dental arch or crowded teeth</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Chronic nasal obstruction</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Snoring</div>
          <div class="symptom-item"><span class="symptom-dot"></span>TMJ pain or jaw clicking</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Forward head posture</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Chronic fatigue and brain fog</div>
        </div>

        <h2>Dr. Haller's training</h2>
        <p>Dr. Haller has trained directly with the leading innovators in epigenetic dentistry:</p>
        <div class="card-grid card-grid-2" style="margin:20px 0">
          <div class="card"><div class="card-icon">👨‍⚕️</div><div class="card-title">Dr. Felix Liao</div><div class="card-body">Certified AMD (Airway Mouth Doctor). Dr. Liao's approach integrates airway, jaw, and whole-body health into a unified treatment framework.</div></div>
          <div class="card"><div class="card-icon">👨‍⚕️</div><div class="card-title">Dr. Theodore Belfor</div><div class="card-body">Homeoblock certified. Dr. Belfor's system uses the body's own biology to drive facial and airway development.</div></div>
          <div class="card"><div class="card-icon">🏥</div><div class="card-title">Vivos Therapeutics</div><div class="card-body">Certified Vivos provider. The only FDA-cleared epigenetic system for adult sleep apnea treatment.</div></div>
          <div class="card"><div class="card-icon">🏥</div><div class="card-title">AHS &amp; AAGO</div><div class="card-body">Member of the Academy of Homeopathic Surgery and American Academy of Gnathologic Orthopedics.</div></div>
        </div>

        <h2>The treatment process</h2>
        <div class="timeline">
          <div class="timeline-item"><div class="timeline-dot">1</div><h3>Comprehensive evaluation</h3><p>CBCT imaging, airway analysis, jaw assessment, sleep history review, and tongue posture evaluation. A full picture is essential before selecting the right appliance system.</p></div>
          <div class="timeline-item"><div class="timeline-dot">2</div><h3>Appliance selection &amp; fabrication</h3><p>The right appliance system is selected based on your anatomy, goals, and lifestyle. Custom fabrication takes 2–3 weeks.</p></div>
          <div class="timeline-item"><div class="timeline-dot">3</div><h3>Active treatment (12–24 months)</h3><p>The appliance is worn primarily at night. Regular check-ins every 4–8 weeks to monitor progress, adjust the appliance, and track airway changes.</p></div>
          <div class="timeline-item"><div class="timeline-dot">4</div><h3>Retention &amp; maintenance</h3><p>Once target expansion is achieved, a retainer phase maintains the result. Many patients continue to see improvement during retention as bone remodeling completes.</p></div>
        </div>
      </div>

      <div class="sticky-sidebar">
        <div class="sidebar-cta">
          <h3>Ready for a permanent solution?</h3>
          <p>Book a consultation with Dr. Haller. We'll evaluate your airway and determine whether epigenetic expansion is right for you.</p>
          <a href="index.html#contact" class="btn btn-gold">Book Consultation</a>
          <a href="tel:3054479199" class="btn btn-outline" style="color:rgba(255,255,255,.8)">Call (305) 447-9199</a>
        </div>
        <div class="sidebar-card">
          <h3>Credentials</h3>
          <ul style="font-size:13px;color:var(--gray);line-height:1.9;padding-left:16px">
            <li>Harvard School of Dental Medicine</li>
            <li>Certified AMD (Dr. Felix Liao)</li>
            <li>Homeoblock certified (Dr. Belfor)</li>
            <li>Vivos provider</li>
            <li>Board Certified Laser Dentist (ALD)</li>
            <li>Board Certified Dental Sleep Medicine (ASBA)</li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>Related treatments</h3>
          <a href="sleep-apnea.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ Sleep Apnea Treatment</a>
          <a href="nrt.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ Nasal Release Therapy</a>
          <a href="childrens-airway.html" style="display:block;color:var(--blue);font-size:14px;font-weight:500">→ Children's Airway</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="cta-strip-inner">
    <h2>The only treatment that<br><em>fixes the anatomy.</em></h2>
    <p>Epigenetic arch expansion creates a permanently larger airway — without surgery. 12–24 months. Results that last a lifetime.</p>
    <div class="cta-buttons">
      <a href="index.html#contact" class="btn btn-gold">Book a Consultation →</a>
      <a href="physician-referral.html" class="btn btn-outline">For Physicians</a>
    </div>
  </div>
</section>"""
    return page(
        "Adult Airway Expansion — Epigenetic Remodeling — Dental Solutions of South Florida",
        "Epigenetic arch expansion for adults. Permanent structural airway widening without surgery. Vivos, Homeoblock, Start Thriving Appliance in Coral Gables, FL.",
        "Sleep & Airway", "Adult Airway Expansion", body)


def build_childrens_airway():
    body = """
<section class="page-hero">
  <div class="page-hero-inner">
    <div class="page-hero-eyebrow"><span class="hero-badge-dot"></span>Children's Airway & Orthodontics</div>
    <h1>Fix It Early.<br><em>Fix It Forever.</em></h1>
    <p class="page-hero-sub">Functional appliances and early intervention guide jaw development in children — preventing a lifetime of airway problems. "Fix before six" is our standard.</p>
    <div class="page-hero-badges">
      <span class="hero-badge"><span class="hero-badge-dot"></span>Early Intervention Specialist</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>Healthy Start Provider</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>Pediatric Orthodontics</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sidebar-layout">
      <div class="prose">
        <p class="section-eyebrow">Why Early Matters</p>
        <h2>The jaw develops most in the first 6 years</h2>
        <p>The dental arch and nasal passages develop rapidly in early childhood. By age 6, approximately 60% of facial growth is complete. By age 12, it's 90%. This means the window for the easiest, most effective intervention is early — and it closes quickly.</p>
        <p>When children mouth breathe, have tongue ties, or develop narrow arches, the consequences compound over years: crowded teeth, narrow palates, enlarged tonsils, disrupted sleep, ADHD-like symptoms, and a lifetime of airway problems that could have been prevented.</p>

        <div class="callout">
          <div class="callout-icon">💡</div>
          <div class="callout-title">"Fix before six" is our standard</div>
          <div class="callout-body">The earlier we intervene, the more we can guide development rather than correct it. A child seen at age 4 with a narrow arch and tongue tie can often avoid years of orthodontics, tonsil surgery, and sleep problems entirely.</div>
        </div>

        <h2>Signs your child may need an airway evaluation</h2>
        <div class="symptom-grid" style="margin:20px 0 28px">
          <div class="symptom-item"><span class="symptom-dot"></span>Mouth breathing (day or night)</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Snoring or noisy breathing during sleep</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Restless sleep, frequent waking</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Bedwetting beyond age 5</div>
          <div class="symptom-item"><span class="symptom-dot"></span>ADHD diagnosis or ADHD-like symptoms</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Difficulty concentrating at school</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Crowded or crooked teeth</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Narrow upper arch or high palate</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Enlarged tonsils or adenoids</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Tongue tie (diagnosed or suspected)</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Forward head posture</div>
          <div class="symptom-item"><span class="symptom-dot"></span>Chronic ear infections</div>
        </div>

        <h2>Treatment options for children</h2>
        <div class="card-grid card-grid-2" style="margin:20px 0">
          <div class="card"><div class="card-icon">😁</div><div class="card-title">Healthy Start</div><div class="card-body">A habit corrector and arch developer for children ages 2–12. Addresses thumb sucking, tongue thrusting, and mouth breathing while guiding jaw development. Worn at night and 1–2 hours during the day.</div></div>
          <div class="card"><div class="card-icon">🦷</div><div class="card-title">Functional Appliances</div><div class="card-body">Custom removable appliances that guide jaw growth during the critical development window. Multiple systems available depending on the child's specific needs and anatomy.</div></div>
          <div class="card"><div class="card-icon">🔧</div><div class="card-title">Fixed &amp; Removable Expanders</div><div class="card-body">Traditional palatal expanders (fixed or removable) to widen the upper arch, create space for permanent teeth, and improve nasal breathing.</div></div>
          <div class="card"><div class="card-icon">🌿</div><div class="card-title">ALF Appliance</div><div class="card-body">Advanced Lightwire Functional appliance. A gentle, flexible wire that works with the body's natural forces to guide arch development with minimal patient compliance required.</div></div>
          <div class="card"><div class="card-icon">💪</div><div class="card-title">Myo Munchee</div><div class="card-body">A chewing exercise device that strengthens jaw muscles, promotes nasal breathing, and improves tongue posture. Used as part of a comprehensive myofunctional protocol.</div></div>
          <div class="card"><div class="card-icon">💅</div><div class="card-title">Tongue Tie Release</div><div class="card-body">CO2 laser frenectomy when tongue tie is contributing to mouth breathing and jaw underdevelopment. Safe from 2 days old. Coordinated with myofunctional therapy.</div></div>
        </div>

        <h2>The chain in children</h2>
        <p>In children, the airway chain often starts earlier and moves faster than in adults. Identifying and treating the upstream causes early prevents the downstream consequences:</p>
        <table class="compare-table" style="margin:20px 0">
          <thead><tr><th>Root Cause</th><th>If Untreated</th><th>Our Intervention</th></tr></thead>
          <tbody>
            <tr><td>Tongue tie</td><td>Mouth breathing, narrow arch, speech delay</td><td>CO2 laser frenectomy + myofunctional therapy</td></tr>
            <tr><td>Mouth breathing</td><td>Enlarged tonsils, narrow palate, poor sleep</td><td>NRT, nasal protocol, habit correction</td></tr>
            <tr><td>Narrow arch</td><td>Crowded teeth, nasal obstruction, sleep apnea</td><td>Functional appliances, expanders</td></tr>
            <tr><td>Enlarged tonsils</td><td>Airway obstruction, ADHD symptoms, poor growth</td><td>CO2 laser tonsil decontamination</td></tr>
            <tr><td>Poor sleep</td><td>Behavior problems, learning difficulties, growth issues</td><td>Full airway protocol</td></tr>
          </tbody>
        </table>

        <h2>Coordination with your child's team</h2>
        <p>Dr. Haller works closely with pediatricians, ENTs, speech therapists, lactation consultants, and myofunctional therapists. Every child's treatment plan is coordinated with their existing providers — and detailed reports are sent to your child's pediatrician after every evaluation.</p>
      </div>

      <div class="sticky-sidebar">
        <div class="sidebar-cta">
          <h3>Is your child a mouth breather?</h3>
          <p>Book a children's airway evaluation with Dr. Haller. Early intervention makes everything easier.</p>
          <a href="index.html#contact" class="btn btn-gold">Book Evaluation</a>
          <a href="tel:3054479199" class="btn btn-outline" style="color:rgba(255,255,255,.8)">Call (305) 447-9199</a>
        </div>
        <div class="sidebar-card">
          <h3>Ages we treat</h3>
          <ul style="font-size:14px;color:var(--gray);line-height:1.9;padding-left:16px">
            <li><strong>Infants:</strong> Tongue tie from 2 days old</li>
            <li><strong>Ages 2–6:</strong> Healthy Start, habit correction</li>
            <li><strong>Ages 6–12:</strong> Functional appliances, expansion</li>
            <li><strong>Ages 12+:</strong> Full orthodontic &amp; airway protocol</li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>Related treatments</h3>
          <a href="tongue-tie.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ Tongue Tie Release</a>
          <a href="tonsils.html" style="display:block;color:var(--blue);font-size:14px;margin-bottom:8px;font-weight:500">→ CO2 Laser Tonsils</a>
          <a href="adult-airway.html" style="display:block;color:var(--blue);font-size:14px;font-weight:500">→ Adult Airway Expansion</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="cta-strip-inner">
    <h2>The best time to treat<br><em>is now.</em></h2>
    <p>Every year of untreated mouth breathing, narrow arch, and poor sleep compounds. Early intervention changes the trajectory of a child's health.</p>
    <div class="cta-buttons">
      <a href="index.html#contact" class="btn btn-gold">Book a Children's Evaluation →</a>
      <a href="physician-referral.html" class="btn btn-outline">Refer a Patient</a>
    </div>
  </div>
</section>"""
    return page(
        "Children's Airway & Orthodontics — Coral Gables, FL — Dental Solutions of South Florida",
        "Early intervention for children's airway problems. Healthy Start, functional appliances, tongue tie release. Fix before six is our standard.",
        "Children", "Children's Airway & Orthodontics", body)


def build_physician_referral():
    body = """
<section class="page-hero">
  <div class="page-hero-inner">
    <div class="page-hero-eyebrow"><span class="hero-badge-dot"></span>For Healthcare Providers</div>
    <h1>The Missing Piece<br>in Your Patient's<br><em>Care Plan</em></h1>
    <p class="page-hero-sub">Dr. Haller is the airway specialist your patients have been missing. We connect the dots between the mouth, airway, and whole-body health — and we keep you informed every step of the way.</p>
    <div class="page-hero-badges">
      <span class="hero-badge"><span class="hero-badge-dot"></span>Prompt Appointments for Referrals</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>Written Reports After Every Visit</span>
      <span class="hero-badge"><span class="hero-badge-dot"></span>Your Patient Relationship Preserved</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="two-col two-col-60">
      <div class="prose">
        <p class="section-eyebrow">A Note from Dr. Haller</p>
        <div class="blockquote">
          <div class="blockquote-text">"The patients I see most often are the ones who have been everywhere else first. They've seen their internist, their ENT, their psychiatrist, their chiropractor — and nobody has connected the dots to the airway. I am not trying to replace any of those providers. I am trying to be the missing piece that makes everything else work better."</div>
          <div class="blockquote-attr">— Dr. Leslie Haller, DMD · Harvard DMD · Board Certified Laser Dentist &amp; Dental Sleep Medicine</div>
        </div>

        <h2>Who we work with</h2>
        <p>Dr. Haller works closely with a wide range of healthcare providers who encounter airway-related conditions in their patient population:</p>
        <div class="card-grid card-grid-3" style="margin:20px 0">
          <div class="card"><div class="card-icon">👂</div><div class="card-title">ENTs</div><div class="card-body">Non-surgical tonsil reduction, tongue tie evaluation, nasal airway restoration — before or instead of surgery.</div></div>
          <div class="card"><div class="card-icon">👶</div><div class="card-title">Pediatricians</div><div class="card-body">Mouth breathing, snoring, bedwetting, ADHD-like symptoms, poor growth — often have an airway component.</div></div>
          <div class="card"><div class="card-icon">😴</div><div class="card-title">Sleep Physicians</div><div class="card-body">MAD devices for CPAP-intolerant patients. Epigenetic expansion for structural resolution. Coordination throughout.</div></div>
          <div class="card"><div class="card-icon">🧠</div><div class="card-title">Neurologists &amp; Psychiatrists</div><div class="card-body">ADHD, depression, anxiety, brain fog — often improve dramatically when sleep and airway are restored.</div></div>
          <div class="card"><div class="card-icon">❤️</div><div class="card-title">Cardiologists &amp; Internists</div><div class="card-body">Resistant hypertension, metabolic dysregulation, acid reflux, nocturia — well-documented airway mechanisms.</div></div>
          <div class="card"><div class="card-icon">🤱</div><div class="card-title">Lactation Consultants</div><div class="card-body">Tongue tie evaluation and CO2 laser frenectomy for infants. Coordination before and after release.</div></div>
        </div>

        <h2>What we can do for your referred patients</h2>
        <div class="steps-list">
          <div class="step-item">
            <div class="step-num-circle">👅</div>
            <div class="step-content"><h3>CO2 Laser Tongue Tie Release</h3><p>For infants, children, and adults. Anterior and posterior ties. Safe from 2 days old. No sutures, no bleeding, no anesthesia for infants. Hundreds of releases performed. Coordination with lactation consultants and myofunctional therapists.</p></div>
          </div>
          <div class="step-item">
            <div class="step-num-circle">😴</div>
            <div class="step-content"><h3>Sleep Apnea &amp; Snoring Treatment</h3><p>Custom MAD devices (billable to medical insurance with sleep study). Epigenetic arch expansion for structural resolution. Laser snoring treatment — 5–10 minutes, no downtime, results in 1–5 days. CPAP alternatives for intolerant patients.</p></div>
          </div>
          <div class="step-item">
            <div class="step-num-circle">🦷</div>
            <div class="step-content"><h3>CO2 Laser Tonsil Decontamination</h3><p>Non-surgical tonsil reduction via fractional CO2 laser. Eliminates chronic bacterial biofilm in tonsillar crypts. Tonsils measurably reduce within days. Often effective where antibiotics have failed. Coordinated with ENT throughout.</p></div>
          </div>
          <div class="step-item">
            <div class="step-num-circle">👃</div>
            <div class="step-content"><h3>Nasal Release Therapy (NRT)</h3><p>Balloon-assisted cranial restriction release through the nasal passage. Particularly effective for patients with head or facial trauma history, difficult birth, or chronic nasal obstruction not responding to other treatment.</p></div>
          </div>
          <div class="step-item">
            <div class="step-num-circle">🌱</div>
            <div class="step-content"><h3>Epigenetic Arch Expansion</h3><p>Non-surgical widening of the dental arch and nasal passages in adults and children. Trained directly with Dr. Felix Liao, Dr. Theodore Belfor, Vivos, and AHS. Custom protocol per patient. 12–24 months. Often eliminates need for nightly CPAP or MAD.</p></div>
          </div>
          <div class="step-item">
            <div class="step-num-circle">🧒</div>
            <div class="step-content"><h3>Children's Airway &amp; Orthodontics</h3><p>Functional appliances, traditional expanders, ALF appliance, Myo Munchee, Healthy Start habit corrector. "Fix before six" is our standard. Coordination with pediatricians, ENTs, speech therapists, and myofunctional therapists.</p></div>
          </div>
        </div>
      </div>

      <div>
        <div class="sidebar-cta" style="background:var(--navy);border-radius:var(--radius);padding:36px;margin-bottom:24px">
          <h3 style="font-family:'DM Serif Display',serif;font-size:22px;color:white;margin-bottom:12px">Make a referral</h3>
          <p style="font-size:14px;color:rgba(255,255,255,.7);margin-bottom:20px;line-height:1.6">Call or email us. Let us know the patient's name, your clinical concern, and any relevant history. We'll take it from there.</p>
          <a href="tel:3054479199" class="btn btn-gold" style="width:100%;justify-content:center;margin-bottom:10px">📞 (305) 447-9199</a>
          <a href="mailto:dentistry@lesliehallerdmd.com" class="btn btn-outline" style="width:100%;justify-content:center;color:rgba(255,255,255,.8)">✉ Email Dr. Haller</a>
        </div>
        <div class="sidebar-card">
          <h3>Our commitment to you</h3>
          <ul style="font-size:14px;color:var(--gray);line-height:1.9;padding-left:16px">
            <li>Prompt appointments for referred patients</li>
            <li>Written report after every evaluation</li>
            <li>Progress updates throughout treatment</li>
            <li>Available for case discussion</li>
            <li>Your patient relationship preserved</li>
            <li>We do not practice general dentistry</li>
          </ul>
        </div>
        <div class="sidebar-card">
          <h3>Lunch &amp; Learn</h3>
          <p style="font-size:14px;color:var(--gray);line-height:1.6;margin-bottom:12px">Dr. Haller is available to present to your practice team — explaining airway dentistry, what to look for in your patient population, and how the referral process works. Free, at your convenience.</p>
          <a href="mailto:dentistry@lesliehallerdmd.com" class="btn btn-navy" style="font-size:14px;padding:12px 20px">Schedule a Lunch &amp; Learn</a>
        </div>
        <div class="sidebar-card">
          <h3>Dr. Haller's credentials</h3>
          <ul style="font-size:13px;color:var(--gray);line-height:1.9;padding-left:16px">
            <li>Harvard School of Dental Medicine (DMD)</li>
            <li>Board Certified Laser Dentist (ALD)</li>
            <li>Board Certified Dental Sleep Medicine (ASBA)</li>
            <li>Certified AMD (Dr. Felix Liao)</li>
            <li>Homeoblock certified (Dr. Belfor)</li>
            <li>Vivos provider</li>
            <li>Published Researcher — Journal of Rare Disorders</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cta-strip">
  <div class="cta-strip-inner">
    <h2>We make referrals<br><em>easy.</em></h2>
    <p>Call us, email us, or have your patient call directly and mention your name. We'll take it from there — and keep you informed every step of the way.</p>
    <div class="cta-buttons">
      <a href="tel:3054479199" class="btn btn-gold">Call (305) 447-9199</a>
      <a href="mailto:dentistry@lesliehallerdmd.com" class="btn btn-outline">Email Dr. Haller</a>
    </div>
  </div>
</section>"""
    return page(
        "Physician Referrals — Dental Solutions of South Florida",
        "Refer patients to Dr. Leslie Haller for airway dentistry, tongue tie release, sleep apnea, tonsil treatment, and epigenetic expansion in Coral Gables, FL.",
        "Physicians", "Physician Referrals", body)


# ════════════════════════════════════════════════════════════════════════════
# WRITE ALL PAGES
# ════════════════════════════════════════════════════════════════════════════
OUT = '/home/ubuntu/dental-modern'

pages_to_build = [
    ('sleep-apnea.html',       build_sleep_apnea),
    ('tonsils.html',           build_tonsils),
    ('tongue-tie.html',        build_tongue_tie),
    ('nrt.html',               build_nrt),
    ('snoring.html',           build_snoring),
    ('adult-airway.html',      build_adult_airway),
    ('childrens-airway.html',  build_childrens_airway),
    ('physician-referral.html',build_physician_referral),
]

for filename, builder in pages_to_build:
    html = builder()
    path = os.path.join(OUT, filename)
    with open(path, 'w') as f:
        f.write(html)
    print(f"Written: {filename} ({len(html):,} chars)")

print("\nAll pages built successfully.")
