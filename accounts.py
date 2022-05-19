import pickle , bcrypt
from errors import *
from globals import *

class user:
    def __init__(self , user_name , password) -> None:
        self.user_name = user_name
        self.password = get_hashed_password(password)
        self.balance = 1000
    def __str__(self) -> str:
        return f'{self.user_name}   balance : {self.balance}'
try:
    with open("secret.pkl" , "rb") as secret:
        accounts = pickle.load(secret)
except:
    accounts = {}
print(accounts)


def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)

def save():
    with open("secret.pkl" , "wb") as secret:
        pickle.dump(accounts , secret)

def create_account(user_name , password):

    accounts[user_name] = user(user_name , password)
    save()
    
    
def login(user_name , password):
    if user_name not in accounts: raise NoUserException

    elif check_password(password ,accounts[user_name].password) == False: raise InvalidPassword

    return True

