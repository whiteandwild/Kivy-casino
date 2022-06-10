from accounts import *

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
    return storage.current_user.balance
def return_coins():
    storage.current_user.balance += storage.current_bet
    storage.current_bet = 0
    return storage.current_user.balance

def max_coins(): return storage.current_user.balance

def bet_end(is_win , ratio):

    tmp = storage.current_bet
    storage.current_bet = 0

    if not is_win : return 0
    
    coins_won = tmp * ratio * 2
    storage.current_user.balance += coins_won

    return coins_won

def create_guest():

    storage.current_user = user("Guest" , "" , is_guest = True)
    