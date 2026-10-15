---
name: skl_glb_tst1
description: Create a PDF file containing text supplied by the user, written 5 times on separate rows, and save it in the current working directory. Use when the user invokes /skl_glb_tst1 followed by the text to put in the PDF.
---

# skl_glb_tst1 — text to PDF

The user calls this skill with the text they want in the PDF (the skill arguments).

## Steps

1. Take the text exactly as the user provided it (everything after `/skl_glb_tst1`). If no text was given, ask the user for it and stop.
2. Write the text to a temporary file in your scratchpad directory (UTF-8), so quoting/newlines are preserved.
3. Run the bundled script, with the current working directory as the output folder:

   ```bash
   python "${CLAUDE_PLUGIN_ROOT}/skills/skl_glb_tst1/make_pdf.py" --input "<temp text file>" --outdir "<current working directory>"
   ```

   The script writes the text 5 times, each copy on its own row (`--repeat N` changes the count).

   Optional: `--name <file.pdf>` if the user asked for a specific filename. Otherwise the script names it `skl_glb_tst1_<timestamp>.pdf`.
4. Report the full path of the created PDF to the user (as a clickable link).

## Notes

- Requires Python with `reportlab` (`pip install reportlab` if missing).
- Long lines are wrapped and pages are added automatically; blank lines are kept.
