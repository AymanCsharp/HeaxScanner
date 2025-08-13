#!/usr/bin/env python3
"""
HEAX Scanner - Quick Launch File
"""

import os
import sys
import subprocess
import time

def main():
    """Run the tool directly"""
    print(" HEAX Scanner...")

    try:
        if os.path.exists('heax_scanner.py'):
            subprocess.run([sys.executable, 'heax_scanner.py'])
        else:
            print(" File 'heax_scanner.py' not found")
            print(" Make sure you are in the correct directory")
    except Exception as e:
        print(f" Error during execution: {e}")
        print(" Try running 'quick_start.py' instead")

if __name__ == "__main__":
    main()

