from globals import * 


def validate_access(current_user): # Check if user is admin acc
    return current_user.user_name == "admin"

def check_if_exist(user_name): # Check if user exits
    if user_name not in storage.accounts:
        print('Non-existing user')
        return False
    return True

def get_all_users(): # Print all user's names
    print("\n Registred Users: ")
    for user in storage.accounts:
        print(storage.accounts[user].user_name)

def print_user(user_name): # Print user info
    if not check_if_exist(user_name) : return False
    
    print(storage.accounts[user_name])
    return True

def set_balance(user_name , money): # Set balance of user
    if not check_if_exist(user_name) : return False
    storage.accounts[user_name].balance = money
    save()
    return True

def remove_user(user_name): # Remove user's account
    if not check_if_exist(user_name) : return False

    del storage.accounts[user_name]
    save()

