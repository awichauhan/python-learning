from pathlib import Path

def read_text_file(file_path):   # function to take a file path as input
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()    # sends the file content back to whoever called the function
    except FileNotFoundError:
        print("File not found: {file_path}")
        return ""
    except PermissionError:
        print(f"No permission to read file: {file_path}")
        return ""
