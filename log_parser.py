#!/usr/bin/env python3
"""
Simple Log Parser for Failed Login Detection
Author: Portfolio Project
Description: Parses sample text logs to identify and flag failed authentication attempts.
"""

import os

def parse_auth_logs(file_path):
    print(f"[*] Analyzing log file: {file_path}\n")
    
    total_lines = 0
    anomalies_found = 0

    if not os.path.exists(file_path):
        print(f"[-] Error: File '{file_path}' not found.")
        return

    with open(file_path, 'r') as file:
        for line in file:
            total_lines += 1
            # Filter for authentication failure keywords
            if "FAILED" in line or "Invalid user" in line or "authentication failure" in line:
                anomalies_found += 1
                print(f"[ALERT] Line {total_lines:02d}: {line.strip()}")

    print(f"\n[*] Scan complete. Processed {total_lines} lines. Flagged {anomalies_found} failed authentication event(s).")

if __name__ == "__main__":
    sample_log = "sample_auth.log"
    
    # Generate a quick dummy log file if one doesn't exist locally
    if not os.path.exists(sample_log):
        with open(sample_log, 'w') as f:
            f.write("2026-10-27 10:01:22 - INFO: User admin logged in successfully.\n")
            f.write("2026-10-27 10:05:12 - WARNING: FAILED login attempt for root from 192.168.1.50\n")
            f.write("2026-10-27 10:05:15 - WARNING: FAILED login attempt for root from 192.168.1.50\n")
            f.write("2026-10-27 10:10:00 - INFO: User user_01 logged in successfully.\n")

    parse_auth_logs(sample_log)
