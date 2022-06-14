import pickle , bcrypt #saving | hashing passwords

from globals import storage


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
        pickle.dump(storage.acc , secret)

def create_account(user_name , password):
    if user_name in storage.accounts : return "User already exists"

    storage.acc[user_name] = user(user_name , password)
    save()
    
    
def login(user_name , password):
    if user_name not in storage.accounts: raise NoUserException # Not existing username
    if storage.accounts[user_name].Active == False : raise NoUserException # Account is disabled

    elif check_password(password ,storage.accounts[user_name].password) == False: raise InvalidPassword # Wrong password

    return True

def load_users_file(): # Load storage.accounts from secret file
    
    print(storage)
    try:
        with open("secret.pkl" , "rb") as secret:
            storage.acc = pickle.load(secret)
    except:
        storage.acc = {}
