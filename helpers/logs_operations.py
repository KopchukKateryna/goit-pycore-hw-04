from colorama import init, Fore, Style


init(autoreset=True)


def log_error(msg: str) -> str:
    """
    A function that returns a formatted string in red.

    Args:
      * msg(str): The message to be formatted.
      
    Returns:
      * str: The formatted message.
    """
    return f"{Fore.RED}{Style.BRIGHT}{msg}{Style.RESET_ALL}"


def log_color(msg: str, color) -> str:
    """
    A function that returns a formatted string in a given color.

    Args:
      * msg(str): The message to be formatted.
      * color(str): The color to be used.

    Returns:
      * str: The formatted message.
    """
    color_code = getattr(Fore, color.upper(), Fore.WHITE)
    return f"{color_code}{Style.BRIGHT}{msg}{Style.RESET_ALL}"
