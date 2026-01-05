#!/bin/bash
# Clone external repositories for local development

# 1. Fetch content from master branch (Setup, Ecosystem, index)
echo "Fetching master branch content..."
mkdir -p master-content
git archive master | tar -x -C master-content
cp master-content/README.md docs/index.md
rm -rf docs/setup docs/ecosystem
cp -r master-content/setup docs/
mv docs/setup/README.md docs/setup/index.md
cp -r master-content/ecosystem docs/
mv docs/ecosystem/README.md docs/ecosystem/index.md
rm -rf master-content
echo "  Copied Setup and Ecosystem from master"

echo "Cloning modules repository..."
if [ -d "modules-repo" ]; then
    echo "modules-repo directory already exists, pulling latest..."
    cd modules-repo && git pull && cd ..
else
    git clone https://github.com/microrack/modules.git modules-repo
fi

echo "Copying modules to docs/modules/..."
mkdir -p docs/modules
# Copy modules index page
cp modules-repo/README.md docs/modules/index.md
echo "  Copied index.md"
# Copy each module directory
for dir in modules-repo/mod-*/; do
    module=$(basename "$dir")
    echo "  Copying ${module}/"
    cp -r "$dir" "docs/modules/"
done

echo "Cloning specs repository..."
if [ -d "specs-repo" ]; then
    echo "specs-repo directory already exists, pulling latest..."
    cd specs-repo && git pull && cd ..
else
    git clone https://github.com/microrack/specs.git specs-repo
fi

echo "Copying specifications to docs/specification/..."
mkdir -p docs/specification
cp specs-repo/README.md docs/specification/index.md

# Copy mechanical folder (README.md + images)
mkdir -p docs/specification/mechanical
cp -r specs-repo/mechanical/* docs/specification/mechanical/
echo "  Copied mechanical spec"

# Copy electrical folder (README.md + images)
mkdir -p docs/specification/electrical
cp -r specs-repo/electrical/* docs/specification/electrical/
echo "  Copied electrical spec"

# Cleanup cloned repos to keep root clean
rm -rf modules-repo specs-repo
echo "  Cleaned up temporary repositories"

echo ""
echo "Updating navigation with sections..."
python3 scripts/update_sections_nav.py

echo "Updating navigation with module list..."
python3 scripts/update_nav.py

echo "Updating index page with navigation sections..."
python3 scripts/update_index.py

echo ""
echo "Done! External content copied successfully."
echo "You can now run: mkdocs serve"
