"""
розробити функцію get_cats_info(path), яка читає файл та повертає 
список словників з інформацією про кожного кота.
"""

from pathlib import Path

from constants.cats import cats
from helpers.file_operations import create_path, write_file


def get_cats_info(path: str) -> list:
    """
    Retrieves information about cats from a specified file. If the file does not exist,
    it creates the file with predefined data and then reads the information.

    Args:
        path (str): The file path where the cat information is stored.

    Returns:
        list: A list of dictionaries. Each containing the id, name, and age of a cat.
    """
    file_path = Path(path)
    if not file_path.exists():
        try:
            file_path = create_path(path)
            data = "\n".join(
                [f"{cat['id']},{cat['name']},{cat['age']}" for cat in cats]
            )
            write_file(file_path, data)
        except Exception as e:
            print(e)
    cats_dict = []
    with open(file_path, "r", encoding="utf-8") as file_data:
        file_data = file_data.read().splitlines()
        cats_dict = [
            {"id": cat[0], "name": cat[1], "age": cat[2]}
            for line in file_data
            for cat in [line.split(",")]
        ]

    return cats_dict


cats_info = get_cats_info("assets/cats_file.txt")
print(cats_info)
