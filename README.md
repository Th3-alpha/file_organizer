# Smart File Organizer (Python)

A Python automation tool that organizes files in a folder into categorized directories based on file type.

## Overview
This project helps automate the process of cleaning up messy folders by sorting files into categories like Images, Documents, Videos, Audio, and Others.

It also includes safety and usability features such as duplicate file handling, dry-run mode, and logging.

---

## Features
- Automatic file categorization (Images, Documents, Videos, Audio, Others)
- Duplicate file handling (renames files to avoid overwriting)
- Command-line interface (CLI support)
- Dry-run mode for safe preview
- Activity logging

---

## Project Structure
file_organizer/
│
├── organizer.py
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
---

## Usage
Run the script:
```bash
python organizer.py <folder_path>
```

Example:
```bash
python organizer.py "C:\Users\YourName\Downloads"
```
Dry-run mode (preview only):
```bash
python organizer.py "C:\Users\YourName\Downloads" --dry-run
```

Example Output
Moved: image.jpg -> Images/image.jpg
Moved: doc.pdf -> Documents/doc.pdf

--- SUMMARY ---
Images: 1 files
Documents: 1 files

Total files processed: 2

---

## Technologies Used
- Python
- os module (file system operations)
- shutil module (file movement)

---

## Future Improvements

- GUI version (Tkinter)
- Drag-and-drop support
- Undo feature for file organization
- Convert to executable (.exe)


👤 Author
Abdullah Ameen-Ikoyi
