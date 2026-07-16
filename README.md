# ⛏️ Minecraft Saves Backup

A lightweight Python utility that automatically backs up your Minecraft worlds from different launchers and mod loaders.

The script copies all saves from the selected launcher and stores them in a dedicated backup folder inside your Documents directory.

## ⬇️ Downloads:
* [MC SAVE WOLRDS.exe](https://github.com/Just-Nicks/MC-Save-Backup/releases/download/v1.0/backup-saves_menu.exe)
* [MC SAVE BACKUP.zip](https://github.com/Just-Nicks/MC-Save-Backup/archive/refs/tags/v1.0.zip)

* EXE = Executable
* ZIP = ALL FILES OF REPOSITORE  

## ✨ Features

* Supports the official Minecraft Launcher
* Supports CurseForge instances
* Supports Modrinth profiles
* Progress bar during backup operations
* Automatic save detection
* Existing backup overwrite protection
* Simple terminal-based interface powered by Rich

## 👋 Supported Launchers

### Minecraft Launcher

Backs up worlds from:

```text
%AppData%/.minecraft/saves
```

### CurseForge

Backs up worlds from:

```text
C:/Users/<username>/curseforge/minecraft/Instances/<instance>/saves
```

### Modrinth

Backs up worlds from:

```text
%AppData%/ModrinthApp/profiles/<profile>/saves
```

## 🗃️ Backup Location

All backups are stored in:

```text
Documents/
└── Saves Backups MC/
```

Example structure:

```text
Saves Backups MC/
├── minecraft/
│   ├── World 1/
│   └── World 2/
├── curseforge/
│   └── Better MC/
│       ├── World 1/
│       └── World 2/
└── modrinth/
    └── Fabric Survival/
        ├── World 1/
        └── World 2/
```

## 🚩 Requirements

* Windows
* Python 3.8+
* Rich

Install all required packages using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```

Or install Rich manually:

```bash
pip install rich
```

## 🤔 How to use

Run the script:

```bash
python main.py
```

### ❗❗OR RUN THE EXECUTABLE❗❗

You will be asked to choose your launcher:

```text
1 Minecraft Launcher
2 CurseForge
3 Modrinth
```

For CurseForge and Modrinth, enter the exact instance/profile name when prompted.

The script will:

1. Verify the selected instance exists.
2. Check if save files are available.
3. Ask before overwriting an existing backup.
4. Copy all worlds to the backup directory.
5. Display a progress bar while copying.

## Example

```text
Select your launcher: 2
Enter the instance name: Better MC
```

The worlds from:

```text
curseforge/minecraft/Instances/Better MC/saves
```

will be copied to:

```text
Documents/Saves Backups MC/curseforge/Better MC
```

## ❓ Why I Built This

I frequently play on multiple Minecraft launchers and modpacks. Manually locating and backing up worlds every time became tedious, especially before updating mods or testing new versions.

This tool provides a quick way to create backups before making changes that could potentially corrupt a world.

## Future Ideas

* SAVE MODS
* SAVE CONFIGS
* SCREENSHOTS
