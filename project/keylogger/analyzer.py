import json
import hashlib
import os

class LogAnalyzer:
    def __init__(self, log_file='keylog.json'):
        self.log_file = log_file

    def load_logs(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                logs = json.load(f)
            return logs
        else:
            print("No logs found.")
            return []

    def analyze_logs(self):
        logs = self.load_logs()

        # Example analysis: Calculate hash of all key sequences
        keys = ''.join([log['key'] for log in logs if 'key' in log])
        sha256_hash = hashlib.sha256(keys.encode('utf-8')).hexdigest()

        print(f"SHA-256 Hash of logged keys: {sha256_hash}")

        # Perform more analysis as needed

    def generate_report(self):
        logs = self.load_logs()

        report = "Keylogger Report:\n\n"
        for log in logs:
            report += f"Key: {log['key']}, Time: {log['timestamp']}\n"

        with open('keylogger_report.txt', 'w') as f:
            f.write(report)

        print("Keylogger report generated.")
