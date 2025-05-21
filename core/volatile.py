import subprocess
import os

def capture(output):
    path = os.path.join(output, "Memory")
    os.makedirs(path, exist_ok=True)
    cmd = ["date", "uptime", "who", "last", "netstat -tulpena", "ss -tulpan", "arp -a", "ps auxef", "lsof", "df -h", "mount"]
    with open(f"{path}/VolatileData.txt", "w") as f:
        for c in cmd:
            f.write(f"\n--- {c} ---\n")
            subprocess.call(c, shell=True, stdout=f)