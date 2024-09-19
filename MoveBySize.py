import os
import shutil
import argparse
import pyfiglet

def print_banner(mode):
    """Prints the application banner with ASCII art and mode-specific details."""
    ascii_banner = pyfiglet.figlet_format("MoveBySize")
    print(ascii_banner)
    print("----------------------------------------------------")
    print("Coder: @AnonyKs_xD")
    print("Telegram: https://t.me/@AnonyKs_xD")
    print("----------------------------------------------------")
    if mode == "directory":
        print("Mode 1 ~ Directory")
    elif mode == "subdirectories":
        print("Mode 2 - SubDirectories")

def convert_size(size, unit):
    """Converts the size into bytes based on the unit specified."""
    unit = unit.upper()
    if unit == 'KB':
        return int(size * 1024)
    elif unit == 'MB':
        return int(size * 1024 ** 2)
    elif unit == 'GB':
        return int(size * 1024 ** 3)
    else:
        raise ValueError("Unsupported unit. Use KB, MB, or GB.")

def move_files(src, dst, max_size, recursive=False):
    """Moves files based on the specified criteria."""
    if src == dst:
        print("Source and destination cannot be the same.")
        return
    
    if not os.path.exists(dst):
        os.makedirs(dst)

    counter = {}
    
    if recursive:
        for root, dirs, files in os.walk(src):
            for file in files:
                process_file(root, file, dst, max_size, counter)
    else:
        for file in os.listdir(src):
            process_file(src, file, dst, max_size, counter)

def process_file(root, file, dst, max_size, counter):
    """Process each file, move if matches criteria and handle renaming if necessary."""
    source_path = os.path.join(root, file)
    if os.path.isfile(source_path) and os.path.getsize(source_path) < max_size:
        destination_path = os.path.join(dst, file)
        destination_path = handle_conflict(destination_path, counter)
        try:
            shutil.move(source_path, destination_path)
            print(f"Moved {file} to {destination_path}")
        except Exception as e:
            print(f"Could not move {file}: {e}")

def handle_conflict(path, counter):
    """Handle file name conflicts by appending a counter."""
    original_path = path
    while os.path.exists(path):
        root, ext = os.path.splitext(original_path)
        counter[root] = counter.get(root, 0) + 1
        path = f"{root}_{counter[root]}{ext}"
    return path

def main():
    parser = argparse.ArgumentParser(description="Move files by size")
    parser.add_argument('-D', '--directory', action='store_true', help="Move files in the specified directory only")
    parser.add_argument('-S', '--subdirectories', action='store_true', help="Move files in the directory and all subdirectories")
    args = parser.parse_args()

    mode = "directory" if args.directory else "subdirectories"
    print_banner(mode)

    input_folder = input("Enter the input folder path: ")
    output_folder = input("Enter the output folder path: ")
    size = float(input("Enter the maximum file size to move: "))
    unit = input("Enter the unit of size (KB, MB, GB): ")

    size_in_bytes = convert_size(size, unit)

    if args.directory:
        move_files(input_folder, output_folder, size_in_bytes, recursive=False)
    elif args.subdirectories:
        move_files(input_folder, output_folder, size_in_bytes, recursive=True)

if __name__ == "__main__":
    main()
