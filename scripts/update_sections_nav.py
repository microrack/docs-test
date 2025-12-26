#!/usr/bin/env python3
"""
Update mkdocs.yml navigation with Setup and Ecosystem sections from master branch.
Scans numbered folders (e.g., 10-safety, 20-power) and extracts H1 titles for nav entries.
Preserves folder sorting via numeric prefixes while using clean display titles.
"""

import os
import re
import yaml
from pathlib import Path

def get_h1_title(readme_path):
    """Extract the H1 title from a README.md file."""
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Match first H1 heading
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except Exception as e:
        print(f"  Warning: Could not read {readme_path}: {e}")
    
    return None

def folder_sort_key(folder_path):
    """Extract numeric prefix for sorting (e.g., '10-safety' -> 10)."""
    name = folder_path.name
    match = re.match(r'^(\d+)-', name)
    if match:
        return int(match.group(1))
    return 999  # Put non-numbered folders at the end

def get_section_items(section_dir, section_name):
    """Scan a section directory for numbered subdirectories and extract titles."""
    items = []
    
    if not section_dir.exists():
        print(f"Warning: {section_dir} does not exist")
        return items
    
    # Find all numbered directories (e.g., 10-safety, 20-power)
    numbered_dirs = [d for d in section_dir.iterdir() 
                     if d.is_dir() and re.match(r'^\d+-', d.name)]
    
    # Sort by numeric prefix
    for subdir in sorted(numbered_dirs, key=folder_sort_key):
        readme_path = subdir / "README.md"
        if not readme_path.exists():
            print(f"  Warning: No README.md in {subdir}")
            continue
        
        # Get title from H1
        title = get_h1_title(readme_path)
        if not title:
            # Fallback: convert folder name to title (remove number prefix)
            title = re.sub(r'^\d+-', '', subdir.name).replace('-', ' ').title()
        
        items.append({
            'title': title,
            'path': f"{section_name}/{subdir.name}/README.md"
        })
        print(f"  Found: {title} -> {subdir.name}")
    
    return items

def update_mkdocs_nav():
    """Update Setup and Ecosystem sections in mkdocs.yml."""
    mkdocs_path = Path("mkdocs.yml")
    
    if not mkdocs_path.exists():
        print("Error: mkdocs.yml not found")
        return False
    
    with open(mkdocs_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    nav = config.get('nav', [])
    
    # Process Setup section
    print("Scanning setup/...")
    setup_items = get_section_items(Path("docs/setup"), "setup")
    
    # Process Ecosystem section
    print("Scanning ecosystem/...")
    ecosystem_items = get_section_items(Path("docs/ecosystem"), "ecosystem")
    
    # Update nav sections
    for i, section in enumerate(nav):
        if isinstance(section, dict):
            if 'Setup' in section:
                # Build new Setup nav: Introduction first, then items, then System Setup
                setup_nav = [{'Introduction': 'index.md'}]
                for item in setup_items:
                    setup_nav.append({item['title']: item['path']})
                setup_nav.append({'System Setup': 'setup/README.md'})
                nav[i] = {'Setup': setup_nav}
                print(f"Updated Setup with {len(setup_items)} items")
                
            elif 'Ecosystem' in section:
                # Build new Ecosystem nav: Overview first, then items
                ecosystem_nav = [{'Ecosystem': 'ecosystem/README.md'}]
                for item in ecosystem_items:
                    ecosystem_nav.append({item['title']: item['path']})
                nav[i] = {'Ecosystem': ecosystem_nav}
                print(f"Updated Ecosystem with {len(ecosystem_items)} items")
    
    config['nav'] = nav
    
    # Write back with preserved formatting
    with open(mkdocs_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    return True

def main():
    print("Updating Setup and Ecosystem navigation...")
    
    if update_mkdocs_nav():
        print("\nSuccessfully updated mkdocs.yml")
    else:
        print("\nFailed to update mkdocs.yml")

if __name__ == "__main__":
    main()
