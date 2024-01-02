#renumbers the jpg files inside a folder, with the numbering convention of ezgif online video converter

import os

folder_path = "PATH_NAME"

# Ensure the folder exists
if not os.path.exists(folder_path):
    print(f"The folder '{folder_path}' does not exist.")
else:
    # List all files in the folder
    files = os.listdir(folder_path)

    # Sort the files alphabetically
    sorted_files = sorted(files)

    # Enumerate and rename the files without leading zeros
    for i, filename in enumerate(sorted_files, start=1):
        original_path = os.path.join(folder_path, filename)
        new_filename = f"{i}.jpg"  # Remove leading zeros
        new_path = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(original_path, new_path)

        print(f"Renamed '{filename}' to '{new_filename}'")

    print("All files have been renamed without leading zeros.")
