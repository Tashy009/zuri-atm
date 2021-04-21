import random


database = {}


def main():

    print('Welcome to ZURI bank')
    have_account = input('Do yo have account with us: 1. (Yes) 2. (No) \n')
    valid = check_valid(have_account)
    if valid:
        if (int(have_account) == 1):
            login()
        elif (int(have_account) == 2):
            print(register())
        else:
            print('You have selected an invalid option') 
            main()
    else:
        main()


def register():
    global account_number

    print('******************** Register ********************')
    print("********Please enter your correct details*********\n")

    first_name = ''
    while True:
        first_name = input('What is your Firstname: \n').capitalize()
        if first_name == '':
            print('input your first name')
        else:
            break

    last_name = ''
    while True:
        last_name = input('What is your Lastname: \n').capitalize()
        if last_name == '':
            print('input your last name')
        else:
            break
    
    email = ''
    while True:
        email = input('What is your email address: \n').capitalize()
        if email == '':
            print('input your email address')
        else:
            break

    password =''
    while True:
        password = input('Create a password for yourself: \n')
        if password == '':
            print('Create a password for yourself')
        else:
            break
    
    print("")
    account_number = generate_account_num()
    database[account_number] = [ first_name, last_name, email, password,  ]
    
    print('Your Accout have been created')
    print('====**************************====')
    print('Your account number is: %d' % account_number)
    print('====**************************====')
    
    
    login()

def check_valid(have_account):
    try:
        int(have_account)  
        return True
    except ValueError:
        print('Enter an integer')
        return False

def login():

    print('')
    account_number_from_user = input('What is your account Number: \n')
    is_valid = accountValidation(account_number_from_user)

    if is_valid:
        for account_number, detail in database.items():
            if(account_number == int(account_number_from_user)):
                password = input("What is your password \n")
                if(detail[3] == password):
                    bank_operation(detail)
                else:
                    print('Invalid password')
                    login()

            else:
                print('invalid account Number')
                login()
    else:
        main()

def accountValidation(account_number):

    if account_number:

        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True

            except ValueError:
                print('Invalid account number, account should be a Number')
                return False

        else:
            print('Account Number cannot be more or less than 10 digit')
            
    else:
        print('Account Number is required')
        return False

def bank_operation(detail):

    print('Welcome {} {}'.format(detail[0], detail[1]))

    selected_option = input('What would you like to do?\n 1. deposit\n 2. withdrawal\n 3. Exit\n ')
    

    try:
        if ( int(selected_option) == 1):
            deposit()

        elif (int(selected_option) == 2):
            withdrawal(account_number)

        elif (int(selected_option) == 3):
            logout()

        else:
            print('Invalid option choosen')
            bank_operation(detail)
            
    except ValueError:
        print('Enter an integer')
        bank_operation(detail)


def deposit():
    global account_number

    balance = 0
    amt_to_deposit = int(input('How much would you like to deposit:  '))
    balance +=amt_to_deposit

    if len(database[account_number]) == 5:
        database[account_number][4] += balance
    else:
        database[account_number].append(balance)

    print(f'Your new balance is {database[account_number][4]}')
    perform()


def withdrawal(account_number):
    withdraw_amt = int(input('How much would you like to withdraw \n'))
    get_balance = int(database[account_number][4])

    if withdraw_amt > get_balance:
        print('Account balance is low')
        withdrawal(account_number)

    elif withdraw_amt < get_balance:
        balance = get_balance - withdraw_amt
        database[account_number][4] = balance
        print('Take your cash')
        print(f'Your Account balance is {balance}')
        perform()


def perform():
    transaction = int(input('Do you want to peform another? 1.Yes 2.No:\n'))

    if (transaction == 1):
        login()

    elif (transaction == 2):
        logout()


def generate_account_num():
    accnum = random.randrange(1111111111, 9999999999)
    return accnum


def logout():
    print('Thanks for using our service')
    

main()