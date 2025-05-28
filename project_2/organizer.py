# organizer.py
import os
import shutil

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("The folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            file_ext = filename.split(".")[-1].lower()
            target_dir = os.path.join(folder_path, file_ext + "_files")

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            shutil.move(file_path, os.path.join(target_dir, filename))
            print(f"Moved {filename} to {target_dir}")

if __name__ == "__main__":
    folder = input("Enter folder path to organize: ").strip()
    organize_folder(folder)
