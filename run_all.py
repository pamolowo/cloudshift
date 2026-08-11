#!/usr/bin/env python3

import subprocess, datetime, os

os.chdir(os.path.expanduser("/home/ubuntu/cloud_shift"))

print("=== Toolkit run", datetime.datetime.now(), "===")


subprocess.run(["python3", "backup.py"])
subprocess.run(["python3", "monitor.py"])
print("=== Toolkit finished ===")
