#!/usr/bin/env bash

if [[ $# != 1 ]]; then
    echo "usage: $0 title"
    exit 0
fi

title="$1"
branch="$(date +%Y%m%d)-$title"

git checkout -b "$branch" master
git commit --allow-empty -m ":rocket: $branch"

read -p "git push -u origin \"$branch\" (y/N): " yn
if [[ $yn == "y" || $yn == "Y" ]]; then
    git push -u origin "$branch"
fi
