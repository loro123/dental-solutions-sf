import base64

# Read logo (original for nav)
with open('/home/ubuntu/dental-modern/logo.png', 'rb') as f:
    logo_uri = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

# Read transparent logo for footer (white-on-dark)
with open('/home/ubuntu/dental-modern/logo_transparent.png', 'rb') as f:
    logo_transparent_uri = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

# Read flowchart SVG
with open('/tmp/flowchart_orig.svg', 'r') as f:
    flowchart_svg = f.read().strip()

html_parts = []

html_parts.append('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dental Solutions of South Florida — Airway Dentistry</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:"Inter",system-ui,sans-serif;background:#f4f5f7;color:#1e2d42;-webkit-font-smoothing:antialiased;}
:root{
  --brand-blue:#6389c7;
  --brand-blue-dk:#4a6faa;
  --brand-blue-lt:#eef3fb;
  --brand-gold:#c9a84c;
  --brand-gold-lt:#fdf6e3;
  --brand-navy:#1e2d42;
  --brand-navy-mid:#2d4460;
  --brand-green:#2d6a54;
  --brand-green-lt:#e8f5ee;
  --surface:#f8f9fb;
  --border:#e2e8f0;
  --text-dark:#1e2d42;
  --text-mid:#4a5f7a;
  --text-muted:#8a9ab5;
  --white:#ffffff;
}
.site-wrapper{background:#fff;max-width:1920px;margin:0 auto;}
.container{max-width:1800px;margin:0 auto;padding:0 64px;}

/* TOPBAR */
.topbar{background:var(--brand-navy);padding:9px 0;}
.topbar-inner{max-width:1800px;margin:0 auto;padding:0 64px;display:flex;justify-content:space-between;align-items:center;gap:16px;}
.topbar-left{font-size:12px;color:rgba(255,255,255,0.55);letter-spacing:.02em;}
.topbar-sep{color:rgba(255,255,255,0.2);margin:0 8px;}
.topbar-right{display:flex;align-items:center;gap:20px;font-size:12px;color:rgba(255,255,255,0.5);}
.topbar-cta{background:var(--brand-gold);color:var(--brand-navy);font-size:11px;font-weight:700;letter-spacing:.08em;padding:6px 18px;border-radius:100px;border:none;cursor:pointer;text-transform:uppercase;transition:background .2s;}
.topbar-cta:hover{background:#dbb95a;}

/* NAV */
.nav{background:#fff;border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100;box-shadow:0 2px 16px rgba(30,45,66,.07);}
.nav-inner{max-width:1800px;margin:0 auto;padding:0 64px;display:flex;align-items:center;justify-content:space-between;height:72px;gap:24px;}
.nav-logo{height:46px;width:auto;display:block;flex-shrink:0;}
.nav-links{display:flex;align-items:center;gap:2px;}
.nav-links a{font-size:13px;font-weight:500;color:var(--text-mid);text-decoration:none;padding:7px 13px;border-radius:8px;transition:all .15s;white-space:nowrap;}
.nav-links a:hover{background:var(--brand-blue-lt);color:var(--brand-navy);}
.nav-links a.active{color:var(--brand-blue);font-weight:700;background:var(--brand-blue-lt);}
.nav-btn{background:var(--brand-blue);color:#fff;font-size:13px;font-weight:700;padding:11px 26px;border-radius:100px;border:none;cursor:pointer;transition:all .2s;white-space:nowrap;}
.nav-btn:hover{background:var(--brand-blue-dk);box-shadow:0 6px 20px rgba(99,137,199,.35);}

/* HERO */
.hero{background:linear-gradient(155deg,#eef3fb 0%,#f8f9fb 45%,#f5f0e8 100%);padding:80px 0 72px;position:relative;overflow:hidden;}
.hero::before{content:"";position:absolute;top:-160px;right:-120px;width:700px;height:700px;background:radial-gradient(circle,rgba(99,137,199,.08) 0%,transparent 65%);pointer-events:none;}
.hero::after{content:"";position:absolute;bottom:-100px;left:15%;width:500px;height:500px;background:radial-gradient(circle,rgba(201,168,76,.06) 0%,transparent 65%);pointer-events:none;}
.hero-inner{max-width:1800px;margin:0 auto;padding:0 64px;display:grid;grid-template-columns:1fr 420px;gap:72px;align-items:center;position:relative;z-index:1;}
.hero-badge{display:inline-flex;align-items:center;gap:8px;background:var(--brand-green-lt);color:var(--brand-green);font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;padding:6px 16px;border-radius:100px;border:1px solid rgba(45,106,84,.2);margin-bottom:22px;}
.hero-badge::before{content:"";width:6px;height:6px;background:var(--brand-green);border-radius:50%;}
.hero-h1{font-family:"Playfair Display",Georgia,serif;font-size:clamp(40px,3.6vw,62px);font-weight:700;line-height:1.07;color:var(--brand-navy);margin-bottom:22px;letter-spacing:-.02em;}
.hero-h1 em{color:var(--brand-blue);font-style:normal;}
.hero-h1 strong{color:var(--brand-green);}
.hero-sub{font-size:17px;color:var(--text-mid);line-height:1.78;margin-bottom:34px;max-width:580px;}
.hero-actions{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:40px;}
.btn-primary{background:var(--brand-navy);color:#fff;font-size:14px;font-weight:700;padding:14px 30px;border-radius:100px;border:none;cursor:pointer;transition:all .2s;display:inline-flex;align-items:center;gap:8px;}
.btn-primary:hover{background:var(--brand-navy-mid);transform:translateY(-1px);box-shadow:0 8px 24px rgba(30,45,66,.22);}
.btn-gold{background:var(--brand-gold);color:var(--brand-navy);font-size:14px;font-weight:700;padding:14px 30px;border-radius:100px;border:none;cursor:pointer;transition:all .2s;}
.btn-gold:hover{background:#dbb95a;transform:translateY(-1px);box-shadow:0 8px 24px rgba(201,168,76,.3);}
.btn-outline{background:transparent;color:var(--brand-navy);font-size:14px;font-weight:600;padding:14px 30px;border-radius:100px;border:1.5px solid var(--border);cursor:pointer;transition:all .2s;}
.btn-outline:hover{border-color:var(--brand-blue);color:var(--brand-blue);}
.hero-trust{display:flex;gap:24px;flex-wrap:wrap;}
.trust-item{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--text-mid);font-weight:500;}
.trust-check{width:20px;height:20px;background:var(--brand-green-lt);border-radius:50%;display:flex;align-items:center;justify-content:center;color:var(--brand-green);font-size:10px;font-weight:900;flex-shrink:0;}
.hero-cards{display:flex;flex-direction:column;gap:12px;}
.hero-card{background:#fff;border-radius:18px;padding:18px 20px;border:1px solid var(--border);box-shadow:0 2px 14px rgba(30,45,66,.05);transition:all .22s;}
.hero-card:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(30,45,66,.09);}
.hero-card-row{display:flex;align-items:center;gap:12px;margin-bottom:6px;}
.hc-icon{width:38px;height:38px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0;}
.hc-title{font-size:13px;font-weight:700;color:var(--brand-navy);}
.hc-sub{font-size:12px;color:var(--text-muted);margin-top:1px;}
.hc-pill{display:inline-block;font-size:11px;font-weight:600;padding:3px 11px;border-radius:100px;margin-top:8px;}

/* STATS STRIP */
.stats-strip{background:var(--brand-navy);padding:30px 0;}
.stats-inner{max-width:1800px;margin:0 auto;padding:0 64px;display:grid;grid-template-columns:repeat(5,1fr);}
.stat-item{text-align:center;padding:0 24px;border-right:1px solid rgba(255,255,255,.07);}
.stat-item:last-child{border-right:none;}
.stat-num{font-size:14px;font-weight:800;color:#fff;letter-spacing:.01em;line-height:1.2;margin-bottom:4px;}
.stat-num span{color:var(--brand-gold);}
.stat-label{font-size:11px;color:rgba(255,255,255,.45);font-weight:500;line-height:1.4;}

/* SECTION HEADERS */
.eyebrow{font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--brand-gold);}
.section-title{font-family:"Playfair Display",Georgia,serif;font-size:clamp(26px,2.6vw,38px);font-weight:700;color:var(--brand-navy);line-height:1.15;margin-bottom:12px;}
.section-sub{font-size:16px;color:var(--text-mid);line-height:1.75;}
.section-header{margin-bottom:48px;}
.section-header.centered{text-align:center;}
.section-header.centered .section-sub{max-width:600px;margin:0 auto;}

/* SERVICES */
.services-section{background:var(--surface);padding:88px 0;}
.services-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;}
.svc-card{background:#fff;border-radius:20px;padding:28px 24px;border:1px solid var(--border);position:relative;overflow:hidden;transition:all .25s;}
.svc-card:hover{transform:translateY(-4px);box-shadow:0 18px 44px rgba(30,45,66,.09);border-color:transparent;}
.svc-accent{position:absolute;top:0;left:0;right:0;height:3px;border-radius:20px 20px 0 0;}
.svc-icon{width:50px;height:50px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:22px;margin-bottom:16px;}
.svc-name{font-size:15px;font-weight:700;color:var(--brand-navy);margin-bottom:8px;line-height:1.3;}
.svc-desc{font-size:13px;color:var(--text-mid);line-height:1.65;}
.svc-link{display:inline-flex;align-items:center;gap:4px;font-size:13px;font-weight:600;color:var(--brand-blue);margin-top:14px;text-decoration:none;transition:gap .2s;}
.svc-card:hover .svc-link{gap:8px;}

/* CONNECTED / FLOWCHART */
.connected-section{background:var(--brand-navy);padding:96px 0;position:relative;overflow:hidden;}
.connected-section::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 15% 50%,rgba(99,137,199,.22) 0%,transparent 55%),radial-gradient(ellipse at 85% 20%,rgba(201,168,76,.1) 0%,transparent 50%);pointer-events:none;}
.connected-inner{max-width:1800px;margin:0 auto;padding:0 64px;position:relative;z-index:1;}
.connected-header{text-align:center;margin-bottom:52px;}
.connected-header .eyebrow{color:var(--brand-gold);margin-bottom:14px;}
.connected-title{font-family:"Playfair Display",Georgia,serif;font-size:clamp(30px,3vw,46px);font-weight:700;color:#fff;margin-bottom:16px;line-height:1.1;}
.connected-title em{color:var(--brand-gold);font-style:normal;}
.connected-sub{font-size:16px;color:rgba(255,255,255,.55);max-width:620px;margin:0 auto;line-height:1.78;}
.flowchart-wrap{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:20px;padding:36px 40px;margin-bottom:40px;overflow-x:auto;}
.flowchart-wrap svg{display:block;margin:0 auto;max-width:100%;height:auto;}
.chain-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;}
.chain-card{border-radius:16px;padding:22px;border:1px solid;transition:transform .2s;}
.chain-card:hover{transform:translateY(-2px);}
.chain-card-title{font-size:13px;font-weight:700;color:#fff;margin-bottom:8px;line-height:1.4;}
.chain-card-text{font-size:13px;color:rgba(255,255,255,.58);line-height:1.65;}

/* BREAK THE CHAIN */
.break-section{background:#f0f6f2;padding:88px 0;}
.break-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:48px;}
.break-card{background:#fff;border-radius:20px;padding:28px 24px;border:1px solid rgba(181,221,208,.5);position:relative;overflow:hidden;transition:all .25s;}
.break-card:hover{transform:translateY(-4px);box-shadow:0 16px 40px rgba(30,45,66,.07);}
.break-accent{position:absolute;top:0;left:0;right:0;height:3px;border-radius:20px 20px 0 0;}
.break-step{display:inline-flex;align-items:center;gap:6px;background:var(--brand-green-lt);color:var(--brand-green);font-size:11px;font-weight:700;letter-spacing:.06em;padding:4px 12px;border-radius:100px;margin-bottom:14px;}
.break-title{font-size:16px;font-weight:700;color:var(--brand-navy);margin-bottom:8px;line-height:1.3;}
.break-text{font-size:13px;color:var(--text-mid);line-height:1.65;margin-bottom:14px;}
.break-tool{font-size:12px;color:var(--text-mid);padding-left:14px;position:relative;line-height:1.55;margin-bottom:4px;}
.break-tool::before{content:"\\2192";position:absolute;left:0;color:var(--brand-green);font-size:11px;}

/* DR SECTION */
.dr-section{background:#fff;padding:88px 0;}
.dr-inner{max-width:1800px;margin:0 auto;padding:0 64px;display:grid;grid-template-columns:280px 1fr;gap:64px;align-items:start;}
.dr-photo{width:220px;height:270px;background:linear-gradient(145deg,#e2efe8,#dce8f5);border-radius:20px;display:flex;flex-direction:column;align-items:center;justify-content:center;border:2px solid var(--border);margin-bottom:24px;position:relative;overflow:hidden;}
.dr-initials{font-family:"Playfair Display",Georgia,serif;font-size:64px;font-weight:700;color:var(--brand-blue);opacity:.7;}
.dr-photo-note{font-size:10px;color:var(--text-muted);text-align:center;margin-top:8px;}
.dr-cred-block{background:var(--surface);border-radius:16px;padding:20px;border:1px solid var(--border);}
.dr-cred-label{font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--brand-gold);margin-bottom:12px;}
.dr-cred-list{font-size:12px;color:var(--text-mid);line-height:2.1;}
.dr-name{font-family:"Playfair Display",Georgia,serif;font-size:40px;font-weight:700;color:var(--brand-navy);margin-bottom:6px;line-height:1.1;}
.dr-title-line{font-size:14px;font-weight:600;color:var(--brand-blue);margin-bottom:28px;letter-spacing:.02em;}
.dr-quote{background:var(--brand-blue-lt);border-left:4px solid var(--brand-blue);padding:20px 24px;border-radius:0 16px 16px 0;font-size:16px;color:var(--brand-navy-mid);font-style:italic;line-height:1.78;margin-bottom:28px;font-family:"Playfair Display",Georgia,serif;}
.dr-bio{font-size:15px;color:var(--text-mid);line-height:1.82;margin-bottom:28px;}
.dr-badges{display:flex;gap:8px;flex-wrap:wrap;}
.dr-badge{background:var(--brand-blue-lt);border:1px solid rgba(99,137,199,.25);color:var(--brand-blue);font-size:12px;font-weight:600;padding:5px 14px;border-radius:100px;}

/* CTA BANNER */
.gold-rule{height:2px;background:linear-gradient(to right,transparent,var(--brand-gold),transparent);}
.cta-banner{background:linear-gradient(135deg,#0d2a1a 0%,var(--brand-navy) 50%,#1a3a5f 100%);padding:72px 0;position:relative;overflow:hidden;}
.cta-banner::before{content:"";position:absolute;top:-100px;right:-100px;width:500px;height:500px;background:radial-gradient(circle,rgba(201,168,76,.12) 0%,transparent 60%);pointer-events:none;}
.cta-inner{max-width:1800px;margin:0 auto;padding:0 64px;display:flex;align-items:center;justify-content:space-between;gap:48px;}
.cta-eyebrow{color:var(--brand-gold);margin-bottom:12px;}
.cta-headline{font-family:"Playfair Display",Georgia,serif;font-size:clamp(26px,2.5vw,40px);font-weight:700;color:#fff;line-height:1.15;margin-bottom:14px;}
.cta-headline span{color:var(--brand-gold);}
.cta-sub{font-size:15px;color:rgba(255,255,255,.58);max-width:520px;line-height:1.78;}
.cta-actions{display:flex;gap:12px;flex-shrink:0;}

/* TESTIMONIALS */
.test-section{background:var(--surface);padding:88px 0;}
.test-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:48px;}
.test-card{background:#fff;border-radius:20px;padding:28px;border:1px solid var(--border);transition:all .2s;position:relative;}
.test-card:hover{transform:translateY(-3px);box-shadow:0 12px 32px rgba(30,45,66,.07);}
.test-card::before{content:'"';position:absolute;top:14px;right:22px;font-family:"Playfair Display",Georgia,serif;font-size:80px;color:var(--brand-gold);opacity:.13;line-height:1;}
.test-stars{color:var(--brand-gold);font-size:14px;letter-spacing:3px;margin-bottom:14px;}
.test-quote{font-size:14px;color:var(--text-mid);line-height:1.78;font-style:italic;margin-bottom:20px;}
.test-row{display:flex;align-items:center;gap:12px;padding-top:16px;border-top:1px solid var(--border);}
.test-avatar{width:36px;height:36px;border-radius:50%;background:var(--brand-blue-lt);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:var(--brand-blue);flex-shrink:0;}
.test-author{font-size:13px;font-weight:700;color:var(--brand-navy);}
.test-type{font-size:12px;color:var(--text-muted);margin-top:1px;}

/* BOOKS */
.books-section{background:#fff;padding:88px 0;}
.books-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:48px;}
.book-card{display:flex;gap:20px;background:var(--surface);border-radius:20px;padding:24px;border:1px solid var(--border);transition:all .2s;}
.book-card:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(30,45,66,.06);}
.book-cover{width:56px;height:72px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:26px;flex-shrink:0;box-shadow:2px 4px 12px rgba(30,45,66,.12);}
.book-title{font-size:14px;font-weight:700;color:var(--brand-navy);margin-bottom:4px;line-height:1.35;}
.book-author{font-size:12px;color:var(--brand-blue);font-weight:600;margin-bottom:8px;}
.book-desc{font-size:13px;color:var(--text-mid);line-height:1.62;}

/* CONTACT */
.contact-section{background:linear-gradient(160deg,#f0f6f2 0%,#eef3fb 100%);padding:88px 0;}
.contact-inner{max-width:1800px;margin:0 auto;padding:0 64px;display:grid;grid-template-columns:1fr 1fr;gap:64px;}
.contact-title{font-family:"Playfair Display",Georgia,serif;font-size:28px;font-weight:700;color:var(--brand-navy);margin-bottom:28px;}
.form-field{margin-bottom:16px;}
.form-label{display:block;font-size:11px;font-weight:700;color:var(--text-mid);margin-bottom:6px;letter-spacing:.06em;text-transform:uppercase;}
.form-input{width:100%;padding:13px 16px;border:1.5px solid var(--border);border-radius:12px;font-size:14px;color:var(--brand-navy);background:#fff;font-family:"Inter",sans-serif;transition:border-color .2s,box-shadow .2s;outline:none;}
.form-input:focus{border-color:var(--brand-blue);box-shadow:0 0 0 3px rgba(99,137,199,.12);}
.form-submit{width:100%;background:var(--brand-blue);color:#fff;padding:15px;border-radius:100px;border:none;font-size:14px;font-weight:700;cursor:pointer;margin-top:8px;font-family:"Inter",sans-serif;letter-spacing:.02em;transition:all .2s;}
.form-submit:hover{background:var(--brand-blue-dk);transform:translateY(-1px);box-shadow:0 8px 24px rgba(99,137,199,.3);}
.form-note{margin-top:14px;font-size:12px;color:var(--text-muted);font-style:italic;line-height:1.65;}
.contact-detail{display:flex;gap:14px;margin-bottom:20px;align-items:flex-start;}
.contact-icon{width:42px;height:42px;background:#fff;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:16px;border:1px solid var(--border);flex-shrink:0;box-shadow:0 2px 8px rgba(30,45,66,.04);}
.contact-dt{font-size:14px;font-weight:700;color:var(--brand-navy);}
.contact-ds{font-size:12px;color:var(--text-muted);margin-top:2px;}
.map-ph{background:#fff;border-radius:16px;height:130px;display:flex;align-items:center;justify-content:center;border:1.5px dashed var(--border);margin-top:20px;font-size:13px;color:var(--text-muted);font-style:italic;}

/* FOOTER */
.footer{background:var(--brand-navy);padding:64px 0 0;}
.footer-inner{max-width:1800px;margin:0 auto;padding:0 64px 48px;display:grid;grid-template-columns:1.8fr 1fr 1fr 1fr;gap:48px;}
.footer-logo{height:52px;width:auto;margin-bottom:14px;filter:brightness(0) invert(1);}
.footer-tagline{color:var(--brand-gold);font-size:12px;font-style:italic;margin-bottom:16px;}
.footer-contact{color:rgba(255,255,255,.42);font-size:13px;line-height:2.1;}
.footer-col-title{color:#fff;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;margin-bottom:16px;}
.footer-link{color:rgba(255,255,255,.42);font-size:13px;display:block;margin-bottom:8px;text-decoration:none;transition:color .15s;}
.footer-link:hover{color:#fff;}
.footer-bottom{background:rgba(0,0,0,.22);border-top:1px solid rgba(255,255,255,.06);}
.footer-bottom-inner{max-width:1800px;margin:0 auto;padding:16px 64px;display:flex;justify-content:space-between;font-size:12px;color:rgba(255,255,255,.28);}

/* RESPONSIVE */
@media(max-width:1400px){
  .container,.hero-inner,.stats-inner,.connected-inner,.dr-inner,.cta-inner,.contact-inner,.footer-inner,.footer-bottom-inner,.topbar-inner,.nav-inner{padding-left:40px;padding-right:40px;}
}
@media(max-width:1100px){
  .services-grid{grid-template-columns:repeat(2,1fr);}
  .hero-inner{grid-template-columns:1fr;}
  .stats-inner{grid-template-columns:repeat(3,1fr);}
  .chain-cards{grid-template-columns:repeat(2,1fr);}
  .break-grid{grid-template-columns:repeat(2,1fr);}
  .dr-inner{grid-template-columns:1fr;}
  .footer-inner{grid-template-columns:1fr 1fr;}
}
@media(max-width:768px){
  .container,.hero-inner,.stats-inner,.connected-inner,.dr-inner,.cta-inner,.contact-inner,.footer-inner,.footer-bottom-inner,.topbar-inner,.nav-inner{padding-left:20px;padding-right:20px;}
  .services-grid,.test-grid,.books-grid,.chain-cards,.break-grid{grid-template-columns:1fr;}
  .cta-inner{flex-direction:column;}
  .contact-inner{grid-template-columns:1fr;}
  .stats-inner{grid-template-columns:repeat(2,1fr);}
  .footer-inner{grid-template-columns:1fr;}
  .topbar-right,.nav-links{display:none;}
  .hero-h1{font-size:34px;}
}
</style>
</head>
<body>
<div class="site-wrapper">
''')

html_parts.append(f'''
<!-- TOPBAR -->
<div class="topbar">
  <div class="topbar-inner">
    <div class="topbar-left">
      Coral Gables Airway Dentistry<span class="topbar-sep">&middot;</span>348 Alhambra Circle<span class="topbar-sep">&middot;</span>(305) 447-9199
    </div>
    <div class="topbar-right">
      <span>dentistry@lesliehallerdmd.com</span>
      <span style="color:rgba(255,255,255,.15)">|</span>
      <span>Physician Referrals</span>
      <button class="topbar-cta">Book Appointment</button>
    </div>
  </div>
</div>

<!-- NAV -->
<nav class="nav">
  <div class="nav-inner">
    <img src="{logo_uri}" alt="Dental Solutions of South Florida" class="nav-logo">
    <div class="nav-links">
      <a href="#" class="active">Home</a>
      <a href="#">Sleep &amp; Airway</a>
      <a href="#">Treatments</a>
      <a href="#">Children</a>
      <a href="#">About</a>
      <a href="#">Blog</a>
      <a href="#">Contact</a>
    </div>
    <button class="nav-btn">Book Appointment</button>
  </div>
</nav>
''')

html_parts.append('''
<!-- HERO -->
<section class="hero">
  <div class="hero-inner">
    <div>
      <div class="hero-badge">Harvard-Trained &middot; Board Certified &middot; Coral Gables, FL</div>
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
        <button class="btn-outline">Explore Treatments</button>
      </div>
      <div class="hero-trust">
        <div class="trust-item"><div class="trust-check">&#10003;</div>Board Certified Laser Dentist (ALD)</div>
        <div class="trust-item"><div class="trust-check">&#10003;</div>Board Certified in Dental Sleep Medicine (ASBA)</div>
        <div class="trust-item"><div class="trust-check">&#10003;</div>Published Researcher</div>
      </div>
    </div>
    <div class="hero-cards">
      <div class="hero-card">
        <div class="hero-card-row">
          <div class="hc-icon" style="background:#e8f5ee;">&#127769;</div>
          <div><div class="hc-title">Sleep Solutions</div><div class="hc-sub">Custom oral appliances &middot; Epigenetic arch remodeling</div></div>
        </div>
        <div class="hc-pill" style="background:#e8f5ee;color:#2d6a54;">CPAP alternative</div>
      </div>
      <div class="hero-card">
        <div class="hero-card-row">
          <div class="hc-icon" style="background:#eef3fb;">&#10024;</div>
          <div><div class="hc-title">Tongue Ties, Tonsils &amp; NRT</div><div class="hc-sub">CO2 laser &middot; Painless, fast recovery</div></div>
        </div>
        <div class="hc-pill" style="background:#eef3fb;color:#4a6faa;">15-min procedure</div>
      </div>
      <div class="hero-card">
        <div class="hero-card-row">
          <div class="hc-icon" style="background:#fdf6e3;">&#129306;</div>
          <div><div class="hc-title">Children&#39;s Airway Care</div><div class="hc-sub">Guided growth &amp; expansion &middot; Healthy Start &middot; Myo Munchee</div></div>
        </div>
        <div class="hc-pill" style="background:#fdf6e3;color:#7a5a1a;">Early intervention</div>
      </div>
    </div>
  </div>
</section>

<!-- STATS STRIP -->
<div class="stats-strip">
  <div class="stats-inner">
    <div class="stat-item">
      <div class="stat-num">Harvard <span>School</span></div>
      <div class="stat-label">of Dental Medicine</div>
    </div>
    <div class="stat-item">
      <div class="stat-num"><span>Board</span> Certified</div>
      <div class="stat-label">Laser Dentist (ALD)</div>
    </div>
    <div class="stat-item">
      <div class="stat-num"><span>Board</span> Certified</div>
      <div class="stat-label">Dental Sleep Medicine (ASBA)</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">Published <span>Researcher</span></div>
      <div class="stat-label">Journal of Rare Disorders, 2016</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">ALD &middot; ICAP &middot; <span>ASBA</span></div>
      <div class="stat-label">AADSM &middot; AAGO &middot; AHS memberships</div>
    </div>
  </div>
</div>

<!-- SERVICES -->
<section class="services-section">
  <div class="container">
    <div class="section-header">
      <div class="eyebrow" style="margin-bottom:10px;">What we treat</div>
      <div class="section-title">Airway-focused services for adults &amp; children</div>
    </div>
    <div class="services-grid">
      <div class="svc-card">
        <div class="svc-accent" style="background:linear-gradient(to right,#1a6b4a,#4a9a7a);"></div>
        <div class="svc-icon" style="background:#e8f5ee;">&#127769;</div>
        <div class="svc-name">Sleep Apnea &amp; Oral Appliances</div>
        <div class="svc-desc">Custom mandibular advancement devices (MAD) for diagnosed sleep apnea. A comfortable, effective CPAP alternative covered by medical insurance.</div>
        <a class="svc-link" href="#">Learn more &rarr;</a>
      </div>
      <div class="svc-card">
        <div class="svc-accent" style="background:linear-gradient(to right,#6389c7,#8aaad8);"></div>
        <div class="svc-icon" style="background:#eef3fb;">&#128142;</div>
        <div class="svc-name">CO2 Laser Tonsil Treatment</div>
        <div class="svc-desc">Laser decontamination shrinks enlarged tonsils without surgery. No hospital, no general anesthesia, no recovery time. Results in 4&ndash;6 sessions.</div>
        <a class="svc-link" href="#">Learn more &rarr;</a>
      </div>
      <div class="svc-card">
        <div class="svc-accent" style="background:linear-gradient(to right,#c9a84c,#e0bc5a);"></div>
        <div class="svc-icon" style="background:#fdf6e3;">&#128133;</div>
        <div class="svc-name">Tongue Tie Release (Frenectomy)</div>
        <div class="svc-desc">CO2 laser frenectomy for infants, children, and adults. Minimal discomfort, rapid healing, and paired with myofunctional therapy for lasting results.</div>
        <a class="svc-link" href="#">Learn more &rarr;</a>
      </div>
      <div class="svc-card">
        <div class="svc-accent" style="background:linear-gradient(to right,#6a3ab5,#9a6ad5);"></div>
        <div class="svc-icon" style="background:#f5f0fb;">&#129306;</div>
        <div class="svc-name">Airway Expansion (Epigenetic)</div>
        <div class="svc-desc">Epigenetic appliances create permanent structural change &mdash; widening dental arches and nasal passages. Vivos, Homeoblock, Start Thriving Appliance&reg;.</div>
        <a class="svc-link" href="#">Learn more &rarr;</a>
      </div>
      <div class="svc-card">
        <div class="svc-accent" style="background:linear-gradient(to right,#1a6a7a,#2a9aaa);"></div>
        <div class="svc-icon" style="background:#e8fafd;">&#128067;</div>
        <div class="svc-name">Nasal Release Therapy (NRT)</div>
        <div class="svc-desc">Opens the nasal airway to enable nasal breathing. Combined with SONU headband, mouth tape, and nasal sprays for a complete breathing protocol.</div>
        <a class="svc-link" href="#">Learn more &rarr;</a>
      </div>
      <div class="svc-card">
        <div class="svc-accent" style="background:linear-gradient(to right,#c97a4a,#e09a6a);"></div>
        <div class="svc-icon" style="background:#fdf0e8;">&#128548;</div>
        <div class="svc-name">Snoring Laser Treatment</div>
        <div class="svc-desc">Fractional ablative laser therapy tightens soft palate tissue to reduce snoring. Non-surgical, no downtime, effective in 3 sessions.</div>
        <a class="svc-link" href="#">Learn more &rarr;</a>
      </div>
      <div class="svc-card">
        <div class="svc-accent" style="background:linear-gradient(to right,#2d6a54,#4a9a7a);"></div>
        <div class="svc-icon" style="background:#e8f5ee;">&#129306;</div>
        <div class="svc-name">Children&#39;s Airway &amp; Orthodontics</div>
        <div class="svc-desc">Healthy Start and functional appliances guide jaw development in children. Early intervention prevents a lifetime of airway problems.</div>
        <a class="svc-link" href="#">Learn more &rarr;</a>
      </div>
      <div class="svc-card">
        <div class="svc-accent" style="background:linear-gradient(to right,#2d5fa3,#5a87c3);"></div>
        <div class="svc-icon" style="background:#eef3fb;">&#128203;</div>
        <div class="svc-name">Physician Referral Program</div>
        <div class="svc-desc">We work closely with ENTs, pediatricians, sleep physicians, and myofunctional therapists. Detailed reports and collaborative care for every patient.</div>
        <a class="svc-link" href="#">Learn more &rarr;</a>
      </div>
    </div>
  </div>
</section>
''')

html_parts.append(f'''
<!-- CONNECTED / FLOWCHART -->
<section class="connected-section">
  <div class="connected-inner">
    <div class="connected-header">
      <div class="eyebrow" style="margin-bottom:14px;">The bigger picture</div>
      <h2 class="connected-title">Everything is <em>connected.</em></h2>
      <p class="connected-sub">Tongue tie, mouth breathing, enlarged tonsils, poor sleep, and systemic disease aren&rsquo;t separate problems. They form a chain &mdash; and we treat the root.</p>
    </div>
    <div class="flowchart-wrap">
      {flowchart_svg}
    </div>
    <div class="chain-cards">
      <div class="chain-card" style="background:rgba(216,90,48,.15);border-color:rgba(216,90,48,.35);">
        <div class="chain-card-title">&#128133; Tongue tie &rarr; mouth breathing</div>
        <div class="chain-card-text">A restricted tongue can&#39;t rest on the roof of the mouth. It sits low, forcing mouth breathing &mdash; and sending unfiltered, bacteria-laden air directly to the tonsils.</div>
      </div>
      <div class="chain-card" style="background:rgba(186,117,23,.15);border-color:rgba(201,168,76,.35);">
        <div class="chain-card-title">&#128558; Mouth breathing &rarr; enlarged tonsils</div>
        <div class="chain-card-text">The nose filters, humidifies, and cleans air before it reaches the tonsils. Mouth breathing bypasses all of this &mdash; delivering dirty air full of bacteria directly to tonsil tissue.</div>
      </div>
      <div class="chain-card" style="background:rgba(163,45,45,.15);border-color:rgba(226,75,74,.35);">
        <div class="chain-card-title">&#128260; Enlarged tonsils &rarr; more mouth breathing</div>
        <div class="chain-card-text">Once tonsils enlarge, they obstruct the airway further &mdash; forcing even more mouth breathing. A self-reinforcing cycle that worsens over time without treatment.</div>
      </div>
      <div class="chain-card" style="background:rgba(99,153,34,.15);border-color:rgba(99,153,34,.35);">
        <div class="chain-card-title">&#129704; Forward head posture &rarr; neck &amp; shoulder pain</div>
        <div class="chain-card-text">Mouth breathing shifts the head forward to open the airway. Over time this causes forward head posture, neck strain, and chronic shoulder pain &mdash; a direct consequence of tongue tie.</div>
      </div>
      <div class="chain-card" style="background:rgba(55,138,221,.15);border-color:rgba(55,138,221,.35);">
        <div class="chain-card-title">&#128164; Poor sleep &rarr; whole-body consequences</div>
        <div class="chain-card-text">Narrowed airway &rarr; snoring, apnea, low oxygen. Every night of disrupted sleep compounds over years: ADHD-like symptoms, fatigue, brain fog, mood disorders, cardiovascular risk.</div>
      </div>
      <div class="chain-card" style="background:rgba(15,110,86,.15);border-color:rgba(29,158,117,.35);">
        <div class="chain-card-title">&#128279; Fix the root &mdash; fix everything</div>
        <div class="chain-card-text">Because everything is connected, treating the root cause ripples through the chain. Better tongue posture &rarr; nasal breathing &rarr; smaller tonsils &rarr; better sleep &rarr; healthier life.</div>
      </div>
    </div>
  </div>
</section>
''')

html_parts.append('''
<!-- BREAK THE CHAIN -->
<section class="break-section">
  <div class="container">
    <div class="section-header">
      <div class="eyebrow" style="margin-bottom:10px;">Breaking the cycle</div>
      <div class="section-title">Treating the root &mdash; not just the symptom</div>
    </div>
    <div class="break-grid">
      <div class="break-card">
        <div class="break-accent" style="background:#6389c7;"></div>
        <div class="break-step">Step 1 &middot; Find the origin</div>
        <div class="break-title">Is there a tongue tie?</div>
        <div class="break-text">A restricted tongue is often where the chain begins. Releasing it allows the tongue to rest on the palate.</div>
        <div class="break-tool">CO2 laser frenectomy</div>
        <div class="break-tool">Myofunctional therapy</div>
      </div>
      <div class="break-card">
        <div class="break-accent" style="background:#4a9a7a;"></div>
        <div class="break-step">Step 2 &middot; Stop mouth breathing</div>
        <div class="break-title">Open the nasal airway</div>
        <div class="break-text">Patients can&#39;t nasal breathe if they can&#39;t breathe through their nose.</div>
        <div class="break-tool">Nasal Release Therapy (NRT)</div>
        <div class="break-tool">SONU headband (15 min morning + before bed)</div>
        <div class="break-tool">Nasal sprays &middot; Mouth tape at night</div>
      </div>
      <div class="break-card">
        <div class="break-accent" style="background:#c9a84c;"></div>
        <div class="break-step">Step 3 &middot; Treat the tonsils</div>
        <div class="break-title">Shrink tonsils &amp; prevent recurrence</div>
        <div class="break-text">Laser decontamination shrinks tonsils. But if mouth breathing continues, they may enlarge again.</div>
        <div class="break-tool">CO2 laser tonsil decontamination</div>
        <div class="break-tool">Nasal breathing to prevent recurrence</div>
      </div>
      <div class="break-card">
        <div class="break-accent" style="background:#7a5ab5;"></div>
        <div class="break-step">Step 4 &middot; Expand the airway</div>
        <div class="break-title">Grow a permanently larger airway</div>
        <div class="break-text">Epigenetic appliances create permanent structural change &mdash; widening the dental arches and nasal passages without surgery.</div>
        <div class="break-tool">Epigenetic arch remodeling &mdash; multiple systems available</div>
        <div class="break-tool">Healthy Start &middot; Functional appliances (children)</div>
      </div>
      <div class="break-card">
        <div class="break-accent" style="background:#c97a4a;"></div>
        <div class="break-step">Step 5 &middot; Address sleep</div>
        <div class="break-title">Restore restorative sleep</div>
        <div class="break-text">MAD devices and snoring laser bridge the gap while expansion is underway.</div>
        <div class="break-tool">Custom MAD device for diagnosed sleep apnea</div>
        <div class="break-tool">Snoring laser (fractional ablative therapy)</div>
      </div>
      <div class="break-card">
        <div class="break-accent" style="background:#1a6a7a;"></div>
        <div class="break-step">Step 6 &middot; Reinforce &amp; maintain</div>
        <div class="break-title">Make it stick for life</div>
        <div class="break-text">Myofunctional therapy retrains tongue, face, and throat muscles.</div>
        <div class="break-tool">Myofunctional therapy referral</div>
        <div class="break-tool">Nasal breathing habit reinforcement</div>
      </div>
    </div>
  </div>
</section>

<!-- DR HALLER -->
<section class="dr-section">
  <div class="dr-inner">
    <div>
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
    <div>
      <div class="eyebrow" style="margin-bottom:12px;">Meet Dr. Haller</div>
      <div class="dr-name">Leslie Haller, DMD</div>
      <div class="dr-title-line">Airway Dentist &middot; CO2 Laser Specialist &middot; Coral Gables, FL</div>
      <div class="dr-quote">&ldquo;Along with releasing tongue ties, airway remodeling is the most satisfying work of my life. I have had patients tell me their tinnitus went away, that they could smell their wife&rsquo;s perfume for the first time, that their child finally slept through the night.&rdquo;</div>
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

<!-- CTA BANNER -->
<div class="gold-rule"></div>
<section class="cta-banner">
  <div class="cta-inner">
    <div>
      <div class="eyebrow cta-eyebrow">Ready to breathe better?</div>
      <div class="cta-headline">Your airway is the <span>root cause</span>.<br>Let&#39;s fix it &mdash; for good.</div>
      <p class="cta-sub">Our practice is fee-for-service. We provide a Letter of Medical Necessity and insurance codes for you to submit to your insurance company for potential reimbursement.</p>
    </div>
    <div class="cta-actions">
      <button class="btn-gold">Book a Consultation</button>
      <button class="btn-outline" style="color:#fff;border-color:rgba(255,255,255,.3);">For Physicians</button>
    </div>
  </div>
</section>
<div class="gold-rule"></div>

<!-- TESTIMONIALS -->
<section class="test-section">
  <div class="container">
    <div class="section-header">
      <div class="eyebrow" style="margin-bottom:10px;">Patient stories</div>
      <div class="section-title">What our patients say</div>
    </div>
    <div class="test-grid">
      <div class="test-card">
        <div class="test-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <div class="test-quote">&ldquo;My son&#39;s tonsils were Grade 3 and his pediatrician wanted a surgical referral. After 4 laser sessions with Dr. Haller, they&#39;re barely visible. No surgery, no hospital, no recovery time.&rdquo;</div>
        <div class="test-row">
          <div class="test-avatar">MT</div>
          <div><div class="test-author">Maria T.</div><div class="test-type">Tonsil Laser Treatment &middot; Parent</div></div>
        </div>
      </div>
      <div class="test-card">
        <div class="test-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <div class="test-quote">&ldquo;I tried CPAP for two years and couldn&#39;t tolerate it. Dr. Haller made me a custom oral appliance and I sleep through the night for the first time in a decade.&rdquo;</div>
        <div class="test-row">
          <div class="test-avatar">RM</div>
          <div><div class="test-author">Robert M.</div><div class="test-type">Sleep Apnea &middot; Oral Appliance</div></div>
        </div>
      </div>
      <div class="test-card">
        <div class="test-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <div class="test-quote">&ldquo;My infant had a posterior tongue tie nobody else caught. The CO2 laser release took 15 minutes and transformed her ability to nurse. Dr. Haller literally changed our lives.&rdquo;</div>
        <div class="test-row">
          <div class="test-avatar">JK</div>
          <div><div class="test-author">Jennifer K.</div><div class="test-type">Infant Tongue Tie &middot; Mother</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- BOOKS -->
<section class="books-section">
  <div class="container">
    <div class="section-header">
      <div class="eyebrow" style="margin-bottom:10px;">Recommended reading</div>
      <div class="section-title">Understand the problem &mdash; and the solution</div>
    </div>
    <div class="books-grid">
      <div class="book-card">
        <div class="book-cover" style="background:#dce8f5;">&#128218;</div>
        <div>
          <div class="book-title">Breath: The New Science of a Lost Art</div>
          <div class="book-author">James Nestor</div>
          <div class="book-desc">How the way we breathe affects our health &mdash; and how to fix it.</div>
        </div>
      </div>
      <div class="book-card">
        <div class="book-cover" style="background:#e8f5ee;">&#128218;</div>
        <div>
          <div class="book-title">Six-Foot Tiger in a Three-Foot Cage</div>
          <div class="book-author">Dr. Felix Liao</div>
          <div class="book-desc">How an underdeveloped jaw is the hidden cause of sleep apnea, TMJ, and chronic pain.</div>
        </div>
      </div>
      <div class="book-card">
        <div class="book-cover" style="background:#f5f0e8;">&#128218;</div>
        <div>
          <div class="book-title">Licensed to Thrive</div>
          <div class="book-author">Dr. Felix Liao</div>
          <div class="book-desc">Dr. Liao&#39;s newest book on the Holistic Mouth Solutions framework.</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section class="contact-section">
  <div class="contact-inner">
    <div>
      <div class="contact-title">Request an appointment</div>
      <div class="form-field"><label class="form-label">Your name</label><input class="form-input" placeholder="Full name" type="text"/></div>
      <div class="form-field"><label class="form-label">Phone or email</label><input class="form-input" placeholder="Best way to reach you" type="text"/></div>
      <div class="form-field"><label class="form-label">Patient age group</label>
        <select class="form-input"><option>Adult (18+)</option><option>Child / Teen</option><option>Infant</option></select>
      </div>
      <div class="form-field"><label class="form-label">I&#39;m interested in&hellip;</label>
        <select class="form-input">
          <option>Sleep Apnea / Oral Appliance</option>
          <option>CO2 Laser Tonsil Treatment</option>
          <option>Tongue Tie Release</option>
          <option>Children&#39;s Airway / Orthodontics</option>
          <option>Nasal Release Therapy (NRT)</option>
          <option>Snoring Laser Treatment</option>
          <option>Adult Airway Expansion</option>
        </select>
      </div>
      <button class="form-submit">Send Request &rarr;</button>
      <div class="form-note">Our practice is fee-for-service. We provide a Letter of Medical Necessity and insurance codes for you to submit to your insurance company for potential reimbursement.</div>
    </div>
    <div>
      <div class="contact-title">Find us</div>
      <div class="contact-detail"><div class="contact-icon">&#128205;</div><div><div class="contact-dt">348 Alhambra Circle</div><div class="contact-ds">Coral Gables, Florida 33134</div></div></div>
      <div class="contact-detail"><div class="contact-icon">&#128222;</div><div><div class="contact-dt">(305) 447-9199</div><div class="contact-ds">Call or text anytime</div></div></div>
      <div class="contact-detail"><div class="contact-icon">&#9993;</div><div><div class="contact-dt">dentistry@lesliehallerdmd.com</div><div class="contact-ds">We respond within one business day</div></div></div>
      <div class="contact-detail"><div class="contact-icon">&#128336;</div><div><div class="contact-dt">Mon &ndash; Fri, 9am &ndash; 5pm</div><div class="contact-ds">Contact us to schedule</div></div></div>
      <div class="map-ph">Google Map embed goes here</div>
    </div>
  </div>
</section>
''')

html_parts.append(f'''
<!-- FOOTER -->
<footer class="footer">
  <div class="footer-inner">
    <div>
      <img src="{logo_transparent_uri}" alt="Dental Solutions of South Florida" class="footer-logo">
      <div class="footer-tagline">Breathe Better. Sleep Better. Live Better.</div>
      <div class="footer-contact">348 Alhambra Circle<br>Coral Gables, FL 33134<br>(305) 447-9199<br>dentistry@lesliehallerdmd.com</div>
    </div>
    <div>
      <div class="footer-col-title">Treatments</div>
      <a class="footer-link" href="#">Tongue Tie Release</a>
      <a class="footer-link" href="#">Sleep Apnea</a>
      <a class="footer-link" href="#">CO2 Laser Tonsils</a>
      <a class="footer-link" href="#">Airway Expansion</a>
      <a class="footer-link" href="#">Children&#39;s Airway</a>
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

</div>
</body>
</html>
''')

full_html = ''.join(html_parts)
with open('/home/ubuntu/dental-modern/index.html', 'w') as f:
    f.write(full_html)

print(f"Written: {len(full_html):,} chars, {len(full_html.splitlines())} lines")
