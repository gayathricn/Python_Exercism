"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):

    if card in {'J', 'Q','K'}:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)



def higher_card(card_one, card_two):

    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two
    elif value_of_card(card_one) > value_of_card(card_two):
        return card_one
    else:
        return card_two
    

def value_of_ace(card_one, card_two):

    if card_one == 'A' or card_two == 'A':
        return 1
    
    total = value_of_card(card_one) + value_of_card(card_two)

    if total + 11 > 21:
        return 1
    else:
        return 11



def is_blackjack(card_one, card_two):
  
    if card_one == 'A' and value_of_card(card_two) == 10 or (card_two == 'A' and value_of_card(card_one) == 10):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False
    
def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    if total == 9 or total == 10 or total == 11:
        return True
    else:
        return False