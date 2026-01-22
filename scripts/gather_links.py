#!/usr/bin/env python3
"""
Gather metadata for tools in the repository.
Scans for .html files and their corresponding .docs.md files.
"""

import os
import glob
from pathlib import Path


def gather_links():
    """
    Returns a list of dicts with tool metadata.
    Each dict: {'name': 'tool-name', 'html': 'tool-name.html', 'docs': 'tool-name.docs.md', 'description': 'first line of docs.md'}
    """
    tools = []
    html_files = glob.glob("*.html")
    for html_file in html_files:
        if html_file in ["index.html", "colophon.html"]:  # Skip generated files
            continue
        base = Path(html_file).stem
        docs_file = f"{base}.docs.md"
        description = ""
        if os.path.exists(docs_file):
            with open(docs_file, "r") as f:
                first_line = f.readline().strip()
                description = first_line if first_line else f"Description for {base}"
        else:
            description = f"Tool: {base}"
        tools.append(
            {
                "name": base.replace("-", " ").title(),
                "html": html_file,
                "docs": docs_file,
                "description": description,
            }
        )
    return tools


if __name__ == "__main__":
    tools = gather_links()
    for tool in tools:
        print(f"- [{tool['name']}]({tool['html']}) - {tool['description']}")
