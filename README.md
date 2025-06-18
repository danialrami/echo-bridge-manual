# Echo Bridge Manual 🎛️

A professional, retro-styled documentation website for the Echo Bridge audio effects pedal by LUFS Audio. This repository contains a custom static site generator that transforms Markdown documentation into a beautifully branded, animated webpage.

![Echo Bridge Manual](https://img.shields.io/badge/LUFS_Audio-Echo_Bridge-78BEBA?style=flat-square)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/license-GPL-blue?style=flat-square)

## 🎨 Features

- **Markdown to HTML Conversion**: Write documentation in simple Markdown, get a professional website
- **Retro DIY Aesthetic**: Flat design with pixelated elements and CRT-style effects
- **LUFS Brand Aligned**: Custom color palette and typography matching LUFS Audio branding
- **Animated Elements**: Floating shapes, pulsing backgrounds, and interactive hover effects
- **Responsive Design**: Works beautifully on desktop, tablet, and mobile devices
- **Sticky Navigation**: Smart header that appears when scrolling
- **Retro Web Buttons**: Animated 88x31 buttons with blinking clouds and sparkle effects
- **Dynamic Copyright**: Auto-updates year without rebuilding

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/echo-bridge-manual.git
   cd echo-bridge-manual
   ```

2. **Edit your documentation**
   - Modify `Echo-Bridge.md` with your pedal documentation

3. **Build the site**
   ```bash
   ./build.sh
   ```

4. **Deploy**
   - Push to GitHub
   - Your `index.html` is ready for Hostinger or any static host

## 📁 Project Structure

```
echo-bridge/
├── Echo-Bridge.md          # Source documentation (Markdown)
├── template.html           # HTML template with placeholders
├── build_manual.py         # Python build script
├── build.sh               # Bash automation script
├── styles.css             # LUFS-branded styling
├── script.js              # Interactive animations
├── favicon.svg            # Echo Bridge logo
├── *-button.html          # Retro web buttons
├── fonts/                 # Custom typography
│   ├── HostGrotesk-*.ttf
│   └── PublicSans-*.ttf
└── index.html             # Generated output (git-ignored)
```

## 🔧 How It Works

### Build Pipeline

1. **`build.sh`** - Orchestrates the build process
   - Creates/activates Python virtual environment
   - Installs dependencies (`markdown`, `beautifulsoup4`)
   - Runs the Python build script

2. **`build_manual.py`** - Core conversion logic
   - Reads `Echo-Bridge.md`
   - Converts Markdown to HTML
   - Extracts button HTML and CSS from `*-button.html` files
   - Injects content into `template.html`
   - Outputs final `index.html`

3. **Template System**
   - `{{MARKDOWN_CONTENT}}` - Converted documentation
   - `{{BUTTON_CONTENT}}` - Collected retro buttons
   - `{{FAVICON_SVG}}` - Logo injection

### Key Features

#### Retro Button System
The build script automatically discovers and integrates any `*-button.html` files, extracting both HTML and CSS to preserve animations:
- Blinking cloud eyes
- Floating animations
- Sparkle effects
- LUFS brand colors

#### Smart Styling
- Responsive tables with hover effects
- CRT-style text shadows for headers
- Pixelated rendering for retro feel
- LUFS color palette: teal, red, yellow, blue

#### Interactive Elements
- Floating geometric shapes in background
- Pulsing glow effects
- Smooth scroll animations
- Keyboard shortcuts (Ctrl+↑/↓)

## 🎯 Customization

### Adding New Buttons
1. Create a new HTML file ending in `-button.html`
2. Include your button HTML and styles
3. Run build script - automatically integrated!

### Modifying Colors
Edit CSS variables in `styles.css`:
```css
:root {
    --lufs-teal: #78BEBA;
    --lufs-red: #D35233;
    --lufs-yellow: #E7B225;
    --lufs-blue: #2069af;
}
```

### Updating Documentation
Simply edit `Echo-Bridge.md` and rebuild. Supports:
- Tables with full styling
- Headers (h1-h4) with unique colors
- Lists, links, and emphasis
- Code blocks

## 🚢 Deployment

### Option A: Pre-built (Recommended)
1. Run `./build.sh`
2. Commit `index.html`
3. Push to GitHub
4. Configure Hostinger webhook

### Option B: Build on Deploy
1. Add `index.html` to `.gitignore`
2. Configure build process on server
3. Requires Python environment

### Required Files for Deployment
- `index.html` (generated)
- `styles.css`
- `script.js`
- `favicon.svg`
- `fonts/` directory

## 🛠️ Development

### Prerequisites
- Python 3.6+
- Bash shell
- Git

### Local Development
```bash
# Build and watch for changes
./build.sh

# Open in browser
open index.html
```

### Adding Features
1. Modify `template.html` for structure
2. Update `styles.css` for appearance
3. Enhance `script.js` for interactions
4. Adjust `build_manual.py` for new placeholders

## 📝 Documentation Format

The `Echo-Bridge.md` file uses standard Markdown with special attention to:
- Control tables with three columns
- Nested lists for sub-items
- Strong emphasis for control positions
- Links to external resources

Example:
```markdown
| CONTROL | DESCRIPTION | NOTES |
| ------- | ----------- | ----- |
| KNOB 1  | Reverb Mix  | 0-100% wet signal |
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the GNU General Public License (GPL) - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hardware**: Hothouse by [Cleveland Music Co](https://github.com/clevelandmusicco)
- **Software**: Fork of [Flick effect](https://github.com/joulupukki/hothouse-effects/tree/main/src/Flick)
- **Platform**: Built on Daisy Seed
- **Design**: Inspired by 90s web aesthetics and DIY pedal culture

## 🎸 About Echo Bridge

Echo Bridge is a versatile reverb, tremolo, and delay pedal that started as an emulation of the bridge by Tandem but evolved into something more akin to a Strymon Flint plus delay. It's a fun, time-based multi-effect that can create everything from subtle ambience to experimental soundscapes.

---

Built with ❤️ by LUFS Audio | [lufs.audio](https://lufs.audio)