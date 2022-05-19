from globals import * 
from accounts import save

def validate_access(current_user):
    return current_user.user_name == "admin"

def check_if_exist(user_name):
    if user_name not in accounts:
        print('Non-existing user')
        return False
    return True
def get_all_users():
    print("\n Registred Users: ")
    for user in accounts:
        print(accounts[user].user_name)
def print_user(user_name):
    if not check_if_exist(user_name) : return False
    
    print(accounts[user_name])
    return True
def set_balance(user_name , money):
    if not check_if_exist(user_name) : return False
    accounts[user_name].balance = money
    save()
    return True
def remove_user(user_name):
    if not check_if_exist(user_name) : return False

    del accounts[user_name]
    save()

get_all_users()