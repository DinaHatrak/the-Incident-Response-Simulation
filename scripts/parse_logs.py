# SCRIPT TO AUTOMATICALLY PARSE LOGS FOR CRITICAL SECURITY EVENTS

def analyze_logs(file_path):
    print(f"[+] Starting log analysis for: {file_path}")
    with open(file_path, 'r') as file:
        for line in file:
            if "CRITICAL" in line or "Authentication failed" in line:
                print(f"[🚨 ALERT] Action Required: {line.strip()}")

if __name__ == "__main__":
    # Path to the mock log file
    analyze_logs("logs/auth_failed.log")
