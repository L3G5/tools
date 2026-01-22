#!/usr/bin/env python3
"""
Build index.html from README.md, incorporating tool descriptions from .docs.md files.
"""

import markdown
import re
from gather_links import gather_links


def build_index():
    # Read README.md
    with open("README.md", "r") as f:
        readme_content = f.read()

    # Get tools metadata
    tools = gather_links()

    # Generate tools list in markdown
    tools_list = []
    for tool in tools:
        tools_list.append(f"- [{tool['name']}]({tool['html']}) - {tool['description']}")
    tools_md = "\n".join(tools_list)

    # Replace the placeholder in README.md
    # Assume the Tools section has a placeholder or we replace after ## Tools
    # For simplicity, replace the entire ## Tools section
    pattern = r"(## Tools\n).*?(\n## |\n$)"  # Match from ## Tools to next ## or end
    replacement = r"\1" + tools_md + r"\2"
    updated_readme = re.sub(pattern, replacement, readme_content, flags=re.DOTALL)

    # Convert to HTML
    html_body = markdown.markdown(updated_readme, extensions=["fenced_code"])

    # Wrap in HTML template
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tools Repository</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1, h2 {{ color: #333; }}
        ul {{ list-style: none; padding: 0; }}
        li {{ margin: 10px 0; }}
        a {{ text-decoration: none; color: #007acc; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
{html_body}
</body>
</html>"""

    # Write to index.html
    with open("index.html", "w") as f:
        f.write(html_template)

    print("index.html generated.")


if __name__ == "__main__":
    build_index()
