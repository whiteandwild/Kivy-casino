import os , time ,threading
from cards import *


decision_time = 10000

to_print = []

def wait_for_valid_input(l):
    
    while l[0] not in ["up" , "down"]:
        
        l[0] = input("Którą opcje wybierasz |up| , |down| :    ")


def printer():
    for elem in to_print:
        print(elem)
def timer():
    time_spend = 0
    while time_spend < decision_time:
        # print(decision_time-time_spend , flush=False , end=None )
        print(f"Pozostały czas {((decision_time-time_spend)/1000):.1f}")
        time.sleep(0.1)
        time_spend += 100
        
        
        



def main_loop():
    balance = 1000
    cards = generate_cards()
    
    current_card = choose_random_card(cards)
    
    remove_card(cards , current_card)
    os.system('CLS')
    print(f'Aktualna karta to {current_card}')
    print(f'kurs na wyższą karte to TEMPLATE / kurs na niższą karte to TEMPLATE')
  

    to_print.append(f'Aktualna karta to {current_card}')
    to_print.append(f'kurs na wyższą karte to TEMPLATE / kurs na niższą karte to TEMPLATE')
    user_input = [None]



    mythread = threading.Thread(target=wait_for_valid_input, args=(user_input,))
    
    

    t = 1 if user_input == "up" else 0
    new_card = choose_random_card(cards)
    
    if compare_cards(new_card , current_card , t):
        print("Wygrana")

    else:
        print("przegrana")
    
    
    
    
    timer()
    print("Nie zdecydowałeś się")
    


if __name__ == "__main__":
    main_loop()