current_user = None #type -> user
accounts = None

def hex_to_kv(hexcolor , alpha = 1): # Convert normal hex-code to stupid kivy color
    r = (int(hexcolor[1:3] ,16))/255
    g = (int(hexcolor[3:5] ,16))/255
    b = (int(hexcolor[5:7] ,16))/255
   
    return (r , g , b , alpha)

def make_bet(value):
    if value < current_user.balance : return False

    current_user.balance -= value
    return value

def max_coins(): return current_user.balance

def bet_end(bet , is_win , ratio):
    if not is_win : return

    current_user.balance += bet * ratio

    return current_user.balance