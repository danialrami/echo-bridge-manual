#!/usr/bin/env python3
"""
Build script for Echo Bridge Manual
Converts Markdown to styled HTML using template with button integration, favicon support, and diagram generation
"""

import os
import sys
import re
import json
import base64
from pathlib import Path
from io import BytesIO
import math

try:
    import markdown
    from bs4 import BeautifulSoup
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    USE_ENHANCED_PARSING = True
    print("✅ Using enhanced markdown parsing with full feature support")
except ImportError:
    USE_ENHANCED_PARSING = False
    print("⚠️  Required packages not found. Install with:")
    print("   pip install markdown beautifulsoup4 matplotlib")
    print("   Falling back to basic parsing...")

def create_pedal_diagram(patch_settings, patch_name="Patch"):
    """Generate pedal diagram with specific patch settings"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 12))
    ax.set_xlim(-200, 200)
    ax.set_ylim(-300, 300)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Pedal enclosure
    enclosure = patches.FancyBboxPatch(
        (-190, -290), 380, 580,
        boxstyle="round,pad=10",
        facecolor='#f8f8f8',
        edgecolor='#444',
        linewidth=4
    )
    ax.add_patch(enclosure)
    
    # Title
    ax.text(0, 250, patch_name, ha='center', va='center', 
           fontsize=16, weight='bold', color='#333')
    
    # Knob positions and settings
    knob_positions = [
        (-100, 100), (0, 100), (100, 100),    # Top row
        (-100, 20), (0, 20), (100, 20)        # Bottom row
    ]
    
    knob_labels = ['REVERB', 'TREM SPEED', 'TREM DEPTH',
                   'DELAY TIME', 'DELAY FB', 'DELAY MIX']
    
    # Draw knobs with patch-specific positions
    for i, (x, y) in enumerate(knob_positions):
        # Knob body
        knob = patches.Circle((x, y), 30, facecolor='white',
                            edgecolor='black', linewidth=2)
        ax.add_patch(knob)
        
        # Knob indicator (position based on patch settings)
        if patch_settings and i < len(patch_settings):
            # Convert 0-1 to -135 to +135 degrees
            angle = patch_settings[i] * 270 - 135
        else:
            angle = 0  # Default to 12 o'clock
            
        indicator_x = x + 22 * math.sin(math.radians(angle))
        indicator_y = y + 22 * math.cos(math.radians(angle))
        ax.plot([x, indicator_x], [y, indicator_y],
               color='#1a73e8', linewidth=4)
        
        # Value text (show the actual setting)
        if patch_settings and i < len(patch_settings):
            value_text = f"{int(patch_settings[i] * 100)}%"
            ax.text(x, y-5, value_text, ha='center', va='center',
                   fontsize=8, weight='bold', color='#1a73e8')
        
        # Label
        ax.text(x, y-60, knob_labels[i], ha='center', va='center',
               fontsize=10, weight='bold')
    
    # Switch positions (simplified representation)
    switch_positions = [(-100, -80), (0, -80), (100, -80)]
    switch_labels = ['REVERB MODE', 'TREM WAVE', 'MAKEUP GAIN']
    
    # Get switch settings from patch_settings if available
    switch_settings = patch_settings[6:9] if patch_settings and len(patch_settings) > 8 else [0.5, 0.5, 0.5]
    
    for i, (x, y) in enumerate(switch_positions):
        # Switch body
        switch = patches.Rectangle((x-15, y-10), 30, 20, 
                                 facecolor='#ddd', edgecolor='black', linewidth=1)
        ax.add_patch(switch)
        
        # Switch position indicator
        if switch_settings[i] < 0.33:
            pos_text = "UP"
            indicator_y = y + 5
        elif switch_settings[i] < 0.67:
            pos_text = "MID"
            indicator_y = y
        else:
            pos_text = "DOWN"
            indicator_y = y - 5
            
        ax.plot([x-10, x+10], [indicator_y, indicator_y], 
               color='#e74c3c', linewidth=3)
        
        # Label
        ax.text(x, y-35, switch_labels[i], ha='center', va='center',
               fontsize=9, weight='bold')
    
    # Footswitches
    footswitch_positions = [(-60, -200), (60, -200)]
    footswitch_labels = ['REVERB', 'DELAY/TREM']
    
    for i, (x, y) in enumerate(footswitch_positions):
        # Footswitch body
        footswitch = patches.Circle((x, y), 25, facecolor='#333',
                                  edgecolor='black', linewidth=2)
        ax.add_patch(footswitch)
        
        # LED indicator
        led = patches.Circle((x, y+35), 5, facecolor='#ff0000' if i == 0 else '#00ff00',
                           edgecolor='black', linewidth=1)
        ax.add_patch(led)
        
        # Label
        ax.text(x, y-45, footswitch_labels[i], ha='center', va='center',
               fontsize=10, weight='bold')
    
    # Convert to base64
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight', 
               facecolor='white', edgecolor='none')
    plt.close(fig)
    
    encoded = base64.b64encode(buf.getvalue()).decode('utf-8')
    return f'<img src="data:image/png;base64,{encoded}" alt="{patch_name} Diagram" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; margin: 20px 0;">'

def process_diagram_blocks(markdown_content):
    """
    Process diagram code blocks in markdown and replace them with generated diagrams
    
    Expected format:
    ```
    {
        "name": "Echo Bridge",
        "knobs": [0.3, 0.6, 0.4, 0.7, 0.5, 0.2],
        "switches": [0.5, 0.0, 1.0]
    }
    ```
    """
    if not USE_ENHANCED_PARSING:
        print("⚠️  Diagram generation requires matplotlib. Skipping diagrams.")
        return markdown_content
    
    # Pattern to match json code blocks that contain diagram configurations
    pattern = r'``````'
    
    def replace_diagram(match):
        try:
            # Parse the JSON configuration
            config_text = match.group(1).strip()
            config = json.loads(config_text)
            
            # Check if this is a diagram config (has required keys)
            if 'name' in config and 'knobs' in config:
                # Extract settings
                patch_name = config.get('name', 'Patch')
                knob_settings = config.get('knobs', [0.5] * 6)
                switch_settings = config.get('switches', [0.5] * 3)
                
                # Combine settings
                all_settings = knob_settings + switch_settings
                
                # Generate diagram
                diagram_html = create_pedal_diagram(all_settings, patch_name)
                
                print(f"✅ Generated diagram for: {patch_name}")
                return diagram_html
            else:
                # Not a diagram config, return original
                return match.group(0)
            
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing diagram config: {e}")
            return f'<p><em>Error: Invalid diagram configuration - {e}</em></p>'
        except Exception as e:
            print(f"❌ Error generating diagram: {e}")
            return f'<p><em>Error: Could not generate diagram - {e}</em></p>'
    
    # Replace all diagram blocks
    processed_content = re.sub(pattern, replace_diagram, markdown_content, flags=re.DOTALL)
    
    return processed_content

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
                head_styles = soup.head.find_all('style')
                for style in head_styles:
                    if style not in style_tags:
                        button_styles += f"\n/* Additional styles from {button_file.name} */\n"
                        button_styles += style.get_text()
        else:
            # Fallback to regex parsing
            pattern = r'<a[^>]*class=["\']webring-button["\'][^>]*>.*?</a>'
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                button_html = match.group(0)
            
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
    
    for file_path in Path('.').glob('*button*.html'):
        if file_path.name not in ['index.html', 'template.html']:
            button_files.append(file_path)
    
    if not button_files:
        print("No button HTML files found (looking for *button*.html)")
        return "", ""
    
    print(f"Found button files: {[f.name for f in button_files]}")
    
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
        
        favicon_svg = re.sub(r'<\?xml[^>]*\?>', '', favicon_svg).strip()
        
        if 'viewBox' not in favicon_svg and 'svg' in favicon_svg:
            width_match = re.search(r'width=["\']([^"\']+)["\']', favicon_svg)
            height_match = re.search(r'height=["\']([^"\']+)["\']', favicon_svg)
            
            if width_match and height_match:
                width = width_match.group(1)
                height = height_match.group(1)
                width = re.sub(r'[a-zA-Z%]+', '', width)
                height = re.sub(r'[a-zA-Z%]+', '', height)
                viewbox = f'viewBox="0 0 {width} {height}"'
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
        md = markdown.Markdown(extensions=[
            'tables',
            'fenced_code',
            'codehilite',
            'toc',
            'nl2br',
            'attr_list',
            'def_list',
            'footnotes',
            'md_in_html'
        ])
        return md.convert(markdown_content)
    else:
        return simple_markdown_to_html(markdown_content)

def simple_markdown_to_html(markdown_text):
    """
    Enhanced fallback markdown parser using only built-in Python libraries
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
            if in_table:
                html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
            html_lines.append(f'<h1>{html.escape(line[2:])}</h1>')
        elif line.startswith('## '):
            if in_table:
                html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
            html_lines.append(f'<h2>{html.escape(line[3:])}</h2>')
        elif line.startswith('### '):
            if in_table:
                html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
            html_lines.append(f'<h3>{html.escape(line[4:])}</h3>')
        elif line.startswith('#### '):
            if in_table:
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
            if line.startswith('#'):
                html_lines.append('</tbody>')
                html_lines.append('</table>')
                in_table = False
                if line.startswith('#### '):
                    html_lines.append(f'<h4>{html.escape(line[5:])}</h4>')
                elif line.startswith('### '):
                    html_lines.append(f'<h3>{html.escape(line[4:])}</h3>')
                elif line.startswith('## '):
                    html_lines.append(f'<h2>{html.escape(line[3:])}</h2>')
                elif line.startswith('# '):
                    html_lines.append(f'<h1>{html.escape(line[2:])}</h1>')
            else:
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
    """
    if not button_styles:
        return template_html
    
    style_tag = f"\n    <!-- Button Styles -->\n    <style>\n{button_styles}\n    </style>\n"
    
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
    """
    
    files_to_check = [markdown_file, template_file]
    for file_path in files_to_check:
        if not Path(file_path).exists():
            print(f"Error: {file_path} not found!")
            return False
    
    if not Path(css_file).exists():
        print(f"Warning: {css_file} not found - styling won't work!")
    
    try:
        # Read markdown content
        with open(markdown_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Process diagram blocks BEFORE converting to HTML
        markdown_content = process_diagram_blocks(markdown_content)
        
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
    
    markdown_file = "Echo-Bridge.md"
    template_file = "template.html"
    output_file = "index.html"
    css_file = "styles.css"
    favicon_file = "favicon.svg"
    
    if len(sys.argv) > 1:
        markdown_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    print("🔨 Building Echo Bridge Manual with Diagram Generation...")
    print(f"   Source: {markdown_file}")
    print(f"   Output: {output_file}")
    print()
    
    success = build_manual(markdown_file, template_file, output_file, css_file, favicon_file)
    
    if success:
        print()
        print("🚀 Ready to deploy! Your manual is ready at:", output_file)
        print()
        print("💡 Pro tip: Add more patches by creating new JSON code blocks!")
        print("   Each diagram will be automatically generated and embedded.")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
