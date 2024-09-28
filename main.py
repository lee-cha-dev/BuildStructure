import os
import datetime

# Directories and files to ignore
IGNORE_LIST = {
    '.git', '.github', '.gitignore', '.prettierrc', '.idea',
    '.vscode', '__pycache__', 'venv', 'env', 'node_modules'
}


# Generate the initial path and write the items in the directory to file
def generate_structure(startpath, basename, output_file):
    with open(output_file, 'w') as f:
        f.write(f"Project Structure (generated on {datetime.datetime.now()}):\n\n")
        f.write(f"{os.path.basename(basename)}/\n")
        for item in sorted(os.listdir(startpath)):
            if item in IGNORE_LIST:
                continue
            if os.path.isdir(os.path.join(startpath, item)):
                _write_directory(f, startpath, item, 1)
            else:
                f.write(f"├── {item}\n")


def _write_directory(f, parent, dirname, level):
    indent = '│   ' * (level - 1) + '├── '
    f.write(f"{indent}{dirname}/\n")
    path = os.path.join(parent, dirname)
    items = sorted(os.listdir(path))
    for i, item in enumerate(items):
        if item in IGNORE_LIST:
            continue
        if i == len(items) - 1:
            new_indent = '│   ' * level + '└── '
        else:
            new_indent = '│   ' * level + '├── '
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            _write_directory(f, path, item, level + 1)
        else:
            f.write(f"{new_indent}{item}\n")


def ensure_structure_dir():
    if not os.path.exists('structure'):
        os.makedirs('structure')


def main():
    ensure_structure_dir()
    output_file = os.path.join('structure', 'project_structure.txt')
    generate_structure('./', os.path.basename(os.getcwd()), output_file)
    print(f"Project structure has been written to {output_file}")


if __name__ == "__main__":
    main()
