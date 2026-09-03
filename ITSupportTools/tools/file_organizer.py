import os
import shutil

def organize_files(folder):
    if not os.path.exists(folder):
        return f"Folder does not exist: {folder}"

    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".flac"],
        "Archives": [".zip", ".rar", ".7z"]
    }

    moved = 0
    log = []

    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)

        if not os.path.isfile(full_path):
            continue

        extension = os.path.splitext(filename)[1].lower()
        category = None

        for name, extensions in categories.items():
            if extension in extensions:
                category = name
                break

        if category is None:
            category = "Others"

        category_folder = os.path.join(folder, category)
        os.makedirs(category_folder, exist_ok=True)
        destination = os.path.join(category_folder, filename)

        try:
            shutil.move(full_path, destination)
            moved += 1
            log.append(f"Moved: {filename} -> {category}")
        except Exception as error:
            log.append(f"Could not move {filename}: {error}")

    log.append(f"\nFinished. {moved} file(s) organized.")
    return "\n".join(log)