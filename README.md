# Tools Repository

A collection of lightweight web tools built with HTML, CSS, and JavaScript. Each tool is a self-contained HTML file with inline styles and scripts, designed for simplicity and ease of use. Tools are hosted on GitHub Pages and can be used offline.

This repository is inspired by [Simon Willison's tools repository](https://github.com/simonw/tools).

## Tools

<!-- Tool list will be maintained manually here. Scripts will parse this for index.html -->

- [Tool Name](tool-name.html) - Brief description from tool-name.docs.md
- Add more tools as they are created...

## Getting Started

- Open any `.html` file in your browser to use the tool.
- Tools are static and work offline.
- Contribute by adding new HTML files following the naming convention: `tool-name.html` with optional `tool-name.docs.md`.

## Building

To update `index.html` and `colophon.html`:

```bash
./scripts/build.sh
```

Requires `uv` for Python dependency management.
