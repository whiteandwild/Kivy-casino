import pickle , bcrypt
from errors import *


class storage:
    current_user = None #type -> user
    accounts = None
    c_root = None
    current_bet = 0

def hex_to_kv(hexcolor , alpha = 1): # Convert normal hex-code to stupid kivy color
    
    r = (int(hexcolor[1:3] ,16))/255
    g = (int(hexcolor[3:5] ,16))/255
    b = (int(hexcolor[5:7] ,16))/255
   
    return (r , g , b , alpha)

def make_bet(value):
    
    if value > storage.current_user.balance : return False

    storage.current_bet += value

    storage.current_user.balance -= value
    save()
    return storage.current_user.balance

def return_coins():
    storage.current_user.balance += storage.current_bet
    storage.current_bet = 0
    save()
    return storage.current_user.balance

def max_coins(): 
    return storage.current_user.balance

def bet_end(is_win , ratio):

    tmp = storage.current_bet
    storage.current_bet = 0

    if not is_win : return 0
    
    coins_won = tmp * ratio * 2
    storage.current_user.balance += coins_won
    save()
    return coins_won

def create_guest():

    storage.current_user = user("Guest" , "" , is_guest = True)
    



class user:
    def __init__(self , user_name , password , is_guest) -> None:
        self.user_name = user_name
        if not is_guest:
            self.password = get_hashed_password(password)
        self.balance = 1000
        self.totalBets = 0
        self.isHidden = False
        self.Active = True
        self.Autologin = False
    def __str__(self) -> str: #print info about user
        return f'{self.user_name}   balance : {self.balance} | total bets {self.totalBets}'



def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)

def save(): #saves storage.accounts
    with open("secret.pkl" , "wb") as secret:
        pickle.dump(storage.accounts , secret)

def create_account(user_name , password):
    if user_name in storage.accounts : return "User already exists"

    storage.accounts[user_name] = user(user_name , password , is_guest= False)
    save()
    
def delete_accout(user_name):
    if user_name in storage.accounts: return False

    del storage.accounts[user_name]

    save()
    

def login(user_name , password):


    print(storage.accounts)
    if user_name not in storage.accounts: # Not existing username
         return "Non-exitsing username"       
         raise NoUserException
    if storage.accounts[user_name].Active == False : 
        return "Account disabled"
    elif check_password(password ,storage.accounts[user_name].password) == False: 
        return "Invalid password"
    return True

def load_users_file(): # Load storage.accounts from secret file
    
    
    try:
        with open("secret.pkl" , "rb") as secret:
            storage.accounts = pickle.load(secret)
    except:
        storage.accounts = {}

    print(storage.accounts)

def fix_accounts():
    for acc in storage.accounts:
        u = storage.accounts[acc]

        tmp = user(u.user_name,None , True)
        
        tmp.password = u.password
        
        tmp.balance = u.balance
        try:
            tmp.totalBets = u.totalBets
        except:pass

        try:
            tmp.isHidden = u.isHidden
        except:pass

        try:
            tmp.Autologin = u.Autologin
        except:pass
        
        storage.accounts[acc] = tmp
    save()
        
