from itertools import product
import random
from enum import Enum

class RoundOutcome(Enum):
    PUSH = "PUSH"
    PLAYER_BLACKJACK = "PLAYER_BLACKJACK"

def generate_deck():
    suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    ranks = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    return list(product(suits, ranks))


def shuffle(deck):
    return random.shuffle(deck)


def card_value(card):
    rank = card[1]

    if rank in ['K', 'Q', 'J']:
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank)

    
def hand_value(hand):
    hand_val = 0  
    ace_count = 0

    for card in hand:
        hand_val += card_value(card)
        if card[1] == 'A':
            ace_count += 1

    while ace_count > 0 and hand_val > 21:
        hand_val -= 10
        ace_count -= 1

    return hand_val

    
def draw_card(deck):
    return deck.pop()
     

def draw_hand(deck):
    return [deck.pop(), deck.pop()]


def check_for_blackjack(hand):
    return len(hand) == 2 and hand_value(hand) == 21


class InsuranceOption(Enum):
    YES = "YES"
    NO = "NO"

def offer_insurance():
    while True:
        decision = input("The dealer's upcard is an Ace. Do you want to take insurance? (yes/no) ").upper()
        if decision == InsuranceOption.YES.value:
            return True
        elif decision == InsuranceOption.NO.value:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def player_turn(deck, player_hand):
    while True:
        print("Player's Hand:", player_hand)

        if hand_value(player_hand) == 21:
            print("You have 21!")
            return None
        
        decision = input("Do you want to hit or stand? ").lower()

        if decision == 'hit':
            player_hand.append(draw_card(deck))
            if hand_value(player_hand) > 21:
                print("Bust! You went over 21.")
                return "BUST"
        elif decision == 'stand':
            return None
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")