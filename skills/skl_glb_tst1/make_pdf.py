"""Create a PDF from a text file. Used by the skl_glb_tst1 skill."""
import argparse
import os
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def pick_font():
    # Prefer a TTF font for broad Unicode coverage; fall back to Helvetica.
    for path in (r"C:\Windows\Fonts\arial.ttf",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                 "/Library/Fonts/Arial.ttf"):
        if os.path.exists(path):
            pdfmetrics.registerFont(TTFont("BodyFont", path))
            return "BodyFont"
    return "Helvetica"


def wrap(line, font, size, max_width):
    if not line:
        return [""]
    out, current = [], ""
    for word in line.split(" "):
        candidate = word if not current else current + " " + word
        if pdfmetrics.stringWidth(candidate, font, size) <= max_width:
            current = candidate
            continue
        if current:
            out.append(current)
        # Break words longer than the line width.
        while pdfmetrics.stringWidth(word, font, size) > max_width:
            i = len(word)
            while i > 1 and pdfmetrics.stringWidth(word[:i], font, size) > max_width:
                i -= 1
            out.append(word[:i])
            word = word[i:]
        current = word
    out.append(current)
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="UTF-8 text file with the content")
    p.add_argument("--outdir", default=os.getcwd())
    p.add_argument("--name", default=None)
    p.add_argument("--repeat", type=int, default=5, help="how many times to write the text, each on its own row")
    args = p.parse_args()

    with open(args.input, encoding="utf-8-sig") as f:
        text = f.read()
    # Write the text --repeat times, each copy starting on a new row.
    text = "\n".join([text.rstrip("\r\n")] * max(args.repeat, 1))

    name = args.name or f"skl_glb_tst1_{datetime.now():%Y%m%d_%H%M%S}.pdf"
    if not name.lower().endswith(".pdf"):
        name += ".pdf"
    out_path = os.path.abspath(os.path.join(args.outdir, name))

    font, size, leading, margin = pick_font(), 12, 16, 56
    width, height = A4
    c = canvas.Canvas(out_path, pagesize=A4)
    c.setFont(font, size)
    y = height - margin
    for raw in text.splitlines() or [""]:
        for line in wrap(raw, font, size, width - 2 * margin):
            if y < margin:
                c.showPage()
                c.setFont(font, size)
                y = height - margin
            c.drawString(margin, y, line)
            y -= leading
    c.save()
    print(out_path)


if __name__ == "__main__":
    main()
