import os

def find_python_files(folder_path):
    python_files = []
    for root, dirs, files in os.walk(folder_path):
        if ".venv" in dirs:
            dirs.remove(".venv")  # Exclude the .venv folder
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

def copy_python_files(folder_path, output_file):
    python_files = find_python_files(folder_path)
    with open(output_file, "w", encoding="utf-8") as output:
        for file in python_files:
            with open(file, "r", encoding="utf-8") as input_file:
                output.write(f"# File: {file}\n")
                output.write(f"# Script: {os.path.basename(file)}\n")
                output.write(input_file.read())
                output.write("\n\n")


if __name__ == "__main__":
    copy_python_files("./", "./project_code.py")
