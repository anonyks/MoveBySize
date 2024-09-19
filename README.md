# MoveBySize ~ #Only4ThoseWhoKnows

`MoveBySize` is a Python script tailored for users who need to organize large quantities of files across directories. It allows for sorting files by size within specified ranges and can operate within a single directory or recursively through subdirectories. This utility also handles potential duplicates by renaming them, ensuring no data loss during the operation.

## Features

- **Flexible Size Sorting**: Move files based on a specified size range, such as 0 to <1024 KB or any other defined range.
- **Dual Mode Operation**: Works in two modes, allowing users to target a single directory (`-D` mode) or include all subdirectories (`-S` mode).
- **Duplicate Handling**: Automatically renames duplicate files during the moving process to prevent overwriting.

## Getting Started

### Prerequisites

Before running `MoveBySize`, ensure you have Python installed on your system. This script also depends on the `pyfiglet` library for generating ASCII art headers.

Install `pyfiglet` using pip:

```bash
pip install pyfiglet
```

### Installation

Clone this repository to get started with `MoveBySize`:

```bash
git clone https://github.com/anonyks/MoveBySize.git
cd MoveBySize
```

### Usage

To use `MoveBySize`, run the script with the appropriate mode flag depending on your needs:

**For single directory mode:**

```bash
python MoveBySize.py -D
```

**For recursive subdirectory mode:**

```bash
python MoveBySize.py -S
```

Follow the prompts to specify the input and output directories, the maximum file size to move, and the unit of size (KB, MB, GB).

## Contributing

Contributions are welcome! If you have improvements or bug fixes, please fork the repository and submit a pull request. You can also open an issue if you encounter problems or have suggestions for new features.


## Contact

- Coder: @AnonyKs_xD
- Telegram: [https://t.me/@AnonyKs_xD](https://t.me/@AnonyKs_xD)
