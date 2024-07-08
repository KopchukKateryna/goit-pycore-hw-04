"""
Розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та 
середню суму заробітної плати всіх розробників.
"""

from pathlib import Path

from constants.developers import developers
from helpers.file_operations import create_path, write_file


def total_salary(path):
    """
    Calculates the total and average salary from a given file. If the file does not exist,
    it creates the file and writes the data of developers constants into it.

    Args:
        path (str): The path to the file containing the salary data.

    Returns:
        tuple: A tuple containing the total salary and the average salary.
    """
    file_path = Path(path)
    if not file_path.exists():
        try:
            file_path = create_path(path)
            data = "\n".join([f"{dev['name']},{dev['salary']}" for dev in developers])
            write_file(file_path, data)
        except Exception as e:
            print(e)
    total_count = 0
    average_count = 0
    with open(file_path, "r", encoding="utf-8") as file_data:
        file_data = file_data.read().splitlines()
        total_count = sum(int(line.split(",")[1]) for line in file_data)
        average_count = total_count // len(file_data)

    return (total_count, average_count)


total, average = total_salary("assets/salary_file.txt")
print(f"Total salary: {total}, Average salary: {average}")
