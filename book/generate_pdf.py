#!/usr/bin/env python3
"""
Generate a PDF export for The Opportunity Mindset using fpdf2.
Run from workspace root: python3 book/generate_pdf.py
"""

import os, re, io, urllib.request
from pathlib import Path
from fpdf import FPDF
from PIL import Image as PILImage

# ── Constants ────────────────────────────────────────────────────────────────
# 8.5" × 11" in mm
PAGE_W  = 215.9
PAGE_H  = 279.4
MARGIN  = 25.4   # 1 inch

IMAGE_DIR = Path("/tmp/book_images")
IMAGE_DIR.mkdir(exist_ok=True)

# DejaVu Serif TTF paths (downloaded to /tmp)
FONT_DIR  = Path("/tmp/dejavu-fonts-ttf-2.37/ttf")
FONT_R    = str(FONT_DIR / "DejaVuSerif.ttf")
FONT_B    = str(FONT_DIR / "DejaVuSerif-Bold.ttf")
FONT_I    = str(FONT_DIR / "DejaVuSerif-Italic.ttf")
FONT_BI   = str(FONT_DIR / "DejaVuSerif-BoldItalic.ttf")

BOOK_FILES = [
    "book/01_preface.md",
    "book/02_introduction.md",
    "book/03_about.md",
] + [
    f"book/{str(i+4).zfill(2)}_chapter{str(i+1).zfill(2)}.md"
    for i in range(31)
] + [
    "book/35_conclusion.md",
    "book/36_appendix_a.md",
    "book/37_appendix_b.md",
    "book/38_appendix_c.md",
    "book/39_appendix_d.md",
    "book/40_appendix_e.md",
    "book/41_appendix_f.md",
    "book/42_bonus_resources.md",
]

# ── Image fetching ───────────────────────────────────────────────────────────
_IMG_CACHE = {}  # url -> Path or None

def fetch_image(url):
    """Download image and return a Path to a local JPEG, or None on failure."""
    if url in _IMG_CACHE:
        return _IMG_CACHE[url]
    safe = re.sub(r'[^a-zA-Z0-9]', '_', url)[-80:] + '.jpg'
    dest = IMAGE_DIR / safe
    if dest.exists():
        _IMG_CACHE[url] = dest
        return dest
    url_dl = re.sub(r'w=\d+', 'w=900', url)
    url_dl = re.sub(r'h=\d+', 'h=540', url_dl)
    try:
        req = urllib.request.Request(url_dl, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read()
        img = PILImage.open(io.BytesIO(raw))
        if img.mode not in ('RGB', 'L'):
            img = img.convert('RGB')
        img.save(str(dest), format='JPEG', quality=85)
        _IMG_CACHE[url] = dest
        return dest
    except Exception as e:
        print(f"    [warn] Could not fetch image: {url_dl} — {e}")
        _IMG_CACHE[url] = None
        return None

# ── Helpers ──────────────────────────────────────────────────────────────────
def strip_md(text):
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text

def prep_text(text):
    """Prepare text for fpdf2: strip links, convert bold to ** (fpdf2 markdown)."""
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)          # strip links
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'**\1**', text)      # bold+italic → bold
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'\1', text)  # strip *italic*
    text = re.sub(r'`(.+?)`', r'\1', text)                    # strip code
    return text

# ── PDF class ────────────────────────────────────────────────────────────────
class BookPDF(FPDF):
    def header(self):
        if self.page_no() <= 1:
            return
        self.set_font('DejaVu', 'I', 8)
        self.set_text_color(154, 128, 112)
        self.cell(0, 6, 'The Opportunity Mindset  \u00b7  Bernard Baah', align='C', new_x='LMARGIN', new_y='NEXT')
        self.set_draw_color(210, 195, 180)
        self.set_line_width(0.2)
        self.line(self.l_margin, self.get_y(), PAGE_W - self.r_margin, self.get_y())
        self.ln(3)

    def footer(self):
        self.set_y(-14)
        self.set_font('DejaVu', '', 9)
        self.set_text_color(154, 128, 112)
        self.cell(0, 6, str(self.page_no()), align='C')

# ── File processor ────────────────────────────────────────────────────────────
def process_file(pdf, filepath, is_first=False):
    if not is_first:
        pdf.add_page()

    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()

    list_items  = []
    table_rows  = []
    in_table    = False
    in_code     = False
    code_lines  = []

    def flush_list():
        nonlocal list_items
        if not list_items:
            return
        for item in list_items:
            clean = re.sub(r'^[\s\-\*\+]+', '', item).strip()
            clean = re.sub(r'^\d+\.\s+', '', clean)
            clean = prep_text(clean)
            pdf.set_font('DejaVu', '', 11)
            pdf.set_text_color(26, 26, 24)
            # Bullet + indented text
            pdf.set_x(pdf.l_margin + 2)
            pdf.cell(5, 6, '\xe2\x80\xa2'.encode('latin-1', 'replace').decode('latin-1'))
            pdf.set_x(pdf.l_margin + 8)
            try:
                pdf.multi_cell(
                    PAGE_W - 2 * MARGIN - 8, 6, clean,
                    markdown=True, new_x='LMARGIN', new_y='NEXT'
                )
            except Exception:
                pdf.multi_cell(
                    PAGE_W - 2 * MARGIN - 8, 6, strip_md(clean),
                    new_x='LMARGIN', new_y='NEXT'
                )
        list_items.clear()

    def flush_code():
        nonlocal code_lines
        if not code_lines:
            return
        pdf.set_font('DejaVu', '', 9)
        pdf.set_text_color(50, 50, 50)
        pdf.set_fill_color(244, 240, 235)
        for cl in code_lines:
            pdf.multi_cell(0, 5, cl, fill=True, new_x='LMARGIN', new_y='NEXT')
        pdf.ln(3)
        code_lines.clear()

    def flush_table():
        nonlocal table_rows
        if len(table_rows) < 2:
            table_rows.clear(); return
        headers = [c.strip() for c in table_rows[0].strip().strip('|').split('|')]
        data = [
            [c.strip() for c in r.strip().strip('|').split('|')]
            for r in table_rows[2:]
            if r.strip() and not re.match(r'^\|[-| :]+\|$', r.strip())
        ]
        if not headers:
            table_rows.clear(); return
        n = len(headers)
        col_w = (PAGE_W - 2 * MARGIN) / n
        # header
        pdf.set_font('DejaVu', 'B', 10)
        pdf.set_fill_color(28, 37, 51)
        pdf.set_text_color(240, 232, 216)
        for h in headers:
            pdf.cell(col_w, 7, strip_md(h)[:35], border=1, fill=True)
        pdf.ln()
        # rows
        pdf.set_font('DejaVu', '', 10)
        pdf.set_text_color(26, 26, 24)
        for ri, row in enumerate(data):
            fill = ri % 2 == 1
            if fill:
                pdf.set_fill_color(250, 247, 243)
            else:
                pdf.set_fill_color(255, 255, 255)
            for ci in range(n):
                cell_text = strip_md(row[ci])[:40] if ci < len(row) else ''
                pdf.cell(col_w, 6, cell_text, border=1, fill=True)
            pdf.ln()
        pdf.ln(4)
        table_rows.clear()

    def add_image(url, alt):
        path = fetch_image(url)
        if path:
            try:
                img = PILImage.open(str(path))
                text_w = PAGE_W - 2 * MARGIN
                aspect = img.height / img.width
                img_h = min(text_w * aspect, 75.0)  # cap at 75mm
                img_w = img_h / aspect if img_h == 75.0 else text_w
                if pdf.get_y() + img_h + 15 > PAGE_H - MARGIN:
                    pdf.add_page()
                x = (PAGE_W - img_w) / 2
                pdf.image(str(path), x=x, w=img_w, h=img_h)
                pdf.ln(2)
                if alt:
                    pdf.set_font('DejaVu', 'I', 9)
                    pdf.set_text_color(122, 102, 85)
                    pdf.multi_cell(0, 5, alt, align='C', new_x='LMARGIN', new_y='NEXT')
                    pdf.set_text_color(26, 26, 24)
                pdf.ln(4)
            except Exception as e:
                print(f"    [warn] Image embed failed: {e}")
                _placeholder(alt)
        else:
            _placeholder(alt)

    def _placeholder(alt):
        if alt:
            pdf.set_font('DejaVu', 'I', 9)
            pdf.set_text_color(170, 170, 170)
            pdf.multi_cell(0, 5, f'[Image: {alt}]', align='C', new_x='LMARGIN', new_y='NEXT')
            pdf.set_text_color(26, 26, 24)
            pdf.ln(2)

    # ── Main line loop ───────────────────────────────────────────────────────
    for line in lines:
        s = line.rstrip('\n')

        # Code fence
        if s.startswith('```'):
            if in_code:
                flush_code()
                in_code = False
            else:
                flush_list()
                flush_table(); in_table = False
                in_code = True
            continue

        if in_code:
            code_lines.append(s)
            continue

        # Table row
        if s.startswith('|') and '|' in s[1:]:
            flush_list()
            in_table = True
            table_rows.append(s)
            continue
        else:
            if in_table:
                flush_table()
                in_table = False

        # Blank line
        if not s.strip():
            flush_list()
            pdf.ln(3)
            continue

        # Heading
        hm = re.match(r'^(#{1,6})\s+(.+)', s)
        if hm:
            flush_list()
            level = len(hm.group(1))
            text  = strip_md(hm.group(2)).strip()
            pdf.set_text_color(28, 37, 51)
            if level == 1:
                if pdf.get_y() > PAGE_H * 0.65:
                    pdf.add_page()
                else:
                    pdf.ln(12)
                pdf.set_font('DejaVu', 'B', 22)
                pdf.multi_cell(0, 11, text, new_x='LMARGIN', new_y='NEXT')
                y = pdf.get_y() + 2
                pdf.set_draw_color(181, 74, 28)
                pdf.set_line_width(0.8)
                pdf.line(pdf.l_margin, y, PAGE_W - pdf.r_margin, y)
                pdf.set_line_width(0.2)
                pdf.ln(8)
            elif level == 2:
                pdf.ln(7)
                pdf.set_font('DejaVu', 'B', 16)
                pdf.multi_cell(0, 9, text, new_x='LMARGIN', new_y='NEXT')
                pdf.ln(3)
            elif level == 3:
                pdf.ln(5)
                pdf.set_font('DejaVu', 'B', 13)
                pdf.multi_cell(0, 7, text, new_x='LMARGIN', new_y='NEXT')
                pdf.ln(2)
            else:
                pdf.ln(3)
                pdf.set_font('DejaVu', 'B', 12)
                pdf.multi_cell(0, 7, text, new_x='LMARGIN', new_y='NEXT')
                pdf.ln(1)
            pdf.set_text_color(26, 26, 24)
            continue

        # Horizontal rule
        if re.match(r'^[-*_]{3,}$', s.strip()):
            pdf.ln(4)
            pdf.set_draw_color(200, 185, 170)
            pdf.set_line_width(0.3)
            pdf.line(pdf.l_margin, pdf.get_y(), PAGE_W - pdf.r_margin, pdf.get_y())
            pdf.ln(8)
            continue

        # Blockquote
        if s.startswith('>'):
            flush_list()
            content = strip_md(re.sub(r'^>\s*', '', s))
            bq_y = pdf.get_y()
            pdf.set_x(pdf.l_margin + 5)
            pdf.set_font('DejaVu', 'I', 11)
            pdf.set_text_color(90, 74, 58)
            pdf.multi_cell(PAGE_W - 2 * MARGIN - 5, 6.5, content,
                           new_x='LMARGIN', new_y='NEXT')
            bq_end = pdf.get_y()
            pdf.set_draw_color(181, 74, 28)
            pdf.set_line_width(1.5)
            pdf.line(pdf.l_margin, bq_y, pdf.l_margin, bq_end)
            pdf.set_line_width(0.2)
            pdf.set_text_color(26, 26, 24)
            pdf.ln(2)
            continue

        # List item
        if re.match(r'^(\s*[-*+]|\s*\d+\.)\s+', s):
            list_items.append(s)
            continue

        # Markdown image
        img_m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', s)
        if img_m:
            flush_list()
            add_image(img_m.group(2).strip(), img_m.group(1))
            continue

        # Regular paragraph
        flush_list()
        clean = prep_text(s)
        pdf.set_font('DejaVu', '', 12)
        pdf.set_text_color(26, 26, 24)
        try:
            pdf.multi_cell(0, 7, clean, markdown=True, new_x='LMARGIN', new_y='NEXT')
        except Exception:
            pdf.multi_cell(0, 7, strip_md(clean), new_x='LMARGIN', new_y='NEXT')
        pdf.ln(2)

    flush_list()
    if in_table:
        flush_table()
    if in_code:
        flush_code()


# ── Main ─────────────────────────────────────────────────────────────────────
def generate_pdf():
    print("Generating PDF (8.5\" × 11\")...")

    pdf = BookPDF()
    pdf.add_font('DejaVu', '',   FONT_R)
    pdf.add_font('DejaVu', 'B',  FONT_B)
    pdf.add_font('DejaVu', 'I',  FONT_I)
    pdf.add_font('DejaVu', 'BI', FONT_BI)
    pdf.set_margins(MARGIN, MARGIN, MARGIN)
    pdf.set_auto_page_break(auto=True, margin=MARGIN + 5)
    pdf.set_title('The Opportunity Mindset')
    pdf.set_author('Bernard Baah')

    # ── Title page ──────────────────────────────────────────────────────────
    pdf.add_page()
    pdf.ln(45)
    pdf.set_font('DejaVu', 'B', 32)
    pdf.set_text_color(28, 37, 51)
    pdf.multi_cell(0, 14, 'The\nOpportunity\nMindset', align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(10)
    pdf.set_font('DejaVu', 'I', 14)
    pdf.set_text_color(122, 102, 85)
    pdf.multi_cell(0, 8, 'How to Recognize, Create, and Capture Opportunity',
                   align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(22)
    # decorative rule
    cx = PAGE_W / 2
    pdf.set_draw_color(181, 74, 28)
    pdf.set_line_width(0.5)
    pdf.line(cx - 25, pdf.get_y(), cx + 25, pdf.get_y())
    pdf.ln(14)
    pdf.set_font('DejaVu', 'B', 16)
    pdf.set_text_color(181, 74, 28)
    pdf.multi_cell(0, 9, 'Bernard Baah', align='C', new_x='LMARGIN', new_y='NEXT')
    pdf.ln(4)
    pdf.set_font('DejaVu', '', 10)
    pdf.set_text_color(154, 128, 112)
    pdf.multi_cell(0, 6, 'FILLY CODER  \xb7  AI FUTURE SERIES',
                   align='C', new_x='LMARGIN', new_y='NEXT')

    # ── Chapters ────────────────────────────────────────────────────────────
    for idx, filepath in enumerate(BOOK_FILES):
        if not os.path.exists(filepath):
            print(f"  Skipping missing: {filepath}")
            continue
        print(f"  Adding: {filepath}")
        process_file(pdf, filepath, is_first=(idx == 0))

    out = Path("book/downloads") / "the-opportunity-mindset.pdf"
    pdf.output(str(out))
    size = out.stat().st_size / (1024 * 1024)
    print(f"\nPDF saved: {out} ({size:.1f} MB)")


if __name__ == '__main__':
    generate_pdf()
