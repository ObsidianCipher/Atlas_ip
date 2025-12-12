#!/usr/bin/env bash
set -euo pipefail

# git_upload.sh - Interactive helper to create a new Git repo containing only the contents
# of the `atlas_ip/` directory and push them to a remote repository. This avoids pushing the
# entire top-level repo when you want the atlas_ip folder to be a standalone GitHub repo.
#
# Usage examples:
# 1) Push to an existing remote URL:
#    bash scripts/git_upload.sh --remote git@github.com:username/repo.git
# 2) Create using GitHub's HTTP remote (you will need to provide credentials or PAT):
#    bash scripts/git_upload.sh --remote https://github.com/username/repo.git
# 3) Use interactive prompts to provide details.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY_DIR="$ROOT_DIR"

usage() {
  cat <<'EOF'
Usage: bash scripts/git_upload.sh [--remote REMOTE_URL] [--repo-name REPO] [--branch BRANCH]
Options:
  --remote      Remote URL for the new repo (git@github.com:user/repo.git or https://...)
  --repo-name   If remote not provided, create name for remote but you must push manually
  --branch      Branch to push (default: main)
EOF
  exit 1
}

REMOTE_URL=""
REPO_NAME=""
BRANCH="main"

while [[ $# -gt 0 ]]; do
  case $1 in
    --remote)
      REMOTE_URL="$2"; shift 2;;
    --repo-name)
      REPO_NAME="$2"; shift 2;;
    --branch)
      BRANCH="$2"; shift 2;;
    -h|--help)
      usage;;
    *) echo "Unknown arg: $1"; usage;;
  esac
done

if [ -z "$REMOTE_URL" ] && [ -z "$REPO_NAME" ]; then
  read -p "Enter remote URL (git@github.com:user/repo.git or https://...) or press Enter to create a local repo: " REMOTE_URL
fi

TMP_DIR=$(mktemp -d)
echo "Creating temporary repo at $TMP_DIR..."
# Prefer rsync when available so we can exclude caches and pyc files.
if command -v rsync >/dev/null 2>&1; then
  rsync -a --exclude='__pycache__/' --exclude='*.pyc' "$PY_DIR/" "$TMP_DIR/"
else
  # Fallback to cp and then remove unwanted files.
  cp -r "$PY_DIR"/* "$TMP_DIR/"
  find "$TMP_DIR" -type d -name '__pycache__' -prune -exec rm -rf {} + 2>/dev/null || true
  find "$TMP_DIR" -type f -name '*.pyc' -delete 2>/dev/null || true
fi
cd "$TMP_DIR"

echo "Initializing git repository..."
git init
git add .
git config user.email "obsidianlogicalcipher@gmail.com" || true
git config user.name "ObsidianCipher" || true
git commit -m "Initial commit - atlas_ip project" || true
git branch -M "$BRANCH"

if [ -n "$REMOTE_URL" ]; then
  echo "Adding remote: $REMOTE_URL"
  git remote add origin "$REMOTE_URL"
  echo "Pushing to $REMOTE_URL on branch $BRANCH..."
  git push -u origin "$BRANCH"
  echo "Repo pushed to $REMOTE_URL"
else
  if [ -n "$REPO_NAME" ]; then
    echo "No remote provided - created local repository with name: $REPO_NAME"
  else
    echo "No remote provided - repository created locally at: $TMP_DIR"
  fi
fi

echo "Temporary repo at $TMP_DIR can be removed when no longer needed."
