import subprocess
import os

def capture(output):
    path = os.path.join(output, "Network")
    os.makedirs(path, exist_ok=True)
    with open(f"{path}/NetworkInfo.txt", "w") as f:
        subprocess.call("iptables-save", shell=True, stdout=f)
        subprocess.call("ip a", shell=True, stdout=f)
        subprocess.call("ip route", shell=True, stdout=f)
        subprocess.call("ip neigh", shell=True, stdout=f)