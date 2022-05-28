import operation
import sys

opt = operation.Operation

def intro():
    try:
        print('''
        Welcome to the Phone Directory
        ------------------------------
        1) Show All Contacts
        2) Search for Contact
        3) Add New Contact
        4) Update Contact
        5) Delete Contact
        0) Quit
    ''')

        user_inp = int(input("Select any one of the option above:\t"))
        if user_inp == 1:
            print("----------------------All Contacts----------------------")
            opt.allContacts()
            intro()
        elif user_inp == 2:
            print("----------------------Search Contacts----------------------")
            opt.searchContact()
            intro()
        elif user_inp == 3:
            print("----------------------Add New Contact----------------------")
            opt.addContact()
            intro()
        elif user_inp == 4:
            print("----------------------Update Contact----------------------")
            opt.updateContact(opt.searchContact())
            intro()
        elif user_inp == 5:
            print("----------------------Delete Contact----------------------")
            opt.deleteContact(opt.searchContact())
            intro()
        elif user_inp == 0:
            sys.exit()
        else:
            print("----------------------No Operation Found Try Again----------------------")
            intro()
    except Exception as e:
        print(f"Unknown exception occured: {e}")

intro()