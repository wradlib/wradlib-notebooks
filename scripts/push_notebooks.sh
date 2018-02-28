#!/usr/bin/env bash
# Copyright (c) 2016, wradlib developers.
# Distributed under the MIT License. See LICENSE.txt for more info.
# Adapted from the continuous_integration/push_notebooks.sh file from the pyart project
# https://github.com/ARM-DOE/pyart/

set -e

export PING_SLEEP=30s
export WORKDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export BUILD_OUTPUT=$WORKDIR/build.out

touch $BUILD_OUTPUT

dump_output() {
   echo Tailing the last 500 lines of output:
   tail -500 $BUILD_OUTPUT
}
error_handler() {
  echo ERROR: An error was encountered with the build.
  dump_output
  exit 1
}

# If an error occurs, run our error handler to output a tail of the build.
trap 'error_handler' ERR

# Set up a repeating loop to send some output to Travis.
bash -c "while true; do echo \$(date) - building ...; sleep $PING_SLEEP; done" &
PING_LOOP_PID=$!

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
    rm .travis.yml
    git add .
    git commit -m "Render notebooks"

    git log
    echo "Should push now"
    # git push https://$GH_TOKEN@github.com/wradlib/wradlib-notebooks.git devel -fq
fi

ls -lart
cd ..
ls -lart

# The build finished without returning an error so dump a tail of the output.
dump_output

# Nicely terminate the ping output loop.
kill $PING_LOOP_PID
rm -rf $BUILD_OUTPUT
