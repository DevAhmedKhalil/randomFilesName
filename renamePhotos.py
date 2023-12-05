import os
import random
import string

def generate_random_name(length=10):
    # Generate a random name
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def rename_files_in_folder(folder_path):
    # List all files in the folder
    files_in_folder = os.listdir(folder_path)

    for original_file_name in files_in_folder:
        # Generate a random name for each file
        random_name = generate_random_name()

        # Get the file extension
        _, file_extension = os.path.splitext(original_file_name)

        # Construct the new file name with the random name and original extension
        new_file_name = random_name + file_extension

        # Construct the full paths for the old and new file names
        old_file_path = os.path.join(folder_path, original_file_name)
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)

if __name__ == "__main__":
    # Specify the folder path containing the files
    folder_path_to_rename = r"E:\wallpapers\1-Flare\Quotes"

    # Rename files in the specified folder
    rename_files_in_folder(folder_path_to_rename)
