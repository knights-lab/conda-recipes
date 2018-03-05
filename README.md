# conda-recipes

# Updating a conda recipe
```
# First Update conda
conda update conda
# Change directory into recipes folder
# Build the recipe
cd recipes
conda build <tool>
# Upload the recipe
anaconda upload <location of tar bz2 from conda build> --user knights-lab
```
