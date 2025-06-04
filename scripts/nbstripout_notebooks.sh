#!/usr/bin/env bash
# Copyright (c) 2016, wradlib developers.
# Distributed under the MIT License. See LICENSE.txt for more info.

# get notebooks list
notebooks=`find notebooks -path notebooks/*.ipynb_checkpoints -prune -o -name *.ipynb -print`
echo $notebooks

# convert notebooks to python scripts
for nb in $notebooks; do
    nbstripout --extra-keys "metadata.kernelspec cell.metadata.pycharm cell.metadata.tags" $nb
done
