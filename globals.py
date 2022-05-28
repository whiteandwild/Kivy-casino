current_user = None #type -> user
accounts = None

def hex_to_kv(hexcolor , alpha = 1): # Convert normal hex-code to stupid kivy color
    r = (int(hexcolor[1:3] ,16))/255
    g = (int(hexcolor[3:5] ,16))/255
    b = (int(hexcolor[5:7] ,16))/255
   
    return (r , g , b , alpha)

