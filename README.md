# Echo Bridge Manual 🎛️

A retro-styled documentation website for the Echo Bridge audio effects pedal by LUFS Audio. This repository contains a custom static site generator that transforms Markdown documentation into an animated webpage with auto-generated pedal diagrams.

![Echo Bridge Manual](https://img.shields.io/badge/LUFS_Audio-Echo_Bridge-78BEBA?style=flat-square)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/license-GPL-blue?style=flat-square)

## 🎨 Features

- **Markdown to HTML Conversion**: Write documentation in simple Markdown, get a professional website
- **Auto-Generated Pedal Diagrams**: JSON patch configurations automatically become visual diagrams
- **Retro DIY Aesthetic**: Flat design with pixelated elements and CRT-style effects
- **LUFS Brand Aligned**: Custom color palette and typography matching LUFS Audio branding
- **Animated Elements**: Floating shapes, pulsing backgrounds, and interactive hover effects
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Sticky Navigation**: Smart header that appears when scrolling
- **Retro Web Buttons**: Animated 88x31 buttons with blinking clouds and sparkle effects

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/danialrami/echo-bridge-manual
   cd echo-bridge-manual
   ```

2. **Edit your documentation**
   - Modify `Echo-Bridge.md` with your pedal documentation
   - Add patch configurations as JSON code blocks

3. **Build the site**
   ```bash
   ./build.sh
   ```

4. **Deploy**
   - Your `index.html` is ready for any static host
   - Push to any web server

## 📁 Project Structure

```
echo-bridge-manual/
├── Echo-Bridge.md          # Source documentation (Markdown)
├── template.html           # HTML template with placeholders
├── build_manual.py         # Python build script with diagram generation
├── build.sh               # Bash automation script
├── styles.css             # LUFS-branded styling
├── script.js              # Interactive animations
├── favicon.svg            # Echo Bridge logo
├── *-button.html          # Retro web buttons
├── fonts/                 # Custom typography
│   ├── HostGrotesk-*.woff/woff2
│   └── PublicSans-*.woff/woff2
├── venv/                  # Python virtual environment (auto-created)
└── index.html             # Generated output
```

## 🔧 How It Works

### Build Pipeline

1. **`build.sh`** - Orchestrates the build process
   - Creates/activates Python virtual environment
   - Installs dependencies (`markdown`, `beautifulsoup4`, `matplotlib`)
   - Runs the Python build script
   - Shows build status with colored output

2. **`build_manual.py`** - Core conversion logic
   - Reads `Echo-Bridge.md`
   - Converts Markdown to HTML
   - **Generates pedal diagrams from JSON configurations**
   - Extracts button HTML and CSS from `*-button.html` files
   - Injects content into `template.html`
   - Outputs final `index.html`

3. **Template System**
   - `{{MARKDOWN_CONTENT}}` - Converted documentation
   - `{{BUTTON_CONTENT}}` - Collected retro buttons
   - `{{FAVICON_SVG}}` - Logo injection

### Key Features

#### 🎨 Automatic Pedal Diagrams
The build script automatically converts JSON patch configurations into visual pedal diagrams:

```json
{
  "name": "Echo Bridge",
  "knobs": [0.35, 0.45, 0.25, 0.6, 0.4, 0.3],
  "switches": [0.5, 0.0, 0.5]
}
```

This becomes a full pedal diagram showing:
- Knob positions with percentage values
- Switch positions (UP/MID/DOWN)
- Professional pedal layout
- Patch name as title

#### Retro Button System
The build script automatically discovers and integrates any `*-button.html` files:
- Blinking cloud eyes (danialrami button)
- Floating animations
- Sparkle effects
- LUFS brand colors

#### Smart Styling
- Responsive tables with hover effects
- CRT-style text shadows for headers
- Pixelated rendering for retro feel
- LUFS color palette: teal, red, yellow, blue
- Custom fonts: Host Grotesk & Public Sans

#### Interactive Elements
- Floating geometric shapes in background
- Pulsing glow effects
- Smooth scroll animations
- Keyboard shortcuts (Ctrl+↑/↓)
- Dynamic year in copyright

## 🎯 Customization

### Adding New Patches
Simply add a JSON code block in your markdown:

```json
{
  "name": "Your Patch Name",
  "knobs": [0.5, 0.7, 0.3, 0.8, 0.4, 0.6],
  "switches": [0.0, 0.5, 1.0]
}
```

The build script will automatically generate a diagram!

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
- Code blocks and JSON patches
- Inline formatting

## 🚢 Deployment

### Option A: Simple Static Hosting
1. Run `./build.sh`
2. Upload `index.html` and assets to your host
3. Done!

### Required Files for Deployment
- `index.html` (generated)
- `styles.css`
- `script.js`
- `favicon.svg`
- `fonts/` directory

### Hosting Options
- **GitHub Pages**: Push to `gh-pages` branch
- **Netlify**: Drag and drop the folder
- **Vercel**: Connect your repo

## 🛠️ Development

### Prerequisites
- Python 3.6+
- Bash shell (macOS/Linux)
- Git

### Local Development
```bash
# First time setup
chmod +x build.sh
./build.sh

# Build after changes
./build.sh

# Open in browser
open index.html
```

### Virtual Environment
The build script automatically:
- Creates a Python virtual environment
- Installs required packages
- Activates/deactivates as needed
- No manual pip install required!

### Adding Features
1. Modify `template.html` for structure
2. Update `styles.css` for appearance
3. Enhance `script.js` for interactions
4. Adjust `build_manual.py` for new features

## 📝 Documentation Format

The `Echo-Bridge.md` file uses standard Markdown with special features:

### Control Tables
```markdown
| CONTROL | DESCRIPTION | NOTES |
| ------- | ----------- | ----- |
| KNOB 1  | Reverb Mix  | 0-100% wet signal |
```

### Patch Diagrams

```json
{
  "name": "Ambient Wash",
  "knobs": [0.8, 0.2, 0.3, 0.85, 0.7, 0.5],
  "switches": [0.0, 0.5, 0.0]
}
```

### Special Formatting
- **Bold** for control positions
- Links to external resources
- Nested lists with `<br/>` for complex notes

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the GNU General Public License (GPL) - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hardware**: [Hothouse](https://clevelandmusicco.com/hothouse-diy-digital-signal-processing-platform-kit/) by [Cleveland Music Co](https://github.com/clevelandmusicco)
- **Software**: Fork of [Flick effect](https://github.com/joulupukki/hothouse-effects/tree/main/src/Flick)
- **Platform**: Built on [Daisy Seed](https://electro-smith.com/products/daisy-seed?variant=45234245140772)
- **Design**: Inspired by 90s web aesthetics and DIY pedal culture

## 🎸 About Echo Bridge

Echo Bridge is a versatile reverb, tremolo, and delay pedal that started as an emulation of the bridge by Tandem but evolved into something more akin to a Strymon Flint plus delay. It's a fun, time-based multi-effect that can create everything from subtle ambience to experimental soundscapes.

### Current Patches
- **Echo Bridge**: The classic warm reverb with tremolo and delay
- **Plate-y Reverb**: Classic plate reverb emulation
- **Tremolo Delay**: Rhythmic, asynchronous pulsing textures
- **Ambient Wash**: Lush atmospheric soundscapes
- **Slapback Echo**: Quick punchy delays for indie and country

---

Built with ❤️ by LUFS Audio | [lufs.audio](https://lufs.audio)