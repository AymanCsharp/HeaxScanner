#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HEAX Quick Start - Quick launcher for the tool
Quick Start for HEAX Scanner
"""

import os
import sys
import subprocess
import time

def print_banner():
    """Display the tool banner"""
    banner = """
     __    __                            
|  \  |  \                           
| ▓▓  | ▓▓ ______   ______  __    __ 
| ▓▓__| ▓▓/      \ |      \|  \  /  \
| ▓▓    ▓▓  ▓▓▓▓▓▓\ \▓▓▓▓▓▓\\▓▓\/  ▓▓
| ▓▓▓▓▓▓▓▓ ▓▓    ▓▓/      ▓▓ >▓▓  ▓▓ 
| ▓▓  | ▓▓ ▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓/  ▓▓▓▓\ 
| ▓▓  | ▓▓\▓▓     \\▓▓    ▓▓  ▓▓ \▓▓\
 \▓▓   \▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓   \▓▓
                                     
                                     
                                     

    """
    print(banner)

def check_python():
    """Check for Python installation"""
    print("Checking for Python...")
    try:
        result = subprocess.run(['python', '--version'], 
                              capture_output=True, text=True, check=True)
        version = result.stdout.strip()
        print(f"{version}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            result = subprocess.run(['python3', '--version'], 
                                  capture_output=True, text=True, check=True)
            version = result.stdout.strip()
            print(f"{version}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Python is not installed")
            print("Please install Python 3.8+ from https://python.org")
            return False

def install_requirements():
    """Install dependencies"""
    print("\nInstalling dependencies...")
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], 
                      check=True, capture_output=True)
        print("Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        try:
            subprocess.run(['pip3', 'install', '-r', 'requirements.txt'], 
                          check=True, capture_output=True)
            print("Dependencies installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("Failed to install dependencies")
            return False

def run_scanner():
    """Run the scanner tool"""
    print("\nLaunching HEAX Scanner...")
    try:
        subprocess.run(['python', 'heax_scanner.py'], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            subprocess.run(['python3', 'heax_scanner.py'], check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Failed to launch the tool")

def main():
    """Main function"""
    print_banner()
    
    print("Welcome to HEAX Scanner!")
    print("We will set up and launch the tool...")
    
    # Check Python
    if not check_python():
        input("\nPress Enter to exit...")
        return
    
    # Install requirements
    if not install_requirements():
        print("\nWarning: Some features may not work")
        time.sleep(2)
    
    # Show options
    print("\n" + "="*60)
    print("Launch options:")
    print("1. Launch main tool")
    print("2. Launch with custom settings")
    print("3. Show help")
    print("4. Exit")
    print("="*60)
    
    while True:
        try:
            choice = input("\nChoose an option (1-4): ").strip()
            
            if choice == "1":
                run_scanner()
                break
            elif choice == "2":
                print("Advanced features will be available soon...")
                time.sleep(2)
                run_scanner()
                break
            elif choice == "3":
                print_help()
            elif choice == "4":
                print("Thanks for using HEAX Scanner!")
                break
            else:
                print("Invalid option, please try again")
                
        except KeyboardInterrupt:
            print("\nTool stopped by user")
            break
        except Exception as e:
            print(f"Error: {e}")

def print_help():
    """Display help"""
    help_text = """
Quick Start Guide:

Main Features:
• Multi-network scanning
• AI-powered vulnerability detection
• Comprehensive detailed reports
• Integration with other security tools

Quick Usage:
1. Select "Launch main tool"
2. Choose the scan type
3. Enter the target (IP or range)
4. Wait for results

Requirements:
• Python 3.8+
• Internet connection
• Administrative privileges (optional)

Support:
• GitHub Issues
• Email Support
• Documentation

Legal Notice:
Use the tool only on systems you own or have permission to scan.
    """
    print(help_text)
    input("\nPress Enter to return...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTool stopped by user")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        input("\nPress Enter to exit...")


