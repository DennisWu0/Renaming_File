import os

def rename_files_in_directory(directory_path, renaming_dict):
    # List all files in the specified directory
    files = os.listdir(directory_path)

    # Perform the renaming of the files using the renaming_dict
    for old_name in files:
        # Extract the file number from the old name, e.g., "2 (1)" -> "2"
        file_number = old_name.split("(")[-1].split(")")[0]

        # Check if the file_number is present in the renaming_dict
        if file_number in renaming_dict:
            new_name = renaming_dict[file_number]
            old_path = os.path.join(directory_path, old_name)
            new_path = os.path.join(directory_path, new_name)

            # Preserve the original file extension
            _, old_extension = os.path.splitext(old_name)
            new_path_with_extension = new_path + old_extension

            try:
                os.rename(old_path, new_path_with_extension)
                print(f"File '{old_name}' renamed to '{new_name}' successfully.")
            except FileNotFoundError:
                print(f"Error: The file '{old_name}' was not found.")
            except OSError as e:
                print(f"Error: Renaming file '{old_name}' to '{new_name}' failed - {e}")

if __name__ == "__main__":
    target_directory = "D:\Student_file"  # Replace this with your actual directory path

    renaming_dict = {
        "1": "A",
        "2": "B",
        "3": "C",
        "4": "D",
        "5": "E",
        "6": "F",
        "7": "G",
        "8": "H",
        "9": "I",
        "10": "J",
        "11": "K",
        "12": "L",
        "13": "M",
        "14": "N",
        "15": "O",
        "16": "P",
        "17": "Q",
        "18": "R",
        "19": "S",
        "20": "T",
        "21": "U",
        "22": "V",
        "23": "W",
        "24": "X",
        "25": "Y",
        "26": "Z",

        # Add more filename mappings as needed
    }

    rename_files_in_directory(target_directory, renaming_dict)
