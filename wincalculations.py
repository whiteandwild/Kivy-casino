# from cards import generate_cards , choose_random_card , compare_cards
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
        k = 8 * MatchingCards ** (log((1/5) , totalCards/2))
        # k = 10 * MatchingCards ** (log((1/5) , totalCards/2))
        # print(8 * MatchingCards ** (log((1/5) , totalCards/2)))
        # print(10 * MatchingCards ** (log((1/5) , totalCards/2)))
        
        # if k < 2 : k = 2

  
    
    return int(bet * k * mul)

def test():
    c = generate_cards()

    s = None
    s = choose_random_card(c)

    choose = -1
   
    print(LowerHigherWin(1000 , c , s , 2 , choose , 1))


def tests():

    tests_amouts = 5000
    wins = 0
    loses = 0

    for i in range(tests_amouts):

        c = generate_cards()
        a = choose_random_card(c)
        b = choose_random_card(c)

        if compare_cards(a , b ,-1):
            wins +=1
        else: loses +=1


    print(wins , loses)

# tests()