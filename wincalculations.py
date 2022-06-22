# from cards import generate_cards , choose_random_card
from math import log
def LowerHigherWin(bet , cards , c_card ,jokers ,choose , mul):
    
    # 0 Joker
    # 1 Higher
    # -1 Lower

    totalCards = len(cards)
    c_cardScore = c_card.score
    
    # Jokers
    if choose == 0:
        if jokers == 0 : return 0
        return bet * 10 if jokers == 2 else bet*15

    MatchingCards = 0

    if choose == -1:
        for card in cards:
            if card.score < c_cardScore: MatchingCards +=1
    if choose == 1:
        for card in cards:
            if card.score > c_cardScore: MatchingCards +=1
        
    ratio = (MatchingCards / totalCards)

    
    if MatchingCards == 0 : return 0

    if ratio >= 0.5:
        k = -2 / totalCards * MatchingCards + 3
    else:
        k = 10 * MatchingCards ** (log((1/5) , totalCards/2))
        

    print(bet * k * mul  , k , mul)
    
    return int(bet * k * mul)

# def test():
#     c = generate_cards()

#     s = None
#     for card in c:
#         if card.symbol == "♦" and card.figure == "2":
#             s = card

#     choose = -1
   
#     print(LowerHigherWin(1000 , c , s , 2 , choose , 1))


# test()