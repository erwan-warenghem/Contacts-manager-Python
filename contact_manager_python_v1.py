# ========================================================================================================
# CONTACT MANAGER PYTHON V1.1
# ========================================================================================================
# Athors : Erwan Warenghem
# Description: Contact manager with unique IDs and full CRUD functionality.

# --------------------------------------------------------------------------------------------------------
# 1. IMPORT EXTERNAL MODULE
# --------------------------------------------------------------------------------------------------------

import subprocess
import platform

# --------------------------------------------------------------------------------------------------------
# 2. DEFINITION OF FUNCTIONS
# --------------------------------------------------------------------------------------------------------

def clean_screen():
    """ 
    Clear the terminal using the modern subprocess module.

    Args:
        None

    Returns:
        None: This function executes a system command and returns nothing.

    Logic:
        1. Identify the OS using platform.system().
        2. Execute 'cls' for Windows or 'clear' for others via subprocess.
    """
    command = "cls" if platform.system() == "Windows" else "clear"
    subprocess.run(command, shell=True)

def find_id(directory, searched_name):
    """
    Match a contact name to its unique ID within the directory.

    Args:
        directory (dict): The main contact database.
        searched_name (str): The name to look for.

    Returns:
        int : The unique ID of the contact.
        None : If no contact matches the name.

    Logic:
        1. Normalize 'searched_name' using .capitalize() to match stored format.
        2. Perform a list comprehension over directory items to find matching 'Name' values.
        3. Return the first ID (key) from the resulting list to handle potential duplicates.
    """
    res = [cid for cid, info in directory.items() if info["Name"] == searched_name.capitalize()]
    if res:
        return res[0]
    else:
        return None

def display_menu():
    """ Display a textual menu to navigate the program.

        Serves as a visual guide for the user to select available actions.
    """
    print(f"\n---------- Contact Manager Menu ----------\n")
    print("1. Add contact")
    print("2. View contact")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Filter contact")
    print("6. Exit contact manager program")

def add_contact(contacts_book):
    """ 
    Create a new contact record and store it in the main dictionary.

    Args:
        contacts_book (dict): The main dictionary containing all contact records.

    Returns: 
        None : This function modifies the dictionary in place.

    Logic:
        1. Normalize and check if the name already exists using find_id().
        2. If the contact exists, print an error message and go back to Menu.
        3. Collect secondary data (email, phones, type), storing None for empty inputs.
        4. Generate a unique integer ID based on the current maximum key value.
        5. Store all information in a nested dictionary under the new ID.
    """

    name = input(f"\nPlease type the name contact you want to add in contact reccord: ").strip().lower() # TODO For V1.2 => add security with function : clean_name
    # Validation : we check if the name already exist in contact dict
    if find_id(contacts_book, name):
        print(f"\n[ERROR] - Contact {name.capitalize()} already exist!")
        input("\nPress Enter to return to the menu...")
        return # leaving the function prematurely
    # Secondary data colleection (email, perso_phone, pro_phone, contact_type)
    email = input(f"\nType the email adresse of {name.capitalize()} contact: ").lower() or None # TODO For V1.2 => add security with function : clean_email
    perso_phone = input(f"\nType the personal phone of {name.capitalize()} contact: ") or None # TODO For V1.2 => add security with function : clean_phone
    pro_phone = input(f"\nType the professional phone of {name.capitalize()} contact: ") or None # TODO For V1.2 => add security with function : clean_phone
    contact_type = input(f"\nType the type of contact (ex : town hall, individual, association, bar, etc.) of {name.capitalize()} contact: ") or None
    contact_id = max(contacts_book.keys(), default = 0) + 1 # Define the ID number
    # Structured storage in a sub-dictionary
    contacts_book[contact_id] = {"Name" : name.capitalize(),
                                 "Email" : email,
                                 "Personal phone" : perso_phone,
                                 "Professionnal phone" : pro_phone,
                                 "Contact type" : contact_type
                                 }
    print(f"\n[OK] - Contact {name.capitalize()} successfully added!")
    input("\nPress Enter to return to the menu...")

def view_contact(contacts_book):
    """
    Search and display all information for a specific contact.

    Args:
        contacts_book (dict): The main dictionary containing all contact records.

    Returns:
        None: This function prints to the console and does not return a value.

    Logic:
        1. Check if the directory is empty
        2. If main dictonary is empty, display an error message and go back to Menu.
        3. Retrieve contact ID using find_id (handles name normalization).
        4. If no ID is found, display an error message and go back to Menu.
        5. Access the sub-dictionary and print each field with clear labels.
    """

    # Validation : we check if the main dictionary is empty
    if not contacts_book:
        print(f"\n[ERROR] - The contact reccord is empty!")
        input("\nPress Enter to return to the menu...")
        return  # leaving the function prematurely
    name = input(f"\nPlease type the contact name you want to consult: ").strip().lower()
    # Validation : we check if the name exist in contact dict
    contact_id = find_id(contacts_book, name)
    if contact_id is None:
        print(f"\n[ERROR] - Contact {name.capitalize()} doesn't exist!")
        input("\nPress Enter to return to the menu...")
        return # leaving the function prematurely
    else:
        info = contacts_book[contact_id] # We go one level down (sub dictionary) and fix there for display the formatted data
        print() # Line break to separate the contact blocks
        print(f"Name                  : {info['Name']}")
        print(f"Email                 : {info['Email'] or 'Not provided'}")
        print(f"Personal phone        : {info['Personal phone'] or 'Not provided'}")
        print(f"Professionnal phone   : {info['Professionnal phone'] or 'Not provided'}")
        print(f"Contact type          : {info['Contact type'] or 'Not provided'}")
        print() # Line break to separate the contact blocks
        input("\nPress Enter to return to the menu...")


def edit_contact(contacts_book):
    """ Search and edit information of an existing contact.
        Args: 
            contacts_book (dict): The main dictionary containing all contact records.

        Returns: 
            None : This function modifies the dictionary in place.

        Logic:
            1. Check if the directory is empty
            2. If main dictonary is empty, display an error message and go back to Menu.
            3. Retrieve contact ID using find_id (handles name normalization).
            4. If no ID is found, display an error message and go back to Menu.
            5. Access the sub-dictionary and edit the contact info or keep the old one.
        """

    # Validation : we check if the main dictionary is empty
    if not contacts_book:
        print(f"\n[ERROR] - The contact reccord is empty!")
        input("\nPress Enter to return to the menu...")
        return  # leaving the function prematurely
    name = input(f"\nPlease type the contact name you want to edit: ").strip().lower()
    # Validation : we check if the name exist in contact dict
    contact_id = find_id(contacts_book, name)
    if contact_id is None:
        print(f"\n[ERROR] - Contact {name.capitalize()} doesn't exist!")
        input("\nPress Enter to return to the menu...")
        return # leaving the function prematurely
    else:
        info = contacts_book[contact_id] # We go one level down (sub dictionary) and fix there for display the formatted data
        info["Email"] = input(f"\nType the new email adresse of {name.capitalize()} contact or press Enter to skip: ").lower().strip() or info["Email"] # TODO For V1.2 => add security with function : clean_email
        info["Personal phone"] = input(f"\nType the new personal phone of {name.capitalize()} contact or press Enter to skip: ").strip() or info["Personal phone"] # TODO For V1.2 => add security with function : clean_phone
        info["Professionnal phone"] = input(f"\nType the new professional phone of {name.capitalize()} contact or press Enter to skip: ").strip() or info["Professionnal phone"] # TODO For V1.2 => add security with function : clean_phone
        info["Contact type"] = input(f"\nType the new type of contact (ex : town hall, individual, association, bar, cofee shop) of {name.capitalize()} contact or press Enter to skip: ").strip() or info["Contact type"] # TODO STR must be in list of choice 
        print(f"\n[OK] - Contact successfully edited!")
        input("\nPress Enter to return to the menu...")

def delete_contact(contacts_book): 
    """ Search and  delete an existant contact.
        Args: 
            contacts_book : the main dictionary that contains the contacts

        Logic:
            1. Check if the directory is empty
            2. If main dictonary is empty, display an error message and go back to Menu.
            3. Retrieve contact ID using find_id (handles name normalization).
            4. If no ID is found, display an error message and go back to Menu.
            5. Confirmation of deletion
            6. If yes, delete the contact thanks to the contact_id.
            7. If no, display a cancelled message and go back to Menu.
        """

    # Validation : we check if the main dictionary is empty
    if not contacts_book:
        print(f"\n[ERROR] - The contact reccord is empty!")
        input("\nPress Enter to return to the menu...")
        return  # leaving the function prematurely
    name = input(f"\nPlease type the contact name you want to delete: ").strip().lower()
    # Validation : we check if the name exist in contact dict
    contact_id = find_id(contacts_book, name)
    if contact_id is None:
        print(f"\n[ERROR] - Contact {name.capitalize()} doesn't exist!")
        input("\nPress Enter to return to the menu...")
        return # leaving the function prematurely
    else:
        confirm = input(f"\nDo you confirm to delete {name.capitalize()} contact? Type Y or N: ").lower().strip() # TODO add security if not Y or N in str!
        if confirm == "y" :
            del contacts_book[contact_id]
            print(f"\n[OK] - Contact {name.capitalize()} successfully deleted!")
            input("\nPress Enter to return to the menu...")
        else:
            print(f"\n[CANCELlED] - Deletion aborted!")
            input("\nPress Enter to return to the menu...")
            return # leaving the function prematurely


def filter_contact(contacts_book): # TODO Codding the function!
    """ Allow to show a list of filtered existant contacts
        Args: 
            contacts_book : the main dictionary that contains the contacts
        
        Logic:
            1-
            2-
        """
    pass

# --------------------------------------------------------------------------------------------------------
# 1. PROGRAM LAUNCH (Main Loop)
# --------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    contacts_book = {} # Initialization of the main dictionary
    while True:
        clean_screen()
        display_menu()
        try:
            choice = int(input(f"\nPlease type your choice (1-6): "))
        except ValueError:
            choice = -1  # Invalide value manage by the else
        if choice == 1:
            add_contact(contacts_book)
        elif choice == 2:
            view_contact(contacts_book)
        elif choice == 3:
            edit_contact(contacts_book)
        elif choice == 4:
            delete_contact(contacts_book)
        elif choice == 5:
            filter_contact(contacts_book)
        elif choice == 6:
            print(f"\n [END] Goddbye!")
            break # Exit program
        else:
            print(f"\n [ERROR] Please choose an option between 1 and 6!")
            input("\nPress Enter to return to the menu...")