#!/bin/bash
binaries="\
burst12 \
burst15 \
"

mkdir $PREFIX/bin
for i in $binaries; do cp $i $PREFIX/bin/$i && chmod +x $PREFIX/bin/$i; done