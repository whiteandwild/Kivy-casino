import random

cards_symbols = {"♣" : ["clubs" ,0 ] , "♦" : ["diamonds" ,1 ] , "♥" : ["hearts" ,2 ] , "♠" : ["spades" ,3 ]}
cards_orders = {'2': ["2",0], '3': ["3" , 1], '4': ["4" ,2] , '5': ["5",3], '6': ["6",4], '7': ["7",5], '8': ["8",6], '9': ["9",7] , 
                '10' : ["10",8] , "J" : ["jack" , 9] , "Q" : ["queen" , 10] , "K" : ["king" , 11] , "A" : ["ace" , 12]
}

class card:
    def __init__(self , symbol , figure) -> None:
        self.symbol = symbol
        self.figure = figure
        if figure != "joker":
            self.src = f"photos/{cards_orders[figure][0]}_of_{cards_symbols[symbol][0]}.png" # Src for card's photo

    def __str__(self) -> str:
        return f'{self.symbol}{self.figure}'

def generate_cards(): # Generates all cards
    cards = []
    for figure in cards_orders.keys():
        for symbol in cards_symbols.keys():
            c = card(symbol , figure)
            c.score = cards_symbols[symbol][1]  + cards_orders[figure][1] * 10
            cards.append(c)
    Rjoker = card(None , "joker")
    Bjoker = card(None , "joker")
    Rjoker.score , Bjoker.score = 130 , 131
    Rjoker.src , Bjoker.src = "photos/red_joker.png" , "photos/black_joker.png"
    cards.extend([Rjoker , Bjoker])

    return cards


choose_random_card = lambda cards : random.choice(cards) # Rolls 1 card

def compare_cards(cardA , cardB , t):
    """
    t - > 1 look for higher card
    t - > 0 look for joker
    t - > -1 look for lower card
    """
    match t:
        case 1: return cardA.score < cardB.score
        case -1: return cardA.score > cardB.score
        case 0 : return cardB.figure == "joker"
    