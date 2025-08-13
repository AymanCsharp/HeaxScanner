#!/bin/bash

# الون
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # بدون لون

echo -e "${BLUE}"
echo "==============="
echo "   HEAX Scanner"
echo "==============="
echo -e "${NC}"

echo -e "${YELLOW}[*] Checking for Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR] Python3 is not installed${NC}"
    echo -e "${YELLOW}[INFO] Please install Python 3.8+${NC}"
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo -e "${BLUE}Ubuntu/Debian: sudo apt install python3 python3-pip${NC}"
        echo -e "${BLUE}CentOS/RHEL: sudo yum install python3 python3-pip${NC}"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo -e "${BLUE}macOS: brew install python3${NC}"
    fi
    exit 1
fi

PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo -e "${RED}[ERROR] Required Python version: 3.8+${NC}"
    echo -e "${YELLOW}[INFO] Current version: $PYTHON_VERSION${NC}"
    exit 1
fi

echo -e "${GREEN}[✓] Python $PYTHON_VERSION is installed${NC}"

echo -e "${YELLOW}[*] Checking for pip...${NC}"
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}[ERROR] pip3 is not installed${NC}"
    echo -e "${YELLOW}[INFO] Installing pip3...${NC}"
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt install python3-pip -y
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install python3
    fi
fi

echo -e "${GREEN}[✓] pip3 is installed${NC}"

echo -e "${YELLOW}[*] Checking for required libraries...${NC}"
python3 -c "import rich, colorama, pyfiglet" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}[INFO] Installing required libraries...${NC}"
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo -e "${RED}[ERROR] Failed to install libraries${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}[✓] All required libraries are installed${NC}"

echo -e "${YELLOW}[*] Launching HEAX Scanner...${NC}"
echo

export LANG=ar_SA.UTF-8
export LC_ALL=ar_SA.UTF-8

python3 heax_scanner.py

if [ $? -ne 0 ]; then
    echo
    echo -e "${RED}[ERROR] An error occurred while running the tool${NC}"
fi

echo
echo -e "${GREEN}[INFO] Tool execution finished${NC}"

