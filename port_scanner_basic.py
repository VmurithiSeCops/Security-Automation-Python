#!/usr/bin/env python3
"""
Basic TCP Port Checker
Author: Portfolio Project
Description: Checks if common ports are open on a target IP address using sockets.
"""

import socket
import sys
from datetime import datetime

def scan_target(target_ip, ports):
    print("-" * 50)
    print(f"Scanning target: {target_ip}")
    print(f"Time started: {str(datetime.now())}")
    print("-" * 50)

    try:
        for port in ports:
            # Create a socket object (IPv4, TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)  # 1 second timeout
            
            # Attempt connection
            result = s.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"[+] Port {port:<5}: OPEN")
            else:
                # Port is closed or filtered
                pass
            s.close()
            
    except KeyboardInterrupt:
        print("\nExiting script...")
        sys.exit()
    except socket.gaierror:
        print("\nHostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\nCould not connect to server.")
        sys.exit()

if __name__ == "__main__":
    # Example target (localhost) and common administrative ports
    target = "127.0.0.1" 
    common_ports = [21, 22, 80, 443, 3389, 8080]
    
    scan_target(target, common_ports)
