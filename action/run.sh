#!/bin/bash
echo "I solemnly swear that I am up to no good."
current_branch=$(git branch --show-current)
export ACTION_CURRENT_BRANCH="${current_branch}"

timestamp=$(date +%s)
export ACTION_BRANCHNAME="dockerfile-updater/${timestamp}"

# Init git config
git config --local user.email "action@github.com"
git config --local user.name "GitHub Action"

# Crate new branch
git checkout -b "${ACTION_BRANCHNAME}"

# Execute action
python3 /action/run.py


# Push branch and create PR if needed
if [ -s changes ]; then
    git push "https://x-access-token:${INPUT_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" "${ACTION_BRANCHNAME}"
    python3 /action/create_pr.py
fi

# Set back the active branch
git checkout "${ACTION_CURRENT_BRANCH}"
echo "Mischief managed!"