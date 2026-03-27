#!/usr/bin/env python3
"""
Full WCAG 2.1 AA Accessibility Audit
Dental Solutions of South Florida — https://loro123.github.io/dental-solutions-sf/
Uses axe-core injected via Playwright for automated rule-based testing,
plus custom checks for contrast, focus, headings, alt text, etc.
"""

import json, re, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "file:///home/ubuntu/dental-modern/"
PAGES = {
    "Homepage":          BASE + "index.html",
    "Sleep Apnea":       BASE + "sleep-apnea.html",
    "Tonsils":           BASE + "tonsils.html",
    "Tongue Tie":        BASE + "tongue-tie.html",
    "NRT":               BASE + "nrt.html",
    "Snoring":           BASE + "snoring.html",
    "Adult Airway":      BASE + "adult-airway.html",
    "Childrens Airway":  BASE + "childrens-airway.html",
    "Physician Referral":BASE + "physician-referral.html",
}

# Fetch axe-core from CDN
AXE_JS_PATH = "/home/ubuntu/dental-modern/axe.min.js"
with open(AXE_JS_PATH, 'r') as _f:
    AXE_JS_INLINE = _f.read()

WCAG_AA_TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "best-practice"]

results = {}

def run_axe(page):
    """Inject axe-core and run WCAG 2.1 AA audit."""
    # Inject axe-core inline (bypasses CSP)
    page.evaluate(AXE_JS_INLINE)
    page.wait_for_function("typeof axe !== 'undefined'", timeout=10000)
    time.sleep(1)  # let page settle
    raw = page.evaluate("""
        async () => {
            const r = await axe.run(document, {
                runOnly: { type: 'tag', values: ['wcag2a','wcag2aa','wcag21a','wcag21aa','best-practice'] },
                resultTypes: ['violations', 'incomplete']
            });
            return {
                violations: r.violations,
                incomplete: r.incomplete
            };
        }
    """)
    return raw

def run_custom_checks(page, url):
    """Custom checks beyond axe-core."""
    issues = []

    # 1. Check for images without alt text
    imgs_no_alt = page.evaluate("""
        () => {
            const imgs = Array.from(document.querySelectorAll('img'));
            return imgs.filter(img => !img.hasAttribute('alt') || img.getAttribute('alt') === null)
                       .map(img => ({ src: img.src.substring(0,80), tag: img.outerHTML.substring(0,120) }));
        }
    """)
    for img in imgs_no_alt:
        issues.append({"type": "MISSING_ALT", "severity": "critical",
                        "desc": f"Image missing alt attribute", "detail": img['src']})

    # 2. Check heading hierarchy
    headings = page.evaluate("""
        () => {
            const hs = Array.from(document.querySelectorAll('h1,h2,h3,h4,h5,h6'));
            return hs.map(h => ({ level: parseInt(h.tagName[1]), text: h.textContent.trim().substring(0,60) }));
        }
    """)
    prev_level = 0
    for h in headings:
        if h['level'] > prev_level + 1 and prev_level > 0:
            issues.append({"type": "HEADING_SKIP", "severity": "warning",
                            "desc": f"Heading jumps from H{prev_level} to H{h['level']}: \"{h['text']}\""})
        prev_level = h['level']

    h1_count = sum(1 for h in headings if h['level'] == 1)
    if h1_count == 0:
        issues.append({"type": "NO_H1", "severity": "critical", "desc": "Page has no H1 element"})
    elif h1_count > 1:
        issues.append({"type": "MULTIPLE_H1", "severity": "warning",
                        "desc": f"Page has {h1_count} H1 elements (should be 1)"})

    # 3. Check links with no discernible text
    empty_links = page.evaluate("""
        () => {
            const links = Array.from(document.querySelectorAll('a'));
            return links.filter(a => {
                const text = a.textContent.trim();
                const aria = a.getAttribute('aria-label') || '';
                const title = a.getAttribute('title') || '';
                return !text && !aria && !title;
            }).map(a => a.outerHTML.substring(0,120));
        }
    """)
    for lnk in empty_links:
        issues.append({"type": "EMPTY_LINK", "severity": "critical",
                        "desc": "Link has no accessible text", "detail": lnk})

    # 4. Check buttons with no text
    empty_btns = page.evaluate("""
        () => {
            const btns = Array.from(document.querySelectorAll('button'));
            return btns.filter(b => {
                const text = b.textContent.trim();
                const aria = b.getAttribute('aria-label') || '';
                return !text && !aria;
            }).map(b => b.outerHTML.substring(0,120));
        }
    """)
    for btn in empty_btns:
        issues.append({"type": "EMPTY_BUTTON", "severity": "critical",
                        "desc": "Button has no accessible text", "detail": btn})

    # 5. Check form inputs without labels
    unlabeled_inputs = page.evaluate("""
        () => {
            const inputs = Array.from(document.querySelectorAll('input,select,textarea'))
                .filter(el => el.type !== 'hidden' && el.type !== 'submit' && el.type !== 'button');
            return inputs.filter(el => {
                const id = el.id;
                const aria = el.getAttribute('aria-label') || el.getAttribute('aria-labelledby') || '';
                const placeholder = el.getAttribute('placeholder') || '';
                const hasLabel = id && document.querySelector('label[for="' + id + '"]');
                return !hasLabel && !aria && !placeholder;
            }).map(el => ({ type: el.type, name: el.name, id: el.id }));
        }
    """)
    for inp in unlabeled_inputs:
        issues.append({"type": "UNLABELED_INPUT", "severity": "critical",
                        "desc": f"Form input missing label", "detail": str(inp)})

    # 6. Check for skip navigation link
    skip_link = page.evaluate("""
        () => {
            const links = Array.from(document.querySelectorAll('a'));
            return links.some(a => {
                const href = a.getAttribute('href') || '';
                const text = a.textContent.toLowerCase();
                return (href.startsWith('#') && (text.includes('skip') || text.includes('main')));
            });
        }
    """)
    if not skip_link:
        issues.append({"type": "NO_SKIP_LINK", "severity": "warning",
                        "desc": "No skip-to-main-content link found (keyboard navigation)"})

    # 7. Check lang attribute on html element
    lang = page.evaluate("() => document.documentElement.getAttribute('lang')")
    if not lang:
        issues.append({"type": "NO_LANG", "severity": "critical",
                        "desc": "HTML element missing lang attribute"})

    # 8. Check for focus visible styles (basic check)
    focus_style = page.evaluate("""
        () => {
            const style = document.createElement('style');
            style.textContent = '*:focus { outline: 2px solid red !important; }';
            document.head.appendChild(style);
            // Check if any :focus rule exists in stylesheets
            let hasFocusRule = false;
            for (const sheet of document.styleSheets) {
                try {
                    for (const rule of sheet.cssRules || []) {
                        if (rule.selectorText && rule.selectorText.includes(':focus')) {
                            hasFocusRule = true;
                            break;
                        }
                    }
                } catch(e) {}
            }
            style.remove();
            return hasFocusRule;
        }
    """)
    if not focus_style:
        issues.append({"type": "NO_FOCUS_STYLE", "severity": "warning",
                        "desc": "No CSS :focus rules detected — keyboard focus indicators may be missing"})

    # 9. Check touch target sizes (buttons/links < 44x44px)
    small_targets = page.evaluate("""
        () => {
            const els = Array.from(document.querySelectorAll('a, button, [role="button"], input[type="submit"]'));
            return els.filter(el => {
                const r = el.getBoundingClientRect();
                return (r.width > 0 && r.height > 0) && (r.width < 44 || r.height < 44);
            }).slice(0,10).map(el => ({
                tag: el.tagName,
                text: el.textContent.trim().substring(0,40),
                w: Math.round(el.getBoundingClientRect().width),
                h: Math.round(el.getBoundingClientRect().height)
            }));
        }
    """)
    for t in small_targets:
        issues.append({"type": "SMALL_TARGET", "severity": "warning",
                        "desc": f"Touch target too small ({t['w']}x{t['h']}px, min 44x44px)",
                        "detail": f"{t['tag']}: \"{t['text']}\""})

    # 10. Check color contrast manually for known problem areas
    contrast_checks = page.evaluate("""
        () => {
            const results = [];
            // Check ghost numbers (.svc-num, .step-num, decorative numbers)
            const ghostNums = document.querySelectorAll('.svc-num, .step-num, .inner-step-num, [class*="ghost"], [class*="num"]');
            ghostNums.forEach(el => {
                const style = window.getComputedStyle(el);
                results.push({
                    selector: el.className,
                    color: style.color,
                    bg: style.backgroundColor,
                    text: el.textContent.trim().substring(0,20)
                });
            });
            // Check LEARN MORE / svc-link
            const learnMore = document.querySelectorAll('.svc-link, .learn-more, [class*="learn"]');
            learnMore.forEach(el => {
                const style = window.getComputedStyle(el);
                results.push({
                    selector: el.className,
                    color: style.color,
                    bg: style.backgroundColor,
                    text: el.textContent.trim().substring(0,20)
                });
            });
            return results;
        }
    """)
    for c in contrast_checks:
        issues.append({"type": "CONTRAST_CHECK", "severity": "info",
                        "desc": f"Manual contrast check needed",
                        "detail": f"class='{c['selector']}' color={c['color']} bg={c['bg']} text='{c['text']}'"})

    # 11. Check for tabindex > 0 (anti-pattern)
    bad_tabindex = page.evaluate("""
        () => {
            return Array.from(document.querySelectorAll('[tabindex]'))
                .filter(el => parseInt(el.getAttribute('tabindex')) > 0)
                .map(el => ({ tag: el.tagName, tabindex: el.getAttribute('tabindex'), text: el.textContent.trim().substring(0,40) }));
        }
    """)
    for t in bad_tabindex:
        issues.append({"type": "POSITIVE_TABINDEX", "severity": "warning",
                        "desc": f"tabindex={t['tabindex']} disrupts natural tab order",
                        "detail": f"{t['tag']}: \"{t['text']}\""})

    # 12. Check for role="presentation" on interactive elements
    bad_roles = page.evaluate("""
        () => {
            return Array.from(document.querySelectorAll('[role="presentation"], [role="none"]'))
                .filter(el => ['A','BUTTON','INPUT','SELECT','TEXTAREA'].includes(el.tagName))
                .map(el => el.outerHTML.substring(0,100));
        }
    """)
    for r in bad_roles:
        issues.append({"type": "PRESENTATION_INTERACTIVE", "severity": "critical",
                        "desc": "Interactive element has role=presentation/none", "detail": r})

    # 13. Check viewport meta tag
    viewport = page.evaluate("""
        () => {
            const meta = document.querySelector('meta[name="viewport"]');
            if (!meta) return null;
            return meta.getAttribute('content');
        }
    """)
    if viewport and 'user-scalable=no' in viewport:
        issues.append({"type": "NO_ZOOM", "severity": "critical",
                        "desc": "Viewport meta disables user zoom (user-scalable=no) — violates WCAG 1.4.4"})
    if viewport and 'maximum-scale=1' in viewport:
        issues.append({"type": "NO_ZOOM", "severity": "critical",
                        "desc": "Viewport meta restricts zoom (maximum-scale=1) — violates WCAG 1.4.4"})

    # 14. Check for title element
    title = page.evaluate("() => document.title")
    if not title or title.strip() == '':
        issues.append({"type": "NO_TITLE", "severity": "critical",
                        "desc": "Page missing <title> element"})

    # 15. Check for main landmark
    main_landmark = page.evaluate("""
        () => {
            return !!(document.querySelector('main') || document.querySelector('[role="main"]'));
        }
    """)
    if not main_landmark:
        issues.append({"type": "NO_MAIN_LANDMARK", "severity": "warning",
                        "desc": "No <main> landmark element found"})

    # 16. Check nav landmark
    nav_landmark = page.evaluate("""
        () => !!(document.querySelector('nav') || document.querySelector('[role="navigation"]'))
    """)
    if not nav_landmark:
        issues.append({"type": "NO_NAV_LANDMARK", "severity": "warning",
                        "desc": "No <nav> landmark element found"})

    # 17. Check for duplicate IDs
    dup_ids = page.evaluate("""
        () => {
            const ids = Array.from(document.querySelectorAll('[id]')).map(el => el.id);
            const seen = {}, dups = [];
            ids.forEach(id => { if (seen[id]) dups.push(id); else seen[id] = true; });
            return [...new Set(dups)];
        }
    """)
    for did in dup_ids:
        issues.append({"type": "DUPLICATE_ID", "severity": "critical",
                        "desc": f"Duplicate ID: #{did}"})

    # 18. Check for aria-label on SVGs
    svgs_no_title = page.evaluate("""
        () => {
            return Array.from(document.querySelectorAll('svg'))
                .filter(svg => {
                    const role = svg.getAttribute('role');
                    const aria = svg.getAttribute('aria-label') || svg.getAttribute('aria-labelledby') || '';
                    const title = svg.querySelector('title');
                    const hidden = svg.getAttribute('aria-hidden');
                    return !hidden && !aria && !title;
                })
                .map(svg => svg.outerHTML.substring(0,100));
        }
    """)
    for svg in svgs_no_title:
        issues.append({"type": "SVG_NO_LABEL", "severity": "warning",
                        "desc": "SVG missing accessible label (aria-label, aria-labelledby, or <title>)",
                        "detail": svg[:80]})

    return issues


def severity_order(s):
    return {"critical": 0, "warning": 1, "info": 2}.get(s, 3)


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1440, "height": 900})

    for page_name, url in PAGES.items():
        print(f"\n{'='*60}")
        print(f"Auditing: {page_name}")
        print(f"URL: {url}")
        print('='*60)

        page = context.new_page()
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            time.sleep(2)

            # Run axe-core
            print("  Running axe-core...")
            axe_results = run_axe(page)

            # Run custom checks
            print("  Running custom checks...")
            custom_issues = run_custom_checks(page, url)

            results[page_name] = {
                "url": url,
                "axe_violations": axe_results.get("violations", []),
                "axe_incomplete": axe_results.get("incomplete", []),
                "custom_issues": sorted(custom_issues, key=lambda x: severity_order(x.get("severity","info")))
            }

            vcount = len(axe_results.get("violations", []))
            icount = len(axe_results.get("incomplete", []))
            ccount = len(custom_issues)
            print(f"  axe violations: {vcount}, incomplete: {icount}, custom: {ccount}")

        except Exception as e:
            print(f"  ERROR: {e}")
            results[page_name] = {"url": url, "error": str(e),
                                   "axe_violations": [], "axe_incomplete": [], "custom_issues": []}
        finally:
            page.close()

    browser.close()

# Save raw JSON results
out_path = Path("/home/ubuntu/dental-modern/audit_results.json")
out_path.write_text(json.dumps(results, indent=2))
print(f"\n\nRaw results saved to {out_path}")

# ── Generate human-readable report ────────────────────────────────────────────
print("\n\nGenerating report...")

report_lines = []
report_lines.append("# WCAG 2.1 AA Accessibility Audit Report")
report_lines.append("## Dental Solutions of South Florida")
report_lines.append(f"**Audit Date:** March 27, 2026  ")
report_lines.append(f"**Tool:** axe-core 4.9.1 + custom checks via Playwright  ")
report_lines.append(f"**Standard:** WCAG 2.1 Level AA  ")
report_lines.append(f"**Pages Audited:** {len(PAGES)}  ")
report_lines.append("")

# Summary table
report_lines.append("## Executive Summary")
report_lines.append("")
report_lines.append("| Page | axe Violations | axe Incomplete | Custom Issues (Critical) | Custom Issues (Warning) |")
report_lines.append("|------|---------------|----------------|--------------------------|------------------------|")

total_violations = 0
total_incomplete = 0
total_critical = 0
total_warning = 0

for page_name, data in results.items():
    v = len(data.get("axe_violations", []))
    i = len(data.get("axe_incomplete", []))
    ci = data.get("custom_issues", [])
    crit = sum(1 for x in ci if x.get("severity") == "critical")
    warn = sum(1 for x in ci if x.get("severity") == "warning")
    total_violations += v
    total_incomplete += i
    total_critical += crit
    total_warning += warn
    status = "✅" if v == 0 and crit == 0 else "❌"
    report_lines.append(f"| {status} {page_name} | {v} | {i} | {crit} | {warn} |")

report_lines.append(f"| **TOTAL** | **{total_violations}** | **{total_incomplete}** | **{total_critical}** | **{total_warning}** |")
report_lines.append("")

# Detailed findings
report_lines.append("---")
report_lines.append("")
report_lines.append("## Detailed Findings by Page")
report_lines.append("")

for page_name, data in results.items():
    report_lines.append(f"### {page_name}")
    report_lines.append(f"**URL:** {data['url']}  ")
    report_lines.append("")

    if "error" in data:
        report_lines.append(f"> ⚠️ **Error loading page:** {data['error']}")
        report_lines.append("")
        continue

    axe_v = data.get("axe_violations", [])
    axe_i = data.get("axe_incomplete", [])
    custom = data.get("custom_issues", [])

    if not axe_v and not axe_i and not custom:
        report_lines.append("✅ No violations detected.")
        report_lines.append("")
        continue

    # axe violations
    if axe_v:
        report_lines.append("#### axe-core Violations (WCAG Failures)")
        report_lines.append("")
        for v in axe_v:
            impact = v.get("impact", "unknown").upper()
            rule_id = v.get("id", "")
            desc = v.get("description", "")
            help_url = v.get("helpUrl", "")
            nodes = v.get("nodes", [])
            tags = ", ".join(v.get("tags", []))

            report_lines.append(f"**[{impact}] {rule_id}** — {desc}")
            report_lines.append(f"*WCAG criteria: {tags}*  ")
            if help_url:
                report_lines.append(f"*Reference: {help_url}*  ")
            report_lines.append(f"*Affected elements: {len(nodes)}*")
            if nodes:
                for node in nodes[:3]:  # show first 3 nodes
                    html_snip = node.get("html", "")[:120]
                    target = node.get("target", [])
                    fixes = node.get("failureSummary", "")[:200]
                    report_lines.append(f"  - `{html_snip}`")
                    if fixes:
                        report_lines.append(f"    Fix: {fixes}")
            report_lines.append("")

    # axe incomplete (needs manual review)
    if axe_i:
        report_lines.append("#### axe-core Incomplete (Needs Manual Review)")
        report_lines.append("")
        for v in axe_i[:5]:  # limit to 5
            impact = v.get("impact", "unknown").upper() if v.get("impact") else "REVIEW"
            rule_id = v.get("id", "")
            desc = v.get("description", "")
            nodes = v.get("nodes", [])
            report_lines.append(f"**[{impact}] {rule_id}** — {desc} ({len(nodes)} elements)")
            report_lines.append("")

    # Custom issues
    if custom:
        report_lines.append("#### Custom Checks")
        report_lines.append("")
        for issue in custom:
            sev = issue.get("severity", "info").upper()
            icon = {"CRITICAL": "🔴", "WARNING": "🟡", "INFO": "🔵"}.get(sev, "⚪")
            itype = issue.get("type", "")
            desc = issue.get("desc", "")
            detail = issue.get("detail", "")
            report_lines.append(f"{icon} **[{sev}] {itype}** — {desc}")
            if detail:
                report_lines.append(f"  - `{detail}`")
            report_lines.append("")

    report_lines.append("---")
    report_lines.append("")

# Consolidated issue list for fixing
report_lines.append("## Consolidated Fix List")
report_lines.append("")
report_lines.append("Issues ranked by severity and frequency across all pages:")
report_lines.append("")

# Aggregate axe violations across all pages
all_violations = {}
for page_name, data in results.items():
    for v in data.get("axe_violations", []):
        rid = v.get("id", "")
        if rid not in all_violations:
            all_violations[rid] = {
                "id": rid,
                "impact": v.get("impact", ""),
                "description": v.get("description", ""),
                "helpUrl": v.get("helpUrl", ""),
                "pages": [],
                "total_nodes": 0
            }
        all_violations[rid]["pages"].append(page_name)
        all_violations[rid]["total_nodes"] += len(v.get("nodes", []))

# Sort by impact then frequency
impact_order = {"critical": 0, "serious": 1, "moderate": 2, "minor": 3}
sorted_violations = sorted(all_violations.values(),
    key=lambda x: (impact_order.get(x["impact"], 4), -len(x["pages"])))

if sorted_violations:
    report_lines.append("### axe-core Violations (Unique Rules)")
    report_lines.append("")
    report_lines.append("| Impact | Rule ID | Description | Pages Affected | Total Elements |")
    report_lines.append("|--------|---------|-------------|----------------|----------------|")
    for v in sorted_violations:
        pages_str = ", ".join(v["pages"])
        report_lines.append(f"| {v['impact'].upper()} | {v['id']} | {v['description'][:60]} | {pages_str} | {v['total_nodes']} |")
    report_lines.append("")

# Aggregate custom issues
all_custom = {}
for page_name, data in results.items():
    for issue in data.get("custom_issues", []):
        itype = issue.get("type", "")
        sev = issue.get("severity", "info")
        if itype not in all_custom:
            all_custom[itype] = {"type": itype, "severity": sev, "desc": issue.get("desc",""), "pages": []}
        if page_name not in all_custom[itype]["pages"]:
            all_custom[itype]["pages"].append(page_name)

sorted_custom = sorted(all_custom.values(), key=lambda x: (severity_order(x["severity"]), -len(x["pages"])))
crit_custom = [x for x in sorted_custom if x["severity"] == "critical"]
warn_custom = [x for x in sorted_custom if x["severity"] == "warning"]

if crit_custom:
    report_lines.append("### Critical Custom Issues")
    report_lines.append("")
    report_lines.append("| Type | Description | Pages Affected |")
    report_lines.append("|------|-------------|----------------|")
    for c in crit_custom:
        report_lines.append(f"| {c['type']} | {c['desc']} | {', '.join(c['pages'])} |")
    report_lines.append("")

if warn_custom:
    report_lines.append("### Warning Custom Issues")
    report_lines.append("")
    report_lines.append("| Type | Description | Pages Affected |")
    report_lines.append("|------|-------------|----------------|")
    for c in warn_custom:
        report_lines.append(f"| {c['type']} | {c['desc']} | {', '.join(c['pages'])} |")
    report_lines.append("")

report_lines.append("---")
report_lines.append("")
report_lines.append("## WCAG 2.1 AA Criteria Reference")
report_lines.append("")
report_lines.append("| Criterion | Level | Description |")
report_lines.append("|-----------|-------|-------------|")
report_lines.append("| 1.1.1 | A | Non-text Content — all images need alt text |")
report_lines.append("| 1.3.1 | A | Info and Relationships — structure conveyed through markup |")
report_lines.append("| 1.4.3 | AA | Contrast (Minimum) — 4.5:1 for normal text, 3:1 for large text |")
report_lines.append("| 1.4.4 | AA | Resize Text — text resizable up to 200% without loss |")
report_lines.append("| 1.4.10 | AA | Reflow — content reflows at 320px width |")
report_lines.append("| 1.4.11 | AA | Non-text Contrast — UI components 3:1 contrast |")
report_lines.append("| 2.1.1 | A | Keyboard — all functionality via keyboard |")
report_lines.append("| 2.4.1 | A | Bypass Blocks — skip navigation link |")
report_lines.append("| 2.4.2 | A | Page Titled — descriptive page titles |")
report_lines.append("| 2.4.3 | A | Focus Order — logical focus sequence |")
report_lines.append("| 2.4.7 | AA | Focus Visible — keyboard focus indicator visible |")
report_lines.append("| 3.1.1 | A | Language of Page — html lang attribute |")
report_lines.append("| 4.1.1 | A | Parsing — no duplicate IDs, valid markup |")
report_lines.append("| 4.1.2 | A | Name, Role, Value — all UI components have accessible names |")
report_lines.append("")

report_text = "\n".join(report_lines)
report_path = Path("/home/ubuntu/dental-modern/accessibility_audit_report.md")
report_path.write_text(report_text)
print(f"Report saved to {report_path}")
print(f"\nSummary: {total_violations} axe violations, {total_critical} critical custom issues, {total_warning} warnings")
