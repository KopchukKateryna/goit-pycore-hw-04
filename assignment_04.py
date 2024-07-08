def parse_input(user_input: str):
    """
    A function that receives the row, breaks it into words,
    the first word leads to lower case and removes extra characters.

    Args:
        * user_input (str): The user input.
    Returns:
        * cmd (str): the first word of the string without spaces in lower case
        * args (list): the rest of the words in the string
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list, contacts: dict):
    """
    A function that adds a new contact to the contacts dictionary.

    Args:
        * args (list): the list of words after the command
        * contacts (dict): the dictionary of contacts
    Returns:
    * str: "Contact added."
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list, contacts: dict):
    """
    A function that changes the phone number of an existing contact.

    Args:
        * args (list): the list of words after the command
        * contacts (dict): the dictionary of contacts

    Returns:
        * str: "Contact changed." if success and "Contact not found." if failed.
    """
    name, phone = args
    if name in contacts:
        contacts.update({name: phone})
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args: list, contacts: dict):
    """
    A function that shows the phone number of a contact.
    
    Args:
        * args (list): the list of words after the command
        * contacts (dict): the dictionary of contacts
    
    Returns:
        * str: the phone number if found and "Contact not found." if failed.
    """
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def list_all(contacts: dict):
    """
    A function that lists all contacts and their phone numbers.
    
    Args:
        * contacts (dict): the dictionary of contacts
    
    Returns:
        * str: the list of contacts and their phone numbers.
    """
    all_contacts = "\n".join([
        f"{name}: {phone}" for name, phone in contacts.items()
    ])
    return all_contacts


def main():
    """
        This is a simple phonebook application.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(list_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
