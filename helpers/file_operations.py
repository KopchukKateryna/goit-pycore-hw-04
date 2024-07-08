from pathlib import Path


def create_path(path: str) -> Path:
    """
    A function that creates a directory if the path consists of dir, or
    creates a file

    Args:
        * path: path to the file or directory

    Returns:
        * class Path: path to the  created file or directory
    """
    p = Path(path)

    if p.is_absolute() or p.parent != Path("."):
        p.parent.mkdir(parents=True, exist_ok=True)

    p.touch(exist_ok=True)
    return p


def write_file(path: Path, data: str, encoding="utf-8"):
    """
    A function that writes data to file

    Args:
        * path (Path): Path to file
        * data (str): Data to write
        * encoding (str): Encoding to use. Default - utf-8

    Returns:
        * True or Error: True if data is written, and throws an Error instance if not.
    """
    if not isinstance(path, Path):
        raise TypeError("path must be a Path object")
    try:
        path.write_text(data, encoding)
        return True
    except FileNotFoundError as e:
        return FileNotFoundError(f"The file does not exist in this path: {e}")
    except IsADirectoryError as e:
        return IsADirectoryError(f"A path is a directory path, not a file: {e}")
    except PermissionError as e:
        return PermissionError(f"Permission denied: {e}")
    except Exception as e:
        return Exception(f"An error occurred while writing to the file: {e}")
