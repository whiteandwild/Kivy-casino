import pickle , bcrypt



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

def bet_end(is_win , coins_won):

    tmp = storage.current_bet
    storage.current_bet = 0

    Round_update_stats(tmp ,iswin=is_win , win=coins_won)
    if not is_win : return 0
    
    
    storage.current_user.balance += coins_won
    save()
    return coins_won

def Round_update_stats(bet , iswin , win = 0):
    storage.current_user.totalBets += bet
    storage.current_user.wins += iswin
    storage.current_user.loses += not iswin

    storage.current_user.maxBet = max(storage.current_user.maxBet , bet)
    if iswin:
        storage.current_user.maxWin = max(storage.current_user.maxBet , win)

def create_guest():

    storage.current_user = user("Guest" , "" , is_guest = True)

def calc_winratio(user):

    total = user.wins + user.loses
    if user.loses == 0 : return 100 if user.wins > 0 else 0

    
    return int(user.wins / total * 100)




class user:
    def __init__(self , user_name , password , is_guest) -> None:
        self.user_name = user_name
        if not is_guest:
            self.password = get_hashed_password(password)
        self.balance = 1000
        self.totalBets = 0
        self.isHidden = False
        self.isAdmin = False
        self.Active = True
        self.Autologin = False
        self.maxBet = 0
        self.maxWin = 0
        self.wins = 0
        self.loses = 0

    def __str__(self) -> str: #print info about user
        return f'{self.user_name} balance : {self.balance} | total bets {self.totalBets}'

    def reset(self):
        self.balance = 1000
        self.totalBets = 0
        self.maxBet = 0
        self.wins = 0
        self.loses = 0
        self.maxWin = 0


def get_hashed_password(plain_text_password):
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password, hashed_password)

def save(): #saves storage.accounts
    with open("secret.pkl" , "wb") as secret:
        pickle.dump(storage.accounts , secret)

def create_account(user_name , password ,rememberme):
    if user_name in storage.accounts : return "User already exists"

    storage.accounts[user_name] = user(user_name , password , is_guest= False)
    if rememberme:
        storage.current_user.Autologin = True
    save()
    return True
    
def delete_account(user_name):
    if user_name not in storage.accounts: return False

    del storage.accounts[user_name]

    save()
    

def login(user_name , password , rememberme):
    if user_name not in storage.accounts: # Not existing username
         return "Non-exitsing username"       
    if storage.accounts[user_name].Active == False : 
        return "Account disabled"
    elif check_password(password ,storage.accounts[user_name].password) == False: 
        return "Invalid password"

    storage.current_user = storage.accounts[user_name]
    if rememberme:
        storage.current_user.Autologin = True
        save()

    return True

def logout():
    if storage.current_user.Autologin:
        storage.current_user.Autologin = False
        save()
    
    create_guest()

def SearchAutoLogin():
    for account in storage.accounts:
        if storage.accounts[account].Autologin:
            print("Found auto login")
            storage.current_user = storage.accounts[account]
            return True
    return False

def DisableAutoLogin():
    for account in storage.accounts: storage.accounts[account].Autologin = False

def load_users_file(): # Load storage.accounts from secret file
    
    
    try:
        with open("secret.pkl" , "rb") as secret:
            storage.accounts = pickle.load(secret)
    except:
        storage.accounts = {}

    print(storage.accounts)

def fix_accounts():

    tmp = user("",None , True)

    attrs = vars(tmp)

    for acc in storage.accounts:
        u = storage.accounts[acc]
        for attr in attrs:
            exec(f"u.{attr} = getattr(u , '{attr}' , tmp.{attr})")
        
        

        # tmp = user(u.user_name,None , True)
        
        # tmp.password = getattr(u , "password" , "")
        # tmp.balance = getattr(u , "balance" , 0)
        # tmp.totalBets = getattr(u , "totalBets" , 0)
        # tmp.isHidden = getattr(u , "isHidden" , False)
        # tmp.Autologin = getattr(u , "Autologin" , False)
        # tmp.Active = getattr(u , "Active" , True)

        # storage.accounts[acc] = tmp
    print(storage.accounts)
    save()
        
