# project 
# Name: Anointing Adebayo

# phone boot
# 1. save contacts (name,number)
# 2. delete saved contacts
# 3. make a call call
# 4. view and search contacts(search by name or number)

                
# contact dictionary 
contacts = {}

# function to store contacts in the dictionary
def add_contacts():
    name = input('Contact name: ')
    phone_number = input('Phone number: ')
    if phone_number.isalpha():
        print('Alphabets are not allowed')
    else:
        if  name in contacts:
            print("Name already exist")
        if phone_number in contacts:
            print("Contact already exist")    
        else:
            contacts[name] = [phone_number] 
            for index, number in enumerate(contacts[name], start=1):
                print(f'{index}. {name.title()}   Contact: {number}')
            print('Contact saved successfully')
      
      
#function to search , update , and delete  contacts   
def search_contacts():
    search = input("Search for contacts: ")
    found = False
    index = 1

    for name in contacts:
        if search in name or name.startswith(search) or name.endswith(search):
            found = True
            phone_numbers = contacts[name]
            for number in phone_numbers:
                print(f'{index}. {name}, contact: {number}')
                index += 1
    
    if found:
        print("Select a contact by name:")
        user_select = input("Enter name: ")
        if user_select in contacts:
            print("1. Delete contact")
            print("2. Update contact")
            user_input = input("Enter a number: ")

            if user_input == '1':
                del contacts[user_select]
                print('Contact deleted')
            elif user_input == '2':
                new_name = input("Enter the new name (leave blank to keep the current name): ")
                if new_name == "":
                    new_name = user_select
                if new_name != user_select:
                    contacts[new_name] = contacts.pop(user_select)
                print("Current phone numbers:", contacts[new_name])
                new_number = input("Enter the new phone number (leave blank to keep current numbers): ")
                if new_number:
                    contacts[new_name] = [new_number]
                    for index, number in enumerate(contacts[new_name], start=1):
                            print(f'Updated contact list for {index}. {new_name}: {number}')
            else:
                print("Enter a number according to the option displayed")
        else:
            print("Name not found or incorrect")
    else:
        print("No contacts found matching the search criteria")

                
                
#function to view contacts 
def view_contacts():
    if not contacts:
        print('No contacts available')
    else:
        for name,Phone_number in contacts.items():
            print("Contacts:")
            print(f'name: {name}\nphone number: {Phone_number}\n')    





        
# logic 
while True:
    print('phone book')
    print('1: Add contacts/save contact')
    print('2: search for contact')
    print('3: view contact')
    print('4: make a call')
    user = input('Enter a number: ')
    if user == '1':
        while True:
            add_contacts()
            break
    elif user == '2':
        while True:
            search_contacts()
            break
    elif user == '3':
        while True:
            view_contacts()
            break
    elif user == '4':
        while True:
            search = input("Search for contacts: ")
            found = False
            index = 1
            for name in contacts:
                if search in name or name.startswith(search) or name.endswith(search):
                    found = True
                    phone_numbers = contacts[name]
                    for number in phone_numbers:
                        print(f'{index}. {name}, contact: {number}')
                        index += 1
            if found:
                print("Select a contact by name:")
                user_select = input("Enter name: ")
                if user_select in contacts:
                    print("1. make a call")
                    user_input = input("Enter a number: ")
                    print("calling.......",user_select)
                    print("calling........",user_select)
                    break
    else:
        print('please enter a number')    

        



