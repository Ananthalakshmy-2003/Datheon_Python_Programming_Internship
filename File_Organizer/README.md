# Automatic File Organizer

## Project Description

The Automatic File Organizer is a Python-based utility that automatically organizes files into different folders based on their file extensions.

It helps users manage cluttered directories by sorting files into categories such as Documents, Images, Videos, Archives, and Code.

## Features

- Automatically scans files in a selected folder.
- Identifies file types using their extensions.
- Creates category folders automatically.
- Moves files into their respective folders.
- Handles duplicate filenames without overwriting existing files.
- Handles permission and file errors.
- Displays a summary of organized files.

## Technologies Used

- **Python** – Programming language.
- **os** – Scanning directories and accessing files.
- **shutil** – Moving files between folders.
- **pathlib** – Handling file and folder paths.

## File Categories

| File Extensions | Category |
|---|---|
| .pdf, .doc, .docx, .txt, .ppt, .pptx | Documents |
| .jpg, .jpeg, .png, .gif | Images |
| .mp4, .mkv, .avi | Videos |
| .zip, .rar, .7z | Archives |
| .py, .java, .c, .cpp, .js, .html, .css | Code |

## Project Structure

```text
File_Organizer/
│
├── organizer.py
│
├── README.md
│
└── Test_Files/
    │
    ├── Documents/
    ├── Images/
    ├── Videos/
    ├── Archives/
    └── Code/
```

## Requirements

- Python 3.x
- Visual Studio Code (recommended)

No external Python packages are required.

## How to Run

**Step 1:** Clone or download this project.

**Step 2:** Open the project folder in Visual Studio Code.

**Step 3:** Place the files you want to organize inside the `Test_Files` folder.

**Step 4:** Open the terminal and execute:

```bash
python organizer.py
```

**Step 5:** The program automatically creates category folders and moves the files.

## Sample Output

```text
===== ORGANIZING FILES =====

Moved: movie.mp4 -> Videos
Moved: notes.pdf -> Documents
Moved: photo.jpg -> Images
Moved: program.py -> Code
Moved: project.zip -> Archives

===== ORGANIZATION SUMMARY =====

Files moved: 5
Files skipped: 0
Errors: 0
```

## Learning Outcomes

Through this project, I learned:

- File handling in Python.
- Working with directories and file paths.
- Using the os and shutil modules.
- Creating folders dynamically.
- Handling exceptions.
- Automating file management tasks.

## Author

Python Beginner Project

## License

This project is created for educational and learning purposes.