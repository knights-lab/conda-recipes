#!/bin/bash
#!/bin/bash
binaries="\
burst12 \
burst15 \
"

for i in $binaries; do cp $i $PREFIX/bin/$i && chmod +x $PREFIX/bin/$i; done