# Initializing system

import random
import datetime      
database = {}


def init():
     
    print('===========|  WELCOME TO \'SAYO BANK  |===========')
    answer = int(input('Do you have an account with us:\n (1) Yes\n (2) No\nSelect an option\n'))
       
    if(answer == 1):
        login()

    elif (answer == 2):
        register()
    else:
        print('You have selected an invalid option')
        init()



# creating a Login function to include:(Account number or Full name, Password)
def login():
    print('==========| Login |==========')

    user_account_number = int(input('Enter your account number.\n'))
    password = input('Enter your password.\n')

    for account_number, user_details in database.items():
        if(account_number == user_account_number):
            if(user_details[-2] == password):
                print('============================')
                bank_operation(user_details)

            else:
                print('Invalid account or password')
                login()

        from datetime import timedelta
        print(str(datetime.datetime.now()))

        
    

# Registering a new user which to include:(First Name, Last Name, Password, Email)

def register():

    print('==========| Fill in you details |==========')

    title = int(input('select a title:\n(1) Mr\n(2) Mrs\n(3) Miss\n'))
    first_name = input('Enter First Name\n')
    last_name = input('Enter Last Name\n')
    email = input('Enter a vaild email address\n')
    password = input('Enter your preferred password\n')
    full_name = first_name + ' ' + last_name
   

    account_number = genarate_account_number()

    database[account_number] = [title, first_name, last_name, email, password, 1000]
    
    print('Your account number has been generated %s'  %full_name.capitalize())
    print('=== ==== ==== ==== ==== ==== ==== ===')
    print('This is your account number: %d' %account_number)
    
    login()
          
   
# Generating account number and its function
def genarate_account_number():
    return random.randrange(0000000000, 9999999999)
  
  
# creating bank operation function

def bank_operation(user):
    
    print('Welcome %s %s' %(user[1], user[2].capitalize()))
    print('Which transaction would you like to perform?\n (1) Withdrawal\n (2) Deposit\n (3) Complaint\n (4) Logout\n  (5) Available balance\n (6) Exit\n')
    
    choice = int(input("Please select an option\n"))

    if (choice == 1):
        
        withdrawal()  
    elif (choice ==2):
        
        deposit()
    elif (choice ==3):
        
        complaint()
    elif (choice == 4):
        login()
    elif (choice ==5):

        available_balance()    
    elif (choice == 6):
        exit()
    else:
        print('You have selected an invalid option.\nTry again.')
        bank_operation(user)



#_____(Creating deposit, withdrawal, complaint and logout function)
def withdrawal():
    amount = int(input("Enter an amount to withdraw\n"))
    if amount >= 1000:
        print('Insufficient funds')
    else:
        print('Take your cash.\nThank you for banking with us.')

    new_transaction = int(input('Do you want to perform another transaction\n (1)Yes\n (2)No\n'))
    
    if new_transaction == 1:
        
        bank_operation(user)
    elif new_transaction == 2:
        print('Take your card\n Thank you for banking with us')
        exit()


def deposit():
    amount_deposited = float(input('Enter amount to deposit.\n'))
    print(f"Your deposit of ${amount_deposited} is successful")
    new_transaction = int(input('Do you want to perform another transaction\n (1)Yes\n (2)No\n'))

    if (new_transaction == 1):

        bank_operation(user)
    elif (new_transaction == 2):
        print('Take your card\n Thank you for banking with us')
        exit()

def complaint():
    user_complaint = input('What is you complaint?\n')
    print('Thank you for contacting us.\nYour complaint will be resolved in 48 hours\nPlease bear with us.')
    new_transaction = int(input('Do you want to perform another transaction\n (1)Yes\n (2)No\n'))

    if (new_transaction == 1):

        bank_operation(user)
    elif (new_transaction == 2):
        print('Take your card\nThank you for banking with us')
        exit()

def logout():
    #This would logout user and refer back to login 
    login()

def available_balance():
    
    for user_details in database.items():
        return user_details[-1]




init()

