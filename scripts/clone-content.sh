#!/bin/bash
# Clone external repositories for local development

echo "Cloning modules-test repository..."
if [ -d "modules" ]; then
    echo "modules directory already exists, pulling latest..."
    cd modules && git pull && cd ..
else
    git clone https://github.com/microrack/modules-test.git modules
fi

echo "Copying modules to docs/modules/..."
mkdir -p docs/modules
for dir in modules/mod-*/; do
    module=$(basename "$dir")
    echo "  Copying ${module}/"
    cp -r "$dir" "docs/modules/"
done

echo "Cloning specs-test repository..."
if [ -d "specification" ]; then
    echo "specification directory already exists, pulling latest..."
    cd specification && git pull && cd ..
else
    git clone https://github.com/microrack/specs-test.git specification
fi

echo "Copying specifications to docs/specification/..."
mkdir -p docs/specification
cp specification/mechanical.md docs/specification/
cp specification/electronical.md docs/specification/

echo ""
echo "Updating navigation with module list..."
python3 scripts/update_nav.py

echo "Updating index page with navigation sections..."
python3 scripts/update_index.py

echo ""
echo "Done! External content copied successfully."
echo "You can now run: mkdocs serve"
