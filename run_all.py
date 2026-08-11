#!/usr/bin/env python3

import subprocess, datetime, os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

print("=== Toolkit run", datetime.datetime.now(), "===")


subprocess.run(["python3", "backup.py"])
subprocess.run(["python3", "monitor.py"])
print("=== Toolkit finished ===")
