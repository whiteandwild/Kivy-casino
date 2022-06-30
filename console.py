from globals import * 


def validate_access(current_user): # Check if user is admin acc
    return current_user.user_name == "admin"

def check_if_exist(user_name): # Check if user exits
    if user_name not in storage.accounts:
        print('Non-existing user')
        return False
    return True

def get_all_users(args): # Print all user's names
    output = []
    for user in storage.accounts:
        output.append(f'{user} - {storage.accounts[user].user_name}')
    return output

def getusersObjects(showhidden = False):
    output = []
    for u in storage.accounts:
        tmp = storage.accounts[u]
        if not showhidden and not tmp.isHidden:
            output.append(tmp)
        else:
            output.append(tmp)
    return output

def getUser(user_name , showhidden = False):
    if user_name not in storage.accounts:
        return "User not found"
    
    tmp = storage.accounts[user_name]
    if tmp.isHidden and not showhidden:
        return "User not found"
    
    return tmp



def print_user(args): # Print user info
    

    showhidden = False

    if len(args) > 1:
        if args[1] == "--showhidden":
            showhidden = True
        else:
            return ["Invalid flag argument"]
    if args[0] == "all":
        output = []
        for u in getusersObjects(showhidden=showhidden):
            output.append(u.__str__())
        return output
    else:   
        tmp = getUser(user_name = args[0],showhidden=showhidden)
        if not isinstance(tmp,user): return [tmp]

        return [tmp.__str__()]
  

def set_balance(args): # Set balance of user

    tmp = getUser(user_name = args[0],showhidden=True)
    if not isinstance(tmp,user): return [tmp]

    tmp.balance = int(args[1])
    save()
    return True

def remove_user(args): # Remove user's account
    tmp = getUser(user_name = args[0],showhidden=True)
    if not isinstance(tmp,user): return [tmp]

    del storage.accounts[args[0]]
    save()
    return [f"Removed user {args[0]}"]

def create_user(args):
    if len(args) != 2:
        return ["Invalid parameters"] 

    r = create_account(args[0] , args[1] , False)

    if r != True:
        return [r]
    return [f"user {args[0]} created"]

def reset_acc(args):
    storage.current_user.reset()
    return ["Acc reseted"]

def balance(args):
    return [f"your balance is {storage.current_user.balance}"]

def send_balance(args):
    if len(args) != 2 or not args[1].isnumeric():
        return ["Invalid parameters" , "send_balance <user> <amount>"]
    if args[0] not in storage.accounts:
        return ["User not found"]
    b = int(args[1])
    if b > storage.current_user.balance:
        return ["Not enought balance"]
    
    storage.current_user.balance -= b
    storage.accounts[args[0]].balance += b
    save()

    return [f"Transfered {b} coins to {args[0]}"]

def get_user_commands():
    return {"help" : help , "balance" : balance , "send_balance" : send_balance, 'reset_account' : reset_acc}
def get_admin_commands():
    return get_user_commands() | {"set_balance": set_balance , "remove_user" : remove_user , "get_all_users" : get_all_users , "create_user" : create_user , "print_user" : print_user}

def help(args):
    output = []

    output.append("help - this command")
    output.append("balance - your balance")
    output.append("send_balance <user> <amount> - send balance to user")
    output.append("reset_account - resets your acc")
    if storage.current_user.isAdmin:
        output.append("set_balance <user> <new_balance> - set balance of a user")
        output.append("remove_user <user> - removes user")
        output.append("create_user <user_name> <password> - creates user")
        output.append("print_user <user/all> - show user info . Use --showhidden to see hidden users")

    return output

