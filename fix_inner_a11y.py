import re

with open('/home/ubuntu/dental-modern/build_inner3.py', 'r') as f:
    content = f.read()

# Fix empty link in nav logo
content = content.replace(
    '<a href="index.html" aria-label="Home"><img src="{logo_uri}" alt="Dental Solutions of South Florida" class="nav-logo"></a>',
    '<a href="index.html" aria-label="Home" class="nav-logo-link"><img src="{logo_uri}" alt="Dental Solutions of South Florida" class="nav-logo"></a>'
)

# Fix empty link in mobile nav logo
content = content.replace(
    '<img src="{logo_uri}" alt="Dental Solutions of South Florida" style="height:52px">',
    '<a href="index.html" aria-label="Home" class="nav-logo-link"><img src="{logo_uri}" alt="Dental Solutions of South Florida" style="height:52px"></a>'
)

# Fix small targets in CSS
css_fixes = """
  .nav-logo-link { display: inline-block; min-height: 44px; min-width: 44px; }
  .nav-links a { min-height: 44px; display: inline-flex; align-items: center; }
  .nav-link-dd { min-height: 44px; display: inline-flex; align-items: center; }
  .mob-sub { min-height: 44px; display: flex; align-items: center; }
  .breadcrumb a { min-height: 44px; display: inline-flex; align-items: center; }
"""

if '.nav-logo-link' not in content:
    content = content.replace('/* TOUCH TARGETS */', '/* TOUCH TARGETS */' + css_fixes)

with open('/home/ubuntu/dental-modern/build_inner3.py', 'w') as f:
    f.write(content)

print("Fixed build_inner3.py")
