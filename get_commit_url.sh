#!/bin/sh

# Get the latest commit hash
latest_commit=$(git rev-parse HEAD)

# Your GitHub repository URL
repo_url="https://github.com/DatCodeMania/GymTracker"

# Construct the commit URL
commit_url="${repo_url}/commit/${latest_commit}"

# Output the commit URL
echo $commit_url