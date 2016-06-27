#!/bin/bash

$PYTHON setup.py install

# Add more build steps here, if they are necessary.

# See
# http://docs.continuum.io/conda/build.html
# for a list of environment variables that are set during the build process.
mkdir -p $PREFIX/bin

binaries="bin"

for f in $binaries/*; do cp $f $PREFIX/bin; done
chmod +x $PREFIX/bin/*
