#!/bin/bash
binaries="\
utree-search_gg \
utree-build_gg \
utree-compress \
"

for i in $binaries; do cp $i $PREFIX/bin/$i && chmod +x $PREFIX/bin/$i; done
