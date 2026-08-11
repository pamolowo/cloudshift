#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime

APP_DIR = "/var/www/app"

os.makedirs(APP_DIR, exist_ok=True)
os.chdir(APP_DIR)

# Pretend new release files were copied here.
result = subprocess.run(
    ["systemctl", "restart", "cron"],
    check=False
)

check = subprocess.run(
    ["systemctl", "is-active", "--quiet", "cron"],
    check=False
)

timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

if result.returncode == 0 and check.returncode == 0:
    print("Deploy OK", timestamp)
else:
    print("Deployment FAILED!", timestamp)

