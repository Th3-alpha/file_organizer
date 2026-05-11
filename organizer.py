import os
import shutil
import sys

# CONFIGURATION
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
}

LOG_FILE = "organizer.log"
DRY_RUN = False  # Set True if you want to preview actions first


# UTILITY FUNCTIONS
def log_action(message):
    """Logs actions to a file."""
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")


def get_unique_filename(destination_folder, filename):
    """Avoids overwriting files by renaming duplicates."""
    base_name, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(destination_folder, new_filename)):
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
def organize_files(folder_path):
    """Organizes files into categorized folders."""

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    files_moved = 0
    summary = {}

    print(f"\n--- Organizing: {folder_path} ---\n")

    for filename in os.listdir(folder_path):
        source_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(source_path):
            continue

        # Skip system/log files
        if filename == LOG_FILE:
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        category = get_category(file_ext)

        target_folder = os.path.join(folder_path, category)
        os.makedirs(target_folder, exist_ok=True)

        unique_name = get_unique_filename(target_folder, filename)
        destination_path = os.path.join(target_folder, unique_name)

        try:
            if DRY_RUN:
                print(f"[DRY RUN] {filename} -> {category}/{unique_name}")
            else:
                shutil.move(source_path, destination_path)
                print(f"Moved: {filename} -> {category}/{unique_name}")
                log_action(f"Moved: {filename} -> {category}/{unique_name}")

            files_moved += 1
            summary[category] = summary.get(category, 0) + 1

        except Exception as e:
            print(f"Failed to move {filename}: {e}")
            log_action(f"ERROR moving {filename}: {e}")

    # SUMMARY
    print("\n--- SUMMARY ---")
    for cat, count in summary.items():
        print(f"{cat}: {count} files")

    print(f"\nTotal files processed: {files_moved}")
    print("--- Done ---")


# MAIN ENTRY
def main():
    global DRY_RUN

    if len(sys.argv) < 2:
        print("Usage: python organizer.py <folder_path> [--dry-run]")
        return

    folder_path = sys.argv[1]

    if len(sys.argv) > 2 and sys.argv[2] == "--dry-run":
        DRY_RUN = True

    try:
        organize_files(folder_path)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
