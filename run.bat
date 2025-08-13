@echo off
chcp 65001 >nul
title HEAX Scanner
color 0A

echo.
echo ========================================
echo    ██╗  ██╗███████╗██╗  ██╗ █████╗     
echo    ██║  ██║██╔════╝╚██╗██╔╝██╔══██╗    
echo    ███████║█████╗   ╚███╔╝ ███████║    
echo    ██╔══██║██╔══╝   ██╔██╗ ██╔══██║    
echo    ██║  ██║███████╗██╔╝ ██╗██║  ██║    
echo    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    
echo.
echo ========================================
echo.

echo [*] Checking for Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed
    echo [INFO] Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo [*] Checking for required libraries...
python -c "import rich, colorama, pyfiglet" >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installing required libraries...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Failed to install libraries
        pause
        exit /b 1
    )
)

echo [*] Launching HEAX Scanner...
echo.
python heax_scanner.py

if errorlevel 1 (
    echo.
    echo [ERROR] An error occurred while running the tool
    pause
)

echo.
echo [INFO] Tool execution finished
pause


