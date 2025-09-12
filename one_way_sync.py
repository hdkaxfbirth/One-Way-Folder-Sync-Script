import os
import shutil
import filecmp
import argparse

def sync_folders(source, target):
    """
    Synchronize the contents of source folder to target folder (one-way sync).
    Files/folders in target that are not in source are deleted.
    Files/folders in source that are not in target are copied over.
    Modified files in source overwrite those in target.
    """
    # Ensure absolute paths
    source = os.path.abspath(source)
    target = os.path.abspath(target)

    # Create target directory if it doesn't exist
    if not os.path.exists(target):
        os.makedirs(target)

    # Get list of items in source and target
    source_items = set(os.listdir(source))
    target_items = set(os.listdir(target))

    # Copy/update files & folders from source to target
    for item in source_items:
        source_path = os.path.join(source, item)
        target_path = os.path.join(target, item)

        if os.path.isdir(source_path):
            sync_folders(source_path, target_path)
        else:
            # Copy if not exists or files are different
            if (not os.path.exists(target_path)) or (not filecmp.cmp(source_path, target_path, shallow=False)):
                shutil.copy2(source_path, target_path)

    # Remove items in target not present in source
    for item in target_items - source_items:
        target_path = os.path.join(target, item)
        if os.path.isdir(target_path):
            shutil.rmtree(target_path)
        else:
            os.remove(target_path)

def main():
    parser = argparse.ArgumentParser(description="One-way folder sync: synchronize source to target.")
    parser.add_argument("source", help="Source directory")
    parser.add_argument("target", help="Target directory")
    args = parser.parse_args()

    if not os.path.isdir(args.source):
        print(f"Source '{args.source}' is not a directory or does not exist.")
        return

    sync_folders(args.source, args.target)
    print(f"Synchronized '{args.source}' --> '{args.target}'")

if __name__ == "__main__":
    main()
