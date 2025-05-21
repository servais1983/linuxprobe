import subprocess
import os

def capture(output):
    path = os.path.join(output, "SystemInfo")
    os.makedirs(path, exist_ok=True)
    cmds = {
        "Kernel.txt": "uname -a",
        "Dmesg.log": "dmesg",
        "KernelModules.txt": "lsmod",
        "Hardware.txt": "lspci -vvv && lsusb -v",
        "HardwareList.txt": "lshw -short"
    }
    for file, cmd in cmds.items():
        with open(f"{path}/{file}", "w") as f:
            subprocess.call(cmd, shell=True, stdout=f, stderr=subprocess.DEVNULL)