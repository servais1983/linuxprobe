import subprocess
import os

def capture(output):
    path = os.path.join(output, "FileSystem")
    os.makedirs(path, exist_ok=True)
    important = [
        "/etc", "/var/log", "/tmp", "/dev", "/proc", "/root/.bash_history",
        "/home/*/.bash_history", "/home/*/.ssh", "/home/*/.mozilla", "/home/*/.cache"
    ]
    for item in important:
        safe = item.replace("/", "_").replace("*", "ALL")
        dest = os.path.join(path, safe)
        subprocess.call(f"rsync -aHAX {item} {dest}", shell=True)