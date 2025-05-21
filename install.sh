#!/bin/bash
echo "[*] Installation de LinuxProbe..."

sudo apt update
sudo apt install -y python3 python3-pip rsync lshw lsb-release net-tools
pip3 install -r requirements.txt

echo "[+] LinuxProbe prêt. Lancez :"
echo "python3 linuxprobe.py"