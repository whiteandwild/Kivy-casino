
from cards import *


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