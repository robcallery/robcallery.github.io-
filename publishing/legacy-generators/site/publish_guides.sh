#!/bin/bash
# usage: publish_guides.sh "commit message"
set -e
S=/tmp/claude-0/-home-claude/9cac7207-2d1b-5bf4-969e-62974606aff5/scratchpad
cd /home/claude && python3 $S/guide.py >/dev/null && python3 $S/seo.py >/dev/null
python3 $S/chkg.py | sed 's/TRAVEL GUIDES · SNAPSHOT[0-9]*NOW SHOWING[^]]*//'
cd /home/claude/robcallery.github.io- && git fetch -q origin main && git reset -q --hard FETCH_HEAD && cp -r ../site/travel-guides . && cp ../site/sitemap.xml . && git add -A
git -c user.name="Rob Callery" -c user.email="robcallery@mail.com" commit -q -m "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01N6D2qveW6YYyaeGfyxncaB"
git push -q origin main; sha=$(git rev-parse HEAD)
for i in $(seq 40); do s=$(gh api "repos/robcallery/robcallery.github.io-/actions/runs?per_page=5" --jq ".workflow_runs[]|select(.head_sha==\"$sha\")|.status+\" \"+(.conclusion//\"\")" | head -1); [ "${s%% *}" = completed ] && echo "$s" && break; sleep 10; done
