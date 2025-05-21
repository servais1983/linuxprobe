import subprocess
import os
import shutil

def capture(output):
    path = os.path.join(output, "Cron")
    os.makedirs(path, exist_ok=True)
    shutil.copytree("/etc/cron.d", f"{path}/cron.d", dirs_exist_ok=True)
    subprocess.call("crontab -l -u root", shell=True, stdout=open(f"{path}/root_cron.txt", "w"), stderr=subprocess.DEVNULL)