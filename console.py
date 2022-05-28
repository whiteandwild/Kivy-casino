from globals import * 
from accounts import save

def validate_access(current_user): # Check if user is admin acc
    return current_user.user_name == "admin"

def check_if_exist(user_name): # Check if user exits
    if user_name not in accounts:
        print('Non-existing user')
        return False
    return True

def get_all_users(): # Print all user's names
    print("\n Registred Users: ")
    for user in accounts:
        print(accounts[user].user_name)

def print_user(user_name): # Print user info
    if not check_if_exist(user_name) : return False
    
    print(accounts[user_name])
    return True

def set_balance(user_name , money): # Set balance of user
    if not check_if_exist(user_name) : return False
    accounts[user_name].balance = money
    save()
    return True

def remove_user(user_name): # Remove user's account
    if not check_if_exist(user_name) : return False

    del accounts[user_name]
    save()

