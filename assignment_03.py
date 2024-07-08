"""
Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, 
виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.
"""
import sys
from pathlib import Path
from helpers.logs_operations import log_error, log_color


def print_tree(p, indent=""):
    """
    A function that prints the directory and file tree to the console

    Args:
        * p (Path): Path to the directory
    
    Returns:
        * prints the directory and file tree to the console
    """
    if p.is_dir():
        print(log_color(indent + p.name + "/", "blue"))
        indent += "    "
        for child in sorted(p.iterdir()):
            print_tree(child, indent)
    else:
        print(log_color(indent + p.name, "green"))


def list_files_and_directories(directory):
    """
    A function that handles errors and prints the directory and file tree to the console

    Args:
        * directory (str): Path to directory

    Returns:
        * prints the directory and file tree to the console
    """
    try:
        path = Path(directory).expanduser().resolve(strict=True)
    except FileNotFoundError as e:
        print(log_error(f"[Error] resolving the path: {e}"))
        return
    if not path.is_dir():
        print(log_error(f"The path {path} is not a directory."))
        return
    print_tree(path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please run script with a directory path ")
    else:
        directory_path = sys.argv[1]
        list_files_and_directories(directory_path)
