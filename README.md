# One-Way Folder Sync Script

This project provides a simple Python script to synchronize the contents of two folders in a **one-way** fashion.

## Features

- Synchronizes all files and subfolders from a source directory to a target directory.
- Copies new and modified files from source to target.
- Removes files and folders from the target that do not exist in the source.
- Preserves file modification times and metadata.

## Usage

```bash
python one_way_sync.py /path/to/source /path/to/target
```

- The script will make the target folder exactly match the source folder.
- Any files or folders in the target but not in the source will be deleted.
- New or modified files/folders in the source will be copied/updated to the target.

## Requirements

- Python 3.6 or higher (uses only the standard library: `os`, `shutil`, `filecmp`, `argparse`).

## Example

Suppose you want to sync the contents of `~/Documents/source/` to `~/Documents/backup/`:

```bash
python one_way_sync.py ~/Documents/source ~/Documents/backup
```

After running, `backup/` will be an exact copy of `source/`.

## License

This script is provided under the MIT License. See [LICENSE](LICENSE) for details.
