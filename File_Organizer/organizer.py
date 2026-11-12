
import os
import shutil
from pathlib import Path


# Step 1: File extension categories
FILE_CATEGORIES = {

    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",

    ".py": "Code",
    ".java": "Code",
    ".c": "Code",
    ".cpp": "Code",
    ".js": "Code",
    ".html": "Code",
    ".css": "Code"
}


# Step 2: Organize files
def organize_files(folder_path):

    folder = Path(folder_path)

    if not folder.exists():
        print("Folder does not exist!")
        return

    if not folder.is_dir():
        print("The given path is not a folder!")
        return

    moved = 0
    skipped = 0
    errors = 0

    print("\n===== ORGANIZING FILES =====")

    for entry in os.scandir(folder):

        if entry.is_file():

            file_path = Path(entry.path)

            extension = file_path.suffix.lower()

            category = FILE_CATEGORIES.get(extension)

            if category:

                destination_folder = folder / category

                try:
                    # Create category folder
                    destination_folder.mkdir(exist_ok=True)

                    destination = destination_folder / file_path.name

                    # Handle duplicate filenames
                    counter = 1

                    while destination.exists():

                        new_name = (
                            file_path.stem + "_" +
                            str(counter) + file_path.suffix
                        )

                        destination = destination_folder / new_name
                        counter += 1

                    # Move file
                    shutil.move(str(file_path), str(destination))

                    print("Moved:", file_path.name, "->", category)

                    moved += 1

                except PermissionError:
                    print("Permission denied:", file_path.name)
                    errors += 1

                except (OSError, shutil.Error) as error:
                    print("Error:", file_path.name, error)
                    errors += 1

            else:
                print("Skipped:", file_path.name)
                skipped += 1

    # Step 3: Display summary
    print("\n===== ORGANIZATION SUMMARY =====")
    print("Files moved:", moved)
    print("Files skipped:", skipped)
    print("Errors:", errors)


# Step 4: Main program
if __name__ == "__main__":

    organize_files("Test_Files")
