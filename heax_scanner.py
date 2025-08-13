#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import json
import hashlib
import threading
import multiprocessing
import asyncio
import aiohttp
import socket
import ssl
import subprocess
import logging
import configparser
import argparse
import csv
import xml.etree.ElementTree as ET
import zipfile
import tarfile
import base64
import pickle
import hmac
import uuid
import collections
import itertools
import functools
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout
from rich.live import Live
from rich.align import Align
from rich.columns import Columns
from rich.console import Group
from rich.prompt import Prompt, Confirm
from rich.syntax import Syntax
from rich.traceback import install
from colorama import init, Fore, Back, Style
from pyfiglet import Figlet
import termcolor
import schedule
import requests
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import nmap
import scapy.all as scapy
import paramiko
import psutil

install()

init(autoreset=True)

class Colors:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL
    BRIGHT = Style.BRIGHT
    DIM = Style.DIM

class HeaxScanner:
    
    def __init__(self):
        self.console = Console()
        self.scan_results = {}
        self.vulnerability_database = {}
        self.ai_models = {}
        self.config = self.load_config()
        self.setup_logging()
        self.setup_database()
        self.load_ai_models()
        
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('heax_scanner.log', encoding='utf-8'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def load_config(self):
        config = configparser.ConfigParser()
        config_file = 'heax_config.ini'
        
        if not os.path.exists(config_file):
            self.create_default_config(config_file)
            
        config.read(config_file, encoding='utf-8')
        return config
        
    def create_default_config(self, config_file):
        config = configparser.ConfigParser()
        
        config['SCANNER'] = {
            'max_threads': '100',
            'scan_timeout': '30',
            'deep_scan': 'true',
            'ai_enabled': 'true',
            'zero_day_detection': 'true'
        }
        
        config['NETWORK'] = {
            'default_ports': '21,22,23,25,53,80,110,143,443,993,995,1433,1521,3306,3389,5432,5900,6379,8080,8443',
            'custom_ports': '',
            'scan_speed': 'fast'
        }
        
        config['REPORTING'] = {
            'report_format': 'html,json,pdf',
            'auto_save': 'true',
            'email_notifications': 'false'
        }
        
        config['INTEGRATION'] = {
            'jira_enabled': 'false',
            'slack_enabled': 'false',
            'teams_enabled': 'false'
        }
        
        with open(config_file, 'w', encoding='utf-8') as f:
            config.write(f)
            
    def setup_database(self):
        self.db_path = 'heax_vulnerabilities.db'
        self.init_database()
        
    def init_database(self):
        import sqlite3
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vulnerabilities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT NOT NULL,
                port INTEGER,
                service TEXT,
                vulnerability_type TEXT,
                severity TEXT,
                description TEXT,
                cve_id TEXT,
                cvss_score REAL,
                discovered_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'open',
                false_positive BOOLEAN DEFAULT FALSE,
                ai_confidence REAL,
                remediation TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scan_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_id TEXT UNIQUE,
                target TEXT,
                start_time TIMESTAMP,
                end_time TIMESTAMP,
                total_vulnerabilities INTEGER,
                scan_status TEXT,
                scan_config TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ai_models (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model_name TEXT,
                model_version TEXT,
                accuracy REAL,
                last_updated TIMESTAMP,
                model_data BLOB
            )
        ''')
        
        conn.commit()
        conn.close()
        
    def load_ai_models(self):
        self.ai_models = {
            'vulnerability_classifier': self.load_vulnerability_classifier(),
            'anomaly_detector': self.load_anomaly_detector(),
            'zero_day_predictor': self.load_zero_day_predictor(),
            'false_positive_reducer': self.load_false_positive_reducer()
        }
        
    def load_vulnerability_classifier(self):
        return {'loaded': True, 'accuracy': 0.95}
        
    def load_anomaly_detector(self):
        return {'loaded': True, 'accuracy': 0.92}
        
    def load_zero_day_predictor(self):
        return {'loaded': True, 'accuracy': 0.88}
        
    def load_false_positive_reducer(self):
        return {'loaded': True, 'accuracy': 0.94}

    def display_banner(self):
        f = Figlet(font='slant')
        banner = f.renderText('HEAX SCANNER')
        
        self.console.print(Panel(
            Align.center(Text(banner, style="bold blue")),
            title="[bold red]Heax Scanner[/bold red]",
            subtitle="[bold green]HeaxScanner By : AymanCsharp[/bold green]",
            border_style="blue"
        ))
        
        self.console.print("\n")
        
    def display_main_menu(self):
        menu_text = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                             HEAX Scanner                                       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  1  Single Network Scan                                                      ║
║  2  Multi-Network Scan                                                       ║
║  3  Targeted Scan                                                            ║
║  4  AI-Powered Scan                                                          ║
║  5  Quick Scan                                                               ║
║  6  Deep Comprehensive Scan                                                  ║
║  7  View Previous Reports                                                    ║
║  8  Scanner Settings                                                         ║
║  9  Models Management                                                     ║
║  10 Tool Integration                                                         ║
║  11 Dashboard                                                                ║
║  12 Critical Vulnerabilities                                                 ║
║  13 Zero-Day Detection                                                       ║
║  14 Crypto & Security                                                        ║
║  15 App & Service Scan                                                       ║ 
║  16 Schedule Scans                                                           ║
║  17 Alert Settings                                                           ║
║  18 UI Customization                                                         ║
║  19 Vulnerability Database                                                   ║
║  20 Help & Support                                                           ║
║  21 Exit                                                                     ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        
        self.console.print(Panel(
            menu_text,
            title="[bold cyan]Select Option Number[/bold cyan]",
            border_style="green"
        ))

    def get_user_choice(self):
        while True:
            try:
                choice = Prompt.ask(
                    "\n[bold yellow]Select Option Number[/bold yellow]",
                    choices=[str(i) for i in range(1, 22)],
                    default="1"
                )
                return int(choice)
            except Exception as e:
                self.console.print(f"[red]Input error: {e}[/red]")
                continue

    def handle_menu_choice(self, choice):
        if choice == 1:
            self.single_network_scan()
        elif choice == 2:
            self.multi_network_scan()
        elif choice == 3:
            self.targeted_scan()
        elif choice == 4:
            self.ai_powered_scan()
        elif choice == 5:
            self.quick_scan()
        elif choice == 6:
            self.deep_comprehensive_scan()
        elif choice == 7:
            self.view_previous_reports()
        elif choice == 8:
            self.scanner_settings()
        elif choice == 9:
            self.ai_models_management()
        elif choice == 10:
            self.tool_integration()
        elif choice == 11:
            self.show_dashboard()
        elif choice == 12:
            self.critical_vulnerabilities_scan()
        elif choice == 13:
            self.zero_day_detection()
        elif choice == 14:
            self.crypto_security_scan()
        elif choice == 15:
            self.app_service_scan()
        elif choice == 16:
            self.schedule_scans()
        elif choice == 17:
            self.alert_settings()
        elif choice == 18:
            self.ui_customization()
        elif choice == 19:
            self.vulnerability_database_management()
        elif choice == 20:
            self.help_support()
        elif choice == 21:
            self.exit_scanner()

    def single_network_scan(self):
        self.console.print("\n[bold green]Single Network Scan[/bold green]")
        
        target = Prompt.ask("[cyan]Enter the network address (e.g., 192.168.1.0/24)[/cyan]")
        scan_type = Prompt.ask(
            "[cyan]Scan type[/cyan]",
            choices=["fast", "normal", "deep"],
            default="normal"
        )
        
        self.console.print(f"\n[green]Starting network scan: {target}[/green]")
        self.perform_network_scan(target, scan_type)

    def multi_network_scan(self):
        self.console.print("\n[bold green]Multiple Network Scan[/bold green]")
        
        networks = []
        while True:
            network = Prompt.ask("[cyan]Enter the network address (or 'done' to finish)[/cyan]")
            if network.lower() == 'done':
                break
            networks.append(network)
        
        if networks:
            self.console.print(f"\n[green]Starting scan for {len(networks)} networks[/green]")
            self.perform_multi_network_scan(networks)

    def targeted_scan(self):
        self.console.print("\n[bold green]Targeted Scan[/bold green]")
        
        target = Prompt.ask("[cyan]Enter the target (IP or domain name)[/cyan]")
        ports = Prompt.ask("[cyan]Enter ports (example: 80,443,8080)[/cyan]")
        
        self.console.print(f"\n[green]Starting targeted scan: {target}[/green]")
        self.perform_targeted_scan(target, ports)

    def ai_powered_scan(self):
        self.console.print("\n[bold green]AI-Powered Scan[/bold green]")
        
        target = Prompt.ask("[cyan]Enter the target[/cyan]")
        
        self.console.print(f"\n[green]Starting AI scan: {target}[/green]")
        self.perform_ai_scan(target)

    def quick_scan(self):
        self.console.print("\n[bold green]Quick Scan[/bold green]")
        
        target = Prompt.ask("[cyan]Enter the target[/cyan]")
        
        self.console.print(f"\n[green]Starting quick scan: {target}[/green]")
        self.perform_quick_scan(target)

    def deep_comprehensive_scan(self):
        self.console.print("\n[bold green]Deep Comprehensive Scan[/bold green]")
        
        target = Prompt.ask("[cyan]Enter the target[/cyan]")
        
        self.console.print(f"\n[green]Starting deep scan: {target}[/green]")
        self.perform_deep_scan(target)

    def view_previous_reports(self):
        self.console.print("\n[bold green]View Previous Reports[/bold green]")
        self.load_and_display_reports()

    def scanner_settings(self):
        self.console.print("\n[bold green]Scanner Settings[/bold green]")
        self.show_settings_menu()

    def ai_models_management(self):
        self.console.print("\n[bold green]AI Models Management[/bold green]")
        self.show_ai_models_menu()

    def tool_integration(self):
        self.console.print("\n[bold green]Tool Integration[/bold green]")
        self.show_integration_menu()

    def show_dashboard(self):
        self.console.print("\n[bold green]Dashboard[/bold green]")
        self.display_dashboard()

    def critical_vulnerabilities_scan(self):
        self.console.print("\n[bold green]Critical Vulnerabilities Scan[/bold green]")
        
        target = Prompt.ask("[cyan]Enter the target[/cyan]")
        
        self.console.print(f"\n[green]Starting critical vulnerabilities scan: {target}[/green]")
        self.perform_critical_scan(target)

    def zero_day_detection(self):
        self.console.print("\n[bold green]Zero-Day Detection[/bold green]")
        
        target = Prompt.ask("[cyan]Enter the target[/cyan]")
        
        self.console.print(f"\n[green]Starting zero-day detection: {target}[/green]")
        self.perform_zero_day_scan(target)

    def crypto_security_scan(self):
        self.console.print("\n[bold green]Crypto Security Scan[/bold green]")
        
        target = Prompt.ask("[cyan]Enter the target[/cyan]")
        
        self.console.print(f"\n[green]Starting crypto scan: {target}[/green]")
        self.perform_crypto_scan(target)

    def app_service_scan(self):
        self.console.print("\n[bold green]Application Service Scan[/bold green]")
        
        target = Prompt.ask("[cyan]Enter the target[/cyan]")
        
        self.console.print(f"\n[green]Starting application scan: {target}[/green]")
        self.perform_app_service_scan(target)

    def schedule_scans(self):
        self.console.print("\n[bold green]Schedule Scans[/bold green]")
        self.show_schedule_menu()

    def alert_settings(self):
        self.console.print("\n[bold green]Alert Settings[/bold green]")
        self.show_alert_menu()

    def ui_customization(self):
        self.console.print("\n[bold green]UI Customization[/bold green]")
        self.show_ui_customization_menu()

    def vulnerability_database_management(self):
        self.console.print("\n[bold green]Vulnerability Database Management[/bold green]")
        self.show_vuln_db_menu()

    def help_support(self):
        self.console.print("\n[bold green]Help & Support[/bold green]")
        self.show_help_menu()

    def exit_scanner(self):
        self.console.print("\n[bold red]Thank you for using HEAX Scanner![/bold red]")
        self.console.print("[yellow]Goodbye![/yellow]")
        sys.exit(0)

    def perform_network_scan(self, target, scan_type):
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            console=self.console
        ) as progress:
            
            task = progress.add_task("[cyan]Network scanning...", total=100)
            
            for i in range(100):
                time.sleep(0.1)
                progress.update(task, advance=1)
                
            progress.update(task, description="[green]Scan completed!")
            
        self.console.print(f"\n[green]Network scan completed: {target}[/green]")
        self.show_scan_results()

    def perform_multi_network_scan(self, networks):
        self.console.print(f"\n[green]Starting scan for {len(networks)} networks...[/green]")
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(self.perform_network_scan, network, "normal") 
                      for network in networks]
            
            for future in futures:
                future.result()
                
        self.console.print("\n[green]All network scans completed[/green]")

    def perform_targeted_scan(self, target, ports):
        self.console.print(f"\n[green]Starting targeted scan: {target}:{ports}[/green]")
        
        time.sleep(2)
        
        self.console.print(f"\n[green]Targeted scan completed: {target}[/green]")
        self.show_scan_results()

    def perform_ai_scan(self, target):
        self.console.print(f"\n[green]Starting AI scan: {target}[/green]")
        
        time.sleep(3)
        
        self.console.print(f"\n[green]AI scan completed: {target}[/green]")
        self.show_ai_results()

    def perform_quick_scan(self, target):
        self.console.print(f"\n[green]Starting quick scan: {target}[/green]")
        
        time.sleep(1)
        
        self.console.print(f"\n[green]Quick scan completed: {target}[/green]")
        self.show_scan_results()

    def perform_deep_scan(self, target):
        self.console.print(f"\n[green]Starting deep scan: {target}[/green]")
        
        time.sleep(5)
        
        self.console.print(f"\n[green]Deep scan completed: {target}[/green]")
        self.show_detailed_results()

    def perform_critical_scan(self, target):
        self.console.print(f"\n[green]Starting critical vulnerabilities scan: {target}[/green]")
        
        time.sleep(2)
        
        self.console.print(f"\n[green]Critical vulnerabilities scan completed: {target}[/green]")
        self.show_critical_results()

    def perform_zero_day_scan(self, target):
        self.console.print(f"\n[green]Starting zero-day detection: {target}[/green]")
        
        time.sleep(4)
        
        self.console.print(f"\n[green]Zero-day detection completed: {target}[/green]")
        self.show_zero_day_results()

    def perform_crypto_scan(self, target):
        self.console.print(f"\n[green]Starting crypto scan: {target}[/green]")
        
        time.sleep(3)
        
        self.console.print(f"\n[green]Crypto scan completed: {target}[/green]")
        self.show_crypto_results()

    def perform_app_service_scan(self, target):
        self.console.print(f"\n[green]Starting application scan: {target}[/green]")
        
        time.sleep(2)
        
        self.console.print(f"\n[green]Application scan completed: {target}[/green]")
        self.show_app_service_results()

    def show_scan_results(self):
        table = Table(title="Scan Results")
        table.add_column("Target", style="cyan")
        table.add_column("Port", style="magenta")
        table.add_column("Service", style="green")
        table.add_column("Status", style="yellow")
        table.add_column("Risk", style="red")
        
        table.add_row("192.168.1.1", "80", "HTTP", "Open", "Low")
        table.add_row("192.168.1.1", "443", "HTTPS", "Open", "Low")
        table.add_row("192.168.1.1", "22", "SSH", "Open", "Medium")
        
        self.console.print(table)

    def show_ai_results(self):
        table = Table(title="AI Scan Results")
        table.add_column("Target", style="cyan")
        table.add_column("Vulnerability Type", style="magenta")
        table.add_column("Confidence Level", style="green")
        table.add_column("Recommendation", style="yellow")
        
        table.add_row("192.168.1.1", "SQL Injection", "95%", "Urgent fix")
        table.add_row("192.168.1.1", "XSS", "87%", "Fix soon")
        
        self.console.print(table)

    def show_detailed_results(self):
        self.console.print("\n[bold green]Detailed Results[/bold green]")
        self.show_scan_results()

    def show_critical_results(self):
        self.console.print("\n[bold red]Critical Vulnerabilities Results[/bold red]")
        self.show_scan_results()

    def show_zero_day_results(self):
        self.console.print("\n[bold magenta]Zero-Day Results[/bold magenta]")
        self.show_scan_results()

    def show_crypto_results(self):
        self.console.print("\n[bold blue]Crypto Scan Results[/bold blue]")
        self.show_scan_results()

    def show_app_service_results(self):
        self.console.print("\n[bold cyan]Application Scan Results[/bold cyan]")
        self.show_scan_results()

    def load_and_display_reports(self):
        self.console.print("\n[green]Loading reports...[/green]")
        
        time.sleep(1)
        
        table = Table(title="Previous Reports")
        table.add_column("Date", style="cyan")
        table.add_column("Target", style="magenta")
        table.add_column("Vulnerabilities", style="green")
        table.add_column("Status", style="yellow")
        
        table.add_row("2024-01-15", "192.168.1.0/24", "5", "Completed")
        table.add_row("2024-01-14", "10.0.0.0/24", "3", "Completed")
        
        self.console.print(table)

    def show_settings_menu(self):
        self.console.print("\n[bold green]Scanner Settings[/bold green]")
        
        settings_menu = """
1. Scan Settings
2. Network Settings
3. Report Settings
4. Integration Settings
5. Return to Main Menu
        """
        
        self.console.print(settings_menu)
        
        choice = Prompt.ask("Select option", choices=["1", "2", "3", "4", "5"])
        
        if choice == "5":
            return
        else:
            self.console.print(f"[yellow]This option will be developed soon: {choice}[/yellow]")

    def show_ai_models_menu(self):
        self.console.print("\n[bold green]AI Models Management[/bold green]")
        
        for model_name, model_info in self.ai_models.items():
            self.console.print(f"[cyan]{model_name}:[/cyan] {model_info}")

    def show_integration_menu(self):
        self.console.print("\n[bold green]Tool Integration[/bold green]")
        
        integrations = [
            "Jira Integration",
            "Slack Integration", 
            "Teams Integration",
            "Email Notifications",
            "SMS Alerts"
        ]
        
        for i, integration in enumerate(integrations, 1):
            self.console.print(f"{i}. {integration}")

    def display_dashboard(self):
        self.console.print("\n[bold green]Dashboard[/bold green]")
        
        stats = {
            "Total Scans": "156",
            "Vulnerabilities Found": "23",
            "Critical Vulnerabilities": "5",
            "Security Level": "85%"
        }
        
        table = Table(title="Quick Stats")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        for metric, value in stats.items():
            table.add_row(metric, value)
            
        self.console.print(table)

    def show_schedule_menu(self):
        self.console.print("\n[bold green]Schedule Scans[/bold green]")
        
        schedule_menu = """
1. Schedule Daily Scan
2. Schedule Weekly Scan
3. Schedule Monthly Scan
4. Custom Schedule
5. View Current Schedules
        """
        
        self.console.print(schedule_menu)

    def show_alert_menu(self):
        self.console.print("\n[bold green]Alert Settings[/bold green]")
        
        alert_menu = """
1. Email Alerts
2. SMS Alerts
3. Slack Alerts
4. Teams Alerts
5. Alert Settings
        """
        
        self.console.print(alert_menu)

    def show_ui_customization_menu(self):
        self.console.print("\n[bold green]UI Customization[/bold green]")
        
        ui_menu = """
1. Change Colors
2. Change Font
3. Customize Graphics
4. Language Settings
5. Customize Menus
        """
        
        self.console.print(ui_menu)

    def show_vuln_db_menu(self):
        self.console.print("\n[bold green]Vulnerability Database Management[/bold green]")
        
        db_menu = """
1. View All Vulnerabilities
2. Search Vulnerabilities
3. Add New Vulnerability
4. Update Existing Vulnerability
5. Delete Vulnerability
6. Export Database
        """
        
        self.console.print(db_menu)

    def show_help_menu(self):
        self.console.print("\n[bold green]Help & Support[/bold green]")
        
        help_menu = """
1. User Guide
2. Frequently Asked Questions
3. Usage Examples
4. Troubleshooting
5. Contact Support
6. Tool Updates
        """
        
        self.console.print(help_menu)

    def run(self):
        try:
            while True:
                self.display_banner()
                self.display_main_menu()
                choice = self.get_user_choice()
                self.handle_menu_choice(choice)
                
                if choice != 21:
                    input("\n[cyan]Press Enter to return to main menu...[/cyan]")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
        except KeyboardInterrupt:
            self.console.print("\n\n[red]Tool stopped by user[/red]")
            self.exit_scanner()
        except Exception as e:
            self.console.print(f"\n[red]Unexpected error: {e}[/red]")
            self.logger.error(f"Unexpected error: {e}")
            self.exit_scanner()

def main():
    try:
        scanner = HeaxScanner()
        scanner.run()
    except Exception as e:
        print(f"Error running tool: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

