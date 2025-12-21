#!/usr/bin/env python3
"""
Update docs/index.md with navigation links.
Generates the main sections list from mkdocs.yml nav structure.
"""

import os
import yaml
from pathlib import Path

def get_nav_sections():
    """Extract top-level navigation sections from mkdocs.yml."""
    mkdocs_path = Path("mkdocs.yml")
    
    if not mkdocs_path.exists():
        print("Error: mkdocs.yml not found")
        return []
    
    with open(mkdocs_path, 'r') as f:
        config = yaml.safe_load(f)
    
    nav = config.get('nav', [])
    sections = []
    
    for item in nav:
        if isinstance(item, dict):
            for key, value in item.items():
                # Skip the "Docs" entry itself
                if key == "Docs":
                    continue
                    
                # Get the first page path for each section
                if isinstance(value, list) and len(value) > 0:
                    first_item = value[0]
                    if isinstance(first_item, dict):
                        first_page = list(first_item.values())[0]
                    else:
                        first_page = value
                    sections.append({
                        'title': key,
                        'path': first_page if isinstance(first_page, str) else first_page
                    })
    
    return sections

def get_section_description(title):
    """Get description for each section."""
    descriptions = {
        'Setup': 'setup and first patches',
        'Modules': 'module overviews and specs',
        'Specification': 'mechanical and electrical specifications',
        'Ecosystem': 'power, I/O, and system connectivity',
        'Tutorials': 'hands-on guides',
        'User Guide': 'techniques and best practices'
    }
    return descriptions.get(title, '')

def update_index():
    """Update docs/index.md with current navigation sections."""
    sections = get_nav_sections()
    
    if not sections:
        print("Warning: No sections found in navigation")
        return
    
    # Build the Start Here section
    start_here = "## Start Here\n\n"
    for section in sections:
        desc = get_section_description(section['title'])
        desc_text = f" — {desc}" if desc else ""
        start_here += f"- [{section['title']}]({section['path']}){desc_text}\n"
    
    # Full index content
    content = f"""# About MICRORACK

MICRORACK is a compact, affordable modular synthesizer system designed for learners, makers, and performers. This site holds the documentation, Specifications, and how-tos you need to build, patch, and integrate MICRORACK.

{start_here}
## Support

- FAQ: [microrack.org/faq](https://microrack.org/faq)
- Community: [Instagram](https://instagram.com/microrack)
- Help: [support@microrack.org](mailto:support@microrack.org)
"""
    
    # Write to index.md
    index_path = Path("docs/index.md")
    with open(index_path, 'w') as f:
        f.write(content)
    
    print(f"Updated docs/index.md with {len(sections)} sections")

if __name__ == "__main__":
    update_index()
