#!/bin/bash
set -e

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "uv is not installed. Please install uv first."
    exit 1
fi

# Sync dependencies
uv sync

# Run scripts
echo "Gathering links..."
uv run python scripts/gather_links.py

echo "Building index.html..."
uv run python scripts/build_index.py

echo "Building colophon.html..."
uv run python scripts/build_colophon.py

echo "Build complete."