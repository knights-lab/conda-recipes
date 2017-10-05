#!/bin/bash

$PYTHON setup.py install

# Add more build steps here, if they are necessary.
set -eu -o pipefail

binaries="\
shi7_trimmer \
gotta_split \
"

cd src/

make

mkdir ${PREFIX}/bin/

for i in $binaries; do cp $i $PREFIX/bin/$i && chmod +x $PREFIX/bin/$i; done

# See
# http://docs.continuum.io/conda/build.html
# for a list of environment variables that are set during the build process.