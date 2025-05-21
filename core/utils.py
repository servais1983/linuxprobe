import os
import yaml
from datetime import datetime
from pathlib import Path

def init_output_dir(base_name):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = Path.home() / f"{base_name}_{ts}"
    os.makedirs(path, exist_ok=True)
    return str(path)

def run_script_yaml(script_path, output):
    from core import volatile, systeminfo, filesystem, users, network, packages, cron, hashing

    with open(script_path, "r") as f:
        data = yaml.safe_load(f)

    for step in data.get("steps", []):
        module = step.get("module")
        if module == "volatile":
            volatile.capture(output)
        elif module == "systeminfo":
            systeminfo.capture(output)
        elif module == "filesystem":
            filesystem.capture(output)
        elif module == "users":
            users.capture(output)
        elif module == "network":
            network.capture(output)
        elif module == "packages":
            packages.capture(output)
        elif module == "cron":
            cron.capture(output)
        elif module == "hashing":
            hashing.capture(output)