# Installation Guide - HEAX Scanner

## Quick Installation

### Windows

```bash
# 1. Clone the project
git clone https://github.com/yourusername/heax-scanner.git
cd heax-scanner

# 2. Run the installer
run.bat

# Or run directly
python heax_scanner.py
```

### Linux/macOS

```bash
# 1. Clone the project
git clone https://github.com/yourusername/heax-scanner.git
cd heax-scanner

# 2. Give execution permission
chmod +x run.sh

# 3. Run the installer
./run.sh

# Or run directly
python3 heax_scanner.py
```

## Requirements

### Operating System

* **Windows**: Windows 10/11 (64-bit)
* **Linux**: Ubuntu 18.04+, CentOS 7+, RHEL 7+
* **macOS**: macOS 10.14+ (Mojave)

### Python

* **Version**: Python 3.8 or higher
* **Path**: Python must be in the system PATH

### Memory

* **Minimum**: 2 GB RAM
* **Recommended**: 4 GB RAM or more

### Disk Space

* **Minimum**: 500 MB free space
* **Recommended**: 1 GB free space

## Manual Installation

### 1. Install Python

#### Windows

```bash
# Download from official website
https://www.python.org/downloads/

# Or using Chocolatey
choco install python

# Or using winget
winget install Python.Python.3.11
```

#### Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

#### CentOS/RHEL

```bash
sudo yum install python3 python3-pip
# or
sudo dnf install python3 python3-pip
```

#### macOS

```bash
# Using Homebrew
brew install python3

# Or download from official website
https://www.python.org/downloads/macos/
```

### 2. Verify Installation

```bash
# Check Python version
python --version
# or
python3 --version

# Check pip
pip --version
# or
pip3 --version
```

### 3. Install Requirements

```bash
# Install all required packages
pip install -r requirements.txt

# or
pip3 install -r requirements.txt
```

### 4. Create Virtual Environment (optional)

```bash
# Create virtual environment
python -m venv heax_env

# Activate virtual environment
# Windows
heax_env\Scripts\activate

# Linux/macOS
source heax_env/bin/activate

# Install requirements inside virtual environment
pip install -r requirements.txt
```

## Troubleshooting

### Common Issues

#### 1. Python not installed

```bash
# Windows
echo %PATH%

# Linux/macOS
which python3
```

#### 2. Missing libraries

```bash
# Upgrade pip
pip install --upgrade pip

# Install specific library
pip install rich colorama pyfiglet

# Install with --user
pip install --user -r requirements.txt
```

#### 3. Permission issues

```bash
# Linux/macOS
sudo pip3 install -r requirements.txt

# Or create local folder
mkdir ~/.local/lib/python3.x/site-packages
export PYTHONPATH=~/.local/lib/python3.x/site-packages:$PYTHONPATH
```

#### 4. Compatibility issues

```bash
# Check Python version
python --version

# If version is less than 3.8
# Update Python
```

### Common Error Messages

#### ModuleNotFoundError

```bash
# Library not installed
pip install [library_name]

# Or upgrade pip
pip install --upgrade pip
```

#### PermissionError

```bash
# Use --user
pip install --user [library_name]

# Or use sudo (Linux/macOS)
sudo pip install [library_name]
```

#### ImportError

```bash
# Check library version
pip show [library_name]

# Reinstall library
pip uninstall [library_name]
pip install [library_name]
```

## Security Settings

### 1. Data Encryption

```ini
# in heax_config.ini
[SECURITY]
encryption_enabled = true
encryption_algorithm = AES-256
```

### 2. File Protection

```bash
# Linux/macOS
chmod 600 heax_config.ini
chmod 600 *.db

# Windows
# Use normal user permissions
```

### 3. Firewall

```bash
# Allow tool in firewall
# Windows: add exception in Windows Defender
# Linux: setup iptables
# macOS: security settings
```

## Installation Testing

### 1. Run the tool

```bash
python heax_scanner.py
# or
python3 heax_scanner.py
```

### 2. Run demo

```bash
python demo.py
# or
python3 demo.py
```

### 3. Run quick start

```bash
python quick_start.py
# or
python3 quick_start.py
```

## Updates

### 1. Update code

```bash
git pull origin main
```

### 2. Update libraries

```bash
pip install --upgrade -r requirements.txt
```

### 3. Update database

```bash
# The tool updates automatically
# or manually from menu
```

## Support

### 1. Technical issues

* **GitHub Issues**: report problems
* **Documentation**: FAQs
* **Troubleshooting**: problem solving

### 2. Security issues

* **Security Policy**: report vulnerabilities
* **Responsible Disclosure**: responsible reporting

### 3. General help

* **Discord**: discussions
* **Email**: direct support
* **Wiki**: detailed documents

## Installation Verification

### Checklist

* [ ] Python 3.8+ installed
* [ ] pip installed and working
* [ ] All libraries installed
* [ ] Tool runs without errors
* [ ] Database created
* [ ] Config files present

### Quick test

```bash
# 1. Check Python
python --version

# 2. Check libraries
python -c "import rich, colorama, pyfiglet; print('All libraries installed')"

# 3. Run the tool
python heax_scanner.py
```

## Next Steps

### 1. Read documentation

* Review `README.md` for features
* Read `heax_config.ini` for settings

### 2. Try the tool

* Run `demo.py` for demo
* Test scanning your local system

### 3. Customize

* Adjust settings as needed
* Add your scan targets

### 4. Explore features

* Explore all functions
* Try different scan types

---

**Congratulations! HEAX Scanner installed successfully**

You can now start using the advanced vulnerability scanning tool.

**Note:** Use the tool only on systems you own or have permission to scan.

