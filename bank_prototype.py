import re
import datetime
import random


def pay_bills(account_number):
    while True:
        print("Select the type of bill you want to pay:")
        print("1. Electricity Bill")
        print("2. Water Bill")
        print("3. Internet Bill")
        bill_type = input("Enter bill type: ")

        if bill_type == '1':
            amount = input("Enter the amount for electricity bill: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    print("Invalid amount. Amount should be greater than zero.")
                    continue
                balance = account_details[account_number]['Balance']
                if amount > balance:
                    print("Insufficient funds.")
                    break
                else:
                    account_details[account_number]['Balance'] -= amount
                    print(f"Electricity bill payment of ₦{amount} successful. Remaining balance: ₦{account_details[account_number]['Balance']}")
                    break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif bill_type == '2':
            amount = input("Enter the amount for water bill: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    print("Invalid amount. Amount should be greater than zero.")
                    continue
                balance = account_details[account_number]['Balance']
                if amount > balance:
                    print("Insufficient funds.")
                    break
                else:
                    account_details[account_number]['Balance'] -= amount
                    print(f"Water bill payment of ₦{amount} successful. Remaining balance: ₦{account_details[account_number]['Balance']}")
                    break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif bill_type == '3':
            amount = input("Enter the amount for internet bill: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    print("Invalid amount. Amount should be greater than zero.")
                    continue
                balance = account_details[account_number]['Balance']
                if amount > balance:
                    print("Insufficient funds.")
                    break
                else:
                    account_details[account_number]['Balance'] -= amount
                    print(f"Internet bill payment of ₦{amount} successful. Remaining balance: ₦{account_details[account_number]['Balance']}")
                    break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        else:
            print("Invalid choice. Please enter a valid option.")



def buy_airtime(account_number):
    while True:
        print("Select network provider:")
        print("1. MTN")
        print("2. Airtel")
        print("3. Glo")
        print("4. 9mobile")
        network_choice = input("Enter your choice: ")
        
        networks = {
            '1': 'MTN',
            '2': 'Airtel',
            '3': 'Glo',
            '4': '9mobile'
        }
        
        network = networks.get(network_choice)
        
        if not network:
            print("Invalid network choice.")
            return
        
        plans = {
            'MTN': {'100': 100, '200': 200, '500': 500},
            'Airtel': {'100': 100, '200': 200, '500': 500},
            'Glo': {'100': 100, '200': 200, '500': 500},
            '9mobile': {'100': 100, '200': 200, '500': 500}
        }
        
        print(f"Select airtime plan for {network}:")
        for amount, price in plans[network].items():
            print(f"{amount} - ₦{price}")
        
        amount_choice = input("Enter amount: ")
        price = plans[network].get(amount_choice)
        
        if not price:
            print("Invalid amount choice.")
            return
        
        balance = account_details[account_number]['Balance']
        if price > balance:
            print("Insufficient funds.")
            return
        else:
            balance -= price
            account_details[account_number]['Balance'] = balance
            print(f"Airtime purchase of ₦{amount_choice} for {network} successful. Remaining balance: ₦{balance}")
            return

def buy_data(account_number):
    while True:
        print("Select network provider:")
        print("1. MTN")
        print("2. Airtel")
        print("3. Glo")
        print("4. 9mobile")
        network_choice = input("Enter your choice: ")
        
        networks = {
            '1': 'MTN',
            '2': 'Airtel',
            '3': 'Glo',
            '4': '9mobile'
        }
        
        network = networks.get(network_choice)
        
        if not network:
            print("Invalid network choice.")
            return
        
        data_plans = {
            'MTN': {'1GB': 1000, '2GB': 2000, '5GB': 5000},
            'Airtel': {'1GB': 1000, '2GB': 1500, '3GB': 2000},
            'Glo': {'1GB': 1000, '2GB': 1500, '4.5GB': 2000},
            '9mobile': {'1GB': 1000, '1.5GB': 1500, '4GB': 3000}
        }
        
        print(f"Select data plan for {network}:")
        for plan, price in data_plans[network].items():
            print(f"{plan} - ₦{price}")
        
        plan_choice = input("Enter data plan: ")
        price = data_plans[network].get(plan_choice)
        
        if not price:
            print("Invalid data plan choice.")
            return
        
        balance = account_details[account_number]['Balance']
        if price > balance:
            print("Insufficient funds.")
            return
        else:
            balance -= price
            account_details[account_number]['Balance'] = balance
            print(f"Data purchase of {plan_choice} for {network} successful. Remaining balance: ₦{balance}")
            return



            

print("Welcome to AGT Bank")

countries_states = {
    "Nigeria": ["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", 
                "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe", "Imo", "Jigawa", 
                "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", 
                "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara",
                "Federal Capital Territory (FCT)"],
}
account_details = {}

while True:
    print("Enter 1 to create an account")
    print("Enter 2 to view account")
    print("Enter 3 to make a transaction")
    print("Enter 4 to buy airtime or data")
    print("Enter 5 to pay bills")
    print("Enter 6 to update account information")
    print("Enter 7 to exit")
    user_input = input("Enter a number: ")

    if user_input ==  '1':
        print("Select the type of account:")
        print("1. Savings Account")
        print("2. Current Account")
        account_type = input("Enter account type: ")

        while True: 
            fullname = input("Enter full name: ")
            if not re.match("^[A-Za-z ]+$", fullname):
                print("Full name can only contain alphabets and spaces")
                continue
            else:
                break
        
        while True:
            dob_str = input("Enter date of birth (YYYY-MM-DD): ")
            try:
                dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d")
                age = (datetime.datetime.now() - dob).days // 365
                if age < 18:
                    print("You must be at least 18 years old to open an account.")
                    continue
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        
        while True:
            contact = input("Enter mobile number:")
            if len(contact) != 11:
                print("Mobile number should be 11 digits long") 
                continue
            else:
                break
        
        while True:
            country = input("Enter country: ")
            if country.isdigit():
                print("Please enter a valid country name")
                continue
            else:
                break
        
        while True:
            state = input("Enter state of origin: ")
            if state not in countries_states['Nigeria']:
                print("State not found in the entered country. Please enter a valid state without adding the state at the end.")
                continue
            else:
                break
        
        while True: 
            bvn = input("Enter BVN: ")
            if not re.match("^[0-9]{11}$", bvn):
                print("BVN should be an 11-digit number")
                continue
            else:
                break    
        
        while True:     
            email = input("Enter email: ")
            if not re.match("[^@]+@[^@]+[^@]+", email):
               print("Invalid email address")
               continue
            else:      
               break    
        
        while True:       
            password = input("Enter password (at least 8 characters): ")
            if len(password) < 8:
                print("Password should be at least 8 characters long")
                continue
            else:
                # Generate a random 8-digit account number
                account_number = ''.join([str(random.randint(0, 9)) for _ in range(8)])
                print("\nPlease review your account details:")
                print(f"Full Name: {fullname}")
                print(f"Date of Birth: {dob_str}")
                print(f"Mobile Number: {contact}")
                print(f"State: {state}")
                print(f"Country: {country}")
                print(f"BVN: {bvn}")
                print(f"Email: {email}")
                print(f"Account Number: {account_number}")
                print(f"Account Type: {'Savings' if account_type == '1' else 'Current'}")
                confirmation = input("Confirm account creation (yes/no): ").lower()
                if confirmation == "yes":
                    account_details[account_number] = {
                        'Full Name': fullname,
                        'Date of Birth': dob_str,
                        'Mobile Number': contact,
                        'State': state,
                        'Country': country,
                        'BVN': bvn,
                        'Email': email,
                        'Password': password,
                        'Account Type': 'Savings' if account_type == '1' else 'Current',
                        'Balance': 0  # Initialize balance to zero
                    }
                    print("Account created successfully")
                    break
                else:
                    print("Account creation canceled")
                    continue
    elif user_input == '2':
        while True:    
            account_number = input("Enter your account number: ")
            if account_number not in account_details:
                print('Account not found. Please enter a valid account number.')
                break
            else:
                account = account_details[account_number]
                print("Account Details:")
                for key, value in account.items():
                    print(f"{key}:{value}")
                break
    elif user_input == '3':
        while True:  
            account_number = input("Enter your account number: ")
            if account_number not in account_details:
                print('Account not found. Please enter a valid account number.')
            else:    
                print("Press 1 to fund account")
                print("Press 2 to withdraw")
                print("Press 3 to transfer")
                user_t = input("Enter a number: ")
                if user_t == '1':
                        account_number = input("Enter your account number: ")
                        if account_number not in account_details:
                            print('Account not found. Please enter a valid account number.')
                            break
                        else:
                            user_fund = input("Enter amount to fund: ")
                            user_fund = int(user_fund)
                            account_details[account_number]['Balance'] += user_fund
                            print('Account funded successfully')
                            break
                if user_t == '2':
                    while True:
                        account_number = input("Enter your account number: ")
                        if account_number not in account_details:
                            print('Account not found. Please enter a valid account number.')
                            break
                        else:
                            user_w = input("Enter amount to withdraw: ")
                            user_w = int(user_w)
                            balance = account_details[account_number]['Balance'] 
                            if user_w > balance:
                                print("Insufficient funds. Please fund your account.")
                                break
                            else:   
                                balance -= user_w
                                account_details[account_number]['Balance'] = balance
                                print("Withdrawal successful")
                                print("Current balance:", balance)
                                break
                if user_t == '3':
                    while True:
                        sender_account = input("Enter your account number: ")
                        if sender_account not in account_details:
                            print('Sender account not found. Please enter a valid account number.')
                            break           
                        else:
                            receiver_account = input("Enter recipient's account number: ")
                            transfer_amount = input("Enter amount to transfer: ")
                            transfer_amount = int(transfer_amount)
                            sender_balance = account_details[sender_account]['Balance']
                            if transfer_amount > sender_balance:
                                print("Insufficient funds.")
                                break
                            else:
                                receiver_balance = account_details.get(receiver_account, {'Balance': 0})['Balance']
                                sender_balance -= transfer_amount
                                receiver_balance += transfer_amount
                                account_details[sender_account]['Balance'] = sender_balance
                                account_details[receiver_account] = {'Balance': receiver_balance}  # Create receiver account if not exists
                                print("Transfer successful")
                                break
    elif user_input == '4':
        while True:
            sender_account = input("Enter your account number: ")
            if sender_account not in account_details:
                print('Account not found. Please enter a valid account number.')
                break
            else:
                print("Press 1 to buy airtime")
                print("Press 2 to buy data")
                service_choice = input("Enter your choice: ")
                if service_choice == '1':
                    buy_airtime(sender_account)
                    break
                elif service_choice == '2':
                    buy_data(sender_account)
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
                    break
    elif user_input == '5':
        while True:
            sender_account = input("Enter your account number: ")
            if sender_account not in account_details:
                print('Account not found. Please enter a valid account number.')
                break
            else:
                pay_bills(sender_account)
                break    
    elif user_input == '6':
        while True:
            if not account_details:
                print("No account found. Please create an account first.")
                break
            else:
                account_number = input("Enter your account number: ")
                if account_number not in account_details:
                    print('Account not found. Please enter a valid account number.')
                    break
                else:
                    print("Select the detail you want to update:")
                    print("1. Full Name")
                    print("2. Date of Birth")
                    print("3. Mobile Number")
                    print("4. State")
                    print("5. Country")
                    print("6. BVN")
                    print("7. Email")
                    print("8. Password")
                    detail_choice = input("Enter your choice: ")
                    
                    if detail_choice == '1':
                        fullname = input("Enter fullname: ")
                        splitted_fullname = fullname.split(' ')
                        for i in splitted_fullname:
                            if i.isdigit():
                                print("Fullname: only alphabet allowed")
                                break
                        else:
                            account_details[account_number]['Full Name'] = fullname
                            print("Fullname updated successfully")
                    
                    elif detail_choice == '2':
                        date_of_birth = input("Enter dob (YYYY-MM-DD): ")
                        try:
                            datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
                            account_details[account_number]['Date of Birth'] = date_of_birth
                            print("Dob updated successfully")
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")
                    
                    elif detail_choice == '3':
                        contact = input("Enter mobile number: ")
                        if not contact.isdigit() or len(contact) != 11:
                            print("Invalid mobile number. Mobile number should be 11 digits long and contain only numbers.")
                        else:
                            account_details[account_number]['Mobile Number'] = contact
                            print("Mobile number updated successfully")
                    
                    elif detail_choice == '4':
                        state = input("Enter state of origin: ")
                        account_details[account_number]['State'] = state
                        print("State of origin updated successfully")
                    
                    elif detail_choice == '5':
                        country = input("Enter country: ")
                        account_details[account_number]['Country'] = country
                        print("Country updated successfully")
                    
                    elif detail_choice == '6':
                        bvn = input("Enter BVN: ")
                        if not re.match("^[0-9]{11}$", bvn):
                            print("Invalid BVN. BVN should be an 11-digit number.")
                        else:
                            account_details[account_number]['BVN'] = bvn
                            print("BVN updated successfully")
                    
                    elif detail_choice == '7':
                        email = input("Enter email: ")
                        if '@' not in email or '.' not in email:
                            print("Invalid email address")
                        else:
                            account_details[account_number]['Email'] = email
                            print("Email updated successfully")
                    
                    elif detail_choice == '8':
                        password = input("Enter password: ")
                        if len(password) < 8:
                            print("Invalid password. Password should be at least 8 characters long.")
                        else:
                            account_details[account_number]['Password'] = password
                            print("Password updated successfully")

                    else:
                        print("Invalid choice. Please enter a valid option.")
                    
                    update_more = input("Do you want to update more details? (yes/no): ").lower()
                    if update_more != "yes":
                        break

        else:                                              
            print("Invalid input. Please try again.")
    elif user_input == '7':
        break


                   



