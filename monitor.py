#!/usr/bin/env python3

import datetime
import subprocess

SERVICES = ["nginx", "cloudshift-app", "cron"]
LOG = "/var/log/monitor.log"

for svc in SERVICES:
    stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

    check = subprocess.run(
        ["systemctl", "is-active", "--quiet", svc],
        check=False
    )

    if check.returncode == 0:
        message = f"{stamp} {svc} OK"
    else:
        restart = subprocess.run(
            ["systemctl", "restart", svc],
            capture_output=True,
            text=True,
            check=False
        )

        if restart.returncode == 0:
            message = f"{stamp} {svc} was DOWN, restarted successfully"
        else:
            error = restart.stderr.strip()
            message = f"{stamp} {svc} restart FAILED: {error}"

    print(message)

    with open(LOG, "a", encoding="utf-8") as log:
        log.write(message + "\n")
