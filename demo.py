#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def demo_banner():
    banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                            __    __                            
                   |  \  |  \                           
                 | ▓▓  | ▓▓ ______   ______  __    __ 
                 | ▓▓__| ▓▓/      \ |      \|  \  /  \
                 | ▓▓    ▓▓  ▓▓▓▓▓▓\ \▓▓▓▓▓▓\\▓▓\/  ▓▓
                 | ▓▓▓▓▓▓▓▓ ▓▓    ▓▓/      ▓▓ >▓▓  ▓▓ 
                 | ▓▓  | ▓▓ ▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓/  ▓▓▓▓\ 
                 | ▓▓  | ▓▓\▓▓     \\▓▓    ▓▓  ▓▓ \▓▓\
                  \▓▓   \▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓   \▓▓
                                     
                                     
                                     

                                                                               ║ 
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print_colored(banner, "94")

def demo_smart_scan():
    print_colored("\nStarting intelligent scan...", "92")
    
    targets = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
    vuln_types = ["SQL Injection", "XSS", "CSRF", "RCE", "LFI", "RFI"]
    
    for i, target in enumerate(targets):
        print_colored(f"\nScanning target: {target}", "96")
        
        for j in range(3):
            vuln_type = random.choice(vuln_types)
            confidence = random.randint(75, 99)
            severity = random.choice(["Low", "Medium", "High", "Critical"])
            
            print_colored(f"  Detection: {vuln_type} (Confidence: {confidence}%, Severity: {severity})", "93")
            time.sleep(0.5)
        
        print_colored(f"  Completed scan for {target}", "92")
        time.sleep(1)

def demo_network_discovery():
    print_colored("\nSmart network discovery...", "92")
    
    devices = [
        ("192.168.1.1", "Router", "Cisco", "Open"),
        ("192.168.1.10", "Server", "Ubuntu", "Protected"),
        ("192.168.1.20", "Workstation", "Windows", "Open"),
        ("192.168.1.30", "IoT Device", "Unknown", "Unsecure")
    ]
    
    for ip, device_type, os, status in devices:
        print_colored(f"  {ip} - {device_type} ({os}) - {status}", "96")
        time.sleep(0.3)
    
    print_colored("  Discovered 4 devices", "92")

def demo_vulnerability_scan():
    print_colored("\nComprehensive vulnerability scan...", "92")
    
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 1433, 1521, 3306, 3389, 5432, 5900, 6379, 8080, 8443]
    
    print_colored("  Port scanning...", "93")
    for port in ports[:10]:
        if random.random() > 0.7:
            service = random.choice(["FTP", "SSH", "Telnet", "SMTP", "DNS", "HTTP", "HTTPS", "IMAP", "POP3", "MSSQL"])
            print_colored(f"    Port {port} open - {service}", "91")
        time.sleep(0.1)
    
    print_colored("  Port scan completed", "92")

def demo_reporting():
    print_colored("\nGenerating comprehensive reports...", "92")
    
    report_types = ["HTML", "JSON", "PDF", "XML"]
    for report_type in report_types:
        print_colored(f"  Creating {report_type} report...", "93")
        time.sleep(0.5)
        print_colored(f"    {report_type} report generated", "92")
    
    print_colored("  Analyzing results...", "93")
    time.sleep(1)
    
    stats = {
        "Total targets": "4",
        "Open ports": "12",
        "Vulnerabilities found": "8",
        "Critical vulnerabilities": "2",
        "Security level": "75%"
    }
    
    for metric, value in stats.items():
        print_colored(f"    {metric}: {value}", "96")
        time.sleep(0.3)

def demo_analysis():
    print_colored("\nAdvanced analysis...", "92")
    
    models = [
        ("Vulnerability classifier", "95%", "Complete"),
        ("Anomaly pattern detector", "92%", "Complete"),
        ("New vulnerability predictor", "88%", "Complete"),
        ("False positive reducer", "94%", "Complete")
    ]
    
    for model_name, accuracy, status in models:
        print_colored(f"  {model_name} - Accuracy: {accuracy} - {status}", "96")
        time.sleep(0.5)
    
    print_colored("  Pattern analysis...", "93")
    time.sleep(1)
    
    patterns = [
        "Potential SQL Injection attack pattern",
        "Abnormal network behavior",
        "Potential new vulnerability (Zero-Day)",
        "Recommendation: Update operating system"
    ]
    
    for pattern in patterns:
        print_colored(f"    {pattern}", "95")
        time.sleep(0.5)

def demo_integration():
    print_colored("\nIntegrating with external tools...", "92")
    
    integrations = [
        ("Jira", "Updating issue tickets"),
        ("Slack", "Sending alerts"),
        ("Teams", "Sharing results"),
        ("Email", "Sending reports")
    ]
    
    for tool, action in integrations:
        print_colored(f"  {tool} - {action}...", "93")
        time.sleep(0.5)
        print_colored(f"    Integrated with {tool}", "92")

def main():
    demo_banner()
    
    print_colored("\nStarting HEAX Scanner demo", "95")
    print_colored("=" * 60, "94")
    
    features = [
        "Multi-network scanning",
        "Machine learning capabilities",
        "Zero-day vulnerability detection",
        "Comprehensive detailed reports",
        "Integration with security tools",
        "Fast scanning with comprehensive coverage",
        "High accuracy with reduced false positives",
        "Automation and scan scheduling"
    ]
    
    print_colored("\nKey features:", "95")
    for feature in features:
        print_colored(f"  {feature}", "96")
        time.sleep(0.3)
    
    input("\nPress Enter to start demo...")
    
    demo_smart_scan()
    demo_network_discovery()
    demo_vulnerability_scan()
    demo_analysis()
    demo_reporting()
    demo_integration()
    
    print_colored("\n" + "=" * 60, "94")
    print_colored("Demo completed!", "95")
    print_colored("To try the real tool, run heax_scanner.py", "92")
    print_colored("For more information, check README.md", "93")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_colored("\n\nDemo stopped by user", "93")
    except Exception as e:
        print_colored(f"\nError: {e}", "91")

