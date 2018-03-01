#!/usr/bin/env bash
# Copyright (c) 2018, wradlib developers.
# Distributed under the MIT License. See LICENSE.txt for more info.

set -e

cd "$NOTEBOOKS_BUILD_DIR"

# print the vars
echo "TRAVIS_PULL_REQUEST " $TRAVIS_PULL_REQUEST
echo "TRAVIS_SECURE_ENV_VARS " $TRAVIS_SECURE_ENV_VARS
echo "TRAVIS_TAG " $TRAVIS_TAG ${TRAVIS_TAG:1}
echo "TRAVIS_BRANCH " $TRAVIS_BRANCH

# add, commit and push changes to devel branch
# if secure token is available.
if [ $TRAVIS_SECURE_ENV_VARS == 'true' ]; then

    git config --global user.email "wradlib-docs@wradlib.org"
    git config --global user.name "wradlib-docs-bot"
    rm -rf minconda.sh
    git add --all .
    git commit -m "Rendering at commit $TRAVIS_COMMIT"
    git branch render

    echo "Should push now"
    git push https://$GH_TOKEN@github.com/wradlib/wradlib-notebooks.git render:devel -fq
fi
