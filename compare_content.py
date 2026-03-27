#!/usr/bin/env python3
"""
Compare live GitHub Pages content against original source HTML files.
Outputs a detailed diff report for each page.
"""
import requests
from bs4 import BeautifulSoup
import difflib
import os

BASE_LIVE = "https://loro123.github.io/dental-solutions-sf/"
SOURCE_DIR = "/home/ubuntu/leslie-site-src/Leslie New SIte/"

PAGES = [
    ("sleep-apnea.html",     "sleep-apnea.html"),
    ("tonsils.html",         "tonsils.html"),
    ("tongue-tie.html",      "tongue-tie.html"),
    ("nrt.html",             "nrt.html"),
    ("snoring.html",         "snoring.html"),
    ("adult-airway.html",    "adult-airway.html"),
    ("childrens-airway.html","childrens-airway.html"),
    ("physician-referral.html","physician-referral.html"),
]

def extract_text(html, label=""):
    """Extract all visible text from HTML, normalized."""
    soup = BeautifulSoup(html, "html.parser")
    # Remove nav, footer, script, style — we only want body content
    for tag in soup.find_all(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    # Get all text, normalize whitespace
    lines = []
    for elem in soup.find_all(["h1","h2","h3","h4","h5","h6","p","li","td","th","blockquote","figcaption","label","dt","dd"]):
        text = elem.get_text(separator=" ", strip=True)
        if text and len(text) > 3:
            lines.append(text)
    return lines

report_lines = []
all_ok = True

for live_slug, src_slug in PAGES:
    live_url = BASE_LIVE + live_slug
    src_path = os.path.join(SOURCE_DIR, src_slug)

    # Fetch live page
    try:
        resp = requests.get(live_url, timeout=15)
        live_html = resp.text
    except Exception as e:
        report_lines.append(f"\n{'='*60}\n{live_slug}: FETCH ERROR — {e}")
        continue

    # Read source file
    if not os.path.exists(src_path):
        report_lines.append(f"\n{'='*60}\n{live_slug}: SOURCE FILE NOT FOUND at {src_path}")
        continue

    with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
        src_html = f.read()

    live_lines = extract_text(live_html, "live")
    src_lines  = extract_text(src_html,  "src")

    # Find lines in source that are missing from live
    missing_from_live = []
    for line in src_lines:
        # Check if this line (or close variant) appears in live
        found = any(
            line.lower()[:60] in l.lower() or l.lower()[:60] in line.lower()
            for l in live_lines
        )
        if not found and len(line) > 20:
            missing_from_live.append(line)

    # Find lines in live that weren't in source (added/changed)
    added_to_live = []
    for line in live_lines:
        found = any(
            line.lower()[:60] in l.lower() or l.lower()[:60] in line.lower()
            for l in src_lines
        )
        if not found and len(line) > 20:
            added_to_live.append(line)

    report_lines.append(f"\n{'='*60}")
    report_lines.append(f"PAGE: {live_slug}")
    report_lines.append(f"Source lines: {len(src_lines)} | Live lines: {len(live_lines)}")

    if missing_from_live:
        all_ok = False
        report_lines.append(f"\n  ❌ MISSING FROM LIVE ({len(missing_from_live)} items):")
        for m in missing_from_live[:30]:
            report_lines.append(f"    - {m[:120]}")
    else:
        report_lines.append("  ✅ No missing content detected")

    if added_to_live:
        report_lines.append(f"\n  ⚠️  IN LIVE BUT NOT IN SOURCE ({len(added_to_live)} items):")
        for a in added_to_live[:20]:
            report_lines.append(f"    + {a[:120]}")

report_lines.append(f"\n{'='*60}")
report_lines.append("OVERALL: " + ("✅ ALL PAGES MATCH" if all_ok else "❌ DISCREPANCIES FOUND — see above"))

report = "\n".join(report_lines)
print(report)

with open("/home/ubuntu/dental-modern/content_comparison_report.txt", "w") as f:
    f.write(report)

print("\nReport saved to content_comparison_report.txt")
