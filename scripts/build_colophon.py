#!/usr/bin/env python3
"""
Build colophon.html with git commit metadata.
"""

import git
from datetime import datetime


def build_colophon():
    # Initialize git repo
    repo = git.Repo(".")

    # Get commits, limit to last 50 or so
    try:
        commits = list(repo.iter_commits(max_count=50))
    except (ValueError, git.GitCommandError):
        commits = []

    # Generate HTML list of commits
    commit_items = []
    for commit in commits:
        date = datetime.fromtimestamp(commit.committed_date).strftime("%Y-%m-%d")
        message = commit.message.strip().split("\n")[0]  # First line
        author = commit.author.name
        commit_items.append(
            f"<li><strong>{date}</strong> - {message} (by {author})</li>"
        )

    commits_html = "\n".join(commit_items)

    # HTML template
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colophon</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1 {{ color: #333; }}
        ul {{ list-style: none; padding: 0; }}
        li {{ margin: 10px 0; border-bottom: 1px solid #eee; padding-bottom: 5px; }}
    </style>
</head>
<body>
    <h1>Colophon</h1>
    <p>This page lists recent commits to the repository.</p>
    <ul>
{commits_html}
    </ul>
</body>
</html>"""

    # Write to colophon.html
    with open("colophon.html", "w") as f:
        f.write(html_template)

    print("colophon.html generated.")


if __name__ == "__main__":
    build_colophon()
