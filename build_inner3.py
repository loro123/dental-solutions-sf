import base64
from bs4 import BeautifulSoup, NavigableString

# ── Assets ────────────────────────────────────────────────────────────────────
with open('/home/ubuntu/upload/airway-dentist-logo.jpg', 'rb') as f:
    logo_uri = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode()
with open('/home/ubuntu/dental-modern/logo_transparent.png', 'rb') as f:
    logo_trans_uri = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

# ── Source files ───────────────────────────────────────────────────────────────
SOURCES = {
    "sleep-apnea":       "/home/ubuntu/leslie-site-src/Leslie New SIte/sleep-apnea.html",
    "tonsils":           "/home/ubuntu/leslie-site-src/Leslie New SIte/tonsil-page-clean (1).html",
    "tongue-tie":        "/home/ubuntu/leslie-site-src/Leslie New SIte/tongue-tie.html",
    "nrt":               "/home/ubuntu/leslie-site-src/Leslie New SIte/nrt.html",
    "snoring":           "/home/ubuntu/leslie-site-src/Leslie New SIte/snoring.html",
    "adult-airway":      "/home/ubuntu/leslie-site-src/Leslie New SIte/adult-airway.html",
    "childrens-airway":  "/home/ubuntu/leslie-site-src/Leslie New SIte/childrens-airway.html",
    "physician-referral":"/home/ubuntu/leslie-site-src/Leslie New SIte/physician-referral.html",
}

# ── Page meta ─────────────────────────────────────────────────────────────────
META = {
    "sleep-apnea":       {"title":"Sleep Apnea Treatment","subtitle":"Without a CPAP Machine","badge":"Sleep Apnea & CPAP Alternatives · Coral Gables, FL","active":"sleep-apnea","crumb":"Sleep Apnea"},
    "tonsils":           {"title":"CO2 Laser Tonsil Treatment","subtitle":"Shrink Enlarged Tonsils Without Surgery","badge":"Laser Dentistry · Coral Gables, FL","active":"tonsils","crumb":"CO2 Laser Tonsils"},
    "tongue-tie":        {"title":"Tongue Tie Frenectomy","subtitle":"CO2 Laser Release for All Ages","badge":"Tongue Tie · Coral Gables, FL","active":"tongue-tie","crumb":"Tongue Tie"},
    "nrt":               {"title":"Nasal Release Therapy","subtitle":"Open the Airway from the Inside","badge":"Nasal Release Therapy · Coral Gables, FL","active":"nrt","crumb":"Nasal Release Therapy"},
    "snoring":           {"title":"Laser Snoring Treatment","subtitle":"Quiet Nights. No Surgery. No Mask.","badge":"Laser Snoring · Coral Gables, FL","active":"snoring","crumb":"Laser Snoring"},
    "adult-airway":      {"title":"Adult Airway Expansion","subtitle":"Expand Your Airway. Permanently. Without Surgery.","badge":"Epigenetic Arch Remodeling · Coral Gables, FL","active":"adult-airway","crumb":"Adult Airway"},
    "childrens-airway":  {"title":"Children's Airway & Orthodontics","subtitle":"Straight Teeth Are the Least Important Part","badge":"Pediatric Airway Dentistry · Coral Gables, FL","active":"childrens-airway","crumb":"Children's Airway"},
    "physician-referral":{"title":"Physician Referrals","subtitle":"A Trusted Airway Partner for Your Practice","badge":"For Medical Providers · Coral Gables, FL","active":"physician-referral","crumb":"Physician Referrals"},
}

# ── Extract all content sections from a source page ───────────────────────────
def extract_sections(slug):
    with open(SOURCES[slug], "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    # Remove chrome
    for tag in soup.find_all(["script","style","head"]):
        tag.decompose()
    for cls in ["nav","topbar","gold-rule","page-label"]:
        for tag in soup.find_all(class_=cls):
            tag.decompose()
    return soup.find_all("div", class_="content-section")

# ── Convert a source section to modern HTML ───────────────────────────────────
def render_section(section, idx):
    label_el = section.find(class_="section-label")
    title_el  = section.find(class_="section-title")
    sub_el    = section.find(class_="section-sub")
    label = label_el.get_text(strip=True) if label_el else ""
    title = title_el.get_text(strip=True) if title_el else ""
    sub   = sub_el.get_text(strip=True)   if sub_el   else ""

    # Determine background alternation
    bg = "#fff" if idx % 2 == 0 else "var(--surface)"

    html = f'<section class="inner-section" style="background:{bg};">\n'
    html += '  <div class="inner-wrap">\n'

    # Section header
    html += '    <div class="inner-section-header">\n'
    if label:
        html += f'      <div class="inner-eyebrow">{label}</div>\n'
    if title:
        html += f'      <h2 class="inner-h2">{title}</h2>\n'
    if sub:
        html += f'      <p class="inner-sub">{sub}</p>\n'
    html += '    </div>\n'

    # ── Render all child elements preserving structure ────────────────────────
    # Remove the label/title/sub elements we already rendered
    if label_el: label_el.decompose()
    if title_el: title_el.decompose()
    if sub_el:   sub_el.decompose()

    html += render_children(section)

    html += '  </div>\n'
    html += '</section>\n'
    return html

def render_children(parent):
    """Recursively render child content into modern HTML, handling all source component classes."""
    out = ""
    for child in parent.children:
        if isinstance(child, NavigableString):
            txt = child.strip()
            if txt:
                out += f'<p class="inner-body">{txt}</p>\n'
            continue
        tag = child
        cls = " ".join(tag.get("class", []))
        name = tag.name

        # Skip empty tags
        if not tag.get_text(strip=True):
            continue

        # ── Headings ──────────────────────────────────────────────────────────
        if name in ["h1","h2","h3","h4","h5","h6"]:
            level = {"h1":"h3","h2":"h3","h3":"h3","h4":"h4","h5":"h5","h6":"h6"}[name]
            out += f'<{level} class="inner-{level}">{tag.get_text(strip=True)}</{level}>\n'

        # ── Paragraphs ────────────────────────────────────────────────────────
        elif name == "p":
            out += f'<p class="inner-body">{tag.decode_contents()}</p>\n'

        # ── Unordered lists ───────────────────────────────────────────────────
        elif name == "ul":
            out += '<ul class="inner-list">\n'
            for li in tag.find_all("li", recursive=False):
                out += f'  <li>{li.decode_contents()}</li>\n'
            out += '</ul>\n'

        # ── Ordered lists ─────────────────────────────────────────────────────
        elif name == "ol":
            out += '<ol class="inner-olist">\n'
            for li in tag.find_all("li", recursive=False):
                out += f'  <li>{li.decode_contents()}</li>\n'
            out += '</ol>\n'

        # ── Tables ────────────────────────────────────────────────────────────
        elif name == "table":
            out += '<div class="inner-table-wrap">\n<table class="inner-table">\n'
            for row in tag.find_all("tr"):
                out += "<tr>"
                for cell in row.find_all(["th","td"]):
                    tag_name = cell.name
                    out += f'<{tag_name}>{cell.decode_contents()}</{tag_name}>'
                out += "</tr>\n"
            out += '</table>\n</div>\n'

        # ── Blockquotes / pull quotes ─────────────────────────────────────────
        elif name == "blockquote":
            out += f'<blockquote class="inner-quote">{tag.decode_contents()}</blockquote>\n'

        # ── Dividers ──────────────────────────────────────────────────────────
        elif name == "hr":
            out += '<hr class="inner-divider">\n'

        # ── Warning / alert boxes ─────────────────────────────────────────────
        elif name == "div" and "warning-box" in cls:
            color = "gold"
            if "red" in cls: color = "red"
            elif "green" in cls: color = "green"
            elif "blue" in cls: color = "blue"
            elif "teal" in cls: color = "teal"
            elif "purple" in cls: color = "purple"
            title_el = tag.find(class_="warning-title") or tag.find(class_=lambda c: c and "warning-title" in c)
            text_el  = tag.find(class_="warning-text")
            title_txt = title_el.get_text(strip=True) if title_el else ""
            body_txt  = text_el.decode_contents() if text_el else tag.get_text(strip=True)
            out += f'<div class="inner-warning inner-warning-{color}">\n'
            if title_txt:
                out += f'  <div class="inner-warning-title">{title_txt}</div>\n'
            out += f'  <div class="inner-warning-body">{body_txt}</div>\n'
            out += '</div>\n'

        # ── Quote boxes ───────────────────────────────────────────────────────
        elif name == "div" and "quote-box" in cls:
            color = "gold"
            if "blue" in cls: color = "blue"
            elif "green" in cls: color = "green"
            elif "teal" in cls: color = "teal"
            out += f'<div class="inner-quote-box inner-quote-box-{color}">{tag.decode_contents()}</div>\n'

        # ── FAQ items ─────────────────────────────────────────────────────────
        elif name == "div" and "faq-item" in cls:
            q_el = tag.find(class_="faq-q")
            a_el = tag.find(class_="faq-a")
            q = q_el.get_text(strip=True) if q_el else ""
            a = a_el.decode_contents() if a_el else tag.get_text(strip=True)
            out += f'<div class="inner-faq">\n'
            out += f'  <div class="inner-faq-q">{q}</div>\n'
            out += f'  <div class="inner-faq-a">{a}</div>\n'
            out += '</div>\n'

        # ── Step rows ─────────────────────────────────────────────────────────
        elif name == "div" and "step-row" in cls:
            out += '<div class="inner-steps">\n'
            for step in tag.find_all("div", class_=lambda c: c and "step-item" in c, recursive=False):
                num_el   = step.find(class_="step-num")
                title_el = step.find(class_="step-title")
                text_el  = step.find(class_="step-text")
                num   = num_el.get_text(strip=True)   if num_el   else ""
                title = title_el.get_text(strip=True) if title_el else ""
                text  = text_el.decode_contents()     if text_el  else ""
                out += f'  <div class="inner-step">\n'
                if num:   out += f'    <div class="inner-step-num">{num}</div>\n'
                if title: out += f'    <div class="inner-step-title">{title}</div>\n'
                if text:  out += f'    <div class="inner-step-text">{text}</div>\n'
                out += '  </div>\n'
            out += '</div>\n'

        # ── Stat cards ────────────────────────────────────────────────────────
        elif name == "div" and "stat-card" in cls:
            num_el   = tag.find(class_=lambda c: c and "stat-num" in c)
            label_el = tag.find(class_="stat-label")
            num   = num_el.get_text(strip=True)   if num_el   else ""
            label = label_el.get_text(strip=True) if label_el else tag.get_text(strip=True)
            out += f'<div class="inner-stat"><div class="inner-stat-num">{num}</div><div class="inner-stat-label">{label}</div></div>\n'

        # ── Three-col / two-col / four-col grids ──────────────────────────────
        elif name == "div" and any(k in cls for k in ["three-col","two-col","four-col","books-grid","cycle-grid","break-grid","referral-grid","credentials-grid","services-grid","test-grid","reading-grid"]):
            # Determine grid columns
            cols = 3
            if "two-col" in cls or "referral-grid" in cls: cols = 2
            elif "four-col" in cls: cols = 4
            out += f'<div class="inner-grid inner-grid-{cols}col">\n'
            # Find all direct child divs that are cards/items
            items = tag.find_all(["div","a"], recursive=False)
            for item in items:
                if not item.get_text(strip=True): continue
                # Check if it has a title-like child
                title_el = item.find(class_=lambda c: c and any(k in c for k in ["title","name","heading","card-title"]))
                icon_el  = item.find(class_=lambda c: c and "icon" in c)
                icon_txt  = icon_el.get_text(strip=True) if icon_el else ""
                title_txt = title_el.get_text(strip=True) if title_el else ""
                if title_el: title_el.decompose()
                if icon_el:
                    try: icon_el.decompose()
                    except: pass
                body_txt = item.get_text(separator="\n", strip=True)
                out += '  <div class="inner-grid-item">\n'
                if icon_txt or title_txt:
                    out += '    <div class="inner-card-header">\n'
                    if icon_txt: out += f'      <span class="inner-card-icon">{icon_txt}</span>\n'
                    if title_txt: out += f'      <div class="inner-card-title">{title_txt}</div>\n'
                    out += '    </div>\n'
                if body_txt:
                    for line in body_txt.split("\n"):
                        line = line.strip()
                        if line:
                            out += f'    <p class="inner-card-body">{line}</p>\n'
                out += '  </div>\n'
            out += '</div>\n'

        # ── Type cards (tongue-tie types, etc.) ───────────────────────────────
        elif name == "div" and "type-card" in cls:
            out += render_card(tag)

        # ── Named card types ──────────────────────────────────────────────────
        elif name == "div" and any(k in cls for k in [
            "card","info-card","stat-card","highlight-card","callout","note-box",
            "insight-box","tip-box","step-card","comparison-row","treatment-card",
            "credential-card","specialty-card","referral-card","quote-card",
            "testimonial-card","result-card","timeline-item","process-step",
            "chain-card","cycle-card","break-card","service-card","grade-card",
            "hs-card","book-card","test-card","outcome-card","connected-card"
        ]):
            out += render_card(tag)

        # ── Inline group divs with emoji label (e.g. 👶 Infants & Newborns) ──
        elif name == "div" and any(k in cls for k in ["group","age-group","patient-group","symptom-group","category"]):
            out += '<div class="inner-group">\n'
            out += render_children(tag)
            out += '</div>\n'

        # ── Testimonial / quote cards ─────────────────────────────────────────
        elif name == "div" and any(k in cls for k in ["testimonial","dr-quote","outcome-quote","test-quote"]):
            txt = tag.get_text(strip=True)
            if txt:
                out += f'<blockquote class="inner-quote">{txt}</blockquote>\n'

        # ── Generic divs — recurse into them ─────────────────────────────────
        elif name == "div":
            inner = render_children(tag)
            if inner.strip():
                out += inner

        # ── Everything else ───────────────────────────────────────────────────
        else:
            txt = tag.get_text(strip=True)
            if txt:
                out += f'<p class="inner-body">{txt}</p>\n'

    return out

def render_card(card):
    """Render a single card element."""
    cls = " ".join(card.get("class", []))
    # Try to find title and body
    title_el = card.find(class_=lambda c: c and any(k in c for k in ["title","heading","name","label","num"]))
    body_els  = card.find_all(class_=lambda c: c and any(k in c for k in ["body","text","desc","sub","detail","content","info"]))

    out = '<div class="inner-card">\n'
    # Icon / emoji if present — render icon and title on the SAME row
    icon_el = card.find(class_=lambda c: c and "icon" in c)
    icon_text = icon_el.get_text(strip=True) if icon_el else ""
    title_text = title_el.get_text(strip=True) if title_el else ""
    if icon_text or title_text:
        out += '  <div class="inner-card-header">\n'
        if icon_text:
            out += f'    <span class="inner-card-icon">{icon_text}</span>\n'
        if title_text:
            out += f'    <div class="inner-card-title">{title_text}</div>\n'
        out += '  </div>\n'
    if title_el:
        title_el.decompose()
    if icon_el:
        try: icon_el.decompose()
        except: pass
    # Render remaining content — handle ul.bullet-list properly
    for child in card.children:
        if not hasattr(child, 'name') or not child.name:
            continue
        child_cls = ' '.join(child.get('class', []))
        if child.name == 'ul':
            out += '  <ul class="inner-card-list">\n'
            for li in child.find_all('li', recursive=False):
                li_text = li.get_text(strip=True).rstrip('•').strip()
                if li_text:
                    out += f'    <li>{li_text}</li>\n'
            out += '  </ul>\n'
        elif child.name == 'p':
            txt = child.get_text(strip=True).rstrip('•').strip()
            if txt:
                out += f'  <p class="inner-card-body">{txt}</p>\n'
        elif child.name in ['h3','h4','h5']:
            txt = child.get_text(strip=True)
            if txt:
                out += f'  <p class="inner-card-subhead">{txt}</p>\n'
        elif 'body' in child_cls or 'text' in child_cls or 'desc' in child_cls:
            txt = child.get_text(strip=True).rstrip('•').strip()
            if txt:
                out += f'  <p class="inner-card-body">{txt}</p>\n'
    out += '</div>\n'
    return out

# ── Hero section for inner pages ──────────────────────────────────────────────
def hero_html(slug):
    m = META[slug]
    return f'''<section class="inner-hero">
  <div class="inner-hero-inner">
    <div class="inner-hero-content">
      <div class="inner-hero-badge">{m["badge"]}</div>
      <h1 class="inner-hero-h1">{m["title"]}<br><span class="inner-hero-sub-h1">{m["subtitle"]}</span></h1>
      <div class="inner-hero-actions">
        <a href="index.html#contact" class="btn-primary">Book a Consultation &rarr;</a>
        <a href="tel:+13054479199" class="btn-ghost">Call (305) 447-9199</a>
      </div>
    </div>
  </div>
</section>'''

# ── Shared nav ────────────────────────────────────────────────────────────────
def nav_html(active_slug):
    def active(slug): return ' class="active"' if slug == active_slug else ''
    return f'''<div class="topbar" role="region" aria-label="Contact Information">
  <div class="topbar-info">
    <span>📍 348 Alhambra Circle, Coral Gables, FL</span>
    <span>📞 (305) 447-9199</span>
    <span>✉ dentistry@lesliehallerdmd.com</span>
  </div>
  <div class="topbar-right">
    <a href="physician-referral.html" class="topbar-link">Physician Referrals</a>
  </div>
</div>
<nav class="nav" aria-label="Main navigation">
  <div class="wrap">
    <a href="index.html" aria-label="Home" class="nav-logo-link"><img src="{logo_uri}" alt="Dental Solutions of South Florida" class="nav-logo"></a>
    <div class="nav-links">
      <a href="index.html">Home</a>
      <div class="nav-item">
        <a class="nav-link-dd">Sleep &amp; Airway ▾</a>
        <div class="nav-dropdown">
          <a href="sleep-apnea.html"{active("sleep-apnea")}>Sleep Apnea &amp; Oral Appliances</a>
          <a href="snoring.html"{active("snoring")}>Laser Snoring Treatment</a>
          <a href="adult-airway.html"{active("adult-airway")}>Adult Airway Expansion</a>
          <a href="nrt.html"{active("nrt")}>Nasal Release Therapy</a>
        </div>
      </div>
      <div class="nav-item">
        <a class="nav-link-dd">Treatments ▾</a>
        <div class="nav-dropdown">
          <a href="tongue-tie.html"{active("tongue-tie")}>Tongue Tie Frenectomy</a>
          <a href="tonsils.html"{active("tonsils")}>CO2 Laser Tonsils</a>
          <a href="adult-airway.html"{active("adult-airway")}>Epigenetic Arch Expansion</a>
          <a href="nrt.html"{active("nrt")}>Nasal Release Therapy</a>
        </div>
      </div>
      <div class="nav-item">
        <a class="nav-link-dd">Children ▾</a>
        <div class="nav-dropdown">
          <a href="childrens-airway.html"{active("childrens-airway")}>Children&#39;s Airway &amp; Orthodontics</a>
          <a href="tongue-tie.html"{active("tongue-tie")}>Tongue Tie (Infants &amp; Children)</a>
          <a href="tonsils.html"{active("tonsils")}>CO2 Laser Tonsils</a>
        </div>
      </div>
      <div class="nav-item">
        <a class="nav-link-dd">About ▾</a>
        <div class="nav-dropdown">
          <a href="index.html#dr-haller">Dr. Leslie Haller</a>
          <a href="index.html#philosophy">Our Philosophy</a>
          <a href="physician-referral.html"{active("physician-referral")}>For Physicians</a>
        </div>
      </div>
      <a href="physician-referral.html"{active("physician-referral")}>Physicians</a>
      <a href="index.html#contact">Contact</a>
    </div>
    <button class="nav-hamburger" aria-label="Open menu" onclick="document.getElementById('navMobile').classList.toggle('open');this.classList.toggle('open')">
      <span></span><span></span><span></span>
    </button>
    <button class="nav-cta" onclick="document.getElementById('contact-section') && document.getElementById('contact-section').scrollIntoView()">Book Appointment</button>
  </div>
</nav>
<div class="nav-mobile" id="navMobile">
  <div class="nav-mobile-header">
    <a href="index.html" aria-label="Home" class="nav-logo-link"><img src="{logo_uri}" alt="Dental Solutions of South Florida" style="height:52px"></a>
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
  <a href="index.html#contact" style="margin-top:24px;background:var(--navy);color:white;text-align:center;border-radius:50px;padding:16px 24px;display:block">Book Appointment</a>
</div>'''

# ── Footer ────────────────────────────────────────────────────────────────────
def footer_html():
    return f'''<footer class="footer" role="contentinfo">
  <div class="footer-inner">
    <div>
      <img src="{logo_trans_uri}" alt="Dental Solutions of South Florida" class="footer-logo">
      <div class="footer-tagline">Breathe Better. Sleep Better. Live Better.</div>
      <div class="footer-contact-info">
        348 Alhambra Circle<br>Coral Gables, FL 33134<br>
        (305) 447-9199<br>dentistry@lesliehallerdmd.com
      </div>
    </div>
    <div>
      <div class="footer-col-title">Treatments</div>
      <a class="footer-link" href="tongue-tie.html">Tongue Tie Release</a>
      <a class="footer-link" href="sleep-apnea.html">Sleep Apnea</a>
      <a class="footer-link" href="tonsils.html">CO2 Laser Tonsils</a>
      <a class="footer-link" href="adult-airway.html">Airway Expansion</a>
      <a class="footer-link" href="childrens-airway.html">Children&rsquo;s Airway</a>
      <a class="footer-link" href="snoring.html">Snoring Laser</a>
      <a class="footer-link" href="nrt.html">NRT</a>
    </div>
    <div>
      <div class="footer-col-title">About</div>
      <a class="footer-link" href="index.html#dr-haller">Dr. Leslie Haller</a>
      <a class="footer-link" href="index.html#philosophy">Our Philosophy</a>
      <a class="footer-link" href="physician-referral.html">For Physicians</a>
    </div>
    <div>
      <div class="footer-col-title">Contact</div>
      <a class="footer-link" href="index.html#contact">Request Appointment</a>
      <a class="footer-link" href="physician-referral.html">Physician Referral</a>
      <a class="footer-link" href="index.html#contact">Directions</a>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="footer-bottom-inner">
      <span>&copy; 2025 Dental Solutions of South Florida &middot; Leslie Haller, DMD</span>
      <span>Privacy Policy &middot; Terms of Use &middot; Accessibility</span>
    </div>
  </div>
</footer>'''

# ── Shared CSS ────────────────────────────────────────────────────────────────
SHARED_CSS = '''
  @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
  :root {
    --navy:#1e2d42; --blue:#6389c7; --blue-on-light:#2d52a0;
    --blue-on-dark:#9ab8e0; --gold:#c9a84c; --ink:#1a2332;
    --body:#3a4a5c; --muted:#5a6a7c; --surface:#f4f6f9;
    --border:#dde3ec; --max-w:1800px; --gutter:64px;
  }
  *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
  html{scroll-behavior:smooth;}
  body{font-family:"Space Grotesk",sans-serif;color:var(--ink);background:#fff;-webkit-font-smoothing:antialiased;}

  /* TOPBAR */
  .topbar{background:var(--navy);padding:10px var(--gutter);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;}
  .topbar-info{display:flex;align-items:center;gap:24px;flex-wrap:wrap;}
  .topbar-info span{font-size:12px;color:rgba(255,255,255,.85);display:flex;align-items:center;gap:6px;}
  .topbar-right{display:flex;align-items:center;gap:24px;}
  .topbar-link{font-size:12px;color:rgba(255,255,255,.85);text-decoration:none;transition:color .2s;}
  .topbar-link:hover{color:#fff;}

  /* NAV */
  .nav{background:rgba(255,255,255,.97);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:200;}
  .nav .wrap{max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter);display:flex;align-items:center;justify-content:space-between;height:100px;gap:32px;}
  .nav-logo{height:80px;width:auto;display:block;flex-shrink:0;}
  .nav-links{display:flex;align-items:center;gap:0;}
  .nav-links > a,.nav-item > a{font-family:"Space Grotesk",sans-serif;font-size:13px;font-weight:500;color:var(--ink);text-decoration:none;padding:8px 16px;border-radius:8px;transition:color .2s,background .2s;white-space:nowrap;}
  .nav-links > a:hover,.nav-item > a:hover{color:var(--blue-on-light);background:rgba(45,82,160,.06);}
  .nav-links > a.active,.nav-item > a.active{color:var(--blue-on-light);font-weight:600;}
  .nav-item{position:relative;}
  .nav-link-dd{cursor:pointer;}
  .nav-dropdown{display:none;position:absolute;top:calc(100% + 8px);left:0;background:#fff;border:1px solid var(--border);border-radius:12px;box-shadow:0 8px 32px rgba(0,0,0,.12);min-width:240px;padding:8px;z-index:300;}
  .nav-dropdown a{display:block;font-size:13px;color:var(--ink);text-decoration:none;padding:10px 16px;border-radius:8px;transition:background .15s,color .15s;}
  .nav-dropdown a:hover{background:var(--surface);color:var(--blue-on-light);}
  .nav-item:hover .nav-dropdown{display:block;}
  .nav-cta{background:var(--navy);color:#fff;font-family:"Space Grotesk",sans-serif;font-size:13px;font-weight:600;padding:12px 24px;border-radius:100px;border:none;cursor:pointer;white-space:nowrap;transition:background .2s;}
  .nav-cta:hover{background:#2d3f5a;}
  .nav-hamburger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:8px;}
  .nav-hamburger span{display:block;width:24px;height:2px;background:var(--ink);border-radius:2px;transition:transform .3s,opacity .3s;}
  .nav-hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg);}
  .nav-hamburger.open span:nth-child(2){opacity:0;}
  .nav-hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg);}
  .nav-mobile{display:none;position:fixed;inset:0;background:#fff;z-index:500;padding:24px;overflow-y:auto;flex-direction:column;gap:4px;}
  .nav-mobile.open{display:flex;}
  .nav-mobile-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;}
  .nav-mobile-close{background:none;border:none;font-size:28px;cursor:pointer;color:var(--ink);}
  .nav-mobile a{display:block;padding:14px 16px;font-size:16px;color:var(--ink);text-decoration:none;border-bottom:1px solid var(--border);}
  .nav-mobile a.mob-sub{font-size:14px;color:var(--muted);padding-left:32px;}
  .mob-section-label{display:block;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue-on-light);padding:16px 16px 4px;}

  /* INNER HERO */
  .inner-hero{background:var(--navy);padding:80px 0 80px;}
  .inner-hero-inner{max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter);}
  .inner-hero-content{max-width:760px;}
  .inner-hero-badge{display:inline-block;background:rgba(201,168,76,.2);color:#f8e5a6;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;padding:6px 16px;border-radius:100px;border:1px solid rgba(201,168,76,.4);margin-bottom:24px;}
  .inner-hero-h1{font-family:"DM Serif Display",serif;font-size:clamp(36px,4vw,64px);color:#fff;line-height:1.1;letter-spacing:-.02em;margin-bottom:32px;}
  .inner-hero-sub-h1{color:#f8e5a6;font-style:italic;display:block;}
  .inner-hero-actions{display:flex;gap:16px;flex-wrap:wrap;}
  .btn-primary{background:var(--gold);color:var(--navy);font-family:"Space Grotesk",sans-serif;font-size:14px;font-weight:700;letter-spacing:.04em;padding:15px 32px;border-radius:100px;border:none;cursor:pointer;transition:background .2s,transform .15s;display:inline-flex;align-items:center;text-decoration:none;min-height:44px;}
  .btn-primary:hover{background:#dbb95a;transform:translateY(-2px);}
  .btn-ghost{background:transparent;color:rgba(255,255,255,.85);font-family:"Space Grotesk",sans-serif;font-size:14px;font-weight:600;padding:15px 32px;border-radius:100px;border:1.5px solid rgba(255,255,255,.3);cursor:pointer;transition:border-color .2s,color .2s;display:inline-flex;align-items:center;text-decoration:none;min-height:44px;}
  .btn-ghost:hover{border-color:rgba(255,255,255,.7);color:#fff;}

  /* BREADCRUMB */
  .breadcrumb{background:var(--surface);border-bottom:1px solid var(--border);padding:12px var(--gutter);}
  .breadcrumb-inner{max-width:var(--max-w);margin:0 auto;font-size:12px;color:var(--muted);}
  .breadcrumb-inner a{color:var(--blue-on-light);text-decoration:underline;}
  .breadcrumb-inner a:hover{text-decoration:underline;}

  /* INNER SECTIONS */
  .inner-section{padding:80px 0;}
  .inner-wrap{max-width:var(--max-w);margin:0 auto;padding:0 var(--gutter);}
  .inner-section-header{margin-bottom:56px;max-width:800px;}
  .inner-eyebrow{font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--blue-on-light);margin-bottom:12px;}
  .inner-h2{font-family:"DM Serif Display",serif;font-size:clamp(28px,3vw,48px);color:var(--ink);line-height:1.15;letter-spacing:-.02em;margin-bottom:16px;}
  .inner-sub{font-size:18px;line-height:1.75;color:var(--body);}
  .inner-h3{font-family:"DM Serif Display",serif;font-size:clamp(20px,2vw,28px);color:var(--ink);margin:32px 0 12px;line-height:1.2;}
  .inner-h4{font-family:"Space Grotesk",sans-serif;font-size:16px;font-weight:700;color:var(--ink);margin:24px 0 8px;}
  .inner-h5{font-family:"Space Grotesk",sans-serif;font-size:14px;font-weight:700;color:var(--blue-on-light);margin:20px 0 6px;text-transform:uppercase;letter-spacing:.06em;}
  .inner-body{font-size:17px;line-height:1.85;color:var(--body);margin-bottom:16px;max-width:800px;}
  .inner-list{margin:0 0 24px 0;padding-left:0;list-style:none;}
  .inner-list li{font-size:16px;line-height:1.75;color:var(--body);padding:10px 0 10px 28px;border-bottom:1px solid var(--border);position:relative;}
  .inner-list li::before{content:"→";position:absolute;left:0;color:var(--blue-on-light);font-weight:700;}
  .inner-card-list{list-style:none;padding:0;margin:8px 0 0 0;}
  .inner-card-list li{font-size:15px;line-height:1.7;color:var(--body);padding:6px 0 6px 20px;position:relative;border-bottom:1px solid var(--border);}
  .inner-card-list li:last-child{border-bottom:none;}
  .inner-card-list li::before{content:"→";position:absolute;left:0;color:var(--blue-on-light);font-weight:700;font-size:13px;}
  .inner-card-subhead{font-size:13px;font-weight:700;color:var(--blue-on-light);text-transform:uppercase;letter-spacing:.06em;margin:12px 0 4px;}
  .inner-olist{margin:0 0 24px 0;padding-left:0;list-style:none;counter-reset:olist;}
  .inner-olist li{font-size:16px;line-height:1.75;color:var(--body);padding:12px 0 12px 48px;border-bottom:1px solid var(--border);position:relative;counter-increment:olist;}
  .inner-olist li::before{content:counter(olist);position:absolute;left:0;top:10px;width:32px;height:32px;background:var(--navy);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;font-family:"Space Grotesk",sans-serif;}
  .inner-table-wrap{overflow-x:auto;margin:24px 0;}
  .inner-table{width:100%;border-collapse:collapse;font-size:16px;}
  .inner-table th{background:var(--navy);color:#fff;padding:12px 16px;text-align:left;font-weight:600;font-size:15px;}
  .inner-table td{padding:12px 16px;border-bottom:1px solid var(--border);color:var(--body);vertical-align:top;}
  .inner-table tr:nth-child(even) td{background:var(--surface);}
  .inner-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;margin:24px 0;}
  .inner-grid-item{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:16px 20px;font-size:16px;color:var(--body);line-height:1.7;}
  .inner-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;margin:24px 0;}
  .inner-card{background:#fff;border:1px solid var(--border);border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,.04);transition:transform .2s,box-shadow .2s;}
  .inner-card:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,0,0,.08);}
  .inner-card-header{display:flex;align-items:center;gap:10px;margin-bottom:12px;}
  .inner-card-icon{font-size:26px;flex-shrink:0;}
  .inner-card-title{font-family:"Space Grotesk",sans-serif;font-size:16px;font-weight:700;color:var(--ink);margin:0;}
  .inner-card-body{font-size:16px;color:var(--body);line-height:1.7;margin-bottom:6px;}
  .inner-quote{border-left:4px solid var(--gold);padding:20px 24px;background:var(--surface);border-radius:0 12px 12px 0;margin:24px 0;font-size:18px;font-style:italic;color:var(--body);line-height:1.8;}
  .inner-divider{border:none;border-top:1px solid var(--border);margin:32px 0;}
  .inner-comparison{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin:24px 0;}

  /* WARNING BOXES */
  .inner-warning{border-radius:12px;padding:20px 24px;margin:20px 0;}
  .inner-warning-gold{background:#fffbf0;border-left:4px solid var(--gold);}
  .inner-warning-red{background:#fff5f5;border-left:4px solid #e24b4a;}
  .inner-warning-green{background:#f0fff4;border-left:4px solid #639922;}
  .inner-warning-blue{background:#f0f4ff;border-left:4px solid var(--blue-on-light);}
  .inner-warning-teal{background:#f0fafa;border-left:4px solid #2a9d8f;}
  .inner-warning-purple{background:#f8f0ff;border-left:4px solid #7c3aed;}
  .inner-warning-title{font-size:14px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px;color:var(--ink);}
  .inner-warning-body{font-size:16px;color:var(--body);line-height:1.75;}

  /* QUOTE BOXES */
  .inner-quote-box{border-radius:12px;padding:24px 28px;margin:20px 0;font-size:17px;font-style:italic;line-height:1.8;}
  .inner-quote-box-gold{background:#fffbf0;border-left:4px solid var(--gold);color:var(--body);}
  .inner-quote-box-blue{background:#f0f4ff;border-left:4px solid var(--blue-on-light);color:var(--body);}
  .inner-quote-box-green{background:#f0fff4;border-left:4px solid #639922;color:var(--body);}
  .inner-quote-box-teal{background:#f0fafa;border-left:4px solid #2a9d8f;color:var(--body);}

  /* FAQ */
  .inner-faq{border:1px solid var(--border);border-radius:12px;margin-bottom:12px;overflow:hidden;}
  .inner-faq-q{font-size:16px;font-weight:700;color:var(--ink);padding:18px 24px;background:var(--surface);cursor:pointer;}
  .inner-faq-a{font-size:16px;color:var(--body);padding:16px 24px;line-height:1.75;border-top:1px solid var(--border);}

  /* STEPS */
  .inner-steps{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:20px;margin:24px 0;}
  .inner-step{background:var(--surface);border-radius:16px;padding:24px;border:1px solid var(--border);}
  .inner-step-num{font-family:"DM Serif Display",serif;font-size:40px;color:#6b829a;line-height:1;margin-bottom:8px;} /* 4.0:1 on white */
  .inner-step-title{font-size:16px;font-weight:700;color:var(--ink);margin-bottom:8px;}
  .inner-step-text{font-size:15px;color:var(--body);line-height:1.7;}

  /* STATS */
  .inner-stat{background:var(--surface);border-radius:12px;padding:20px 24px;text-align:center;border:1px solid var(--border);}
  .inner-stat-num{font-family:"DM Serif Display",serif;font-size:36px;color:var(--blue-on-light);line-height:1;margin-bottom:6px;}
  .inner-stat-label{font-size:14px;color:var(--body);line-height:1.5;}

  /* GRID COLUMN VARIANTS */
  .inner-grid-2col{grid-template-columns:repeat(2,1fr);}
  .inner-grid-3col{grid-template-columns:repeat(3,1fr);}
  .inner-grid-4col{grid-template-columns:repeat(4,1fr);}
  @media(max-width:1024px){
    .inner-grid-4col{grid-template-columns:repeat(2,1fr);}
    .inner-grid-3col{grid-template-columns:repeat(2,1fr);}
  }
  @media(max-width:768px){
    .inner-grid-2col,.inner-grid-3col,.inner-grid-4col{grid-template-columns:1fr;}
    .inner-steps{grid-template-columns:1fr;}
  }

  /* GROUP CONTAINERS */
  .inner-group{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px;margin-bottom:20px;}

  /* CTA STRIP */
  .inner-cta{background:var(--navy);padding:80px var(--gutter);text-align:center;}
  .inner-cta h2{font-family:"DM Serif Display",serif;font-size:clamp(28px,3vw,44px);color:#fff;margin-bottom:16px;}
  .inner-cta p{font-size:16px;color:rgba(255,255,255,.75);margin-bottom:32px;max-width:560px;margin-left:auto;margin-right:auto;}
  .inner-cta-btns{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;}

  /* FOOTER */
  .footer{background:#0d1a2b;padding:80px var(--gutter) 0;}
  .footer-inner{max-width:var(--max-w);margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:64px;padding-bottom:64px;}
  .footer-logo{height:50px;width:auto;margin-bottom:16px;}
  .footer-tagline{font-family:"DM Serif Display",serif;font-style:italic;font-size:16px;color:rgba(255,255,255,.75);margin-bottom:16px;}
  .footer-contact-info{font-size:13px;color:rgba(255,255,255,.65);line-height:2;}
  .footer-col-title{font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.5);margin-bottom:16px;}
  .footer-link{display:block;font-size:13px;color:rgba(255,255,255,.7);text-decoration:none;padding:4px 0;transition:color .2s;}
  .footer-link:hover{color:#fff;}
  .footer-bottom{border-top:1px solid rgba(255,255,255,.08);padding:24px 0;max-width:var(--max-w);margin:0 auto;}
  .footer-bottom-inner{display:flex;justify-content:space-between;font-size:12px;color:rgba(255,255,255,.7);}


  /* SKIP NAVIGATION (WCAG 2.4.1) */
  .skip-link{position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden;background:var(--navy);color:#fff;padding:12px 24px;font-size:14px;font-weight:600;border-radius:0 0 8px 0;z-index:9999;text-decoration:none;}
  .skip-link:focus{position:fixed;left:0;top:0;width:auto;height:auto;overflow:visible;}
  /* BODY COPY LINKS */
  .inner-section a:not(.btn-primary):not(.btn-ghost):not(.footer-link):not(.nav-link){text-decoration:underline;text-underline-offset:3px;}
  /* TOUCH TARGETS */
  .nav-logo-link { display: inline-block; min-height: 44px; min-width: 44px; }
  .nav-links a { min-height: 44px; display: inline-flex; align-items: center; }
  .nav-link-dd { min-height: 44px; display: inline-flex; align-items: center; }
  .mob-sub { min-height: 44px; display: flex; align-items: center; }
  .breadcrumb a { min-height: 44px; display: inline-flex; align-items: center; }

  .nav-hamburger{min-width:44px;min-height:44px;}
  .nav-cta{min-height:44px;}
  .btn-primary,.btn-ghost{min-height:44px;}
  .footer-link{min-height:44px;display:flex;align-items:center;}
  .topbar-link{min-height:44px;display:inline-flex;align-items:center;}

  /* RESPONSIVE */
  @media(max-width:1024px){
    :root{--gutter:40px;}
    .inner-comparison{grid-template-columns:1fr;}
    .footer-inner{grid-template-columns:1fr 1fr;gap:40px;}
  }
  @media(max-width:768px){
    :root{--gutter:20px;}
    .topbar{display:none;}
    .nav .wrap{height:80px;}
    .nav-logo{height:60px;}
    .nav-links,.nav-cta{display:none;}
    .nav-hamburger{display:flex;}
    .inner-hero{padding:60px 0;}
    .inner-section{padding:56px 0;}
    .inner-cards{grid-template-columns:1fr;}
    .inner-grid{grid-template-columns:1fr;}
    .inner-table-wrap{font-size:12px;}
    .footer-inner{grid-template-columns:1fr;}
    .footer-bottom-inner{flex-direction:column;gap:8px;}
    .inner-cta{padding:60px var(--gutter);}
  }
'''

# ── Build a complete page ──────────────────────────────────────────────────────
def build_page(slug):
    m = META[slug]
    sections = extract_sections(slug)
    sections_html = ""
    for i, sec in enumerate(sections):
        sections_html += render_section(sec, i)

    crumb = m["crumb"]
    page_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{m["title"]} — Dental Solutions of South Florida</title>
  <style>{SHARED_CSS}</style>
</head>
<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
{nav_html(slug)}
<main id="main-content">
{hero_html(slug)}
<div class="breadcrumb">
  <div class="breadcrumb-inner">
    <a href="index.html">Home</a> &rsaquo; {crumb}
  </div>
</div>
{sections_html}
<div class="inner-cta" role="complementary" aria-label="Book an appointment">
  <h2>Ready to Breathe Better?</h2>
  <p>Schedule a comprehensive airway evaluation with Dr. Haller. Most patients see results within weeks.</p>
  <div class="inner-cta-btns">
    <a href="index.html#contact" class="btn-primary">Book a Consultation &rarr;</a>
    <a href="tel:+13054479199" class="btn-ghost">Call (305) 447-9199</a>
  </div>
</div>
</main>
{footer_html()}
</body>
</html>'''
    return page_html

# ── Build all pages ────────────────────────────────────────────────────────────
for slug in SOURCES:
    html = build_page(slug)
    out_path = f"/home/ubuntu/dental-modern/{slug}.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    # Count content lines vs source
    from bs4 import BeautifulSoup as BS
    live_text = [l.strip() for l in BS(html,"html.parser").get_text("\n",strip=True).split("\n") if len(l.strip())>15]
    print(f"  {slug}: {len(html):,} chars | {len(live_text)} content lines")

print("\nAll pages built successfully.")
