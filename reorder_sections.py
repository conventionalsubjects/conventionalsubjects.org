#!/usr/bin/env python3
"""Reorder HTML sections to match specification order"""
import re
import sys

def main():
    html_file = 'web/index.html'
    
    # Read the HTML file
    try:
        with open(html_file, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: {html_file} not found")
        sys.exit(1)
    
    # Extract all sections
    section_pattern = r'(      <section id="[^"]+">.*?      </section>)'
    sections_raw = re.findall(section_pattern, content, re.DOTALL)
    
    # Build a dict of section_id -> content
    sections = {}
    for section_html in sections_raw:
        id_match = re.search(r'<section id="([^"]+)">', section_html)
        if id_match:
            sections[id_match.group(1)] = section_html
    
    print(f"Found {len(sections)} sections: {list(sections.keys())}")
    
    # Define the correct order
    correct_order = [
        'purpose',
        'format',
        'example-inbox',
        'when-not',
        'tags',
        'due-dates',
        'anti-patterns',
        'best-practices',
        'ladder',
        'quick-ref',
        'getting-started'
    ]
    
    # Find where sections start in <main>
    main_match = re.search(r'(<main>)(.*?)(</main>)', content, re.DOTALL)
    if not main_match:
        print("ERROR: Could not find <main> tags")
        sys.exit(1)
    
    before_main = content[:main_match.start(2)]
    after_main = content[main_match.end(2):]
    
    # Rebuild sections in correct order
    new_sections = []
    for section_id in correct_order:
        if section_id in sections:
            new_sections.append(sections[section_id])
        else:
            print(f"WARNING: Section '{section_id}' not found!")
    
    # Join with double newline
    new_main_content = '\n\n'.join(new_sections)
    
    # Rebuild full content
    new_content = before_main + '\n' + new_main_content + '\n    ' + after_main
    
    # Write back
    with open(html_file, 'w') as f:
        f.write(new_content)
    
    print("\n✓ Sections reordered successfully!")
    print(f"New order: {' → '.join(correct_order)}")

if __name__ == '__main__':
    main()

