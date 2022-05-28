import json

with open('directory.json', 'r') as fileRead:
    df = json.loads(fileRead.read())

# with open('directory.json', 'w') as fileWrite:
#     df = json.loads(file)

class Operation:
    def allContacts():
        count = 0
        for key, value in df.items():
            count += 1
            print(f'''                ----------------------------------            
                #: {count}
                Name: {value["name"]}
                Contact No: {value["contact"]}
                ----------------------------------''')

    def searchContact():
        userInp = input("Enter Name or Contact Number or First Name or Last Name:\t")
        flag = False
        count = 0
        searchedContact = []
        searchedContactKey = []
        for key, value in df.items():
            if userInp in value["name"]:
                count += 1
                searchedContactKey.append(key)
                print(f'''                ----------------------------------            
                #: {count}
                Name: {value["name"]}
                Contact No: {value["contact"]}
                ----------------------------------''')
                flag = True
                searchedContact.insert(count-1, {count:{
                    "name":value["name"],
                    "contact_no":value["contact"]
                }})
            elif userInp in str(value['contact']):
                searchedContactKey.append(key)
                count += 1
                print(f'''                ----------------------------------            
                #: {count}
                Name: {value["name"]}
                Contact No: {value["contact"]}
                ----------------------------------''')
                flag = True
                searchedContact.insert(count-1, {count:{
                    "name":value["name"],
                    "contact_no":value["contact"]
                }})
        if flag == False:
                print(f"No Contact found having {userInp}")

        return flag, searchedContactKey

    def updateContact(func):
        def updateContactName(key):
            userInp = input("Enter new Name:\t")
            df[str(key)]["name"] = userInp
            with open("directory.json", 'w') as fileRead:
                fileRead.write(json.dumps(df))
            print(f"Name Successfully Update to {userInp}")

        def updateContactNumber(key):
            userInp = int(input("Enter new Number:\t"))
            df[str(key)]["contact"] = userInp
            with open("directory.json", 'w') as fileRead:
                fileRead.write(json.dumps(df))
            print(f"Contact Number Successfully Update to {userInp}")

        flag, contactKey = func
        if flag:
            userInp = int(input("Enter # of the contact you want to update:\t"))
            print(f"You Selected contact {userInp} to update")
            updateMenu = int(input('''                1) Update Name
                2) Update Contact Number

                What do you want to update?\t
            '''))

            if updateMenu == 1:
                updateContactName(contactKey[userInp-1])
            elif updateMenu == 2:
                updateContactNumber(contactKey[userInp-1])

    def addContact():
        newContactName = input("Enter Name:\t")
        newContactNumber = int(input("Enter Contact Number:\t"))
        # with open("directory.json", 'a') as fileAppend:
        df[str(len(df.keys()) + 1)] = {
            "name":newContactName,
            "contact":newContactNumber
        }
        with open("directory.json", "w") as fileWrite:
            fileWrite.write(json.dumps(df))
        print("Contact Added Successfully")

    def deleteContact(func):
        flag, contactKey = func
        if flag:
            userInp = int(input("Enter # of the contact you want to delete:\t"))
            df.pop(contactKey[userInp-1])
            with open("directory.json","w") as fileWrite:
                fileWrite.write(json.dumps(df))
            print("Contact deleted Successfully")