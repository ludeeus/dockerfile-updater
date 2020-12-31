#!/bin/bash
set -e
echo "I solemnly swear that I am up to no good."
cd /github/workspace | exit 1
current_branch=$(git rev-parse --abbrev-ref HEAD)
export ACTION_CURRENT_BRANCH="${current_branch}"

timestamp=$(date +%s)
export ACTION_BRANCHNAME="dockerfile-updater/${timestamp}"

# Init git config
if [ ! -d ".git" ]; then
    git init
fi
git config --local user.email "action@github.com"
git config --local user.name "GitHub Action"

# Crate new branch
git checkout -b "${ACTION_BRANCHNAME}"

# Execute action
mkdir -p /github/workspace/somerandomstringthatdoesnotexsist
cp -r /action/* /github/workspace/somerandomstringthatdoesnotexsist/
set +e
python3 -m somerandomstringthatdoesnotexsist.run
if [ "$?" != "0" ]; then
    exit 1
fi
set -e

# Push branch and create PR if needed
if [ -s changes ]; then
    if [ -n ${INPUT_DISABLE_PR+x} ] || [ "${INPUT_DISABLE_PR}" = "false" ]; then
        git push "https://x-access-token:${INPUT_TOKEN}@github.com/${GITHUB_REPOSITORY}.git" "${ACTION_BRANCHNAME}"
        set +e
        python3 -m somerandomstringthatdoesnotexsist.create_pr
        if [ "$?" != "0" ]; then
            exit 1
        fi
        set -e
    fi
    else
        echo "Automatic PR disabled"
fi

rm -rf /github/workspace/somerandomstringthatdoesnotexsist

# Set back the active branch
git checkout "${ACTION_CURRENT_BRANCH}"
echo "Mischief managed!"