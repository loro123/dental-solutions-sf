#!/usr/bin/env python3
"""
Build all inner pages with 100% verbatim content from source files.
"""
import base64, os

# Load assets
with open('/tmp/logo_data_uri.txt') as f:
    LOGO_URI = f.read().strip()
with open('/home/ubuntu/dental-modern/logo_transparent.png','rb') as f:
    LOGO_WHITE_URI = "data:image/png;base64," + base64.b64encode(f.read()).decode()

# ─── SHARED CSS ────────────────────────────────────────────────────────────────
SHARED_CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600;700;800&display=swap');
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --navy:#0d1f35;
  --navy2:#1a2e4a;
  --blue:#2d52a0;
  --blue-light:#9ab8e0;
  --gold:#c9a84c;
  --gold-dark:#a8893e;
  --white:#ffffff;
  --off-white:#f7f8fc;
  --gray:#64748b;
  --gray-light:#e8ecf4;
  --text:#1a2332;
  --max-w:1800px;
}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;color:var(--text);background:#fff;line-height:1.6}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}

/* ── TOPBAR ── */
.topbar{background:var(--navy);padding:10px 0;font-size:13px}
.topbar-inner{max-width:var(--max-w);margin:0 auto;padding:0 64px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.topbar-contacts{display:flex;align-items:center;gap:28px;flex-wrap:wrap}
.topbar-contact{display:flex;align-items:center;gap:7px;color:rgba(255,255,255,.88);transition:color .2s}
.topbar-contact:hover{color:var(--gold)}
.topbar-contact svg{flex-shrink:0;opacity:.7}
.topbar-right{display:flex;align-items:center;gap:20px}
.topbar-ref{color:rgba(255,255,255,.88);font-size:13px;font-weight:500;letter-spacing:.02em;transition:color .2s}
.topbar-ref:hover{color:var(--gold)}

/* ── NAV ── */
.site-nav{background:#fff;border-bottom:1px solid var(--gray-light);position:sticky;top:0;z-index:1000;box-shadow:0 2px 20px rgba(0,0,0,.06)}
.nav-inner{max-width:var(--max-w);margin:0 auto;padding:0 64px;height:100px;display:flex;align-items:center;justify-content:space-between;gap:32px}
.nav-logo img{height:80px;width:auto;display:block}
.nav-links{display:flex;align-items:center;gap:4px;list-style:none}
.nav-item{position:relative}
.nav-link{display:flex;align-items:center;gap:5px;padding:8px 14px;font-size:14.5px;font-weight:500;color:var(--text);border-radius:8px;transition:all .2s;white-space:nowrap;cursor:pointer}
.nav-link:hover,.nav-item:hover>.nav-link{color:var(--blue);background:rgba(45,82,160,.06)}
.nav-link.active{color:var(--blue);background:rgba(45,82,160,.08)}
.nav-chevron{width:14px;height:14px;transition:transform .25s;flex-shrink:0}
.nav-item:hover .nav-chevron{transform:rotate(180deg)}
.nav-dropdown{position:absolute;top:calc(100% + 8px);left:0;min-width:240px;background:#fff;border:1px solid var(--gray-light);border-radius:12px;box-shadow:0 12px 40px rgba(0,0,0,.12);padding:8px;opacity:0;visibility:hidden;transform:translateY(-8px);transition:all .22s;z-index:200}
.nav-item:hover .nav-dropdown{opacity:1;visibility:visible;transform:translateY(0)}
.nav-dropdown a{display:flex;align-items:center;gap:10px;padding:9px 14px;font-size:14px;font-weight:500;color:var(--text);border-radius:8px;transition:all .18s}
.nav-dropdown a:hover{background:rgba(45,82,160,.07);color:var(--blue)}
.nav-dropdown a .dd-icon{font-size:16px;width:24px;text-align:center;flex-shrink:0}
.nav-cta{background:var(--navy);color:#fff;padding:11px 22px;border-radius:50px;font-size:14px;font-weight:600;letter-spacing:.02em;transition:all .2s;white-space:nowrap;border:none;cursor:pointer}
.nav-cta:hover{background:var(--blue);transform:translateY(-1px)}
.hamburger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:8px}
.hamburger span{display:block;width:24px;height:2px;background:var(--navy);border-radius:2px;transition:all .3s}
.mobile-drawer{display:none;position:fixed;inset:0;z-index:2000;background:var(--navy);padding:24px;overflow-y:auto;transform:translateX(100%);transition:transform .3s ease}
.mobile-drawer.open{transform:translateX(0)}
.drawer-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:32px}
.drawer-close{background:none;border:none;color:#fff;font-size:28px;cursor:pointer;line-height:1}
.drawer-nav{list-style:none}
.drawer-nav li{border-bottom:1px solid rgba(255,255,255,.1)}
.drawer-nav a{display:block;padding:16px 0;color:rgba(255,255,255,.9);font-size:16px;font-weight:500}
.drawer-nav .drawer-sub{padding-left:16px;background:rgba(255,255,255,.04);border-radius:8px;margin:4px 0 8px}
.drawer-nav .drawer-sub a{font-size:14px;padding:10px 12px;color:rgba(255,255,255,.75)}
.drawer-cta-wrap{margin-top:24px}
.drawer-cta{display:block;text-align:center;background:var(--gold);color:var(--navy);padding:14px;border-radius:50px;font-weight:700;font-size:15px}

/* ── PAGE HERO ── */
.page-hero{background:var(--navy);padding:80px 0 72px;position:relative;overflow:hidden}
.page-hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 60% 80% at 80% 50%,rgba(201,168,76,.12) 0%,transparent 70%)}
.page-hero-inner{max-width:var(--max-w);margin:0 auto;padding:0 64px;position:relative;z-index:1}
.page-breadcrumb{display:flex;align-items:center;gap:8px;font-size:13px;color:rgba(255,255,255,.5);margin-bottom:20px}
.page-breadcrumb a{color:rgba(255,255,255,.5);transition:color .2s}
.page-breadcrumb a:hover{color:var(--gold)}
.page-breadcrumb span{color:rgba(255,255,255,.3)}
.page-eyebrow{display:inline-flex;align-items:center;gap:8px;background:rgba(201,168,76,.15);border:1px solid rgba(201,168,76,.3);color:var(--gold);padding:6px 16px;border-radius:50px;font-size:12px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;margin-bottom:24px}
.page-eyebrow::before{content:'✦';font-size:10px}
.page-hero h1{font-family:'DM Serif Display',serif;font-size:clamp(2.4rem,4vw,3.8rem);color:#fff;line-height:1.12;margin-bottom:24px;max-width:800px}
.page-hero h1 em{font-style:italic;color:var(--gold)}
.page-hero-sub{font-size:clamp(1rem,1.5vw,1.2rem);color:rgba(255,255,255,.75);max-width:680px;line-height:1.7;margin-bottom:36px}
.page-hero-cta{display:inline-flex;align-items:center;gap:10px;background:var(--gold);color:var(--navy);padding:14px 28px;border-radius:50px;font-weight:700;font-size:15px;transition:all .2s}
.page-hero-cta:hover{background:#d4b05a;transform:translateY(-2px)}
.page-hero-badges{display:flex;align-items:center;gap:16px;flex-wrap:wrap;margin-top:32px}
.page-hero-badge{display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);padding:8px 16px;border-radius:50px;font-size:13px;color:rgba(255,255,255,.8);font-weight:500}
.page-hero-badge::before{content:'✓';color:var(--gold);font-weight:700}
.page-hero-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:48px;padding-top:40px;border-top:1px solid rgba(255,255,255,.1)}
.hero-stat-val{font-family:'DM Serif Display',serif;font-size:2.4rem;color:var(--gold);line-height:1}
.hero-stat-label{font-size:13px;color:rgba(255,255,255,.6);margin-top:6px;line-height:1.4}

/* ── MAIN LAYOUT ── */
.page-body{max-width:var(--max-w);margin:0 auto;padding:64px 64px;display:grid;grid-template-columns:1fr 340px;gap:64px;align-items:start}
.page-content{}
.page-sidebar{position:sticky;top:120px}

/* ── CONTENT SECTIONS ── */
.content-section{margin-bottom:64px}
.content-section:last-child{margin-bottom:0}
.section-eyebrow{font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--blue);margin-bottom:10px}
.section-title{font-family:'DM Serif Display',serif;font-size:clamp(1.7rem,2.5vw,2.4rem);color:var(--navy);line-height:1.2;margin-bottom:20px}
.section-title em{font-style:italic;color:var(--blue)}
.section-lead{font-size:1.1rem;color:var(--gray);line-height:1.75;margin-bottom:28px}
.section-body p{font-size:15.5px;color:#374151;line-height:1.8;margin-bottom:16px}
.section-body p:last-child{margin-bottom:0}

/* ── FEATURE CARDS ── */
.feature-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin:32px 0}
.feature-card{background:var(--off-white);border:1px solid var(--gray-light);border-radius:16px;padding:28px;transition:all .25s}
.feature-card:hover{transform:translateY(-3px);box-shadow:0 12px 32px rgba(0,0,0,.08)}
.feature-card-icon{font-size:28px;margin-bottom:14px}
.feature-card-title{font-size:16px;font-weight:700;color:var(--navy);margin-bottom:8px}
.feature-card-body{font-size:14.5px;color:var(--gray);line-height:1.7}

/* ── NUMBERED STEPS ── */
.steps-list{list-style:none;margin:28px 0}
.step-item{display:flex;gap:20px;margin-bottom:28px;padding-bottom:28px;border-bottom:1px solid var(--gray-light)}
.step-item:last-child{border-bottom:none;margin-bottom:0;padding-bottom:0}
.step-num{flex-shrink:0;width:40px;height:40px;background:var(--navy);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15px;font-family:'DM Serif Display',serif}
.step-body{}
.step-title{font-size:16px;font-weight:700;color:var(--navy);margin-bottom:6px}
.step-desc{font-size:14.5px;color:var(--gray);line-height:1.7}

/* ── QUOTE BLOCK ── */
.quote-block{background:var(--navy);border-radius:20px;padding:36px 40px;margin:36px 0;position:relative;overflow:hidden}
.quote-block::before{content:'"';position:absolute;top:-20px;left:24px;font-family:'DM Serif Display',serif;font-size:120px;color:rgba(201,168,76,.15);line-height:1}
.quote-text{font-family:'DM Serif Display',serif;font-size:1.2rem;color:#fff;line-height:1.65;font-style:italic;position:relative;z-index:1;margin-bottom:16px}
.quote-attr{font-size:13px;color:var(--gold);font-weight:600;position:relative;z-index:1}

/* ── COMPARISON TABLE ── */
.compare-table{width:100%;border-collapse:collapse;margin:28px 0;font-size:14.5px}
.compare-table th{background:var(--navy);color:#fff;padding:14px 18px;text-align:left;font-weight:600;font-size:13px}
.compare-table th:first-child{border-radius:10px 0 0 0}
.compare-table th:last-child{border-radius:0 10px 0 0}
.compare-table td{padding:13px 18px;border-bottom:1px solid var(--gray-light);color:#374151;vertical-align:top}
.compare-table tr:last-child td{border-bottom:none}
.compare-table tr:nth-child(even) td{background:var(--off-white)}
.compare-table td:first-child{font-weight:600;color:var(--navy)}

/* ── CHECK LIST ── */
.check-list{list-style:none;margin:16px 0}
.check-list li{display:flex;align-items:flex-start;gap:10px;padding:8px 0;font-size:15px;color:#374151;border-bottom:1px solid var(--gray-light)}
.check-list li:last-child{border-bottom:none}
.check-list li::before{content:'✓';color:var(--gold);font-weight:700;flex-shrink:0;margin-top:2px}

/* ── WARNING BOX ── */
.warning-box{background:#fff8ed;border:1px solid #f0d090;border-left:4px solid var(--gold);border-radius:12px;padding:20px 24px;margin:24px 0}
.warning-box p{font-size:14.5px;color:#5a4010;line-height:1.7;margin:0}
.warning-box strong{color:#3d2a00}

/* ── INFO BOX ── */
.info-box{background:rgba(45,82,160,.06);border:1px solid rgba(45,82,160,.15);border-left:4px solid var(--blue);border-radius:12px;padding:20px 24px;margin:24px 0}
.info-box p{font-size:14.5px;color:#1e3a6e;line-height:1.7;margin:0}

/* ── FAQ ── */
.faq-list{margin:24px 0}
.faq-item{border-bottom:1px solid var(--gray-light);padding:20px 0}
.faq-item:first-child{border-top:1px solid var(--gray-light)}
.faq-q{font-size:16px;font-weight:700;color:var(--navy);margin-bottom:10px;cursor:pointer;display:flex;justify-content:space-between;align-items:flex-start;gap:16px}
.faq-a{font-size:14.5px;color:var(--gray);line-height:1.75}

/* ── TESTIMONIALS ── */
.testimonial-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin:28px 0}
.testimonial-card{background:var(--off-white);border:1px solid var(--gray-light);border-radius:16px;padding:28px;position:relative}
.testimonial-stars{color:var(--gold);font-size:16px;margin-bottom:12px}
.testimonial-text{font-size:15px;color:#374151;line-height:1.7;font-style:italic;margin-bottom:16px}
.testimonial-author{font-size:13px;font-weight:700;color:var(--navy)}
.testimonial-role{font-size:12px;color:var(--gray);margin-top:2px}

/* ── SIDEBAR ── */
.sidebar-cta-card{background:var(--navy);border-radius:20px;padding:32px;margin-bottom:28px;text-align:center}
.sidebar-cta-card h3{font-family:'DM Serif Display',serif;font-size:1.4rem;color:#fff;margin-bottom:12px}
.sidebar-cta-card p{font-size:14px;color:rgba(255,255,255,.7);line-height:1.6;margin-bottom:24px}
.sidebar-cta-btn{display:block;background:var(--gold);color:var(--navy);padding:13px 20px;border-radius:50px;font-weight:700;font-size:14px;text-align:center;transition:all .2s;margin-bottom:10px}
.sidebar-cta-btn:hover{background:#d4b05a;transform:translateY(-1px)}
.sidebar-cta-btn-outline{display:block;border:1px solid rgba(255,255,255,.3);color:rgba(255,255,255,.85);padding:12px 20px;border-radius:50px;font-weight:600;font-size:14px;text-align:center;transition:all .2s}
.sidebar-cta-btn-outline:hover{border-color:rgba(255,255,255,.6);color:#fff}
.sidebar-card{background:var(--off-white);border:1px solid var(--gray-light);border-radius:16px;padding:24px;margin-bottom:24px}
.sidebar-card-title{font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--navy);margin-bottom:16px}
.sidebar-links{list-style:none}
.sidebar-links li{border-bottom:1px solid var(--gray-light)}
.sidebar-links li:last-child{border-bottom:none}
.sidebar-links a{display:flex;align-items:center;justify-content:space-between;padding:10px 0;font-size:14px;color:var(--text);transition:color .2s}
.sidebar-links a:hover{color:var(--blue)}
.sidebar-links a::after{content:'→';color:var(--blue);font-size:13px}
.sidebar-fact{display:flex;flex-direction:column;gap:12px}
.sidebar-fact-item{display:flex;gap:12px;align-items:flex-start}
.sidebar-fact-icon{font-size:20px;flex-shrink:0;margin-top:2px}
.sidebar-fact-text{font-size:13.5px;color:var(--gray);line-height:1.55}
.sidebar-fact-text strong{color:var(--navy);display:block;font-size:14px;margin-bottom:2px}

/* ── DARK SECTION ── */
.dark-section{background:var(--navy);padding:72px 0}
.dark-section-inner{max-width:var(--max-w);margin:0 auto;padding:0 64px}
.dark-section .section-eyebrow{color:var(--gold)}
.dark-section .section-title{color:#fff}
.dark-section .section-lead{color:rgba(255,255,255,.7)}
.dark-section .section-body p{color:rgba(255,255,255,.75)}

/* ── CTA BAND ── */
.cta-band{background:var(--navy);padding:80px 0;text-align:center;position:relative;overflow:hidden}
.cta-band::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 50% 80% at 50% 50%,rgba(201,168,76,.15) 0%,transparent 70%)}
.cta-band-inner{max-width:var(--max-w);margin:0 auto;padding:0 64px;position:relative;z-index:1}
.cta-band h2{font-family:'DM Serif Display',serif;font-size:clamp(2rem,3.5vw,3rem);color:#fff;margin-bottom:16px}
.cta-band p{font-size:1.1rem;color:rgba(255,255,255,.7);max-width:600px;margin:0 auto 36px}
.cta-band-btns{display:flex;align-items:center;justify-content:center;gap:16px;flex-wrap:wrap}
.cta-btn-gold{background:var(--gold);color:var(--navy);padding:15px 32px;border-radius:50px;font-weight:700;font-size:15px;transition:all .2s}
.cta-btn-gold:hover{background:#d4b05a;transform:translateY(-2px)}
.cta-btn-outline{border:2px solid rgba(255,255,255,.4);color:#fff;padding:14px 32px;border-radius:50px;font-weight:600;font-size:15px;transition:all .2s}
.cta-btn-outline:hover{border-color:#fff;background:rgba(255,255,255,.08)}

/* ── FOOTER ── */
.site-footer{background:#0a1628;padding:64px 0 0}
.footer-inner{max-width:var(--max-w);margin:0 auto;padding:0 64px;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px}
.footer-brand{}
.footer-logo{height:70px;width:auto;margin-bottom:20px;filter:brightness(0) invert(1) opacity(.85)}
.footer-tagline{font-size:14px;color:rgba(255,255,255,.55);line-height:1.65;max-width:300px}
.footer-col-title{font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.4);margin-bottom:16px}
.footer-links{list-style:none}
.footer-links li{margin-bottom:10px}
.footer-links a{font-size:14px;color:rgba(255,255,255,.65);transition:color .2s}
.footer-links a:hover{color:var(--gold)}
.footer-contact-item{display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;font-size:13.5px;color:rgba(255,255,255,.65)}
.footer-contact-item svg{flex-shrink:0;margin-top:2px;opacity:.6}
.footer-bottom{border-top:1px solid rgba(255,255,255,.08);padding:20px 64px;max-width:var(--max-w);margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:16px}
.footer-copy{font-size:13px;color:rgba(255,255,255,.35)}
.footer-legal{display:flex;gap:20px}
.footer-legal a{font-size:13px;color:rgba(255,255,255,.35);transition:color .2s}
.footer-legal a:hover{color:rgba(255,255,255,.65)}

/* ── RESPONSIVE ── */
@media(max-width:1200px){
  .page-body{grid-template-columns:1fr;gap:48px}
  .page-sidebar{position:static}
  .footer-inner{grid-template-columns:1fr 1fr;gap:36px}
  .page-hero-stats{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:1024px){
  .topbar-inner,.nav-inner,.page-hero-inner,.page-body,.dark-section-inner,.cta-band-inner,.footer-inner,.footer-bottom{padding-left:32px;padding-right:32px}
  .nav-links,.nav-cta{display:none}
  .hamburger{display:flex}
  .mobile-drawer{display:block}
  .nav-inner{height:80px}
  .nav-logo img{height:60px}
}
@media(max-width:768px){
  .topbar{display:none}
  .page-hero{padding:56px 0 48px}
  .page-hero-inner{padding:0 20px}
  .page-hero h1{font-size:2rem}
  .page-hero-stats{grid-template-columns:repeat(2,1fr);gap:16px}
  .page-body{padding:40px 20px}
  .feature-grid{grid-template-columns:1fr}
  .compare-table{font-size:13px}
  .compare-table th,.compare-table td{padding:10px 12px}
  .testimonial-grid{grid-template-columns:1fr}
  .dark-section-inner,.cta-band-inner{padding:0 20px}
  .dark-section{padding:48px 0}
  .cta-band{padding:56px 0}
  .footer-inner{grid-template-columns:1fr;gap:28px;padding:0 20px}
  .footer-bottom{padding:16px 20px;flex-direction:column;text-align:center}
}
"""

# ─── SHARED NAV HTML ────────────────────────────────────────────────────────────
def nav_html(active_page=''):
    pages = {
        'index': 'Home',
        'sleep-apnea': 'Sleep Apnea',
        'tonsils': 'Tonsils',
        'tongue-tie': 'Tongue Tie',
        'nrt': 'NRT',
        'snoring': 'Snoring',
        'adult-airway': 'Adult Airway',
        'childrens-airway': "Children's Airway",
        'physician-referral': 'Physician Referrals',
    }
    def active(p): return ' active' if p == active_page else ''
    return f"""
<div class="topbar">
  <div class="topbar-inner">
    <div class="topbar-contacts">
      <a href="tel:3054479199" class="topbar-contact">
        <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 01.12 1.2 2 2 0 012.11 0h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 14.92z"/></svg>
        (305) 447-9199
      </a>
      <a href="mailto:dentistry@lesliehallerdmd.com" class="topbar-contact">
        <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        dentistry@lesliehallerdmd.com
      </a>
      <a href="#" class="topbar-contact">
        <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
        348 Alhambra Circle, Coral Gables
      </a>
    </div>
    <div class="topbar-right">
      <a href="physician-referral.html" class="topbar-ref">Physician Referrals</a>
    </div>
  </div>
</div>
<nav class="site-nav">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo"><img src="{LOGO_URI}" alt="Dental Solutions of South Florida"></a>
    <ul class="nav-links">
      <li class="nav-item"><a href="index.html" class="nav-link{active('index')}">Home</a></li>
      <li class="nav-item">
        <a href="#" class="nav-link{active('sleep-apnea') or active('snoring')}">Sleep &amp; Airway
          <svg class="nav-chevron" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
        </a>
        <div class="nav-dropdown">
          <a href="sleep-apnea.html"><span class="dd-icon">😴</span>Sleep Apnea &amp; Oral Appliances</a>
          <a href="snoring.html"><span class="dd-icon">💤</span>Laser Snoring Treatment</a>
          <a href="adult-airway.html"><span class="dd-icon">🌱</span>Adult Airway Expansion</a>
        </div>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link{active('tonsils') or active('tongue-tie') or active('nrt')}">Treatments
          <svg class="nav-chevron" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
        </a>
        <div class="nav-dropdown">
          <a href="tonsils.html"><span class="dd-icon">🦷</span>CO2 Laser Tonsil Treatment</a>
          <a href="tongue-tie.html"><span class="dd-icon">👅</span>Tongue Tie Frenectomy</a>
          <a href="nrt.html"><span class="dd-icon">👃</span>Nasal Release Therapy</a>
        </div>
      </li>
      <li class="nav-item">
        <a href="childrens-airway.html" class="nav-link{active('childrens-airway')}">Children</a>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link">About
          <svg class="nav-chevron" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></svg>
        </a>
        <div class="nav-dropdown">
          <a href="index.html#about"><span class="dd-icon">👩‍⚕️</span>Dr. Haller</a>
          <a href="physician-referral.html"><span class="dd-icon">🤝</span>Physician Referrals</a>
        </div>
      </li>
      <li class="nav-item"><a href="index.html#contact" class="nav-link">Contact</a></li>
    </ul>
    <a href="index.html#contact" class="nav-cta">Book Appointment</a>
    <button class="hamburger" onclick="document.getElementById('mobileDrawer').classList.add('open')" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>
<div class="mobile-drawer" id="mobileDrawer">
  <div class="drawer-header">
    <img src="{LOGO_WHITE_URI}" alt="Dental Solutions of South Florida" style="height:50px">
    <button class="drawer-close" onclick="document.getElementById('mobileDrawer').classList.remove('open')">&times;</button>
  </div>
  <ul class="drawer-nav">
    <li><a href="index.html">Home</a></li>
    <li><a href="sleep-apnea.html">Sleep Apnea &amp; Oral Appliances</a></li>
    <li><a href="snoring.html">Laser Snoring Treatment</a></li>
    <li><a href="adult-airway.html">Adult Airway Expansion</a></li>
    <li><a href="tonsils.html">CO2 Laser Tonsil Treatment</a></li>
    <li><a href="tongue-tie.html">Tongue Tie Frenectomy</a></li>
    <li><a href="nrt.html">Nasal Release Therapy</a></li>
    <li><a href="childrens-airway.html">Children's Airway</a></li>
    <li><a href="physician-referral.html">Physician Referrals</a></li>
    <li><a href="index.html#contact">Contact</a></li>
  </ul>
  <div class="drawer-cta-wrap">
    <a href="index.html#contact" class="drawer-cta">Book Appointment</a>
  </div>
</div>
"""

# ─── FOOTER ────────────────────────────────────────────────────────────────────
def footer_html():
    return f"""
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <img src="{LOGO_WHITE_URI}" alt="Dental Solutions of South Florida" class="footer-logo">
      <p class="footer-tagline">Harvard-trained airway dentist serving Coral Gables, Miami, and South Florida. Breathe Better. Sleep Better. Live Better.</p>
    </div>
    <div>
      <div class="footer-col-title">Treatments</div>
      <ul class="footer-links">
        <li><a href="sleep-apnea.html">Sleep Apnea</a></li>
        <li><a href="tonsils.html">Laser Tonsil Treatment</a></li>
        <li><a href="tongue-tie.html">Tongue Tie Release</a></li>
        <li><a href="nrt.html">Nasal Release Therapy</a></li>
        <li><a href="snoring.html">Laser Snoring</a></li>
        <li><a href="adult-airway.html">Adult Airway Expansion</a></li>
        <li><a href="childrens-airway.html">Children's Airway</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-col-title">Practice</div>
      <ul class="footer-links">
        <li><a href="index.html#about">About Dr. Haller</a></li>
        <li><a href="physician-referral.html">Physician Referrals</a></li>
        <li><a href="index.html#contact">Book Appointment</a></li>
      </ul>
    </div>
    <div>
      <div class="footer-col-title">Contact</div>
      <div class="footer-contact-item">
        <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
        348 Alhambra Circle<br>Coral Gables, FL 33134
      </div>
      <div class="footer-contact-item">
        <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 01.12 1.2 2 2 0 012.11 0h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 14.92z"/></svg>
        (305) 447-9199
      </div>
      <div class="footer-contact-item">
        <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        dentistry@lesliehallerdmd.com
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="footer-copy">&copy; 2025 Dental Solutions of South Florida. All rights reserved.</div>
    <div class="footer-legal">
      <a href="#">Privacy Policy</a>
      <a href="#">Terms of Use</a>
      <a href="#">Accessibility</a>
    </div>
  </div>
</footer>
"""

# ─── PAGE WRAPPER ───────────────────────────────────────────────────────────────
def page(title, active, hero_html, body_html, sidebar_html):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Dental Solutions of South Florida</title>
<style>{SHARED_CSS}</style>
</head>
<body>
{nav_html(active)}
{hero_html}
<div class="page-body">
  <main class="page-content">{body_html}</main>
  <aside class="page-sidebar">{sidebar_html}</aside>
</div>
{footer_html()}
</body>
</html>"""

# ════════════════════════════════════════════════════════════════════════════════
# SLEEP APNEA PAGE
# ════════════════════════════════════════════════════════════════════════════════
sleep_hero = """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="page-breadcrumb"><a href="index.html">Home</a><span>/</span><span>Sleep Apnea</span></div>
    <div class="page-eyebrow">Sleep Apnea &amp; CPAP Alternatives · Coral Gables, FL</div>
    <h1>Sleep Apnea Treatment<br><em>Without a CPAP Machine</em></h1>
    <p class="page-hero-sub">CPAP is effective — but half of patients abandon it within three years. Dr. Haller offers custom oral appliances and permanent, non-surgical airway expansion that treat the anatomy causing sleep apnea, not just the symptoms.</p>
    <a href="index.html#contact" class="page-hero-cta">Request a Sleep Consultation →</a>
    <div class="page-hero-badges">
      <span class="page-hero-badge">No mask, no machine</span>
      <span class="page-hero-badge">Custom oral appliances</span>
      <span class="page-hero-badge">Permanent airway expansion</span>
      <span class="page-hero-badge">Board Certified in Dental Sleep Medicine</span>
    </div>
    <div class="page-hero-stats">
      <div><div class="hero-stat-val">1 in 5</div><div class="hero-stat-label">adults has at least mild sleep apnea — most undiagnosed</div></div>
      <div><div class="hero-stat-val">50%</div><div class="hero-stat-label">of CPAP users abandon it within 1–3 years</div></div>
      <div><div class="hero-stat-val">3×</div><div class="hero-stat-label">higher risk of heart disease with untreated sleep apnea</div></div>
      <div><div class="hero-stat-val">7.7→24.1 cm²</div><div class="hero-stat-label">airway growth possible with permanent expansion</div></div>
    </div>
  </div>
</div>"""

sleep_body = """
<div class="content-section">
  <div class="section-eyebrow">Understanding sleep apnea</div>
  <h2 class="section-title">What is sleep apnea — and could you have it <em>without knowing?</em></h2>
  <p class="section-lead">Sleep apnea is not just loud snoring. It is a condition in which the airway partially or fully collapses during sleep — starving the body of oxygen dozens or even hundreds of times per night. Most people with sleep apnea have no idea they have it.</p>
  <div class="feature-grid">
    <div class="feature-card">
      <div class="feature-card-icon">😮‍💨</div>
      <div class="feature-card-title">OSA — Obstructive Sleep Apnea</div>
      <div class="feature-card-body">The most common form. The airway physically collapses during sleep — usually at the level of the tongue, soft palate, or tonsils. The brain rouses the body to restore breathing, often dozens or hundreds of times per night without the patient waking fully or remembering it. Dr. Haller's primary focus.</div>
    </div>
    <div class="feature-card">
      <div class="feature-card-icon">⚡</div>
      <div class="feature-card-title">UARS — Upper Airway Resistance Syndrome</div>
      <div class="feature-card-body">Frequently missed, especially in women. The airway doesn't fully collapse, but airflow is significantly restricted — causing micro-arousals and fragmented sleep. AHI scores are often normal, leading physicians to miss the diagnosis entirely. Often misdiagnosed as anxiety or insomnia.</div>
    </div>
    <div class="feature-card">
      <div class="feature-card-icon">🧠</div>
      <div class="feature-card-title">CSA — Central Sleep Apnea</div>
      <div class="feature-card-body">Less common. The airway is open but the brain fails to send the signal to breathe. Often associated with heart failure, neurological conditions, or opioid use. Requires medical management in addition to dental treatment.</div>
    </div>
  </div>
  <div class="info-box"><p><strong>The UARS patient — often told their sleep is fine:</strong> UARS patients often have normal weight, no dramatic snoring, and normal AHI scores on a sleep study. They are told their sleep is fine — but they feel exhausted, anxious, and wired-but-tired. They may have been diagnosed with anxiety, depression, fibromyalgia, or chronic fatigue syndrome when the root cause is actually a breathing disorder during sleep. Dr. Haller specifically evaluates for UARS, which is frequently overlooked in conventional sleep medicine.</p></div>

  <h3 style="font-family:'DM Serif Display',serif;font-size:1.4rem;color:var(--navy);margin:32px 0 16px">The mechanism — what happens during an apnea event</h3>
  <ol class="steps-list">
    <li class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">Muscles relax</div><div class="step-desc">During sleep, the tongue and soft palate muscles relax. In a normal airway, there is enough space. In a narrow airway, relaxed muscles can cause a collapse which closes off the space either partially or entirely.</div></div></li>
    <li class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">Airway collapses</div><div class="step-desc">The tongue falls back, the soft palate drops, and the airway closes — partially or fully. Airflow stops.</div></div></li>
    <li class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">Oxygen drops</div><div class="step-desc">Blood oxygen saturation falls. In severe cases, it may drop to dangerous levels — putting enormous strain on the heart and brain.</div></div></li>
    <li class="step-item"><div class="step-num">4</div><div class="step-body"><div class="step-title">Brain sounds alarm</div><div class="step-desc">The brain detects the oxygen drop and triggers an arousal — a micro-awakening that restores muscle tone and opens the airway. The patient rarely wakes fully or remembers it.</div></div></li>
    <li class="step-item"><div class="step-num">5</div><div class="step-body"><div class="step-title">Cycle repeats</div><div class="step-desc">This cycle may repeat 5–100+ times per hour all night, every night — preventing deep restorative sleep and stressing every organ system.</div></div></li>
  </ol>
  <div class="quote-block">
    <div class="quote-text">"Sleep apnea is a structural problem — the airway is too small. CPAP holds it open with air pressure, which is effective but requires the machine every night for life. What I do is different: I treat the anatomy itself, to create an airway that stays open on its own."</div>
    <div class="quote-attr">— Dr. Leslie Haller, DMD</div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Do you recognize these?</div>
  <h2 class="section-title">Sleep apnea symptoms — <em>many you wouldn't expect</em></h2>
  <p class="section-lead">Most people think sleep apnea means loud snoring and daytime sleepiness. In reality, it presents in dozens of ways — many of which are routinely misattributed to other conditions.</p>
  <div class="feature-grid">
    <div class="feature-card">
      <div class="feature-card-icon">😴</div>
      <div class="feature-card-title">Classic sleep symptoms</div>
      <div class="feature-card-body">Loud or chronic snoring · Gasping or choking during sleep · Witnessed apneas (partner reports you stop breathing) · Waking unrefreshed despite 7–8 hours · Excessive daytime sleepiness · Falling asleep at inappropriate times · Morning headaches · Dry mouth or sore throat on waking</div>
    </div>
    <div class="feature-card">
      <div class="feature-card-icon">🦷</div>
      <div class="feature-card-title">Pain &amp; structural signs</div>
      <div class="feature-card-body">Bruxism (teeth grinding) — jaw thrusting forward to open airway · TMJ pain or jaw clicking · Frequent nighttime urination (nocturia) · Acid reflux — negative thoracic pressure pulls stomach acid upward · High blood pressure — especially resistant to medication · Chronic neck or shoulder pain · Forward head posture</div>
    </div>
    <div class="feature-card">
      <div class="feature-card-icon">🧠</div>
      <div class="feature-card-title">Cognitive &amp; emotional</div>
      <div class="feature-card-body">Brain fog, poor concentration · Memory problems · Mood swings, irritability · Depression or anxiety — often improve once sleep is restored · ADHD-like symptoms (especially in children) · Reduced libido · Weight gain despite diet &amp; exercise</div>
    </div>
  </div>
  <h3 style="font-family:'DM Serif Display',serif;font-size:1.3rem;color:var(--navy);margin:32px 0 16px">The surprising symptoms — and their mechanisms</h3>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">🦷</div><div class="feature-card-title">Bruxism (teeth grinding)</div><div class="feature-card-body">When the airway narrows, the jaw subconsciously thrusts forward during sleep to open it. This continuous jaw movement causes grinding and clenching — destroying tooth enamel and straining the TMJ. Treating the airway often resolves bruxism without a night guard.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🚽</div><div class="feature-card-title">Nocturia (nighttime urination)</div><div class="feature-card-body">Repeated oxygen deprivation causes the heart to produce atrial natriuretic peptide (ANP) — a hormone that signals the kidneys to produce urine. Many patients with nocturia have sleep apnea as the root cause, not an overactive bladder.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🔥</div><div class="feature-card-title">Acid reflux (GERD)</div><div class="feature-card-body">Each time the airway collapses, the diaphragm creates massive negative pressure trying to pull air in. This pressure pulls stomach acid upward through the esophageal sphincter. Many patients treated for GERD actually have undiagnosed sleep apnea.</div></div>
    <div class="feature-card"><div class="feature-card-icon">⚖️</div><div class="feature-card-title">Weight gain</div><div class="feature-card-body">Sleep deprivation disrupts leptin (the "I'm full" hormone) and ghrelin (the "I'm hungry" hormone). Poor sleep drives cravings for high-carb foods, reduces motivation to exercise, and lowers metabolism. Many patients find weight management dramatically easier once sleep is restored.</div></div>
    <div class="feature-card"><div class="feature-card-icon">😰</div><div class="feature-card-title">Depression &amp; anxiety</div><div class="feature-card-body">The brain cannot regulate mood without adequate deep sleep. Many patients diagnosed with depression or anxiety see significant improvement once their sleep disorder is treated — without changing their psychiatric medications. The wired-but-tired feeling of UARS is particularly often mistaken for anxiety.</div></div>
    <div class="feature-card"><div class="feature-card-icon">💊</div><div class="feature-card-title">Resistant hypertension</div><div class="feature-card-body">Repeated oxygen drops overnight trigger the sympathetic nervous system — raising blood pressure. Many patients on two or three blood pressure medications have undiagnosed sleep apnea as a contributing cause. Treating sleep apnea can meaningfully reduce blood pressure.</div></div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">The stakes</div>
  <h2 class="section-title">Untreated sleep apnea is a <em>serious medical condition</em></h2>
  <p class="section-lead">Every night of untreated sleep apnea is a night of repeated oxygen deprivation, cardiovascular stress, and hormonal disruption. Over years and decades, the cumulative damage is significant — and most of it is preventable.</p>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">❤️</div><div class="feature-card-title">Cardiovascular</div><div class="feature-card-body">3× higher risk of heart disease · 2–4× increased stroke risk · Atrial fibrillation · Resistant hypertension · Heart failure progression</div></div>
    <div class="feature-card"><div class="feature-card-icon">🧪</div><div class="feature-card-title">Metabolic</div><div class="feature-card-body">Type 2 diabetes risk · Insulin resistance · Weight gain cycle · Metabolic syndrome · Chronic inflammation</div></div>
    <div class="feature-card"><div class="feature-card-icon">🧠</div><div class="feature-card-title">Neurological</div><div class="feature-card-body">Accelerated cognitive decline · Dementia risk · Depression &amp; anxiety · ADHD-like symptoms · Memory impairment</div></div>
    <div class="feature-card"><div class="feature-card-icon">⚠️</div><div class="feature-card-title">Safety &amp; quality of life</div><div class="feature-card-body">7× increased car accident risk · Reduced work performance · Relationship strain · Reduced intimacy · Shortened life expectancy</div></div>
  </div>
  <div class="warning-box"><p><strong>⚠ The most dangerous thing about sleep apnea is not knowing you have it.</strong> Most people with sleep apnea are never diagnosed. They attribute their symptoms — fatigue, mood problems, weight gain, brain fog — to stress, age, or lifestyle. Meanwhile, the cumulative oxygen deprivation is quietly damaging the heart, brain, and metabolic system. Early diagnosis and treatment can reverse much of this damage — and dramatically improve quality of life.</p></div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Your options</div>
  <h2 class="section-title">CPAP works — but you have <em>real alternatives</em></h2>
  <p class="section-lead">CPAP is the gold standard for moderate-to-severe OSA — highly effective when worn. The problem is compliance. Half of patients abandon it within one to three years. Dr. Haller offers two alternatives: a custom oral appliance (MAD device) for nightly use, and permanent airway expansion that may eventually eliminate the need for any device at all.</p>
  <table class="compare-table">
    <thead><tr><th>Feature</th><th>CPAP</th><th>MAD Device</th><th>Permanent Expansion</th></tr></thead>
    <tbody>
      <tr><td>Mechanism</td><td>Air pressure splints airway open</td><td>Jaw position holds airway open</td><td>Airway is permanently enlarged</td></tr>
      <tr><td>Nightly use required</td><td>Every night, for life</td><td>Every night, for life</td><td>No — airway stays open naturally</td></tr>
      <tr><td>Noise</td><td>Yes — disturbs partner</td><td>Silent</td><td>Silent</td></tr>
      <tr><td>Travel</td><td>Requires machine + power</td><td>Small, portable</td><td>No device needed</td></tr>
      <tr><td>Compliance</td><td>50% abandon within 3 years</td><td>Much higher than CPAP</td><td>Treatment period only</td></tr>
      <tr><td>Treats anatomy</td><td>No — maintenance only</td><td>No — maintenance only</td><td>Yes — permanent structural change</td></tr>
      <tr><td>Best for</td><td>Moderate-severe OSA, high compliance</td><td>CPAP-intolerant, mild-moderate OSA</td><td>Long-term resolution, motivated patients</td></tr>
    </tbody>
  </table>
  <div class="info-box"><p><strong>Insurance note for MAD devices:</strong> Our practice is fee-for-service. For custom MAD devices, we provide all necessary codes for you to submit to your medical insurance directly. Many medical plans reimburse custom oral appliances for diagnosed OSA. A sleep study diagnosis is generally required prior to coverage.</p></div>
</div>

<div class="content-section">
  <div class="section-eyebrow">The long-term approach</div>
  <h2 class="section-title">Can sleep apnea be <em>permanently resolved?</em></h2>
  <p class="section-lead">CPAP and MAD devices manage sleep apnea — they work only when worn. For patients who want to address the underlying anatomy, Dr. Haller offers a more comprehensive approach that goes beyond nightly devices.</p>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">🦷</div><div class="feature-card-title">Epigenetic arch remodeling</div><div class="feature-card-body">The dental arches can be gradually expanded using custom oral appliances — widening the palate, opening the nasal passages, and creating a structurally larger airway. Dr. Haller has trained extensively with the leading innovators in this field and uses a range of appliance systems tailored to each patient's anatomy and goals.</div></div>
    <div class="feature-card"><div class="feature-card-icon">👅</div><div class="feature-card-title">Tongue tie evaluation</div><div class="feature-card-body">A restricted tongue cannot rest in its correct position on the roof of the mouth — forcing low tongue posture, mouth breathing, and airway narrowing. Dr. Haller evaluates every sleep apnea patient for tongue tie, as releasing it is often the upstream fix that makes everything else work better.</div></div>
    <div class="feature-card"><div class="feature-card-icon">💪</div><div class="feature-card-title">Myofunctional therapy</div><div class="feature-card-body">Myofunctional therapy retrains the tongue, facial, and throat muscles to support nasal breathing and correct tongue posture. When combined with arch expansion and tongue tie release, it reinforces structural changes and helps results last. Dr. Haller coordinates myofunctional therapy referrals as part of a comprehensive airway plan.</div></div>
  </div>
  <div class="info-box"><p><strong>⏱ A realistic picture of what's possible:</strong> Epigenetic arch remodeling typically takes 12–24 months. Results develop gradually and continue even after treatment ends. Many find they need less — or no — nightly device once the airway has been permanently enlarged. Individual results vary depending on starting anatomy, age, and commitment to the full treatment plan. Dr. Haller will give you an honest assessment of what is realistic for your specific situation.</p></div>
  <div class="quote-block">
    <div class="quote-text">"I've had patients come to me wearing a CPAP every night for ten years, desperate for a way out. Addressing the tongue tie, expanding the arches, and retraining the muscles — that combination can be genuinely transformative. That is the most satisfying work in all of dentistry."</div>
    <div class="quote-attr">— Dr. Leslie Haller, DMD</div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Frequently asked questions</div>
  <h2 class="section-title">Your questions <em>answered</em></h2>
  <div class="faq-list">
    <div class="faq-item"><div class="faq-q">Do I need a sleep study before I can be treated?</div><div class="faq-a">For a custom MAD device, a sleep study diagnosis is generally required before medical insurance will cover treatment. For evaluation purposes, Dr. Haller can assess your airway and discuss options at consultation. We can help coordinate a home sleep test if you haven't been diagnosed yet — these are convenient, done in your own home, and far less expensive than an in-lab study.</div></div>
    <div class="faq-item"><div class="faq-q">Is a MAD device as effective as CPAP?</div><div class="faq-a">For mild to moderate OSA, research shows MAD devices achieve comparable outcomes to CPAP — and significantly better real-world results because patients actually wear them consistently. CPAP is more effective on paper; MAD devices are more effective in practice for many patients. For severe OSA, CPAP remains the stronger option, though MAD is still preferable to no treatment at all.</div></div>
    <div class="faq-item"><div class="faq-q">Can sleep apnea be cured — or only managed?</div><div class="faq-a">CPAP and MAD devices manage sleep apnea — they work only when worn. Permanent airway expansion is the only approach that can genuinely resolve the structural cause. Many patients who complete a full expansion protocol find they no longer need any device. Results vary by individual, starting anatomy, and compliance with treatment.</div></div>
    <div class="faq-item"><div class="faq-q">I was told I have mild sleep apnea and don't need treatment. Is that true?</div><div class="faq-a">Even mild sleep apnea carries real health consequences over time — and tends to worsen with age and weight changes. More importantly, mild sleep apnea on a conventional AHI-based study may actually represent UARS, which is significantly underdiagnosed. If you have symptoms — fatigue, brain fog, waking unrefreshed — it is worth a thorough evaluation regardless of what the AHI number says.</div></div>
    <div class="faq-item"><div class="faq-q">I've tried a MAD device before and it hurt my jaw. Can I still try again?</div><div class="faq-a">Yes — often. Many patients who struggled with earlier appliances had poorly fitting or improperly calibrated devices. Custom-fitted appliances with careful titration are dramatically more comfortable. Dr. Haller also evaluates the jaw joint before recommending any appliance — if there is existing TMJ dysfunction, that is addressed as part of the treatment plan.</div></div>
    <div class="faq-item"><div class="faq-q">Does insurance cover these treatments?</div><div class="faq-a">Our practice is fee-for-service. For custom MAD devices, we provide all necessary codes for submission to your medical insurance — many plans reimburse custom oral appliances for diagnosed OSA. Expansion appliances are generally not covered by insurance. We provide a Letter of Medical Necessity and can discuss payment options at consultation.</div></div>
    <div class="faq-item"><div class="faq-q">My partner says I snore but I don't feel tired. Should I be concerned?</div><div class="faq-a">Yes. Many people with significant sleep apnea don't feel sleepy — they've adapted to their baseline level of sleep deprivation and don't recognize it as abnormal. Snoring is always a sign of airway turbulence and worth evaluating. And the cardiovascular consequences of untreated sleep apnea occur regardless of whether you feel tired.</div></div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">What sets Dr. Haller apart</div>
  <h2 class="section-title">Board certified in dental sleep medicine — <em>and trained by the pioneers</em></h2>
  <p class="section-lead">Oral appliance therapy for sleep apnea requires specific training, certification, and ongoing expertise. Dr. Haller is one of a small number of dentists in Florida who combines board certification in dental sleep medicine with advanced training in permanent epigenetic airway expansion.</p>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">🎓</div><div class="feature-card-title">Board certified — ASBA</div><div class="feature-card-body">Dr. Haller is board certified in dental sleep medicine by the American Sleep &amp; Breathing Academy — one of the highest credentials available to dental sleep practitioners.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🔬</div><div class="feature-card-title">Trained by the pioneers</div><div class="feature-card-body">Dr. Haller has trained directly with Dr. Felix Liao (AMD/Holistic Mouth Solutions), Dr. Theodore Belfor (Homeoblock), Vivos Therapeutics, AHS Airway Health Solutions, and others at the forefront of airway expansion.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🔗</div><div class="feature-card-title">The whole airway picture</div><div class="feature-card-body">Dr. Haller doesn't treat sleep apnea in isolation. She evaluates tongue tie, jaw development, nasal airway, and tonsil health together — because sleep apnea is almost always the downstream result of multiple structural issues working together.</div></div>
  </div>
  <div class="quote-block">
    <div class="quote-text">"Along with releasing tongue ties, airway remodeling is the most satisfying work of my life. I have had patients tell me their tinnitus went away, that they could smell their wife's perfume for the first time, that their child finally slept through the night."</div>
    <div class="quote-attr">— Dr. Leslie Haller, DMD</div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Patient stories</div>
  <h2 class="section-title">What our patients say</h2>
  <div class="testimonial-grid">
    <div class="testimonial-card"><div class="testimonial-stars">★★★★★</div><div class="testimonial-text">"I tried CPAP for two years and couldn't tolerate it. Dr. Haller made me a custom oral appliance and I sleep through the night for the first time in a decade."</div><div class="testimonial-author">Robert M.</div><div class="testimonial-role">Sleep Apnea · Oral Appliance</div></div>
    <div class="testimonial-card"><div class="testimonial-stars">★★★★★</div><div class="testimonial-text">"I had been told my sleep study was 'borderline' and nothing was done. Dr. Haller recognized UARS immediately. Six months into expansion therapy I feel like a different person."</div><div class="testimonial-author">Sandra K.</div><div class="testimonial-role">UARS · Airway Expansion</div></div>
    <div class="testimonial-card"><div class="testimonial-stars">★★★★★</div><div class="testimonial-text">"My husband slept in another room for three years because of my snoring and CPAP noise. After 18 months of expansion therapy we sleep in the same room again — no CPAP, no snoring."</div><div class="testimonial-author">Patricia L.</div><div class="testimonial-role">Sleep Apnea · Permanent Expansion</div></div>
  </div>
</div>
"""

sleep_sidebar = """
<div class="sidebar-cta-card">
  <h3>Ready to sleep without a machine?</h3>
  <p>Schedule a consultation with Dr. Haller to discuss your options — custom oral appliance, permanent expansion, or both.</p>
  <a href="index.html#contact" class="sidebar-cta-btn">Request a Consultation</a>
  <a href="tel:3054479199" class="sidebar-cta-btn-outline">(305) 447-9199</a>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Related Treatments</div>
  <ul class="sidebar-links">
    <li><a href="snoring.html">Laser Snoring Treatment</a></li>
    <li><a href="adult-airway.html">Adult Airway Expansion</a></li>
    <li><a href="tongue-tie.html">Tongue Tie Release</a></li>
    <li><a href="tonsils.html">Laser Tonsil Treatment</a></li>
    <li><a href="nrt.html">Nasal Release Therapy</a></li>
  </ul>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Quick Facts</div>
  <div class="sidebar-fact">
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🎓</div><div class="sidebar-fact-text"><strong>Harvard School of Dental Medicine</strong>DMD graduate</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🏅</div><div class="sidebar-fact-text"><strong>Board Certified</strong>American Sleep &amp; Breathing Academy</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">📍</div><div class="sidebar-fact-text"><strong>Coral Gables, FL</strong>Serving all of South Florida</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">💳</div><div class="sidebar-fact-text"><strong>Fee-for-service</strong>MAD devices billable to medical insurance</div></div>
  </div>
</div>
"""

# ════════════════════════════════════════════════════════════════════════════════
# TONSILS PAGE
# ════════════════════════════════════════════════════════════════════════════════
tonsils_hero = """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="page-breadcrumb"><a href="index.html">Home</a><span>/</span><span>Tonsil Treatment</span></div>
    <div class="page-eyebrow">Consider Laser Treatment Before Tonsil Surgery · Children &amp; Adults</div>
    <h1>Laser Treatment to<br><em>Shrink Tonsils Without Surgery</em></h1>
    <p class="page-hero-sub">Enlarged tonsils don't always need a surgeon. Before committing to tonsillectomy, consider laser tonsil decontamination — a painless, in-office treatment that eliminates the bacterial biofilm driving tonsil enlargement, without anesthesia, without a hospital stay, and without removing immune tissue your body needs.</p>
    <a href="index.html#contact" class="page-hero-cta">Request a Consultation →</a>
    <div class="page-hero-badges">
      <span class="page-hero-badge">No surgery required</span>
      <span class="page-hero-badge">No anesthesia</span>
      <span class="page-hero-badge">Zero recovery time</span>
      <span class="page-hero-badge">Children &amp; adults</span>
    </div>
    <div class="page-hero-stats">
      <div><div class="hero-stat-val">15</div><div class="hero-stat-label">minutes avg. session length</div></div>
      <div><div class="hero-stat-val">3–6</div><div class="hero-stat-label">sessions for lasting results</div></div>
      <div><div class="hero-stat-val">0</div><div class="hero-stat-label">days of recovery needed</div></div>
      <div><div class="hero-stat-val">Any</div><div class="hero-stat-label">age — children &amp; adults treated</div></div>
    </div>
  </div>
</div>"""

tonsils_body = """
<div class="content-section">
  <div class="section-eyebrow">The root cause</div>
  <h2 class="section-title">Why do tonsils stay enlarged?</h2>
  <p class="section-lead">It's not just repeated infection — it's bacterial biofilm that antibiotics can't reach.</p>
  <div class="feature-grid">
    <div class="feature-card">
      <div class="feature-card-icon">⚠️</div>
      <div class="feature-card-title">The Problem — Bacterial biofilm in tonsillar crypts</div>
      <div class="feature-card-body">Mouth breathing is usually the underlying cause. The nose is designed to filter, humidify, and clean air before it reaches the tonsils. When someone breathes through their mouth, unfiltered air — full of bacteria, allergens, and pathogens — hits tonsil tissue directly. The tonsils become chronically inflamed fighting off this constant bacterial load. Once established, bacteria form a protective biofilm deep in tonsillar crypts shielded from antibiotics and unreachable by the immune system. The chronic immune response keeps tonsil tissue swollen and permanently enlarged. Result: narrowed airway, disrupted sleep, snoring, ADHD-like symptoms, halitosis.</div>
    </div>
    <div class="feature-card">
      <div class="feature-card-icon">✅</div>
      <div class="feature-card-title">The Solution — CO2 laser penetrates where antibiotics can't</div>
      <div class="feature-card-body">Specialized CO2 laser attachment delivers targeted laser energy into tonsillar crypts. Photobiomodulation eliminates chronic bacterial biofilm at the source. Thermal energy reduces vascular engorgement and stimulates lymphatic drainage. Tonsils measurably shrink as chronic inflammation resolves.</div>
    </div>
  </div>
  <h3 style="font-family:'DM Serif Display',serif;font-size:1.3rem;color:var(--navy);margin:32px 0 16px">How it works — step by step</h3>
  <ol class="steps-list">
    <li class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">Mouth breathing delivers unfiltered air</div><div class="step-desc">The nose filters bacteria and pathogens before air reaches the tonsils. Mouth breathing bypasses this entirely — sending dirty air directly to tonsil tissue, triggering chronic bacterial colonization.</div></div></li>
    <li class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">Chronic immune response</div><div class="step-desc">The body detects persistent infection. Chronic inflammation keeps tonsil tissue swollen and enlarged.</div></div></li>
    <li class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">Laser penetrates crypts</div><div class="step-desc">The specialized CO2 laser attachment targets biofilm deep inside the tonsil's folds — where no antibiotic reaches.</div></div></li>
    <li class="step-item"><div class="step-num">4</div><div class="step-body"><div class="step-title">Inflammation resolves</div><div class="step-desc">Without the bacterial trigger, the immune response calms. Lymphatic drainage resumes and swelling subsides.</div></div></li>
    <li class="step-item"><div class="step-num">5</div><div class="step-body"><div class="step-title">Airway opens</div><div class="step-desc">As tonsils shrink to a healthy size, the airway widens. Breathing, sleep, and behavior often improve measurably.</div></div></li>
  </ol>
</div>

<div class="content-section">
  <div class="section-eyebrow">Ideal candidates</div>
  <h2 class="section-title">Who benefits from laser tonsil treatment?</h2>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">😴</div><div class="feature-card-title">Snoring &amp; mouth breathing</div><div class="feature-card-body">Enlarged tonsils narrow the airway at night, causing turbulent airflow — the source of snoring.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🧠</div><div class="feature-card-title">ADHD with airway component</div><div class="feature-card-body">Many children diagnosed with ADHD are actually experiencing chronic sleep deprivation due to airway obstruction. Tonsil reduction can be transformative.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🔁</div><div class="feature-card-title">Recurrent tonsillitis</div><div class="feature-card-body">Repeated infections despite antibiotic courses — a sign of persistent biofilm that antibiotics can't eliminate.</div></div>
    <div class="feature-card"><div class="feature-card-icon">💨</div><div class="feature-card-title">Halitosis</div><div class="feature-card-body">Chronic bad breath despite good oral hygiene is a classic sign of bacterial biofilm in tonsillar crypts.</div></div>
    <div class="feature-card"><div class="feature-card-icon">😪</div><div class="feature-card-title">Sleep-disordered breathing</div><div class="feature-card-body">Enlarged tonsils are the #1 anatomical cause of pediatric sleep-disordered breathing. Restoring the airway often resolves the sleep disorder.</div></div>
    <div class="feature-card"><div class="feature-card-icon">📈</div><div class="feature-card-title">Grade 2–3 enlarged tonsils</div><div class="feature-card-body">Moderate to significantly enlarged tonsils respond best to laser treatment. Grade 4 ("kissing tonsils") may still benefit from a laser trial before committing to surgery.</div></div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Critical context</div>
  <h2 class="section-title">Mouth breathing is the <em>underlying cause</em></h2>
  <div class="warning-box"><p><strong>⚠ Treating enlarged tonsils without addressing mouth breathing is like bailing out a boat without plugging the hole.</strong> If mouth breathing continues after treatment, tonsils are likely to enlarge again. Laser decontamination is most effective when combined with a plan to restore nasal breathing — and to find the reason nasal breathing broke down in the first place.</p></div>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">👅</div><div class="feature-card-title">Address tongue tie first</div><div class="feature-card-body">If a tongue tie is contributing to low tongue posture and mouth breathing, releasing it is the upstream fix. Dr. Haller evaluates for this at every consultation.</div></div>
    <div class="feature-card"><div class="feature-card-icon">👃</div><div class="feature-card-title">Open the nasal airway</div><div class="feature-card-body">NRT (Nasal Release Therapy), nasal sprays, SONU headband (15 min morning + 15 min before bed), and mouth taping at night (once nasal breathing is established) all support nasal breathing restoration.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🦷</div><div class="feature-card-title">Expand the airway permanently</div><div class="feature-card-body">Epigenetic arch expansion widens the palate and nasal passages permanently — making nasal breathing the path of least resistance. Dr. Haller has trained extensively with the leading innovators in this field and uses a range of appliance systems tailored to each patient.</div></div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">The process</div>
  <h2 class="section-title">What to expect — <em>step by step</em></h2>
  <p class="section-lead">From first evaluation to final session, here is exactly what happens — and why each step matters.</p>
  <ol class="steps-list">
    <li class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">Initial evaluation &amp; grading</div><div class="step-desc">Dr. Haller photographs and grades tonsils using standardized intraoral imaging. She also may evaluate airway anatomy, jaw development, tongue posture, and signs of sleep-disordered breathing using CBCT imaging and clinical exam. A full airway picture is critical — tonsil treatment is most effective when the underlying causes are identified.</div></div></li>
    <li class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">Treatment planning</div><div class="step-desc">A customized protocol is created based on tonsil grade, bacterial load, age, and the patient's airway goals. Co-existing issues (tongue tie, jaw underdevelopment, mouth breathing) may be addressed in parallel or sequentially depending on clinical priority.</div></div></li>
    <li class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">CO2 laser treatment sessions</div><div class="step-desc">The specialized tonsillar laser attachment is applied to each tonsil for a few minutes per session. Most patients — including children — feel mild warmth at most. No topical anesthetic is needed in most cases. Sessions are 10–15 minutes total, after which patients return to school or work immediately. ✓ No anesthesia · ✓ 10–15 min per session · ✓ Same-day return to school · ✓ Painless — well-tolerated by kids</div></div></li>
    <li class="step-item"><div class="step-num">4</div><div class="step-body"><div class="step-title">Gag reflex management</div><div class="step-desc">For patients with a sensitive gag reflex, Dr. Haller uses acupressure wristbands (P6 point), salt on the tongue, breathing coaching, and distraction techniques. In our experience, most children accommodate the treatment easily after the first session.</div></div></li>
    <li class="step-item"><div class="step-num">5</div><div class="step-body"><div class="step-title">Progress monitoring</div><div class="step-desc">Tonsils are photographed and graded at every visit. Families can see measurable reduction within days. Sessions are spaced 1–2 weeks apart. A typical full course is 3–6 sessions. If surgical intervention remains appropriate after the full laser course, we coordinate directly with your ENT.</div></div></li>
  </ol>
</div>

<div class="content-section">
  <div class="section-eyebrow">Making the decision</div>
  <h2 class="section-title">Laser decontamination vs. <em>tonsillectomy</em></h2>
  <p class="section-lead">Surgery is a permanent, irreversible decision. Laser treatment preserves immune tissue, requires no hospital stay, and leaves surgical removal as an option if needed. Nothing is lost by trying laser first.</p>
  <table class="compare-table">
    <thead><tr><th>Feature</th><th>CO2 Laser Decontamination</th><th>Tonsillectomy</th></tr></thead>
    <tbody>
      <tr><td>Procedure type</td><td>Non-surgical, chairside laser</td><td>Surgical — hospital OR</td></tr>
      <tr><td>Anesthesia</td><td>None in most cases</td><td>General anesthesia required</td></tr>
      <tr><td>Recovery time</td><td>Zero — return to school same day</td><td>7–14 days, painful recovery</td></tr>
      <tr><td>Pain level</td><td>Mild warmth at most</td><td>Significant throat pain for 1–2 weeks</td></tr>
      <tr><td>Tonsils preserved</td><td>Yes — immune tissue retained</td><td>No — permanently removed</td></tr>
      <tr><td>Surgical risks</td><td>None</td><td>Bleeding, anesthesia risks, infection</td></tr>
      <tr><td>Sessions</td><td>3–6 sessions, 1–2 weeks apart</td><td>One procedure</td></tr>
      <tr><td>If it doesn't work</td><td>Surgery remains an option — nothing lost</td><td>Irreversible — no going back</td></tr>
      <tr><td>Insurance</td><td>Fee-for-service; Letter of Medical Necessity provided</td><td>Often covered by medical insurance</td></tr>
      <tr><td>Total cost</td><td>Typically a fraction of surgical total cost</td><td>High — hospital + anesthesia + surgeon + lost work/school</td></tr>
    </tbody>
  </table>
  <div class="quote-block">
    <div class="quote-text">"If laser treatment doesn't achieve the reduction we're looking for, surgical removal remains available — and we'll coordinate directly with an ENT of your choice. But in our experience, most Grade 2 and Grade 3 cases respond well to the full laser course. Try the reversible option first."</div>
    <div class="quote-attr">— Dr. Leslie Haller, DMD</div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Frequently asked questions</div>
  <h2 class="section-title">Your questions <em>answered</em></h2>
  <div class="faq-list">
    <div class="faq-item"><div class="faq-q">Is the laser treatment painful?</div><div class="faq-a">Most patients — including young children — report feeling mild warmth at most. No topical anesthetic is needed in the majority of cases. The procedure is routinely well-tolerated and the most common reaction we hear is surprise at how easy it was.</div></div>
    <div class="faq-item"><div class="faq-q">How many sessions will my child need?</div><div class="faq-a">Most patients complete 3–6 sessions spaced 1–2 weeks apart. Grade 2 tonsils often respond in 3–4 sessions. Grade 3 tonsils typically require 4–6. We photograph and grade at every visit so you can see measurable progress throughout.</div></div>
    <div class="faq-item"><div class="faq-q">What if laser treatment doesn't work?</div><div class="faq-a">Surgical removal remains available as a fallback — nothing is lost by trying laser first. If we do not achieve adequate reduction after the full course, we provide a detailed progress report and referral coordination for your ENT. In our experience, most Grade 2 and Grade 3 cases respond well.</div></div>
    <div class="faq-item"><div class="faq-q">Will the tonsils grow back after treatment?</div><div class="faq-a">The laser eliminates the bacterial biofilm that is driving enlargement. If the underlying cause — typically mouth breathing — is also addressed, tonsils generally remain at a healthy size. This is why we always evaluate for tongue tie, jaw underdevelopment, and nasal airway obstruction alongside tonsil treatment.</div></div>
    <div class="faq-item"><div class="faq-q">Is this appropriate for my child's age?</div><div class="faq-a">We treat children and adults of all ages. For very young children (under 4), we evaluate on a case-by-case basis. The procedure requires the patient to open their mouth and remain relatively still for a few minutes — most children aged 4 and older manage this easily.</div></div>
    <div class="faq-item"><div class="faq-q">Does insurance cover this treatment?</div><div class="faq-a">Most insurance plans do not currently cover CO2 laser tonsil decontamination as it is considered an emerging therapy. Our practice is fee-for-service. We provide a Letter of Medical Necessity and the relevant codes so you can submit for potential reimbursement: diagnosis code J35.1 (chronic tonsillitis) and treatment code 42870. We are happy to discuss payment options.</div></div>
    <div class="faq-item"><div class="faq-q">My child's pediatrician recommended an ENT for tonsil removal. Can we still try laser first?</div><div class="faq-a">Absolutely — and many ENTs are receptive to a non-surgical trial before surgery. We will communicate our findings and results directly to your pediatrician and ENT. If surgery is ultimately needed, we coordinate the referral. Many pediatricians now refer patients to us specifically to attempt laser treatment before committing to tonsillectomy.</div></div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Patient stories</div>
  <h2 class="section-title">What families are saying</h2>
  <div class="testimonial-grid">
    <div class="testimonial-card"><div class="testimonial-stars">★★★★★</div><div class="testimonial-text">"My son's tonsils were Grade 3 and his pediatrician wanted a surgical referral. After 4 laser sessions with Dr. Haller, they're barely visible. No surgery, no hospital, no recovery time."</div><div class="testimonial-author">Maria T.</div><div class="testimonial-role">Tonsil Laser Treatment · Parent</div></div>
    <div class="testimonial-card"><div class="testimonial-stars">★★★★★</div><div class="testimonial-text">"My daughter had been snoring since she was three. After two sessions her snoring was noticeably better. By session five it was gone entirely. I wish we'd found Dr. Haller years earlier."</div><div class="testimonial-author">James R.</div><div class="testimonial-role">Tonsil Laser Treatment · Parent</div></div>
    <div class="testimonial-card"><div class="testimonial-stars">★★★★★</div><div class="testimonial-text">"I'd had bad breath for years despite brushing obsessively. Three laser sessions later it's gone. Turns out it was bacterial biofilm in my tonsils the whole time. Simple, painless, life-changing."</div><div class="testimonial-author">Angela M.</div><div class="testimonial-role">Adult · Recurrent Tonsillitis</div></div>
  </div>
</div>
"""

tonsils_sidebar = """
<div class="sidebar-cta-card">
  <h3>Try laser before surgery</h3>
  <p>Nothing is lost by trying laser first. Schedule a consultation to see if your child is a candidate.</p>
  <a href="index.html#contact" class="sidebar-cta-btn">Request a Consultation</a>
  <a href="tel:3054479199" class="sidebar-cta-btn-outline">(305) 447-9199</a>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Related Treatments</div>
  <ul class="sidebar-links">
    <li><a href="tongue-tie.html">Tongue Tie Release</a></li>
    <li><a href="childrens-airway.html">Children's Airway</a></li>
    <li><a href="nrt.html">Nasal Release Therapy</a></li>
    <li><a href="snoring.html">Laser Snoring Treatment</a></li>
  </ul>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Quick Facts</div>
  <div class="sidebar-fact">
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">⏱️</div><div class="sidebar-fact-text"><strong>15 minutes per session</strong>No anesthesia, no downtime</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">📸</div><div class="sidebar-fact-text"><strong>Photographed every visit</strong>Objective tracking of tonsil reduction</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🤝</div><div class="sidebar-fact-text"><strong>ENT coordination</strong>We work with your ENT throughout</div></div>
  </div>
</div>
"""

# ════════════════════════════════════════════════════════════════════════════════
# NRT PAGE
# ════════════════════════════════════════════════════════════════════════════════
nrt_hero = """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="page-breadcrumb"><a href="index.html">Home</a><span>/</span><span>Nasal Release Therapy</span></div>
    <div class="page-eyebrow">Nasal Release Therapy · Cranial Restriction Release</div>
    <h1>Nasal Release Therapy<br><em>Open What's Been Blocked</em></h1>
    <p class="page-hero-sub">NRT is a gentle, precise technique in which a small lubricated balloon is inserted into the nasal passage and briefly inflated — creating a controlled expansion that releases restrictions in the cranial bones surrounding the nasal cavity. The technique has been used for decades in chiropractic and naturopathic medicine and is now being integrated into airway-focused dental practice.</p>
    <a href="index.html#contact" class="page-hero-cta">Request a Consultation →</a>
    <div class="page-hero-badges">
      <span class="page-hero-badge">No surgery</span>
      <span class="page-hero-badge">No incision</span>
      <span class="page-hero-badge">Immediate relief common</span>
      <span class="page-hero-badge">6–8 sessions typical</span>
    </div>
  </div>
</div>"""

nrt_body = """
<div class="content-section">
  <div class="section-eyebrow">Understanding the treatment</div>
  <h2 class="section-title">What is Nasal Release Therapy?</h2>
  <p class="section-lead">NRT is a gentle, precise technique in which a small lubricated balloon is inserted into the nasal passage and briefly inflated — creating a controlled expansion that releases restrictions in the cranial bones surrounding the nasal cavity.</p>
  <div class="section-body">
    <p>A small latex finger cot coated in water-soluble lubricant is attached to an inflation bulb and gently inserted into a nasal meatus — the spaces between the nasal turbinates. When the balloon is briefly inflated, it expands posteriorly past the firmer facial and cranial bones into the softer tissues of the nasopharynx. The patient will hear or feel a "pop" or "click" — the sound of cranial bones releasing at the suture lines. The balloon is deflated immediately. The process takes only seconds per nostril and is repeated across different meatus positions in a specific sequence.</p>
    <p>The nasal cavity is surrounded by some of the most important bones of the skull — the sphenoid, vomer, ethmoid, palatine, and maxillary bones. These bones are directly accessible from inside the nose. When they are restricted or misaligned, the effects ripple through the entire cranial system. NRT reaches these bones directly — without surgery, without incision, and without general anesthesia.</p>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">The science behind NRT</div>
  <h2 class="section-title">Your skull is not one solid bone — <em>and that matters</em></h2>
  <p class="section-lead">Most people picture the skull as a single rigid helmet. In fact, it is composed of 22 bones connected by flexible sutures — joints that allow subtle, rhythmic motion throughout life. When these sutures become restricted or jammed, the consequences reach far beyond the head.</p>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">🧠</div><div class="feature-card-title">The cranial rhythm &amp; CSF connection</div><div class="feature-card-body">The brain and spinal cord are bathed in cerebrospinal fluid (CSF), which pulses in a slow, rhythmic cycle. Normal cranial suture mobility supports this rhythm. When sutures are jammed — by trauma, birth compression, or chronic tension — CSF flow may be impeded. Research has linked altered cranial motion to chronic sinusitis, headaches, brain fog, mood disturbances, and sleep disruption. NRT restores mobility to restricted sutures, often with immediate effects on how patients feel and breathe.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🚗</div><div class="feature-card-title">Adult head &amp; facial trauma</div><div class="feature-card-body">Car accidents, falls, sports injuries, and facial fractures can jam cranial bones in ways that never fully resolve — even after the acute injury heals. The result is often a constellation of symptoms patients and physicians struggle to connect: persistent headaches, tinnitus, brain fog, visual disturbances, facial asymmetry, and chronic nasal obstruction. NRT can release these restrictions years or even decades after the original injury.</div></div>
    <div class="feature-card"><div class="feature-card-icon">👶</div><div class="feature-card-title">Birth trauma — even natural delivery</div><div class="feature-card-body">Passing through the birth canal applies significant compressive forces to the cranial base. The bones are designed to overlap temporarily — but they don't always fully decompress afterward. Forceps or vacuum delivery increases this substantially. These restrictions can persist throughout life without anyone connecting them to ongoing symptoms.</div></div>
  </div>
  <div class="info-box"><p><strong>👁️ Facial asymmetry — a visible sign worth noting:</strong> One eye higher than the other. A nose that trends to one side. An uneven jaw or cheekbones. A chronic head tilt. These are often outward expressions of cranial bone misalignment — and many patients find their features gradually becoming more symmetrical as restrictions release with NRT.</p></div>
  <div class="info-box"><p><strong>📄 Research support:</strong> The nasal specific technique has been documented in chiropractic literature since the 1940s. A 1995 case study published in the Journal of Manipulative and Physiological Therapeutics documented significant relief from chronic sinusitis and sinus headaches — with improvements in post-nasal drainage, visual acuity, sense of smell, sense of taste, and ease of breathing.</p></div>
  <div class="quote-block">
    <div class="quote-text">"I began using NRT because I was seeing patients whose nasal breathing wasn't responding to expansion alone. Once I understood that many of them had cranial restrictions from old injuries or difficult births, NRT became an essential part of what I offer. The results are often immediate and sometimes quite dramatic."</div>
    <div class="quote-attr">— Dr. Leslie Haller, DMD</div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">The experience</div>
  <h2 class="section-title">What to expect — <em>before, during, and after</em></h2>
  <p class="section-lead">NRT is unlike anything most patients have experienced before. Knowing what to expect makes the experience much more manageable — and helps patients understand why the sensation, though unusual, is not harmful.</p>
  <div class="info-box"><p><strong>💡 The honest description — what it actually feels like:</strong> Dr. Haller describes NRT as feeling a little "creepy" — having a balloon inserted into the nose is an unfamiliar sensation, and the brief inflation pressure can be startling, similar to the feeling of aspirating water into the nasal passage. The first session tends to be the most uncomfortable. Successive treatments are progressively more tolerable as the cranial bones begin to open up. Most patients feel immediate relief after each session — often a sudden sense of openness in the nasal passages and head. Treatment is cumulative: each session builds on the last.</p></div>
  <ol class="steps-list">
    <li class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">Preparation</div><div class="step-desc">The nasal passages are lubricated. A small balloon on an inflation bulb is prepared. No anesthesia is required. The patient is fully awake and seated in the dental chair.</div></div></li>
    <li class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">Insertion</div><div class="step-desc">The balloon is gently guided into the nasal meatus — the space between the turbinates. Different meatus positions are used across the treatment sequence: lower, middle, and upper on each side.</div></div></li>
    <li class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">Inflation — a few seconds</div><div class="step-desc">The bulb is squeezed briefly. The balloon inflates and expands posteriorly. The patient may feel a quick pressure, hear a "click" or "pop," and feel a sudden release. The balloon is deflated immediately.</div></div></li>
    <li class="step-item"><div class="step-num">4</div><div class="step-body"><div class="step-title">Repeat across positions</div><div class="step-desc">The sequence is repeated across multiple meatus positions. A full session covers both sides and several positions. The entire procedure takes minutes.</div></div></li>
    <li class="step-item"><div class="step-num">5</div><div class="step-body"><div class="step-title">Immediate relief</div><div class="step-desc">Most patients feel an immediate opening in the nasal passages and a sense of clarity in the head. Some experience significant sinus drainage in the minutes and hours following treatment — this is normal and a sign of release.</div></div></li>
  </ol>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">✅</div><div class="feature-card-title">Common positive responses</div><div class="feature-card-body">Immediate sense of nasal openness · Significant sinus drainage — often a lot, and normal · Feeling of greater clarity in the head · Improved nasal airflow within hours · Perception of straighter posture and more symmetrical features · Feeling mentally and emotionally clearer · Improved sense of smell · Each successive session is more comfortable than the last</div></div>
    <div class="feature-card"><div class="feature-card-icon">⚠️</div><div class="feature-card-title">Temporary reactions — normal and expected</div><div class="feature-card-body">Sore nose and throat for a day or two · Temporary achiness or traveling pains in the head · Fatigue following the session · Temporary worsening of sinus symptoms — resolves quickly · Slight disorientation immediately after · Feeling excited, nervous, or unusually energetic · General body soreness for approximately three days · Occasional bloody nose — not common, resolves quickly</div></div>
  </div>
  <div class="info-box"><p><strong>📋 Cumulative treatment — 6 to 8 sessions typical:</strong> NRT is cumulative therapy. Each session builds on the last as the cranial structures progressively open up — and each session tends to be easier than the previous one. Most patients require 6 to 8 sessions, though some may need more depending on the degree of restriction and history of trauma. Sessions are typically spaced days to weeks apart to allow the cranial system to integrate each treatment before the next.</p></div>
</div>

<div class="content-section">
  <div class="section-eyebrow">The bigger picture</div>
  <h2 class="section-title">How NRT fits into the <em>full airway plan</em></h2>
  <p class="section-lead">NRT is rarely used in isolation. It is most powerful as part of a comprehensive airway treatment plan — opening the nasal passages so that expansion, tongue training, and myofunctional therapy can do their work most effectively.</p>
  <ol class="steps-list">
    <li class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">NRT — open the passages</div><div class="step-desc">Release cranial restrictions and open the nasal passages. Nasal breathing immediately becomes more accessible — setting the stage for everything that follows.</div></div></li>
    <li class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">Tongue tie release — if indicated</div><div class="step-desc">If a tongue tie is present, release it before beginning arch expansion. A free tongue can apply upward pressure on the palate and support nasal breathing.</div></div></li>
    <li class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">Arch expansion — make it permanent</div><div class="step-desc">Widen the palate and nasal passages structurally — making the gains from NRT lasting. Expansion and NRT work synergistically: open passages expand more easily; a wider arch sustains open passages.</div></div></li>
    <li class="step-item"><div class="step-num">4</div><div class="step-body"><div class="step-title">Myofunctional therapy — retrain muscles</div><div class="step-desc">Retrain the tongue, lips, and throat muscles to support nasal breathing permanently. Without this step, old mouth-breathing habits may reassert themselves even after the structural work is done.</div></div></li>
  </ol>
  <div class="quote-block">
    <div class="quote-text">"For patients who are mouth breathers, NRT is often the missing piece. We can expand the arch, release the tongue tie, retrain the muscles — and still have a patient who defaults to mouth breathing because their nasal passages have a structural restriction we haven't addressed. NRT takes care of that."</div>
    <div class="quote-attr">— Dr. Leslie Haller, DMD</div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Frequently asked questions</div>
  <h2 class="section-title">What patients ask most about NRT</h2>
  <div class="faq-list">
    <div class="faq-item"><div class="faq-q">Is NRT painful?</div><div class="faq-a">The honest answer is that it is uncomfortable — particularly the first session. The sensation of having a balloon inserted into the nasal passage is unfamiliar, and the brief inflation can be startling, similar to getting water in the nose. Most patients describe it as more surprising than painful. The good news: each successive session is noticeably easier than the last as the cranial structures open up and become more mobile.</div></div>
    <div class="faq-item"><div class="faq-q">How many sessions will I need?</div><div class="faq-a">Most patients require 6 to 8 sessions, though those with significant restrictions or significant trauma history may need more. Sessions are typically scheduled days to weeks apart. Results are cumulative — most patients notice progressive improvement with each session rather than a single dramatic change.</div></div>
    <div class="faq-item"><div class="faq-q">What will I feel immediately after?</div><div class="faq-a">Most patients feel an immediate sense of openness in the nasal passages — as though something that was blocked has released. There is often significant sinus drainage in the hours following treatment, which is a normal sign of release. Some patients feel slightly disoriented or unusually energetic. Soreness in the nose and throat is common for a day or two. Occasionally there may be a brief bloody nose — this is not common and resolves quickly.</div></div>
    <div class="faq-item"><div class="faq-q">I had a deviated septum diagnosed. Can NRT help?</div><div class="faq-a">Possibly — and it is worth trying before pursuing surgery. NRT addresses the cranial bone component of nasal obstruction, which may be contributing to or exacerbating the symptoms attributed to the deviated septum. It does not physically straighten a deviated septum, but many patients with deviated septum symptoms find significant improvement with NRT. If symptoms persist after a full course of treatment, surgical options remain available.</div></div>
    <div class="faq-item"><div class="faq-q">Can NRT be used for children?</div><div class="faq-a">Yes — and children with birth-related cranial restrictions often respond very well. The cranial system is more responsive in younger patients, and results can be quite rapid. Dr. Haller evaluates every child with persistent nasal obstruction or unexplained symptoms for potential cranial restriction as part of the full airway assessment.</div></div>
    <div class="faq-item"><div class="faq-q">Does insurance cover NRT?</div><div class="faq-a">NRT is generally not covered by insurance as it is considered an emerging therapy. Our practice is fee-for-service. We provide a Letter of Medical Necessity and insurance codes for submission. The cost per session is typically modest — especially in comparison to surgical alternatives.</div></div>
    <div class="faq-item"><div class="faq-q">Are there any contraindications — who should not have NRT?</div><div class="faq-a">Yes. NRT is not appropriate for everyone. Absolute contraindications include hemophilia and severe cranial osteoporosis. Patients on blood thinners can be treated with special preparation — the nasal passages should be lubricated for 3 days prior to treatment. NRT should be avoided with active nasal fistulas with infection, recent unhealed nasal fractures, or previous facial surgery with surgical plates (proceed with caution). Patients with a history of cocaine use or other intranasal substances should disclose this. Occasionally NRT can trigger strong emotional responses — Dr. Haller reviews your full medical history before every session.</div></div>
  </div>
</div>
"""

nrt_sidebar = """
<div class="sidebar-cta-card">
  <h3>Could NRT be the missing piece?</h3>
  <p>If nasal breathing hasn't improved despite other treatment, cranial restriction may be the reason. Schedule a consultation to find out.</p>
  <a href="index.html#contact" class="sidebar-cta-btn">Request a Consultation</a>
  <a href="tel:3054479199" class="sidebar-cta-btn-outline">(305) 447-9199</a>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Related Treatments</div>
  <ul class="sidebar-links">
    <li><a href="tongue-tie.html">Tongue Tie Release</a></li>
    <li><a href="adult-airway.html">Adult Airway Expansion</a></li>
    <li><a href="tonsils.html">Laser Tonsil Treatment</a></li>
    <li><a href="sleep-apnea.html">Sleep Apnea Treatment</a></li>
  </ul>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">NRT May Help If You Have</div>
  <div class="sidebar-fact">
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🚗</div><div class="sidebar-fact-text"><strong>Trauma history</strong>Car accident, sports concussion, fall, nasal fracture</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">👶</div><div class="sidebar-fact-text"><strong>Difficult birth</strong>Long labor, forceps/vacuum delivery</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🤔</div><div class="sidebar-fact-text"><strong>Unexplained symptoms</strong>Chronic headaches, tinnitus, brain fog, facial asymmetry</div></div>
  </div>
</div>
"""

# ════════════════════════════════════════════════════════════════════════════════
# SNORING PAGE
# ════════════════════════════════════════════════════════════════════════════════
snoring_hero = """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="page-breadcrumb"><a href="index.html">Home</a><span>/</span><span>Laser Snoring Treatment</span></div>
    <div class="page-eyebrow">Laser Snoring Treatment · Coral Gables, FL</div>
    <h1>Stop Snoring.<br><em>No Surgery. No Downtime.</em></h1>
    <p class="page-hero-sub">A fractional CO2 laser tightens the soft palate and throat tissue — the same biological principle as microneedling for the face, but completely painless. Most patients notice results within 1–5 days. Two sessions. Annual touch-up. That's it.</p>
    <a href="index.html#contact" class="page-hero-cta">Request a Consultation →</a>
    <div class="page-hero-badges">
      <span class="page-hero-badge">5–10 minute procedure</span>
      <span class="page-hero-badge">No anesthesia</span>
      <span class="page-hero-badge">Results in 1–5 days</span>
      <span class="page-hero-badge">Lasts 12–18 months</span>
    </div>
  </div>
</div>"""

snoring_body = """
<div class="content-section">
  <div class="section-eyebrow">The anatomy of a snore</div>
  <h2 class="section-title">Why do people snore?</h2>
  <p class="section-lead">The throat is a tube. When that tube narrows during sleep, air rushing through causes the surrounding soft tissue to vibrate. That vibration is the sound of snoring.</p>
  <div class="section-body">
    <p>The soft palate, uvula, tonsils, and the sides of the tongue are the primary vibrating surfaces. When this tissue is lax, elongated, or falls back during sleep, it partially blocks the airway — and vibrates with every breath.</p>
  </div>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">😮</div><div class="feature-card-title">Primary causes</div><div class="feature-card-body">Lax or elongated soft palate — the most common cause · Enlarged tonsils — often caused by chronic mouth breathing · Tongue falling backward during sleep · Nasal obstruction — forces mouth breathing, worsening snoring · Low tongue posture from tongue tie</div></div>
    <div class="feature-card"><div class="feature-card-icon">⚠️</div><div class="feature-card-title">Contributing factors that make it worse</div><div class="feature-card-body">Weight gain — increases tissue around the airway · Alcohol and sedatives — relax throat muscles further · Sleeping on your back — tongue falls back more · Underdeveloped jaws — a smaller airway means less room · Age — tissue naturally loses tone over time</div></div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">The treatment</div>
  <h2 class="section-title">How laser snoring treatment works — <em>think microneedling, but for your throat</em></h2>
  <p class="section-lead">If you've heard of microneedling for the face — where tiny controlled injuries trigger new collagen and tighter skin — the principle here is identical. The difference is that the laser is completely painless. Most patients feel nothing at all. The occasional patient notices a little tingling or mild warmth — and that's about as uncomfortable as it gets.</p>
  <ol class="steps-list">
    <li class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">One beam becomes hundreds</div><div class="step-desc">A special fractional attachment splits the laser beam into hundreds of tiny pixel beams — spreading the energy precisely across the treatment area without damaging surrounding tissue.</div></div></li>
    <li class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">Thousands of microscopic injuries</div><div class="step-desc">The pixel beams create a grid of tiny controlled micro-injuries in the soft palate, uvula, tonsils, and sides of the tongue — precisely where the vibration occurs during sleep.</div></div></li>
    <li class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">Wound healing response</div><div class="step-desc">The body heals these microinjuries by producing new collagen — stronger, firmer collagen than was there before. Collagen production peaks at around one month.</div></div></li>
    <li class="step-item"><div class="step-num">4</div><div class="step-body"><div class="step-title">Tissue tightens — snoring reduces</div><div class="step-desc">As the new collagen matures, the soft palate shrinks and firms. The throat opens. The tissue that was vibrating and causing snoring is now tighter, shorter, and far less likely to vibrate.</div></div></li>
  </ol>
  <div class="info-box"><p><strong>😌 What the treatment feels like:</strong> During the procedure, most patients feel mild warmth or a light tingling. Many feel nothing at all. The session takes 5–10 minutes and requires no anesthesia. Afterward, the most common experience is a very mild sore throat that evening — similar to the feeling of coming down with a cold, but without the cold. It resolves within a day or two. Patients return to normal activity immediately.</p></div>
</div>

<div class="content-section">
  <div class="section-eyebrow">What to expect</div>
  <h2 class="section-title">The treatment timeline</h2>
  <p class="section-lead">Two sessions, spaced about a month apart, produce the best and longest-lasting results. An annual touch-up session keeps the results going year after year.</p>
  <ol class="steps-list">
    <li class="step-item"><div class="step-num" style="background:var(--gold);color:var(--navy)">Day 1</div><div class="step-body"><div class="step-title">Session 1 — First session, 5 to 10 minutes</div><div class="step-desc">The fractional laser is applied to the soft palate, uvula, tonsils, and tongue sides. No anesthesia required. You leave the office immediately and resume all normal activities. That evening, a mild sore throat is possible — like the start of a cold, but it isn't one. Most patients notice a reduction in snoring within 1 to 5 days as initial tissue swelling subsides.</div></div></li>
    <li class="step-item"><div class="step-num" style="background:var(--gold);color:var(--navy)">~4 wks</div><div class="step-body"><div class="step-title">Session 2 — Best results</div><div class="step-desc">Collagen regeneration from the first session peaks at around one month. The second session builds on this response — adding a new round of collagen production on top of already-tightening tissue. Most patients achieve their best results after this second session. Results typically last 12 to 18 months.</div></div></li>
    <li class="step-item"><div class="step-num" style="background:var(--gold);color:var(--navy)">Annual</div><div class="step-body"><div class="step-title">Touch-up — Once-a-year maintenance</div><div class="step-desc">A single annual touch-up session keeps the results going. Most patients find the maintenance session even easier and more comfortable than the initial treatments as the tissue has already been conditioned. Many patients schedule their annual session as part of their regular dental care.</div></div></li>
  </ol>
</div>

<div class="content-section">
  <div class="section-eyebrow">Part of the bigger picture</div>
  <h2 class="section-title">Snoring is often a symptom — <em>not a standalone problem</em></h2>
  <p class="section-lead">For many patients, snoring laser treatment is a fast, effective solution. For others, snoring is one sign of a broader airway issue. Dr. Haller evaluates the full picture and can combine treatments for better, longer-lasting results.</p>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">🦷</div><div class="feature-card-title">Tonsil laser decontamination</div><div class="feature-card-body">Enlarged tonsils are a common contributor to snoring. Shrinking them with the CO2 laser — in the same visit — opens the airway further and enhances the effect of snoring treatment.</div></div>
    <div class="feature-card"><div class="feature-card-icon">👃</div><div class="feature-card-title">Nasal Release Therapy</div><div class="feature-card-body">If nasal obstruction is forcing mouth breathing and worsening snoring, NRT opens the nasal passages — making nasal breathing the easier default and reducing snoring from that upstream cause.</div></div>
    <div class="feature-card"><div class="feature-card-icon">👅</div><div class="feature-card-title">Tongue tie evaluation</div><div class="feature-card-body">A tongue tie causes low tongue posture — the tongue falls back during sleep and contributes to airway narrowing. If present, releasing it is the upstream fix that makes everything else work better.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🌱</div><div class="feature-card-title">Airway expansion</div><div class="feature-card-body">For patients who want a more permanent structural solution, epigenetic arch expansion widens the palate and airway — addressing the anatomical root cause of snoring and sleep-disordered breathing.</div></div>
  </div>
  <div class="warning-box"><p><strong>💤 A note on sleep apnea:</strong> Laser snoring treatment reduces snoring effectively — but it is not a treatment for obstructive sleep apnea. If your snoring is accompanied by daytime sleepiness, gasping or choking episodes, or if a bed partner has witnessed pauses in your breathing, it's worth being evaluated for sleep apnea before or alongside snoring treatment. Treating the sound without treating the underlying obstruction leaves the more serious problem unaddressed. Dr. Haller is happy to discuss this at your consultation.</p></div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Frequently asked questions</div>
  <h2 class="section-title">What patients ask most</h2>
  <div class="faq-list">
    <div class="faq-item"><div class="faq-q">Does it hurt?</div><div class="faq-a">No. Most patients feel mild warmth or a light tingling during the procedure — many feel nothing at all. There is no anesthesia required. That evening, a very mild sore throat is possible — similar to the feeling of coming down with a cold. It is not a cold, and it resolves within a day or two. Patients return to all normal activities immediately after treatment.</div></div>
    <div class="faq-item"><div class="faq-q">How quickly will I notice results?</div><div class="faq-a">Most patients notice a reduction in snoring within 1 to 5 days after the first session. The second session, at around 4 weeks, builds on the first. Full results — as the new collagen matures — develop over the following weeks and typically reach their peak at around 6 to 8 weeks after the second session.</div></div>
    <div class="faq-item"><div class="faq-q">How long do results last?</div><div class="faq-a">Results typically last 12 to 18 months. An annual touch-up session — just one, just 5–10 minutes — maintains the results. Most patients find the touch-up session more comfortable than the original treatment, and many schedule it as part of their regular dental care.</div></div>
    <div class="faq-item"><div class="faq-q">Does insurance cover this?</div><div class="faq-a">No. Insurance companies classify snoring treatment as elective and do not cover it. Our practice is fee-for-service. We provide a superbill for your records. Payment is due at time of service.</div></div>
    <div class="faq-item"><div class="faq-q">Can I combine this with other treatments?</div><div class="faq-a">Yes — and for many patients, combining treatments produces better and longer-lasting results. Tonsil laser decontamination and snoring treatment can often be done in the same visit
. Nasal Release Therapy can be done on a separate visit. Dr. Haller will discuss the full picture at your consultation and recommend the combination most appropriate for your situation.</div></div>
    <div class="faq-item"><div class="faq-q">I've tried a mandibular advancement device (MAD) for snoring. Is this different?</div><div class="faq-a">Yes — completely different. A MAD device works by repositioning the jaw to hold the airway open mechanically — it requires wearing a device every night. Laser snoring treatment works by tightening the tissue that vibrates — no device required. Many patients prefer the laser approach precisely because it requires nothing to wear at night. The two approaches are not mutually exclusive — some patients use both.</div></div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Patient stories</div>
  <h2 class="section-title">What our patients say</h2>
  <div class="testimonial-grid">
    <div class="testimonial-card"><div class="testimonial-stars">★★★★★</div><div class="testimonial-text">"My husband had been snoring for 20 years. Two sessions with Dr. Haller and it's essentially gone. He was skeptical going in — he's a convert now."</div><div class="testimonial-author">Carol B.</div><div class="testimonial-role">Laser Snoring Treatment</div></div>
    <div class="testimonial-card"><div class="testimonial-stars">★★★★★</div><div class="testimonial-text">"I was embarrassed to travel because of my snoring. After two sessions I went on a work trip and my roommate said they didn't hear a thing. Completely painless procedure."</div><div class="testimonial-author">David L.</div><div class="testimonial-role">Laser Snoring Treatment</div></div>
  </div>
</div>
"""

snoring_sidebar = """
<div class="sidebar-cta-card">
  <h3>Two sessions. No surgery. No device.</h3>
  <p>Most patients notice results within days. Schedule a consultation to see if laser snoring treatment is right for you.</p>
  <a href="index.html#contact" class="sidebar-cta-btn">Request a Consultation</a>
  <a href="tel:3054479199" class="sidebar-cta-btn-outline">(305) 447-9199</a>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Related Treatments</div>
  <ul class="sidebar-links">
    <li><a href="sleep-apnea.html">Sleep Apnea Treatment</a></li>
    <li><a href="tonsils.html">Laser Tonsil Treatment</a></li>
    <li><a href="tongue-tie.html">Tongue Tie Release</a></li>
    <li><a href="nrt.html">Nasal Release Therapy</a></li>
  </ul>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Quick Facts</div>
  <div class="sidebar-fact">
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">⏱️</div><div class="sidebar-fact-text"><strong>5–10 minutes</strong>No anesthesia, no downtime</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">📅</div><div class="sidebar-fact-text"><strong>2 sessions</strong>Spaced ~4 weeks apart for best results</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🔄</div><div class="sidebar-fact-text"><strong>Annual touch-up</strong>Maintains results year after year</div></div>
  </div>
</div>
"""

# ════════════════════════════════════════════════════════════════════════════════
# TONGUE TIE PAGE
# ════════════════════════════════════════════════════════════════════════════════
tonguetie_hero = """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="page-breadcrumb"><a href="index.html">Home</a><span>/</span><span>Tongue Tie</span></div>
    <div class="page-eyebrow">Tongue Tie Frenectomy · Adults &amp; Children · Coral Gables, FL</div>
    <h1>Tongue Tie Release —<br><em>The Upstream Fix for Airway Problems</em></h1>
    <p class="page-hero-sub">A tongue tie is not just a feeding problem in newborns. In children and adults, a restricted tongue is one of the most common and most overlooked causes of mouth breathing, jaw underdevelopment, sleep-disordered breathing, and a cascade of downstream health consequences.</p>
    <a href="index.html#contact" class="page-hero-cta">Request a Consultation →</a>
    <div class="page-hero-badges">
      <span class="page-hero-badge">CO2 laser frenectomy</span>
      <span class="page-hero-badge">No sutures in most cases</span>
      <span class="page-hero-badge">Children &amp; adults</span>
      <span class="page-hero-badge">Myofunctional therapy coordination</span>
    </div>
  </div>
</div>"""

tonguetie_body = """
<div class="content-section">
  <div class="section-eyebrow">What is a tongue tie?</div>
  <h2 class="section-title">More than a feeding problem — <em>a lifelong airway issue</em></h2>
  <p class="section-lead">A tongue tie (ankyloglossia) is a restriction of the lingual frenum — the band of tissue connecting the underside of the tongue to the floor of the mouth. When this tissue is too short, too thick, or too tightly attached, it limits the tongue's range of motion in ways that affect breathing, jaw development, sleep, and overall health throughout life.</p>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">👶</div><div class="feature-card-title">In infants</div><div class="feature-card-body">Difficulty latching and breastfeeding · Painful nursing for mother · Slow weight gain · Clicking or popping during feeding · Gassiness and reflux from poor latch · Maternal mastitis from poor latch · Bottle-feeding difficulties</div></div>
    <div class="feature-card"><div class="feature-card-icon">🧒</div><div class="feature-card-title">In children</div><div class="feature-card-body">Mouth breathing · Narrow dental arches · Crowded teeth · Prolonged thumb sucking · Speech difficulties (especially "r," "l," "th," "s") · Snoring and sleep-disordered breathing · ADHD-like symptoms from poor sleep · Picky eating and texture aversions · Forward head posture</div></div>
    <div class="feature-card"><div class="feature-card-icon">🧑</div><div class="feature-card-title">In adults</div><div class="feature-card-body">Chronic jaw tension and TMJ pain · Neck and shoulder tightness · Headaches · Sleep apnea and snoring · Difficulty chewing or swallowing certain foods · Speech impediments · Dental crowding and recession · Digestive issues from poor chewing · Chronic mouth breathing</div></div>
  </div>
  <div class="info-box"><p><strong>🔍 The tongue tie most people miss — posterior tongue tie:</strong> The classic tongue tie is easy to see — the tongue can't stick out past the lips, and the frenum is clearly visible. But the most commonly missed type is the posterior tongue tie — where the restriction is deeper in the floor of the mouth, under a mucous membrane, and not visible on casual inspection. The tongue may appear to move freely, but its range of motion is significantly limited. Posterior tongue ties are frequently missed by pediatricians, lactation consultants, and even dentists who are not specifically trained to identify them. Dr. Haller evaluates for both anterior and posterior tongue ties using functional assessment, not just visual inspection.</p></div>
</div>

<div class="content-section">
  <div class="section-eyebrow">The airway connection</div>
  <h2 class="section-title">How tongue tie drives <em>mouth breathing and airway problems</em></h2>
  <p class="section-lead">The tongue's resting position is the most important factor in jaw development and airway health. When the tongue is tied, it cannot rest in its correct position — and the consequences cascade through the entire airway system.</p>
  <ol class="steps-list">
    <li class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">Correct tongue posture</div><div class="step-desc">The tongue should rest with its entire body pressed against the roof of the mouth (the palate). This upward pressure is what shapes the palate and jaw during development — and what keeps the airway open during sleep.</div></div></li>
    <li class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">Tongue tie → low tongue posture</div><div class="step-desc">A restricted tongue cannot reach the palate. It sits low in the floor of the mouth instead — providing no upward pressure on the palate and no forward pressure on the lower jaw.</div></div></li>
    <li class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">Underdeveloped jaws</div><div class="step-desc">Without the tongue's shaping pressure, the palate narrows and the jaws underdevelop. A narrow palate means a narrow nasal floor — directly reducing nasal airway volume. A recessed lower jaw means less space for the tongue, which falls back during sleep.</div></div></li>
    <li class="step-item"><div class="step-num">4</div><div class="step-body"><div class="step-title">Mouth breathing begins</div><div class="step-desc">With a narrow nasal airway, nasal breathing becomes difficult or impossible. The child or adult defaults to mouth breathing — which bypasses the nose's filtration and humidification, dries the mouth, and delivers unfiltered air to the tonsils and throat.</div></div></li>
    <li class="step-item"><div class="step-num">5</div><div class="step-body"><div class="step-title">Sleep-disordered breathing</div><div class="step-desc">During sleep, the low-postured tongue falls back into the airway. Combined with the narrow airway created by underdeveloped jaws, this causes snoring, sleep apnea, and disrupted sleep — with all the downstream health consequences.</div></div></li>
  </ol>
  <div class="quote-block">
    <div class="quote-text">"Tongue tie is upstream of almost everything else I treat. I can expand the arch, release the nasal passages, and treat the tonsils — but if the tongue is still restricted, the tongue will keep pulling everything back. Releasing the tongue tie is often the first and most important step."</div>
    <div class="quote-attr">— Dr. Leslie Haller, DMD</div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">The procedure</div>
  <h2 class="section-title">CO2 laser frenectomy — <em>precise, fast, and well-tolerated</em></h2>
  <p class="section-lead">Dr. Haller performs tongue tie release using a CO2 laser — the gold standard for soft tissue frenectomy. The laser seals blood vessels as it cuts, dramatically reducing bleeding and post-operative discomfort compared to scissors or scalpel techniques.</p>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">⚡</div><div class="feature-card-title">The CO2 laser advantage</div><div class="feature-card-body">Minimal bleeding — vessels are sealed as the laser cuts · Reduced post-operative swelling and discomfort · No sutures required in most cases · Sterile incision — laser sterilizes as it cuts · Faster healing than scissors or scalpel · Precise — only the targeted tissue is affected</div></div>
    <div class="feature-card"><div class="feature-card-icon">⏱️</div><div class="feature-card-title">The procedure itself</div><div class="feature-card-body">Local anesthetic is applied (topical for infants, injectable for older children and adults). The frenum is identified and the release is performed with the CO2 laser. The entire procedure takes minutes. Patients leave with full range of motion immediately. Post-operative exercises are prescribed to maintain the release and prevent reattachment.</div></div>
  </div>
  <div class="info-box"><p><strong>⚠️ Critical: Myofunctional therapy before and after release</strong><br>Tongue tie release without myofunctional therapy is frequently incomplete — and often reattaches. The tongue has been restricted for years or decades. Simply releasing the frenum does not automatically teach the tongue to rest in the correct position. Without active retraining, the tongue reverts to its old low posture, the release site may reattach, and the benefits of the procedure are lost. Dr. Haller coordinates myofunctional therapy referrals for every tongue tie patient. For children old enough to participate (typically 4+), pre-operative myofunctional therapy is strongly recommended to prepare the tongue for its new range of motion. Post-operative exercises are prescribed for all patients regardless of age.</p></div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Frequently asked questions</div>
  <h2 class="section-title">What patients ask most</h2>
  <div class="faq-list">
    <div class="faq-item"><div class="faq-q">My pediatrician said my child's tongue tie doesn't need treatment. Should I get a second opinion?</div><div class="faq-a">Yes — if your child has symptoms. Many pediatricians are trained to identify only the most severe anterior tongue ties and may miss posterior restrictions entirely. The standard assessment is often visual only, without functional testing. If your child has persistent mouth breathing, snoring, speech difficulties, dental crowding, or ADHD-like symptoms, it is worth a functional assessment by a provider specifically trained in tongue tie evaluation.</div></div>
    <div class="faq-item"><div class="faq-q">Is it too late to treat a tongue tie in adulthood?</div><div class="faq-a">No. Adults with tongue ties can benefit significantly from release — particularly for jaw tension, TMJ pain, sleep apnea, and chronic neck and shoulder tightness. The structural changes to the jaw that occurred during development cannot be reversed by release alone in adults — but arch expansion combined with tongue tie release can still achieve meaningful airway improvement at any age. Dr. Haller treats adults with tongue ties regularly.</div></div>
    <div class="faq-item"><div class="faq-q">Will my child need to be sedated?</div><div class="faq-a">No. Dr. Haller performs tongue tie release under local anesthesia — topical for infants, injectable for older children and adults. General anesthesia is not required. The procedure takes minutes. Most children tolerate it well, particularly when pre-operative myofunctional therapy has been done to prepare them.</div></div>
    <div class="faq-item"><div class="faq-q">How do I know if the tongue tie is causing my child's symptoms?</div><div class="faq-a">This is exactly what a functional assessment determines. Dr. Haller evaluates tongue range of motion, tongue posture, jaw development, nasal airway, and signs of sleep-disordered breathing together — to understand whether the tongue tie is a contributing factor and what the likely benefit of release would be. She will give you an honest assessment of what is likely to improve and what may require additional treatment.</div></div>
    <div class="faq-item"><div class="faq-q">What is the recovery like?</div><div class="faq-a">For infants: minimal. Some fussiness for a day or two, resolved with appropriate pain management. Breastfeeding can typically resume immediately. For older children and adults: mild soreness for 2–5 days, managed with over-the-counter pain relief. Post-operative stretching exercises are prescribed to maintain the release and prevent reattachment — these are critical and must be performed consistently for the first several weeks.</div></div>
    <div class="faq-item"><div class="faq-q">Does insurance cover tongue tie release?</div><div class="faq-a">Sometimes — particularly for infants with documented breastfeeding difficulties. Coverage varies significantly by plan. Our practice is fee-for-service. We provide all necessary codes and a Letter of Medical Necessity for insurance submission. We are happy to discuss payment options at consultation.</div></div>
  </div>
</div>
"""

tonguetie_sidebar = """
<div class="sidebar-cta-card">
  <h3>Is tongue tie driving your symptoms?</h3>
  <p>A functional assessment takes 30 minutes and can identify whether tongue tie is contributing to breathing, sleep, or jaw problems.</p>
  <a href="index.html#contact" class="sidebar-cta-btn">Request a Consultation</a>
  <a href="tel:3054479199" class="sidebar-cta-btn-outline">(305) 447-9199</a>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Related Treatments</div>
  <ul class="sidebar-links">
    <li><a href="adult-airway.html">Adult Airway Expansion</a></li>
    <li><a href="childrens-airway.html">Children's Airway</a></li>
    <li><a href="tonsils.html">Laser Tonsil Treatment</a></li>
    <li><a href="sleep-apnea.html">Sleep Apnea Treatment</a></li>
  </ul>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Signs of Tongue Tie</div>
  <div class="sidebar-fact">
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">👅</div><div class="sidebar-fact-text"><strong>Can't touch roof of mouth</strong>Tongue can't fully elevate</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">😮</div><div class="sidebar-fact-text"><strong>Mouth breathing</strong>Default to open-mouth breathing</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">😬</div><div class="sidebar-fact-text"><strong>Jaw tension / TMJ</strong>Chronic clenching or jaw pain</div></div>
  </div>
</div>
"""

# ════════════════════════════════════════════════════════════════════════════════
# ADULT AIRWAY PAGE
# ════════════════════════════════════════════════════════════════════════════════
adult_hero = """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="page-breadcrumb"><a href="index.html">Home</a><span>/</span><span>Adult Airway Expansion</span></div>
    <div class="page-eyebrow">Adult Airway Expansion · Epigenetic Remodeling · Coral Gables, FL</div>
    <h1>Expand Your Airway.<br><em>Permanently. Without Surgery.</em></h1>
    <p class="page-hero-sub">The adult skull is not fully fused. The sutures between the facial bones remain responsive to gentle, sustained forces throughout life. Epigenetic arch remodeling uses custom oral appliances to gradually widen the palate and nasal passages — creating a structurally larger airway that stays open on its own, without a machine or device every night.</p>
    <a href="index.html#contact" class="page-hero-cta">Request a Consultation →</a>
    <div class="page-hero-badges">
      <span class="page-hero-badge">No surgery</span>
      <span class="page-hero-badge">Permanent structural change</span>
      <span class="page-hero-badge">Trained by the pioneers</span>
      <span class="page-hero-badge">12–24 month treatment</span>
    </div>
    <div class="page-hero-stats">
      <div><div class="hero-stat-val">7.7→24.1 cm²</div><div class="hero-stat-label">documented airway growth in published cases</div></div>
      <div><div class="hero-stat-val">12–24</div><div class="hero-stat-label">months typical treatment duration</div></div>
      <div><div class="hero-stat-val">Permanent</div><div class="hero-stat-label">structural change — not maintenance therapy</div></div>
      <div><div class="hero-stat-val">Any age</div><div class="hero-stat-label">adult patients treated — no upper age limit</div></div>
    </div>
  </div>
</div>"""

adult_body = """
<div class="content-section">
  <div class="section-eyebrow">The science</div>
  <h2 class="section-title">The adult skull is not fully fused — <em>and that changes everything</em></h2>
  <p class="section-lead">For decades, the conventional wisdom was that adult facial bones were fused and immovable — that the window for jaw development closed in childhood. That view is now being overturned by a growing body of clinical evidence and the work of pioneering practitioners who have been quietly achieving remarkable results in adult patients.</p>
  <div class="section-body">
    <p>The sutures between the facial bones — the mid-palatal suture, the pterygomaxillary suture, the zygomaticomaxillary suture — do not fully ossify in most adults. They remain as fibrous joints that can respond to gentle, sustained forces. The key is the right appliance, the right force, and the right duration.</p>
    <p>Epigenetic arch remodeling uses custom oral appliances worn during sleep (and sometimes during the day) to apply precisely calibrated forces to the palate and dental arches. Over months and years, these forces gradually widen the palate — expanding the nasal floor, increasing nasal airway volume, and creating more space for the tongue.</p>
  </div>
  <div class="info-box"><p><strong>📐 What "epigenetic" means in this context:</strong> Epigenetics refers to changes in gene expression that don't involve changes to the DNA sequence itself — changes triggered by environmental signals. In this context, the appliance provides a mechanical signal that activates the genes responsible for bone remodeling. The body responds by depositing new bone in the expanded suture — making the change permanent, not just mechanical.</p></div>
  <div class="quote-block">
    <div class="quote-text">"Along with releasing tongue ties, airway remodeling is the most satisfying work of my life. I have had patients tell me their tinnitus went away, that they could smell their wife's perfume for the first time, that their child finally slept through the night. The results can be profound — and they are permanent."</div>
    <div class="quote-attr">— Dr. Leslie Haller, DMD</div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">The appliances</div>
  <h2 class="section-title">Multiple systems — <em>tailored to your anatomy and goals</em></h2>
  <p class="section-lead">Dr. Haller has trained with the leading innovators in epigenetic airway expansion and uses a range of appliance systems — selecting the right tool for each patient's anatomy, severity, and treatment goals.</p>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">🦷</div><div class="feature-card-title">Vivos DNA/mRNA Appliance</div><div class="feature-card-body">The Vivos system is one of the most extensively studied epigenetic appliances. The DNA appliance is worn primarily at night and uses a combination of expansion and mandibular repositioning to widen the arch and advance the jaw. The mRNA appliance adds a mandibular component for patients with both maxillary and mandibular underdevelopment. Vivos has published significant clinical data on airway volume changes in adult patients.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🔬</div><div class="feature-card-title">Homeoblock (Dr. Theodore Belfor)</div><div class="feature-card-body">Developed by Dr. Theodore Belfor, the Homeoblock is a removable appliance that uses a small spring to apply gentle forces to the palate. It is worn primarily at night and works with the body's natural growth signals rather than against them. Dr. Haller has trained directly with Dr. Belfor and uses the Homeoblock for appropriate patients.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🌱</div><div class="feature-card-title">AHS / ALF Appliances</div><div class="feature-card-body">The Advanced Lightwire Functional (ALF) appliance uses extremely light forces — working with the cranial rhythm rather than against it. It is particularly useful for patients with cranial sensitivity, TMJ issues, or those who have not responded well to heavier-force appliances. Dr. Haller has trained with AHS Airway Health Solutions and uses ALF-based systems for appropriate patients.</div></div>
    <div class="feature-card"><div class="feature-card-icon">💡</div><div class="feature-card-title">Holistic Mouth Solutions (Dr. Felix Liao)</div><div class="feature-card-body">Dr. Felix Liao's Holistic Mouth approach addresses the relationship between jaw development, whole-body health, and chronic disease. Dr. Haller has trained with Dr. Liao and incorporates his framework for evaluating the "impaired mouth" as a contributing factor to systemic health problems — from fatigue and pain to cardiovascular risk.</div></div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">What to expect</div>
  <h2 class="section-title">The treatment journey — <em>honest and complete</em></h2>
  <p class="section-lead">Epigenetic arch remodeling is a significant commitment. Dr. Haller believes in giving patients a fully honest picture of what the process involves — so they can make an informed decision and commit with realistic expectations.</p>
  <ol class="steps-list">
    <li class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">Comprehensive evaluation</div><div class="step-desc">CBCT imaging provides a three-dimensional view of the airway, jaw, and cranial structures. Dr. Haller measures airway volume, palate width, jaw position, tongue space, and nasal airway dimensions. A full functional assessment includes tongue tie evaluation, myofunctional assessment, and sleep history. This evaluation determines whether you are a candidate, which appliance system is most appropriate, and what results are realistically achievable.</div></div></li>
    <li class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">Tongue tie release — if indicated</div><div class="step-desc">If a tongue tie is present, releasing it before beginning expansion is critical. The tongue must be free to rest on the palate — both to support the expansion process and to maintain the results afterward. Myofunctional therapy begins before or immediately after release.</div></div></li>
    <li class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">Appliance fitting and activation</div><div class="step-desc">The custom appliance is fabricated from precise impressions or digital scans. Dr. Haller fits and activates the appliance, explaining exactly how to wear it and how to perform the activation protocol. Most appliances are worn primarily at night. Some require daytime wear as well.</div></div></li>
    <li class="step-item"><div class="step-num">4</div><div class="step-body"><div class="step-title">Active expansion phase — 12 to 24 months</div><div class="step-desc">The appliance is worn consistently and activated on a prescribed schedule. Follow-up appointments every 4–8 weeks allow Dr. Haller to monitor progress, adjust the appliance, and address any issues. CBCT imaging at intervals documents measurable changes in airway volume and palate width. Changes develop gradually — most patients notice improvements in nasal breathing, sleep quality, and energy within the first 3–6 months.</div></div></li>
    <li class="step-item"><div class="step-num">5</div><div class="step-body"><div class="step-title">Retention and consolidation</div><div class="step-desc">Once target dimensions are achieved, a retention phase allows the new bone to fully consolidate. Myofunctional therapy continues throughout to retrain the tongue and facial muscles to support the new structure. Most patients transition to a retainer worn only at night.</div></div></li>
    <li class="step-item"><div class="step-num">6</div><div class="step-body"><div class="step-title">Long-term results</div><div class="step-desc">The structural changes are permanent. The new bone does not resorb. Many patients find they no longer need a CPAP or MAD device once the airway has been sufficiently expanded. Individual results vary — Dr. Haller will give you an honest assessment of what is achievable for your specific anatomy.</div></div></li>
  </ol>
  <div class="warning-box"><p><strong>⚠ A realistic picture:</strong> Epigenetic arch remodeling is not a quick fix. It requires consistent appliance wear, regular follow-up, and commitment to the full treatment plan including myofunctional therapy. Results develop gradually over months. Some patients experience temporary discomfort, speech changes, or increased salivation during the early weeks of treatment. These resolve as the body adapts. Dr. Haller will not recommend this treatment unless she believes the potential benefit justifies the commitment — and she will tell you honestly if she thinks a different approach is more appropriate for your situation.</p></div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Frequently asked questions</div>
  <h2 class="section-title">What patients ask most</h2>
  <div class="faq-list">
    <div class="faq-item"><div class="faq-q">Am I too old for this treatment?</div><div class="faq-a">There is no upper age limit. Dr. Haller has treated patients in their 60s and 70s with meaningful results. The rate of change is slower in older patients — the sutures are less responsive — but they remain responsive. A thorough evaluation including CBCT imaging will give you a realistic picture of what is achievable at your age and with your specific anatomy.</div></div>
    <div class="faq-item"><div class="faq-q">Will I need orthodontics afterward?</div><div class="faq-a">Possibly — it depends on your starting point and treatment goals. Arch expansion creates space, which may shift tooth positions. For some patients, the expansion itself improves dental alignment. For others, orthodontic treatment after expansion achieves the best final result. Dr. Haller coordinates with orthodontists who understand airway-focused treatment and will discuss this at your consultation.</div></div>
    <div class="faq-item"><div class="faq-q">Can I stop using CPAP during treatment?</div><div class="faq-a">Not immediately — and not without a follow-up sleep study. As the airway expands, many patients find their CPAP pressure requirements decrease. Some eventually pass a sleep study without CPAP. The decision to discontinue CPAP is always made based on objective data — a follow-up sleep study — not on how you feel. Dr. Haller coordinates this with your sleep physician.</div></div>
    <div class="faq-item"><div class="faq-q">How is this different from regular orthodontic expansion?</div><div class="faq-a">Traditional orthodontic expansion (RPE — rapid palate expander) uses high forces applied quickly. It is effective for children whose sutures are open, but can cause significant discomfort and is less predictable in adults. Epigenetic appliances use much lighter forces applied over a longer period — working with the body's natural remodeling response rather than forcing it. The result is more comfortable, more stable, and more comprehensive — addressing not just the palate but the entire airway complex.</div></div>
    <div class="faq-item"><div class="faq-q">Does insurance cover this?</div><div class="faq-a">Epigenetic arch expansion is generally not covered by dental or medical insurance. Our practice is fee-for-service. We provide a Letter of Medical Necessity and the relevant codes for submission. We are happy to discuss payment options at consultation.</div></div>
  </div>
</div>
"""

adult_sidebar = """
<div class="sidebar-cta-card">
  <h3>Is permanent expansion right for you?</h3>
  <p>A comprehensive evaluation including CBCT imaging will show exactly what's possible for your anatomy. Schedule a consultation.</p>
  <a href="index.html#contact" class="sidebar-cta-btn">Request a Consultation</a>
  <a href="tel:3054479199" class="sidebar-cta-btn-outline">(305) 447-9199</a>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Related Treatments</div>
  <ul class="sidebar-links">
    <li><a href="sleep-apnea.html">Sleep Apnea Treatment</a></li>
    <li><a href="tongue-tie.html">Tongue Tie Release</a></li>
    <li><a href="nrt.html">Nasal Release Therapy</a></li>
    <li><a href="snoring.html">Laser Snoring Treatment</a></li>
  </ul>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Dr. Haller Trained With</div>
  <div class="sidebar-fact">
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🔬</div><div class="sidebar-fact-text"><strong>Dr. Felix Liao</strong>Holistic Mouth Solutions / AMD</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🦷</div><div class="sidebar-fact-text"><strong>Dr. Theodore Belfor</strong>Homeoblock inventor</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🌱</div><div class="sidebar-fact-text"><strong>Vivos Therapeutics</strong>DNA/mRNA appliance system</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">💡</div><div class="sidebar-fact-text"><strong>AHS Airway Health Solutions</strong>ALF appliance training</div></div>
  </div>
</div>
"""

# ════════════════════════════════════════════════════════════════════════════════
# CHILDREN'S AIRWAY PAGE
# ════════════════════════════════════════════════════════════════════════════════
childrens_hero = """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="page-breadcrumb"><a href="index.html">Home</a><span>/</span><span>Children's Airway</span></div>
    <div class="page-eyebrow">Children's Airway &amp; Orthodontics · Coral Gables, FL</div>
    <h1>Straight Teeth Are<br><em>the Least Important Part</em></h1>
    <p class="page-hero-sub">The goal of children's airway dentistry is not straight teeth — it is a fully developed jaw, a wide open airway, and a child who breathes through their nose, sleeps deeply, and has the neurological foundation to learn, focus, and thrive. Straight teeth are a natural result of proper development. They are not the goal.</p>
    <a href="index.html#contact" class="page-hero-cta">Request a Consultation →</a>
    <div class="page-hero-badges">
      <span class="page-hero-badge">Early intervention — age 2+</span>
      <span class="page-hero-badge">Tongue tie evaluation</span>
      <span class="page-hero-badge">Airway-focused orthodontics</span>
      <span class="page-hero-badge">ADHD &amp; sleep evaluation</span>
    </div>
  </div>
</div>"""

childrens_body = """
<div class="content-section">
  <div class="section-eyebrow">The window of opportunity</div>
  <h2 class="section-title">Why childhood is the <em>critical window</em></h2>
  <p class="section-lead">The jaw and facial bones are most responsive to intervention during childhood — when the sutures are open, growth is active, and the body is primed to respond to guidance. What takes 12–24 months in a child may take 3–5 years in an adult, if it's achievable at all. The earlier the intervention, the more complete the result.</p>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">👶</div><div class="feature-card-title">0–2 years — Foundation</div><div class="feature-card-body">Tongue tie evaluation and release if indicated. Breastfeeding support. Establishing nasal breathing from the start. The most important window — habits and structures established here persist for life.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🧒</div><div class="feature-card-title">2–7 years — Rapid growth</div><div class="feature-card-body">The jaw grows fastest in this window. Tongue tie release, tonsil treatment, nasal airway support, and early arch guidance can redirect development before problems become structural. This is the highest-leverage period for intervention.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🧑</div><div class="feature-card-title">7–12 years — Active development</div><div class="feature-card-body">Mixed dentition phase. Arch expansion, space maintenance, and airway-focused guidance. Orthodontic intervention at this stage can be dramatically more effective — and less invasive — than waiting for full adult dentition.</div></div>
    <div class="feature-card"><div class="feature-card-icon">🧑‍🎓</div><div class="feature-card-title">12–18 years — Adolescent</div><div class="feature-card-body">Active growth continues through the mid-teens. Comprehensive airway-focused orthodontics, jaw development, and sleep evaluation. Still highly responsive — and far more so than adulthood.</div></div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Signs to watch for</div>
  <h2 class="section-title">Is your child showing these signs?</h2>
  <p class="section-lead">Many of the most important signs of airway and development problems in children are routinely missed — or attributed to other causes. If your child shows any of these signs, an airway evaluation is warranted.</p>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">😮</div><div class="feature-card-title">Breathing signs</div><div class="feature-card-body">Mouth breathing — even occasionally · Snoring · Noisy breathing during sleep · Frequent colds and ear infections · Chronic runny nose · Allergies that don't respond to treatment · Enlarged tonsils or adenoids</div></div>
    <div class="feature-card"><div class="feature-card-icon">😴</div><div class="feature-card-title">Sleep signs</div><div class="feature-card-body">Restless sleep · Unusual sleep positions (head back, neck extended) · Bedwetting beyond age 5 · Night terrors · Difficulty waking in the morning · Excessive daytime sleepiness · Dark circles under the eyes</div></div>
    <div class="feature-card"><div class="feature-card-icon">🧠</div><div class="feature-card-title">Behavioral &amp; learning signs</div><div class="feature-card-body">ADHD diagnosis or ADHD-like symptoms · Difficulty concentrating · Hyperactivity · Emotional dysregulation · Poor school performance · Anxiety · Social withdrawal · Behavioral problems that worsen with fatigue</div></div>
    <div class="feature-card"><div class="feature-card-icon">🦷</div><div class="feature-card-title">Dental &amp; structural signs</div><div class="feature-card-body">Crowded or crooked teeth · Narrow dental arch · High, narrow palate · Overbite or underbite · Open bite · Prolonged thumb sucking · Tongue thrusting · Speech difficulties · Forward head posture</div></div>
  </div>
  <div class="info-box"><p><strong>💡 The ADHD connection:</strong> A significant proportion of children diagnosed with ADHD are actually experiencing chronic sleep deprivation due to sleep-disordered breathing. The symptoms are nearly identical: inattention, hyperactivity, impulsivity, emotional dysregulation. The difference is the cause — and the treatment. If your child has an ADHD diagnosis, an airway evaluation is worth pursuing before or alongside behavioral and medication management. Treating the airway has resolved or significantly reduced ADHD symptoms in many children.</p></div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Our approach</div>
  <h2 class="section-title">What airway-focused children's dentistry <em>actually involves</em></h2>
  <p class="section-lead">Dr. Haller's approach to children's airway dentistry is comprehensive — addressing the full chain of causes rather than individual symptoms in isolation.</p>
  <ol class="steps-list">
    <li class="step-item"><div class="step-num">1</div><div class="step-body"><div class="step-title">Tongue tie evaluation and release</div><div class="step-desc">The first and most upstream intervention. If a tongue tie is restricting tongue posture and driving mouth breathing, releasing it is the foundation everything else builds on. Dr. Haller evaluates for both anterior and posterior tongue ties using functional assessment.</div></div></li>
    <li class="step-item"><div class="step-num">2</div><div class="step-body"><div class="step-title">Tonsil evaluation and laser treatment</div><div class="step-desc">Enlarged tonsils are the leading anatomical cause of pediatric sleep-disordered breathing. CO2 laser decontamination can shrink tonsils without surgery — preserving immune tissue and avoiding hospital admission. Dr. Haller photographs and grades tonsils at every visit.</div></div></li>
    <li class="step-item"><div class="step-num">3</div><div class="step-body"><div class="step-title">Nasal airway support</div><div class="step-desc">Establishing nasal breathing is the goal. Tools include NRT (Nasal Release Therapy) for cranial restrictions, nasal rinses, SONU headband (15 min morning + 15 min before bed), and mouth taping at night once nasal breathing is established. Addressing nasal obstruction at the source — not just managing symptoms.</div></div></li>
    <li class="step-item"><div class="step-num">4</div><div class="step-body"><div class="step-title">Arch development and expansion</div><div class="step-desc">Custom oral appliances guide jaw development during the growth window — widening the palate, creating space for the tongue, and expanding the nasal floor. This is most powerful in the 2–12 age window when growth is most active. Dr. Haller uses a range of appliance systems appropriate to the child's age and developmental stage.</div></div></li>
    <li class="step-item"><div class="step-num">5</div><div class="step-body"><div class="step-title">Myofunctional therapy</div><div class="step-desc">Retraining the tongue, lip, and facial muscles to support nasal breathing and correct tongue posture. For children old enough to participate (typically 4+), myofunctional therapy is a critical component of lasting results. Dr. Haller coordinates referrals to certified myofunctional therapists.</div></div></li>
    <li class="step-item"><div class="step-num">6</div><div class="step-body"><div class="step-title">Sleep evaluation and coordination</div><div class="step-desc">For children with significant sleep-disordered breathing, Dr. Haller coordinates with pediatric sleep physicians for formal evaluation. She communicates findings and treatment progress to the full care team — pediatrician, ENT, sleep physician, myofunctional therapist, and orthodontist.</div></div></li>
  </ol>
</div>

<div class="content-section">
  <div class="section-eyebrow">Frequently asked questions</div>
  <h2 class="section-title">What parents ask most</h2>
  <div class="faq-list">
    <div class="faq-item"><div class="faq-q">How young can you start treatment?</div><div class="faq-a">Tongue tie evaluation and release can be done from birth. Tonsil laser treatment is appropriate from age 2 and up. Arch development appliances are typically introduced between ages 4 and 7, depending on the child's development and cooperation. The earlier the better — but it is never too late to start.</div></div>
    <div class="faq-item"><div class="faq-q">My child was diagnosed with ADHD. Could it be a sleep problem?</div><div class="faq-a">Possibly — and it is worth evaluating. The symptoms of sleep-disordered breathing in children are nearly identical to ADHD: inattention, hyperactivity, impulsivity, emotional dysregulation. A sleep evaluation and airway assessment can determine whether a breathing component is contributing. This does not mean ADHD is not also present — but treating the airway component can significantly reduce symptoms and improve response to other treatments.</div></div>
    <div class="faq-item"><div class="faq-q">My pediatrician says my child will grow out of mouth breathing. Is that true?</div><div class="faq-a">Rarely. Mouth breathing is almost always structural — the nasal airway is too narrow, the tonsils are too large, or the tongue is restricted. These structural issues do not resolve on their own. And the longer mouth breathing continues, the more it shapes the jaw and face in ways that make nasal breathing harder. Early intervention is far more effective than waiting.</div></div>
    <div class="faq-item"><div class="faq-q">Will my child need braces after this treatment?</div><div class="faq-a">Many children who receive early airway-focused treatment require less orthodontic intervention later — or none at all. When the jaw develops properly, teeth often erupt in better alignment naturally. For children who do need orthodontics, airway-focused treatment first means the orthodontic result is more stable and the airway is not compromised by tooth extraction or jaw surgery.</div></div>
    <div class="faq-item"><div class="faq-q">What does a first visit look like?</div><div class="faq-a">The first visit is a comprehensive evaluation: Dr. Haller reviews your child's health history, sleep history, and behavioral concerns. She performs a full oral and airway examination including tongue tie functional assessment, tonsil grading, palate evaluation, and jaw development assessment. For children over 5, CBCT imaging may be recommended to evaluate the airway in three dimensions. You leave with a clear picture of what is contributing to your child's symptoms and a prioritized treatment plan.</div></div>
  </div>
</div>
"""

childrens_sidebar = """
<div class="sidebar-cta-card">
  <h3>The earlier, the better</h3>
  <p>The growth window closes. Schedule a comprehensive airway evaluation for your child today.</p>
  <a href="index.html#contact" class="sidebar-cta-btn">Request a Consultation</a>
  <a href="tel:3054479199" class="sidebar-cta-btn-outline">(305) 447-9199</a>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Related Treatments</div>
  <ul class="sidebar-links">
    <li><a href="tongue-tie.html">Tongue Tie Release</a></li>
    <li><a href="tonsils.html">Laser Tonsil Treatment</a></li>
    <li><a href="nrt.html">Nasal Release Therapy</a></li>
    <li><a href="adult-airway.html">Adult Airway Expansion</a></li>
  </ul>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Red Flags in Children</div>
  <div class="sidebar-fact">
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">😮</div><div class="sidebar-fact-text"><strong>Mouth breathing</strong>Even occasionally — not normal</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">😴</div><div class="sidebar-fact-text"><strong>Snoring or restless sleep</strong>Sign of airway obstruction</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🧠</div><div class="sidebar-fact-text"><strong>ADHD symptoms</strong>May be sleep-disordered breathing</div></div>
  </div>
</div>
"""

# ════════════════════════════════════════════════════════════════════════════════
# PHYSICIAN REFERRAL PAGE
# ════════════════════════════════════════════════════════════════════════════════
physician_hero = """
<div class="page-hero">
  <div class="page-hero-inner">
    <div class="page-breadcrumb"><a href="index.html">Home</a><span>/</span><span>Physician Referrals</span></div>
    <div class="page-eyebrow">Physician Referrals · Collaborative Care · Coral Gables, FL</div>
    <h1>Partnering with Physicians<br><em>to Treat the Whole Patient</em></h1>
    <p class="page-hero-sub">Sleep apnea, airway obstruction, and jaw underdevelopment are medical problems with dental solutions. Dr. Haller works closely with sleep physicians, ENTs, pediatricians, cardiologists, and other specialists to provide comprehensive airway care — and communicates findings and progress to the full care team.</p>
    <a href="index.html#contact" class="page-hero-cta">Make a Referral →</a>
    <div class="page-hero-badges">
      <span class="page-hero-badge">Board Certified — ASBA</span>
      <span class="page-hero-badge">Harvard School of Dental Medicine</span>
      <span class="page-hero-badge">Detailed progress reports</span>
      <span class="page-hero-badge">Accepts medical insurance codes for MAD</span>
    </div>
  </div>
</div>"""

physician_body = """
<div class="content-section">
  <div class="section-eyebrow">Why refer to Dr. Haller</div>
  <h2 class="section-title">A dental sleep specialist who <em>speaks your language</em></h2>
  <p class="section-lead">Dr. Haller is a Harvard-trained dentist with board certification in dental sleep medicine from the American Sleep &amp; Breathing Academy. She has trained extensively with the leading innovators in airway-focused dentistry and brings a comprehensive, evidence-informed approach to every patient.</p>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">🎓</div><div class="feature-card-title">Credentials</div><div class="feature-card-body">Harvard School of Dental Medicine, DMD · Board Certified, American Sleep &amp; Breathing Academy · Trained with Dr. Felix Liao (AMD/Holistic Mouth Solutions) · Trained with Dr. Theodore Belfor (Homeoblock) · Vivos Therapeutics certified · AHS Airway Health Solutions trained · Board Certified CO2 Laser Dentist · Diplomate, American Board of Laser Surgery</div></div>
    <div class="feature-card"><div class="feature-card-icon">🤝</div><div class="feature-card-title">Collaborative approach</div><div class="feature-card-body">Dr. Haller provides detailed written reports to referring physicians at intake and at key treatment milestones. She communicates directly with the referring provider when clinical findings are relevant to the patient's medical management — including changes in CPAP pressure requirements, airway volume changes on follow-up CBCT, and treatment response. She welcomes co-management and direct physician communication.</div></div>
    <div class="feature-card"><div class="feature-card-icon">📋</div><div class="feature-card-title">Insurance &amp; documentation</div><div class="feature-card-body">For custom MAD devices, Dr. Haller provides all necessary documentation for medical insurance submission — including Letters of Medical Necessity, ICD-10 diagnosis codes, and CDT procedure codes. She works with patients to facilitate reimbursement and can communicate directly with insurance reviewers when needed. The practice is fee-for-service for all other treatments.</div></div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">Referral indications</div>
  <h2 class="section-title">When to refer to Dr. Haller</h2>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">😴</div><div class="feature-card-title">Sleep Medicine / Pulmonology</div><div class="feature-card-body">CPAP-intolerant patients seeking an alternative · Mild-to-moderate OSA appropriate for oral appliance therapy · Patients requesting a non-surgical permanent solution · UARS patients not responding to CPAP · Patients seeking to reduce CPAP dependence through airway expansion · Post-surgical patients with residual OSA</div></div>
    <div class="feature-card"><div class="feature-card-icon">👂</div><div class="feature-card-title">ENT / Otolaryngology</div><div class="feature-card-body">Patients with enlarged tonsils seeking a non-surgical option before tonsillectomy · Chronic sinusitis with suspected cranial restriction component · Nasal obstruction not fully explained by septal deviation · Pediatric snoring and sleep-disordered breathing · Patients with recurrent tonsillitis despite antibiotic management</div></div>
    <div class="feature-card"><div class="feature-card-icon">👶</div><div class="feature-card-title">Pediatrics</div><div class="feature-card-body">Children with mouth breathing, snoring, or restless sleep · ADHD diagnosis with suspected sleep component · Tongue tie — infant or child · Crowded teeth or narrow arch · Enlarged tonsils or adenoids · Recurrent ear infections · Delayed speech development · Behavioral issues with sleep component</div></div>
    <div class="feature-card"><div class="feature-card-icon">❤️</div><div class="feature-card-title">Cardiology / Internal Medicine</div><div class="feature-card-body">Patients with resistant hypertension and suspected OSA · Atrial fibrillation with sleep apnea component · Heart failure patients with OSA · Patients with multiple cardiovascular risk factors and undiagnosed sleep-disordered breathing · Metabolic syndrome with suspected sleep component</div></div>
    <div class="feature-card"><div class="feature-card-icon">🧠</div><div class="feature-card-title">Neurology / Psychiatry</div><div class="feature-card-body">Patients with treatment-resistant depression or anxiety with suspected sleep component · Cognitive decline with suspected sleep-disordered breathing · ADHD patients with suspected airway component · Chronic headache with suspected cranial restriction component · Tinnitus with suspected cranial restriction component</div></div>
    <div class="feature-card"><div class="feature-card-icon">🤰</div><div class="feature-card-title">OB/GYN</div><div class="feature-card-body">Pregnant patients with new or worsening snoring · Gestational hypertension with suspected sleep apnea · Postpartum fatigue disproportionate to sleep deprivation · Women with PCOS and suspected sleep-disordered breathing</div></div>
  </div>
</div>

<div class="content-section">
  <div class="section-eyebrow">What we offer your patients</div>
  <h2 class="section-title">Our full range of <em>airway treatments</em></h2>
  <table class="compare-table">
    <thead><tr><th>Treatment</th><th>Indication</th><th>Key Details</th></tr></thead>
    <tbody>
      <tr><td>Custom MAD Device</td><td>Diagnosed OSA, CPAP intolerance</td><td>Medical insurance billable; sleep study required; board certified provider</td></tr>
      <tr><td>Epigenetic Arch Expansion</td><td>Structural airway narrowing, CPAP reduction goal</td><td>12–24 months; permanent; multiple appliance systems; CBCT monitoring</td></tr>
      <tr><td>CO2 Laser Tonsil Decontamination</td><td>Enlarged tonsils, recurrent tonsillitis, pediatric SDB</td><td>Non-surgical; 3–6 sessions; no anesthesia; children and adults</td></tr>
      <tr><td>CO2 Laser Frenectomy</td><td>Tongue tie — infant, child, adult</td><td>Laser precision; minimal bleeding; myofunctional therapy coordination</td></tr>
      <tr><td>Nasal Release Therapy</td><td>Nasal obstruction, cranial restriction, chronic sinusitis</td><td>Non-surgical; 6–8 sessions; immediate nasal opening common</td></tr>
      <tr><td>Laser Snoring Treatment</td><td>Primary snoring, soft palate laxity</td><td>2 sessions; no anesthesia; results in 1–5 days; annual maintenance</td></tr>
    </tbody>
  </table>
</div>

<div class="content-section">
  <div class="section-eyebrow">Make a referral</div>
  <h2 class="section-title">How to refer a patient</h2>
  <p class="section-lead">Referrals can be made by phone, email, or fax. Dr. Haller's team will contact the patient within one business day to schedule a consultation. A detailed intake report is provided to the referring physician following the initial evaluation.</p>
  <div class="feature-grid">
    <div class="feature-card"><div class="feature-card-icon">📞</div><div class="feature-card-title">Phone</div><div class="feature-card-body">(305) 447-9199<br>Monday–Friday, 9am–5pm EST<br>Ask for the referral coordinator</div></div>
    <div class="feature-card"><div class="feature-card-icon">📧</div><div class="feature-card-title">Email</div><div class="feature-card-body">dentistry@lesliehallerdmd.com<br>Include patient name, DOB, and referral indication<br>Secure messaging available on request</div></div>
    <div class="feature-card"><div class="feature-card-icon">📍</div><div class="feature-card-title">Location</div><div class="feature-card-body">348 Alhambra Circle<br>Coral Gables, FL 33134<br>Serving all of South Florida</div></div>
  </div>
  <div class="quote-block">
    <div class="quote-text">"I trained at Harvard because I wanted to understand medicine, not just dentistry. The mouth is not separate from the body — it is the gateway to the airway, and the airway is the gateway to everything. I am grateful for every physician who understands this and sends their patients to us."</div>
    <div class="quote-attr">— Dr. Leslie Haller, DMD</div>
  </div>
</div>
"""

physician_sidebar = """
<div class="sidebar-cta-card">
  <h3>Make a Referral</h3>
  <p>Call, email, or use the contact form. We respond within one business day and provide a detailed intake report after evaluation.</p>
  <a href="index.html#contact" class="sidebar-cta-btn">Contact Us</a>
  <a href="tel:3054479199" class="sidebar-cta-btn-outline">(305) 447-9199</a>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Dr. Haller's Credentials</div>
  <div class="sidebar-fact">
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🎓</div><div class="sidebar-fact-text"><strong>Harvard School of Dental Medicine</strong>DMD</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🏅</div><div class="sidebar-fact-text"><strong>Board Certified</strong>American Sleep &amp; Breathing Academy</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">⚡</div><div class="sidebar-fact-text"><strong>Board Certified</strong>CO2 Laser Dentist</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">🔬</div><div class="sidebar-fact-text"><strong>Diplomate</strong>American Board of Laser Surgery</div></div>
  </div>
</div>
<div class="sidebar-card">
  <div class="sidebar-card-title">Insurance &amp; Billing</div>
  <div class="sidebar-fact">
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">💳</div><div class="sidebar-fact-text"><strong>MAD devices</strong>Medical insurance billable; all documentation provided</div></div>
    <div class="sidebar-fact-item"><div class="sidebar-fact-icon">📄</div><div class="sidebar-fact-text"><strong>All treatments</strong>Letter of Medical Necessity provided on request</div></div>
  </div>
</div>
"""

# ════════════════════════════════════════════════════════════════════════════════
# BUILD ALL PAGES
# ════════════════════════════════════════════════════════════════════════════════
pages_to_build = [
    ('sleep-apnea.html', 'Sleep Apnea Treatment Without a CPAP Machine', 'sleep-apnea', sleep_hero, sleep_body, sleep_sidebar),
    ('tonsils.html', 'CO2 Laser Tonsil Treatment', 'tonsils', tonsils_hero, tonsils_body, tonsils_sidebar),
    ('nrt.html', 'Nasal Release Therapy', 'nrt', nrt_hero, nrt_body, nrt_sidebar),
    ('snoring.html', 'Laser Snoring Treatment', 'snoring', snoring_hero, snoring_body, snoring_sidebar),
    ('tongue-tie.html', 'Tongue Tie Frenectomy', 'tongue-tie', tonguetie_hero, tonguetie_body, tonguetie_sidebar),
    ('adult-airway.html', 'Adult Airway Expansion', 'adult-airway', adult_hero, adult_body, adult_sidebar),
    ('childrens-airway.html', "Children's Airway & Orthodontics", 'childrens-airway', childrens_hero, childrens_body, childrens_sidebar),
    ('physician-referral.html', 'Physician Referrals', 'physician-referral', physician_hero, physician_body, physician_sidebar),
]

out_dir = '/home/ubuntu/dental-modern'
for filename, title, active, hero, body, sidebar in pages_to_build:
    html = page(title, active, hero, body, sidebar)
    with open(f'{out_dir}/{filename}', 'w') as f:
        f.write(html)
    print(f'Built: {filename}')

print('All pages built successfully.')
