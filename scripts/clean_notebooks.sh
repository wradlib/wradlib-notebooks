#!/usr/bin/env bash
# Copyright (c) 2019-2020, wradlib developers.
# Distributed under the MIT License. See LICENSE.txt for more info.

exit_status=0

notebooks=`find notebooks -path notebooks/*.ipynb_checkpoints -prune -o -name *.ipynb -print`

for nb in $notebooks; do
    jupyter nbconvert --ClearOutputPreprocessor.enabled=True --clear-output $nb
done

(( exit_status = ($? || $exit_status) ))

exit $exit_status
