# Smart File Organizer (Python)

A professional command-line Python application that automatically organizes files into categorized folders based on their file extensions.

Built with Python and pathlib, this project demonstrates file handling, command-line interfaces (CLI), logging, and clean project structure.

---

## Features
- Automatically categorizes files into:
  - Images
  - Documents
  - Videos
  - Audio
  Others
- Prevents duplicate file overwrites by automatically renaming files.
- Command-line interface with argument parsing.
- Dry-run mode to preview changes without moving files.
- Progress indicator while organizing files.
- Execution time summary.
- Activity logging to organizer.log.
- Handles empty directories and invalid folder paths gracefully.
  
---

## Project Structure
file_organizer/
│
├── organizer.py
├── config.py
├── README.md
└── organizer.log (generated after running)

---

## Installation

Make sure you have Python installed.

Clone the repository:

```bash
git clone https://github.com/Th3-alpha/file-organizer.git
cd file-organizer
```

No external libraries are required.

---

## Usage
Organize a folder:
```bash
python organizer.py <folder_path>
```

Example:
```bash
python organizer.py "C:\Users\YourName\Downloads"
```
Dry-run mode (preview changes without moving files):
```bash
python organizer.py "C:\Users\YourName\Downloads" --dry-run
```

## Example Output


========================================
        SMART FILE ORGANIZER
========================================

Directory : C:\Users\YourName\Downloads
Mode      : Normal

[1/3] ✓ image.jpg → Images/image.jpg

[2/3] ✓ report.pdf → Documents/report.pdf

[3/3] ✓ song.mp3 → Audio/song.mp3

========================================
                SUMMARY
========================================

Audio       : 1

Documents   : 1

Images      : 1

----------------------------------------
Files Processed : 3

Time Taken      : 0.08 seconds

Log File        : organizer.log

Done!
========================================

---

## Technologies Used
- Python 3
- pathlib
- shutil
- argparse
- logging
- time

---

## Future Improvements

- Recursive folder organization (--recursive)
- Undo last organization
- Custom file categories
- GUI version (Tkinter or CustomTkinter)
- Drag-and-drop support
- Executable (.exe) release

---

## Author

Abdullah Ameen-Ikoyi

GitHub:https://github.com/Th3-alpha
