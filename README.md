# LinuxProbe – Outil de collecte forensic Linux (CLI)

## 🔍 Fonctionnalités

- Artefacts volatiles (ps, netstat, who)
- Fichiers système et journaux
- Infos utilisateurs et paquets
- Tâches planifiées et services
- SHA256 + timestamp
- Structuré et compressible

## ⚙️ Installation

```bash
chmod +x install.sh
./install.sh
```

## 🚀 Exemple

```bash
python3 linuxprobe.py --run scripts/full_probe.yaml
```

## ✅ Résultat

Dossier horodaté dans `$HOME`, compressable manuellement.