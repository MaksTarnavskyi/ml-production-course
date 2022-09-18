#!/bin/bash
set -euo pipefail

GIT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

docker build -t "maksymtarnavskyi/simple-app:$GIT_BRANCH" .
docker push "maksymtarnavskyi/simple-app:$GIT_BRANCH"
