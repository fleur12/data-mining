"""
github_setup.py — Run this ONCE to initialize the git repo and connect to GitHub.

This file should ONLY setup Git connection.
It should NOT upload all practicals at once.

Steps it performs:
1. git init
2. git config
3. git remote add origin
4. git branch -M main

Then auto_push.py will handle one-by-one daily uploads.

Run:
python github_setup.py
"""

import subprocess
import os

# ──────────────────────────────────────────────
# 🔧 CONFIGURE THESE
# ──────────────────────────────────────────────

GITHUB_USERNAME = "fleur12"
REPO_NAME = "data-mining"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
LOCAL_REPO_PATH = r"C:/Users/Shruti/Downloads/data-mining"

# ──────────────────────────────────────────────

os.chdir(LOCAL_REPO_PATH)

remote_url = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"

commands = [
    ["git", "init"],
    ["git", "config", "user.email", f"{GITHUB_USERNAME}@users.noreply.github.com"],
    ["git", "config", "user.name", GITHUB_USERNAME],
    ["git", "remote", "add", "origin", remote_url],
    ["git", "branch", "-M", "main"],
]

for cmd in commands:
    display = " ".join(cmd).replace(GITHUB_TOKEN if GITHUB_TOKEN else "", "***TOKEN***")
    print(f"Running: {display}")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"  ⚠️  {result.stderr.strip()}")
    else:
        print("  ✅ Done")

print("\n🎉 GitHub connection setup complete!")
print("Now run: python auto_push.py")
print(f"Repository: https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")