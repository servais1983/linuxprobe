import subprocess
import os

def capture(output):
    path = os.path.join(output, "Users")
    os.makedirs(path, exist_ok=True)
    cmds = {
        "Users.txt": "getent passwd",
        "Groups.txt": "getent group",
        "LastLog.txt": "lastlog",
        "LoggedIn.txt": "w"
    }
    for f, cmd in cmds.items():
        with open(f"{path}/{f}", "w") as out:
            subprocess.call(cmd, shell=True, stdout=out)