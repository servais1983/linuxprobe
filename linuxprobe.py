#!/usr/bin/env python3

import argparse
from core.utils import init_output_dir, run_script_yaml

def main():
    parser = argparse.ArgumentParser(description="LinuxProbe - Forensic Collector CLI")
    parser.add_argument("--run", help="Script YAML à exécuter", default="scripts/full_probe.yaml")
    parser.add_argument("--output", help="Répertoire de sortie", default="LinuxForensic")

    args = parser.parse_args()

    output = init_output_dir(args.output)
    run_script_yaml(args.run, output)

if __name__ == "__main__":
    main()