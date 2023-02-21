"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
#%%
face_cards = {"J": 10, "Q": 10, "K": 10}
numbered_cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,}
black_jack = 21

def value_of_card(card):
    if card in face_cards:
        return 10
    elif card == "A":
        return 1
    elif card in numbered_cards:
        return int(card)

def higher_card(card_one, card_two):
    card_one_val = value_of_card(card_one)
    card_two_val = value_of_card(card_two)
    
    if card_one_val > card_two_val:
        return card_one
    elif card_two_val > card_one_val:
        return card_two
    else:
        return card_one, card_two

#%%
def new_value_of_card(card):
    if card in face_cards:
        return 10
    elif card == "A":
        return 11
    elif card in numbered_cards:
        return int(card)
    
    
def value_of_ace(card_one, card_two):
    card_one = new_value_of_card(card_one)
    card_two = new_value_of_card(card_two)
    
    if card_one + card_two <= 10:
        return 11
    else:
        return 1
    

def is_blackjack(card_one, card_two):
   card_one = new_value_of_card(card_one)
   card_two = new_value_of_card(card_two)
   
   if card_one + card_two == 21:
       return True
   else:
       return False


def can_split_pairs(card_one, card_two):
    card_one = new_value_of_card(card_one)
    card_two = new_value_of_card(card_two)
   
    if card_one == card_two:
       return True
    else:
       return False


def can_double_down(card_one, card_two):
    yes = [9,10,11]
    card_one = value_of_card(card_one)
    card_two = value_of_card(card_two)
    
    if card_one + card_two in yes:
        return True
    else:
        return False
    

# %%
