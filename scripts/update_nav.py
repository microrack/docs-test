#!/usr/bin/env python3
"""
Update mkdocs.yml with module navigation entries.
Scans docs/modules/ for mod-* directories and updates the nav section.
"""

import os
import re
from pathlib import Path

def get_module_list():
    """Scan docs/modules for mod-* directories."""
    modules_dir = Path("docs/modules")
    if not modules_dir.exists():
        return []
    
    modules = []
    for item in sorted(modules_dir.iterdir()):
        if item.is_dir() and item.name.startswith("mod-"):
            readme = item / "README.md"
            if readme.exists():
                modules.append(item.name)
    
    return modules

def update_mkdocs_yml():
    """Update mkdocs.yml with current module list."""
    mkdocs_path = Path("mkdocs.yml")
    
    if not mkdocs_path.exists():
        print("Error: mkdocs.yml not found")
        return
    
    # Read current content
    with open(mkdocs_path, 'r') as f:
        content = f.read()
    
    # Get module list
    modules = get_module_list()
    
    # Build modules nav section
    modules_nav = "  - Modules:\n    - Modules: modules/index.md\n"
    for module in modules:
        modules_nav += f"    - {module}: modules/{module}/README.md\n"
    
    # Replace the modules section in nav
    # Match from "  - Modules:" to the next top-level nav item
    pattern = r'  - Modules:.*?(?=\n  - [A-Z]|\nmarkdown_extensions:|\Z)'
    
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, modules_nav.rstrip(), content, flags=re.DOTALL)
    else:
        print("Warning: Could not find Modules section in nav")
        return
    
    # Write back
    with open(mkdocs_path, 'w') as f:
        f.write(content)
    
    print(f"Updated mkdocs.yml with {len(modules)} modules")

if __name__ == "__main__":
    update_mkdocs_yml()
