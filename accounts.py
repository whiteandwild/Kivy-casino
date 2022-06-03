import pickle , bcrypt #saving | hashing passwords
from errors import *
from globals import *

class user:
    def __init__(self , user_name , password) -> None:
        self.user_name = user_name
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

def save(): #saves accounts
    with open("secret.pkl" , "wb") as secret:
        pickle.dump(accounts , secret)

def create_account(user_name , password):
    if user_name in accounts : return "User already exists"

    accounts[user_name] = user(user_name , password)
    save()
    
    
def login(user_name , password):
    if user_name not in accounts: raise NoUserException # Not existing username
    if accounts[user_name].Active == False : raise NoUserException # Account is disabled

    elif check_password(password ,accounts[user_name].password) == False: raise InvalidPassword # Wrong password

    return True

def load_users_file(): # Load accounts from secret file
    global accounts

    try:
        with open("secret.pkl" , "rb") as secret:
            accounts = pickle.load(secret)
    except:
        accounts = {}
