import os
import shutil
import sys
import argparse
import logging
from pathlib import Path

# CONFIGURATION
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
}

LOG_FILE = "organizer.log"

# Set up professional logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# UTILITY FUNCTIONS
def get_unique_filename(destination_folder, filename):
    """Avoids overwriting files by renaming duplicates using pathlib."""
    path = Path(destination_folder) / filename
    base_name = path.stem
    extension = path.suffix
    counter = 1
    new_filename = filename

    while (Path(destination_folder) / new_filename).exists():
        new_filename = f"{base_name}_{counter}{extension}"
        counter += 1

    return new_filename


def get_category(file_ext):
    """Returns category based on file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_ext in extensions:
            return category
    return "Others"


# CORE FUNCTION
def organize_files(folder_path, dry_run=False):
    """Organizes files into categorized folders using pathlib."""
    base_dir = Path(folder_path)

    if not base_dir.is_dir():
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    files_moved = 0
    summary = {}

    print(f"\n--- Organizing: {base_dir.absolute()} ---\n")
    if dry_run:
        print("!!! DRY RUN MODE ENABLED - No files will be moved !!!\n")

    # Iterate through the directory
    for item in base_dir.iterdir():
        # Skip directories and the log file
        if item.is_dir() or item.name == LOG_FILE:
            continue

        file_ext = item.suffix.lower()
        category = get_category(file_ext)

        target_folder = base_dir / category
        
        # Determine unique filename to prevent overwriting
        unique_name = get_unique_filename(target_folder, item.name)
        destination_path = target_folder / unique_name

        try:
            if dry_run:
                print(f"[DRY RUN] {item.name} -> {category}/{unique_name}")
            else:
                # Create category folder if it doesn't exist
                target_folder.mkdir(parents=True, exist_ok=True)
                
                shutil.move(str(item), str(destination_path))
                
                msg = f"Moved: {item.name} -> {category}/{unique_name}"
                print(msg)
                logging.info(msg)

            files_moved += 1
            summary[category] = summary.get(category, 0) + 1

        except Exception as e:
            err_msg = f"Failed to move {item.name}: {e}"
            print(err_msg)
            logging.error(err_msg)

    # SUMMARY
    print("\n--- SUMMARY ---")
    for cat, count in summary.items():
        print(f"{cat}: {count} files")

    print(f"\nTotal files processed: {files_moved}")
    print("--- Done ---")


# MAIN ENTRY
def main():
    parser = argparse.ArgumentParser(description="Automate file organization by category.")
    
    # Positional argument for the folder path
    parser.add_argument("folder", help="Path to the folder you want to organize")
    
    # Optional flag for dry run
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")

    args = parser.parse_args()

    try:
        organize_files(args.folder, dry_run=args.dry_run)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.critical(f"System failure: {e}")


if __name__ == "__main__":
    main()
