import os
import hashlib
import csv

def capture(output):
    hash_file = os.path.join(output, "FileHashes.csv")
    with open(hash_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["File", "SHA256"])
        for root, _, files in os.walk(output):
            for name in files:
                path = os.path.join(root, name)
                try:
                    with open(path, "rb") as file:
                        h = hashlib.sha256(file.read()).hexdigest()
                        writer.writerow([path, h])
                except:
                    continue