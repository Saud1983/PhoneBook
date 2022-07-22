# Python 101 challenge
phonebook = {"Amal": 1111111111, "Mohammed": 2222222222, "Khadijah": 3333333333,
             "Abdullah": 4444444444, "Rawan": 5555555555, "Faisal": 6666666666,
             "Layla": 7777777777}
running = True  # To keep the program running until the user choose to quit.


def new_entry():
    """This function is for adding new entry to the Telephone Book"""

    add = True  # To give the user a chance to double check his entry before submitting it.
    while add:
        t_key = input("Please Enter the Person Name:\n")  # To save a new kay temporarily until the final approval.
        t_value = input("Please Enter the Phone Number:\n")  # To save a new value temporarily until the final approval.
        print(f"The person's name is: '{t_key}', The phone number is: '{t_value}'\n")
        submit = input("Enter 'Y' to save the entry or simply enter any value to add them again\n").lower()

        if submit == "y":  # Save the new key/value pair to the phonebook.
            t_key = t_key.lower().capitalize()
            phonebook[t_key] = int(t_value)
            add = False


def validation(entry):
    """This function is the first validation: used to make sure the entry is a valid number or a correct name"""

    search1 = entry.lower().capitalize()  # Search1 is to correct the name formatting: used ONLY when the 2nd option is True.
    if entry.isnumeric() and len(entry) == 10:  # Must be a numeric value with length of 10.
        search_number(int(entry))

    elif search1 in phonebook.keys():  # Used if searching by names.
        print(f"{phonebook[search1]}\n")

    else:  # If the validation has failed.
        print("This is invalid entry\n")


def search_number(t_number):
    """This function is used to reverse the key/value pair so it can print the key when searching by a value"""

    if t_number in phonebook.values():  # A second validation to make sure that the value entry is in the phonebook.
        reversed_telephone_book = {}  # Temporary container to be used only if the entry was a value not a key.
        for name, number in phonebook.items():
            reversed_telephone_book[number] = name  # The value became a key and the key became a value.
        print(f"{reversed_telephone_book[t_number]}\n")
    else:
        print("Sorry, the number is not found\n")


while running:  # Starting the program.
    choice = input("To search by a person enter the 'Name'.\n"
                   "To search by a phone Number enter the 'number'.\n"
                   "Enter '%%' to view all the numbers.\n"
                   "Enter '@!' for adding a new entry.\n"
                   "Enter '##' to quit.\n ")


#choices
    if choice == "@!":
        new_entry()

    elif choice == "##":
        running = False

    elif choice == "%%":
        for key, value in phonebook.items():
            print(f"{key} : {value}")
        print("")

    else:
        validation(choice)


#test The connection between both pcs in Oct 29, 2021
