#!/usr/bin/env python3
"""
Build script for Echo Bridge Manual
Converts Markdown to styled HTML using template with button integration and favicon support
"""

import os
import sys
import re
from pathlib import Path

try:
    import markdown
    from bs4 import BeautifulSoup
    USE_ENHANCED_PARSING = True
    print("✅ Using enhanced markdown parsing with full feature support")
except ImportError:
    USE_ENHANCED_PARSING = False
    print("⚠️  markdown and/or beautifulsoup4 not found. Install with:")
    print("   pip install markdown beautifulsoup4")
    print("   Falling back to basic parsing...")

def extract_button_content(button_file):
    """
    Extract button content AND styles from a button HTML file
    Returns a tuple of (button_html, button_styles)
    """
    try:
        with open(button_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        button_html = ""
        button_styles = ""
        
        if USE_ENHANCED_PARSING:
            # Use BeautifulSoup for robust HTML parsing
            soup = BeautifulSoup(content, 'html.parser')
            
            # Extract the button
            button = soup.find('a', class_='webring-button')
            if button:
                button_html = str(button)
            
            # Extract all style tags
            style_tags = soup.find_all('style')
            for style in style_tags:
                button_styles += f"\n/* Styles from {button_file.name} */\n"
                button_styles += style.get_text()
            
            # Also check for styles in the head that might be relevant
            if soup.head:
                # Look for any <style> tags we might have missed
                head_styles = soup.head.find_all('style')
                for style in head_styles:
                    if style not in style_tags:  # Avoid duplicates
                        button_styles += f"\n/* Additional styles from {button_file.name} */\n"
                        button_styles += style.get_text()
        else:
            # Fallback to regex parsing
            # Extract button
            pattern = r'<a[^>]*class=["\']webring-button["\'][^>]*>.*?</a>'
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                button_html = match.group(0)
            
            # Extract styles
            style_pattern = r'<style[^>]*>(.*?)</style>'
            style_matches = re.findall(style_pattern, content, re.DOTALL | re.IGNORECASE)
            for style_content in style_matches:
                button_styles += f"\n/* Styles from {button_file.name} */\n"
                button_styles += style_content
        
        if not button_html:
            print(f"Warning: No webring-button found in {button_file}")
        
        return button_html, button_styles
            
    except Exception as e:
        print(f"Warning: Could not read {button_file}: {e}")
        return "", ""

def collect_button_content():
    """
    Collect all button HTML files and combine their content and styles
    Returns a tuple of (combined_html, combined_styles)
    """
    button_files = []
    
    # Look for button HTML files in current directory
    for file_path in Path('.').glob('*button*.html'):
        if file_path.name not in ['index.html', 'template.html']:
            button_files.append(file_path)
    
    if not button_files:
        print("No button HTML files found (looking for *button*.html)")
        return "", ""
    
    print(f"Found button files: {[f.name for f in button_files]}")
    
    # Extract content from each button file
    all_buttons = []
    all_styles = []
    
    for button_file in sorted(button_files):
        button_html, button_styles = extract_button_content(button_file)
        if button_html:
            all_buttons.append(button_html)
        if button_styles:
            all_styles.append(button_styles)
    
    combined_html = '\n                '.join(all_buttons)
    combined_styles = '\n'.join(all_styles)
    
    return combined_html, combined_styles

def get_favicon_svg(favicon_file="favicon.svg"):
    """
    Load and prepare favicon SVG for insertion into template
    """
    if not Path(favicon_file).exists():
        print(f"Warning: {favicon_file} not found - using fallback text logo")
        return "LUFS"
    
    try:
        with open(favicon_file, 'r', encoding='utf-8') as f:
            favicon_svg = f.read()
        
        # Clean up the SVG (remove <?xml declaration if present)
        favicon_svg = re.sub(r'<\?xml[^>]*\?>', '', favicon_svg).strip()
        
        # Make sure it's properly sized for the logo containers
        # Add viewBox if missing and set width/height attributes
        if 'viewBox' not in favicon_svg and 'svg' in favicon_svg:
            # Try to extract existing width/height for viewBox
            width_match = re.search(r'width=["\']([^"\']+)["\']', favicon_svg)
            height_match = re.search(r'height=["\']([^"\']+)["\']', favicon_svg)
            
            if width_match and height_match:
                width = width_match.group(1)
                height = height_match.group(1)
                # Remove units if present (like px)
                width = re.sub(r'[a-zA-Z%]+', '', width)
                height = re.sub(r'[a-zA-Z%]+', '', height)
                viewbox = f'viewBox="0 0 {width} {height}"'
                
                # Insert viewBox into svg tag
                favicon_svg = re.sub(r'<svg([^>]*)', f'<svg {viewbox}\\1', favicon_svg)
        
        return favicon_svg
        
    except Exception as e:
        print(f"Warning: Could not process favicon: {e}")
        return "LUFS"

def convert_markdown_to_html(markdown_content):
    """
    Convert markdown to HTML using the best available method
    """
    if USE_ENHANCED_PARSING:
        # Use the full markdown library with extensions
        md = markdown.Markdown(extensions=[
            'tables',           # For your control tables
            'fenced_code',      # For code blocks
            'codehilite',       # For syntax highlighting
            'toc',              # Table of contents support
            'nl2br',            # Newline to <br> conversion
            'attr_list',        # For attribute lists
            'def_list',         # For definition lists
            'footnotes',        # For footnotes
            'md_in_html'        # For markdown inside HTML
        ])
        return md.convert(markdown_content)
    else:
        # Fallback to basic parsing
        return simple_markdown_to_html(markdown_content)

def simple_markdown_to_html(markdown_text):
    """
    Enhanced fallback markdown parser using only built-in Python libraries
    Improved to handle your specific markdown structure better
    """
    import html
    
    lines = markdown_text.split('\n')
    html_lines = []
    in_table = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if not line:
            if not in_table:
                html_lines.append('')
            i += 1
            continue
        
        # Headers
        if line.startswith('# '):
            if in_table:  # Close table if we're in one
                html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
            html_lines.append(f'<h1>{html.escape(line[2:])}</h1>')
        elif line.startswith('## '):
            if in_table:  # Close table if we're in one
                html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
            html_lines.append(f'<h2>{html.escape(line[3:])}</h2>')
        elif line.startswith('### '):
            if in_table:  # Close table if we're in one
                html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
            html_lines.append(f'<h3>{html.escape(line[4:])}</h3>')
        elif line.startswith('#### '):
            if in_table:  # Close table if we're in one
                html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
            html_lines.append(f'<h4>{html.escape(line[5:])}</h4>')
        
        # Tables
        elif '|' in line and not in_table:
            in_table = True
            table_headers = [cell.strip() for cell in line.split('|')[1:-1]]
            html_lines.append('<table>')
            html_lines.append('<thead>')
            html_lines.append('<tr>')
            for header in table_headers:
                html_lines.append(f'<th>{html.escape(header)}</th>')
            html_lines.append('</tr>')
            html_lines.append('</thead>')
            html_lines.append('<tbody>')
            
            # Skip separator line
            i += 1
            if i < len(lines) and '---' in lines[i]:
                i += 1
                continue
        
        elif '|' in line and in_table:
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            html_lines.append('<tr>')
            for cell in cells:
                formatted_cell = process_inline_formatting(cell)
                html_lines.append(f'<td>{formatted_cell}</td>')
            html_lines.append('</tr>')
        
        elif in_table and '|' not in line:
            # Check if this is a header that should close the table
            if line.startswith('#'):
                html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
                # Process this line as a header
                if line.startswith('#### '):
                    html_lines.append(f'<h4>{html.escape(line[5:])}</h4>')
                elif line.startswith('### '):
                    html_lines.append(f'<h3>{html.escape(line[4:])}</h3>')
                elif line.startswith('## '):
                    html_lines.append(f'<h2>{html.escape(line[3:])}</h2>')
                elif line.startswith('# '):
                    html_lines.append(f'<h1>{html.escape(line[2:])}</h1>')
            else:
                # Close table and continue with normal processing
                html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
                continue
        
        # Lists
        elif line.startswith('* ') or line.startswith('- '):
            if in_table:
                html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
            
            if i == 0 or not (lines[i-1].strip().startswith('* ') or lines[i-1].strip().startswith('- ')):
                html_lines.append('<ul>')
            
            list_content = process_inline_formatting(line[2:])
            html_lines.append(f'<li>{list_content}</li>')
            
            if i == len(lines) - 1 or not (i + 1 < len(lines) and (lines[i+1].strip().startswith('* ') or lines[i+1].strip().startswith('- '))):
                html_lines.append('</ul>')
        
        elif re.match(r'^\d+\. ', line):
            if in_table:
                html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
            
            if i == 0 or not re.match(r'^\d+\. ', lines[i-1].strip()):
                html_lines.append('<ol>')
            
            list_content = process_inline_formatting(re.sub(r'^\d+\. ', '', line))
            html_lines.append(f'<li>{list_content}</li>')
            
            if i == len(lines) - 1 or not (i + 1 < len(lines) and re.match(r'^\d+\. ', lines[i+1].strip())):
                html_lines.append('</ol>')
        
        # Regular paragraphs (only if not in table)
        elif not in_table:
            formatted_line = process_inline_formatting(line)
            html_lines.append(f'<p>{formatted_line}</p>')
        
        i += 1
    
    if in_table:
        html_lines.append('</tbody>')
        html_lines.append('</table>')
    
    return '\n'.join(html_lines)

def process_inline_formatting(text):
    """
    Process inline markdown formatting
    """
    import html
    
    text = html.escape(text)
    
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
    
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)
    
    # Code
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    
    # Links
    text = re.sub(r'\[([^\]]*)\]\(([^)]*)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'(https?://[^\s]+)', r'<a href="\1">\1</a>', text)
    
    return text

def inject_button_styles(template_html, button_styles):
    """
    Inject button styles into the HTML template
    Adds them right before the closing </head> tag
    """
    if not button_styles:
        return template_html
    
    # Create a style tag with all button styles
    style_tag = f"\n    <!-- Button Styles -->\n    <style>\n{button_styles}\n    </style>\n"
    
    # Find the closing head tag and inject styles before it
    head_close_index = template_html.rfind('</head>')
    if head_close_index != -1:
        return template_html[:head_close_index] + style_tag + template_html[head_close_index:]
    else:
        print("Warning: No </head> tag found in template. Button styles may not work correctly.")
        return template_html

def build_manual(
    markdown_file="Echo-Bridge.md",
    template_file="template.html", 
    output_file="index.html",
    css_file="styles.css",
    favicon_file="favicon.svg"
):
    """
    Build the manual by injecting markdown content into HTML template
    
    Args:
        markdown_file: Path to your markdown file
        template_file: Path to HTML template
        output_file: Path for generated HTML file
        css_file: Path to CSS file (for validation)
        favicon_file: Path to favicon SVG file
    """
    
    # Check if files exist
    files_to_check = [markdown_file, template_file]
    for file_path in files_to_check:
        if not Path(file_path).exists():
            print(f"Error: {file_path} not found!")
            return False
    
    # Warn if CSS file doesn't exist
    if not Path(css_file).exists():
        print(f"Warning: {css_file} not found - styling won't work!")
    
    try:
        # Read markdown content
        with open(markdown_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Convert markdown to HTML
        html_content = convert_markdown_to_html(markdown_content)
        
        # Read HTML template
        with open(template_file, 'r', encoding='utf-8') as f:
            template = f.read()
        
        # Collect button content and styles from separate HTML files
        button_html, button_styles = collect_button_content()
        
        # Get favicon SVG content
        favicon_svg = get_favicon_svg(favicon_file)
        
        # Replace placeholders
        final_html = template.replace('{{MARKDOWN_CONTENT}}', html_content)
        final_html = final_html.replace('{{BUTTON_CONTENT}}', button_html)
        final_html = final_html.replace('{{FAVICON_SVG}}', favicon_svg)
        
        # Inject button styles into the HTML
        final_html = inject_button_styles(final_html, button_styles)
        
        # Write output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        print(f"✅ Manual built successfully!")
        print(f"   📄 Markdown: {markdown_file}")
        print(f"   🌐 Output: {output_file}")
        print(f"   🎨 Styling: {css_file}")
        if button_html:
            print(f"   🔘 Buttons: Included from separate HTML files (with styles!)")
        if Path(favicon_file).exists():
            print(f"   🎯 Favicon: {favicon_file} integrated into logos")
        
        return True
        
    except Exception as e:
        print(f"Error building manual: {e}")
        return False

def main():
    """Main function with command line support"""
    
    # Default file names
    markdown_file = "Echo-Bridge.md"
    template_file = "template.html"
    output_file = "index.html"
    css_file = "styles.css"
    favicon_file = "favicon.svg"
    
    # Simple command line argument support
    if len(sys.argv) > 1:
        markdown_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    print("🔨 Building Echo Bridge Manual...")
    print(f"   Source: {markdown_file}")
    print(f"   Output: {output_file}")
    print()
    
    success = build_manual(markdown_file, template_file, output_file, css_file, favicon_file)
    
    if success:
        print()
        print("🚀 Ready to deploy! Your manual is ready at:", output_file)
        print()
        print("💡 Pro tip: Set up a file watcher or GitHub Action to auto-rebuild")
        print("   when you update your markdown file!")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()