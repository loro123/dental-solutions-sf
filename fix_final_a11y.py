import re

# Fix build_inner3.py
with open('/home/ubuntu/dental-modern/build_inner3.py', 'r') as f:
    content = f.read()

# 1. Fix inner-hero-badge contrast
content = content.replace(
    'color:var(--gold);',
    'color:#f8e5a6;' # Lighter gold for better contrast
)

# 2. Fix footer text contrast
content = content.replace(
    'color:#6e7680;',
    'color:#94a3b8;'
)

# 3. Fix breadcrumb link underline
content = content.replace(
    '.breadcrumb a{color:var(--primary);text-decoration:none;font-weight:500;}',
    '.breadcrumb a{color:var(--primary);text-decoration:underline;font-weight:500;}'
)

# 4. Fix topbar region
content = content.replace(
    '<div class="topbar">',
    '<div class="topbar" role="region" aria-label="Contact Information">'
)

with open('/home/ubuntu/dental-modern/build_inner3.py', 'w') as f:
    f.write(content)

# Fix index.html
with open('/home/ubuntu/dental-modern/index.html', 'r') as f:
    content = f.read()

# 1. Fix footer text contrast
content = content.replace(
    'color:#6e7680;',
    'color:#94a3b8;'
)

# 2. Fix topbar region
content = content.replace(
    '<div class="topbar">',
    '<div class="topbar" role="region" aria-label="Contact Information">'
)

with open('/home/ubuntu/dental-modern/index.html', 'w') as f:
    f.write(content)

print("Fixed final issues")
