import sys
import os

print("Python Path:", sys.path)
print("Current Directory:", os.getcwd())

# Ensure 'project_directory' is in the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from keylogger.logger import KeyLogger
from keylogger.analyzer import LogAnalyzer

def main():
    logger = KeyLogger()
    analyzer = LogAnalyzer()

    print("Starting keylogger... Press Esc to stop.")
    logger.start()

    print("\nAnalyzing logs...")
    analyzer.analyze_logs()

    print("\nGenerating report...")
    analyzer.generate_report()

if __name__ == "__main__":
    main()
