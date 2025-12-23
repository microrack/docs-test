#!/usr/bin/env python3
"""
Update mkdocs.yml with module navigation entries.
Scans docs/modules/ for mod-* directories and updates the nav section.
Extracts H1 titles from README.md files for navigation labels.
"""

import yaml
import re
from pathlib import Path

def get_h1_title(readme_path):
    """Extract the first H1 title from a README.md file."""
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    # Remove the "# " prefix and return the title as-is
                    title = line[2:].strip()
                    return title
        return None
    except Exception:
        return None

def get_module_list():
    """Scan docs/modules for mod-* directories and extract titles."""
    modules_dir = Path("docs/modules")
    if not modules_dir.exists():
        return []
    
    modules = []
    for item in sorted(modules_dir.iterdir()):
        if item.is_dir() and item.name.startswith("mod-"):
            readme = item / "README.md"
            if readme.exists():
                title = get_h1_title(readme) or item.name
                modules.append((item.name, title))
    
    return modules

def update_mkdocs_yml():
    """Update mkdocs.yml with current module list."""
    mkdocs_path = Path("mkdocs.yml")
    
    if not mkdocs_path.exists():
        print("Error: mkdocs.yml not found")
        return
    
    # Read current content
    with open(mkdocs_path, 'r') as f:
        config = yaml.safe_load(f)
    
    if not config or 'nav' not in config:
        print("Error: nav section not found in mkdocs.yml")
        return
    
    # Get module list with titles
    modules = get_module_list()
    
    # Build modules nav section
    modules_nav = [{"Modules": "modules/index.md"}]
    for folder_name, title in modules:
        modules_nav.append({title: f"modules/{folder_name}/README.md"})
    
    # Find and update the Modules section in nav
    nav = config['nav']
    for i, item in enumerate(nav):
        if isinstance(item, dict) and 'Modules' in item:
            nav[i] = {'Modules': modules_nav}
            break
    else:
        print("Warning: Could not find Modules section in nav")
        return
    
    # Write back with proper YAML formatting
    with open(mkdocs_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print(f"Updated mkdocs.yml with {len(modules)} modules")

if __name__ == "__main__":
    update_mkdocs_yml()
