import subprocess
import os

def capture(output):
    path = os.path.join(output, "Packages")
    os.makedirs(path, exist_ok=True)
    with open(f"{path}/InstalledPackages.txt", "w") as f:
        for cmd in ["dpkg -l", "apt list --installed", "yum list installed", "snap list"]:
            subprocess.call(cmd, shell=True, stdout=f, stderr=subprocess.DEVNULL)