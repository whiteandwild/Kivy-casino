import random

cards_symbols = {"♣" : ["clubs" ,0 ] , "♦" : ["diamonds" ,1 ] , "♥" : ["hearts" ,2 ] , "♠" : ["spades" ,3 ]}
cards_orders = {'2': ["2",0], '3': ["3" , 1], '4': ["4" ,2] , '5': ["5",3], '6': ["6",4], '7': ["7",5], '8': ["8",6], '9': ["9",7] , 
                '10' : ["10",8] , "J" : ["jack" , 9] , "Q" : ["queen" , 10] , "K" : ["king" , 11] , "A" : ["ace" , 12]
}

class card:
    def __init__(self , symbol , figure) -> None:
        self.symbol = symbol
        self.figure = figure
        self.score = cards_symbols[symbol][1]  + cards_orders[figure][1] * 10
        self.src = f"photos/{cards_orders[figure][0]}_of_{cards_symbols[symbol][0]}.png" # Src for card's photo

    def __str__(self) -> str:
        return f'{self.symbol}{self.figure}'

def generate_cards(): # Generates all cards
    cards = []
    for figure in cards_orders.keys():
        for symbol in cards_symbols.keys():
            cards.append(card(symbol , figure))
    return cards


choose_random_card = lambda cards : random.choice(cards) # Rolls 1 card

def compare_cards(cardA , cardB , t):
    """
    t - > 1 look for higher card
    t - > 0 look for lower card
    """
    return cardA.score > cardB.score if t else cardA.score < cardB.score 
    
def remove_card(cards , c):
    cards.remove(c)
