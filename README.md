# skl-glb-tst1

A Claude Code plugin with one skill: it takes text you supply and creates a PDF with that text written 5 times, each copy on its own row, saved in the current working directory.

## Requirements

- Python 3 with `reportlab`:

  ```bash
  pip install reportlab
  ```

## Install

This folder is both the plugin and a one-plugin marketplace (`yohai-ack-skills`).

From a local copy:

```
/plugin marketplace add ./skl-glb-tst1
/plugin install skl-glb-tst1@yohai-ack-skills
```

From GitHub:

```
/plugin marketplace add Yohai-ack/courseCloudPlugInTest
/plugin install skl-glb-tst1@yohai-ack-skills
```

Restart Claude Code (or run `/reload-plugins`) after installing.

## Usage

```
/skl_glb_tst1 Hello world
```

The namespaced form `/skl-glb-tst1:skl_glb_tst1 Hello world` also works.

Optional: ask for a specific filename, or a different repeat count (the script supports `--repeat N`).

## Layout

```
skl-glb-tst1/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── skills/
│   └── skl_glb_tst1/
│       ├── SKILL.md
│       └── make_pdf.py
└── README.md
```
