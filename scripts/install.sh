#!/usr/bin/env bash
# Copyright (c) 2018, wradlib developers.
# Distributed under the MIT License. See LICENSE.txt for more info.

set -e

# print the vars
echo "TRAVIS_PULL_REQUEST " $TRAVIS_PULL_REQUEST
echo "TRAVIS_SECURE_ENV_VARS " $TRAVIS_SECURE_ENV_VARS
echo "TRAVIS_TAG " $TRAVIS_TAG ${TRAVIS_TAG:1}

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    -O miniconda.sh
chmod +x miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
export PATH=$HOME/miniconda/bin:$PATH

# Add conda-forge channel
conda config --add channels conda-forge
conda update --yes conda

# Create a testenv with the correct Python version
conda create -n wradlib --yes pip python=$PYTHON_VERSION
source activate wradlib

# Install wradlib dependencies
conda install --yes gdal numpy scipy matplotlib netcdf4 h5py deprecation xmltodict notebook nbconvert coverage

# PIP Install wradlib from git source branch
#pip install git+https://github.com/wradlib/wradlib.git@master

# Clone and Install wradlib from git source branch getting tag
git clone https://github.com/wradlib/wradlib.git $HOME/wradlib
cd $HOME/wradlib
export WRADLIB_TAG=`git name-rev --name-only --tags HEAD`
echo "WRADLIB_TAG " $WRADLIB_TAG
python setup.py install
cd $TRAVIS_BUILD_DIR

# Install wradlib-data
git clone https://github.com/wradlib/wradlib-data.git $HOME/wradlib-data

# print some stuff
python --version
pip --version

python -c "import wradlib; print(wradlib.__version__)"
python -c "import numpy; print(numpy.__version__)"
python -c "import numpy; print(numpy.__path__)"

