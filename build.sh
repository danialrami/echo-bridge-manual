#!/bin/bash

# Echo Bridge Manual Build Script
# Handles virtual environment activation and package management

set -e # Exit on any error

echo "🔨 Echo Bridge Manual Builder"
echo "==============================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Project directory (where this script is located)
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$PROJECT_DIR/venv"

echo -e "${BLUE}📁 Project directory: $PROJECT_DIR${NC}"

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${YELLOW}⚠️  Virtual environment not found. Creating...${NC}"
    python3 -m venv "$VENV_DIR" --clear
    echo -e "${GREEN}✅ Virtual environment created${NC}"
fi

# Activate virtual environment
echo -e "${BLUE}🔄 Activating virtual environment...${NC}"
source "$VENV_DIR/bin/activate"

# Verify we're in the venv
if [[ "$VIRTUAL_ENV" == "$VENV_DIR" ]]; then
    echo -e "${GREEN}✅ Virtual environment activated${NC}"
    echo -e "${BLUE}   Python: $(which python)${NC}"
else
    echo -e "${RED}❌ Failed to activate virtual environment${NC}"
    exit 1
fi

# Check and install required packages
echo -e "${BLUE}📦 Checking required packages...${NC}"
PACKAGES_NEEDED=()

# Check for markdown
if ! python -c "import markdown" 2>/dev/null; then
    PACKAGES_NEEDED+=("markdown")
fi

# Check for beautifulsoup4
if ! python -c "from bs4 import BeautifulSoup" 2>/dev/null; then
    PACKAGES_NEEDED+=("beautifulsoup4")
fi

# Check for matplotlib
if ! python -c "import matplotlib.pyplot" 2>/dev/null; then
    PACKAGES_NEEDED+=("matplotlib")
fi

# Install missing packages
if [ ${#PACKAGES_NEEDED[@]} -gt 0 ]; then
    echo -e "${YELLOW}⚠️  Missing packages: ${PACKAGES_NEEDED[*]}${NC}"
    echo -e "${BLUE}📥 Installing missing packages...${NC}"
    pip install "${PACKAGES_NEEDED[@]}"
    echo -e "${GREEN}✅ Packages installed successfully${NC}"
else
    echo -e "${GREEN}✅ All required packages are already installed${NC}"
fi

# Verify packages are working
echo -e "${BLUE}🔍 Verifying package installation...${NC}"
if python -c "import markdown; from bs4 import BeautifulSoup; import matplotlib.pyplot; print('✅ All packages imported successfully')" 2>/dev/null; then
    echo -e "${GREEN}✅ Package verification successful${NC}"
else
    echo -e "${RED}❌ Package verification failed${NC}"
    exit 1
fi

# Run the build script
echo -e "${BLUE}🚀 Running build script...${NC}"
echo "==============================="

# Set PYTHONPATH to ensure local imports work
export PYTHONPATH="$PROJECT_DIR:$PYTHONPATH"

# Run the build script
if python "$PROJECT_DIR/build_manual.py"; then
    echo "==============================="
    echo -e "${GREEN}🎉 Build completed successfully!${NC}"
    echo -e "${BLUE}📄 Generated: index.html${NC}"
    
    # Check if index.html was created and show its size
    if [ -f "$PROJECT_DIR/index.html" ]; then
        SIZE=$(wc -c < "$PROJECT_DIR/index.html")
        echo -e "${BLUE}📊 File size: $SIZE bytes${NC}"
    fi
else
    echo -e "${RED}❌ Build failed${NC}"
    exit 1
fi

# Deactivate virtual environment
deactivate
echo -e "${GREEN}✅ Virtual environment deactivated${NC}"
echo -e "${GREEN}🏁 All done! Your manual is ready to deploy.${NC}"

# Optional: Open the manual in browser (uncomment if you want this)
# if command -v open &> /dev/null; then
#     echo -e "${BLUE}🌐 Opening manual in browser...${NC}"
#     open "$PROJECT_DIR/index.html"
# fi
