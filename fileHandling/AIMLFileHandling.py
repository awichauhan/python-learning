from pathlib import Path

def read_text_file(file_path):   # function to take a file path as input
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()    # sends the file content back to whoever called the function

# Now text contains the content of myData.txt

def write_text_file(file_path, content):  #function takes two parameters: file path, content
    with open(file_path, "w", encoding="utf-8") as file:   # "w" mode overwrites old content
        file.write(content)

# Give me a file path and content, I will write that content into the file from scratch.

def append_text_file(file_path, content):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content)


#Copy a binary file from one location to another:
def copy_binary_file(source_path, destination_path):  # parameters: source file and destination file
    with open(source_path, "rb") as source:
        with open(destination_path, "wb") as destination:
            for chunk in source:    # Read pieces from source file
                destination.write(chunk)  #Write those pieces into destination file


# main function for executing above functions:
def main():
    base_dir = Path(__file__).parent   #Find the folder where this Python file is located.
# base_dir becomes the current script's folder

    input_file = base_dir / "myData.txt"  # create full paths
    output_file = base_dir / "data.txt"  # The / here is not division. With Path, / joins folder and file names.

 # Read content from myData.txt >  Store it in variable text > Write that content into data.txt:

    text = read_text_file(input_file)
    write_text_file(output_file, text)

if __name__ == "__main__":  #Run main() only when this file is executed directly.
    main()