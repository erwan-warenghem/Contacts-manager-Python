# ===
# === CONTACT MANAGER PYTHON V1 ===
# ===

# == Definition of functions
def display_menu():
    """ Allow to display the textual menu of the program
        Serves as a guide for the user
        """
    print(f"\n---------- Contact Manager Menu ----------\n")
    print("1. Add contact")
    print("2. View contact")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Filter contact")
    print("6. Exit contact manager program")

def add_contact(contacts_book):
    """ Allow to add a new contact in the main dictionary
    
        Args:
            contacts_book : the main dictionary that contains the contacts
            
        Logic:
            1- Check if a contact already exists to avoid duplicates 
            2- Add the data in a sub dictionary
            """
    
    name = input(f"Please type the name contact you want to add in contact manager: ").strip().lower()
    # Validation : we check if the name already exist in contact dict
    if name in [c["Name"] for c in contacts_book.values()]:
        print(f"ERROR - Contact {name} already exist!")
        return # leaving the function prematurely
    # Secondary data colleection (email, perso_phone, pro_phone, contact_type)
    email = input(f"\nType the email adresse of {name} contact: ").lower() #add security for '"+"!?,
    perso_phone = input(f"\nType the personnal phone of {name} contact: ").digit #add security for space and alphabetic character 
    pro_phone = input(f"\nType the professional phone of {name} contact: ") #add security for space and alphabetic character
    contact_type = input(f"\nType the type of contact (ex : town hall, individual, association, bar, etc.) of {name} contact: ")
    # Define the ID number
    next_id = max(contacts_book.keys(), default = 0) + 1
    # Formating the contact ID
    contact_id = f"Contact-{next_id:02d}"
    # Structured storage in a sub-dictionary
    contacts_book[contact_id] = {"Name" : name.capitalize(),
                                 "Email" : email,
                                 "Personal phone" : perso_phone,
                                 "Professionnal phone" : pro_phone,
                                 "Contact type" : contact_type
                                 }
    print(f"\nContact {name} succesfully added!")

def view_contact():
    """ Allow to show data of an existant contact
        Args: 
            contacts_book : the main dictionary that contains the contacts
        
        Logic:
            1- Check if the contact exist
            2- Print the contact data
        """
    name = input(f"Please type the name contact you want to consult: ").strip().lower()
    # Validation : we check if the name already exist in contact dict
    if name in [c["Name"] for c in contacts_book.values()]:
        print(f"ERROR - Contact {name} doesn't exist!")
        return # leaving the function prematurely
    print()

def edit_contact():
    """ Allow to edit data of an existant contact
        Args: 
            contacts_book : the main dictionary that contains the contacts
        
        Logic:
            1-
            2-
        """
    pass

def delete_contact():
    """ Allow to delete an existant contact
        Args: 
            contacts_book : the main dictionary that contains the contacts
        
        Logic:
            1-
            2-
        """
    pass

def filter_contact():
    """ Allow to show a list of filtered existant contacts
        Args: 
            contacts_book : the main dictionary that contains the contacts
        
        Logic:
            1-
            2-
        """
    pass

# == Program launch
contacts_book = {} # Initialization of the main dictionary
while True:
    display_menu()
    choice = int(input(f"\nPlease type your choice (1-6): "))
    if choice == 1:
        add_contact(contacts_book)
    elif choice == 2:
        view_contact()
    elif choice == 3:
        edit_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        filter_contact()
    elif choice == 6:
        print(f"\n [END] Goddbye!")
        break # Exit program
    else:
        print(f"\n [ERROR] Please choose an option betwen 1 and 6!")