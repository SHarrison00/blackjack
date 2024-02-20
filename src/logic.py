from itertools import product
import random
from enum import Enum

class RoundOutcome(Enum):
    DEALER_WIN = "DEALER_WIN"
    PLAYER_WIN = "PLAYER_WIN"
    PUSH = "PUSH"
    PLAYER_BLACKJACK = "PLAYER_BLACKJACK"
    DEALER_BLACKJACK = "DEALER_BLACKJACK"


class Insurance(Enum):
    YES = "YES"
    NO = "NO"


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


def offer_insurance():
    while True:
        decision = input("The dealer's upcard is an Ace. Do you want to take insurance? (yes/no) ").upper()
        if decision == Insurance.YES.value:
            return True
        elif decision == Insurance.NO.value:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def ask_player_for_hit():
    while True:
        decision = input("Do you want to hit or stand? ").lower()
        if decision == 'hit':
            return True
        elif decision == 'stand':
            return False
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")


def check_for_bust(hand_value):
    return hand_value > 21


def ask_player_stake(bankroll):
    available_stakes = [1, 2, 5, 10, 20, 50, 100]

    while True:
        print(f"\n\n\n\n\nYour current bankroll is ${bankroll}. Choose your stake:")
        print(", ".join([f"${stake}" for stake in available_stakes]))
        try:
            stake = int(input("Enter your stake: $"))
            if stake not in available_stakes:
                print("Invalid stake. Please choose from the available options.")
            elif stake > bankroll:
                print("You cannot stake more than your bankroll.")
            else:
                return stake
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def ask_player_end_game():
    while True:
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return False
        elif choice in ['no', 'n']:
            return True
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def update_bankroll(bankroll, stake, outcome, insur_decision):
    # Insurance bet is half the stake
    insurance_bet = stake / 2
    
    # Payout ratios
    blackjack_payout = 1.5
    insurance_payout = 2  

    if outcome == RoundOutcome.DEALER_WIN:
        if insur_decision == Insurance.YES:
            return bankroll - stake - insurance_bet
        else:
            return bankroll - stake
    elif outcome == RoundOutcome.PLAYER_WIN:
        if insur_decision == Insurance.YES:
            return bankroll + stake - insurance_bet
        else:
            return bankroll + stake
    elif outcome == RoundOutcome.PUSH:
        if insur_decision == Insurance.YES:
            return bankroll - insurance_bet
        else:
            return bankroll
    elif outcome == RoundOutcome.PLAYER_BLACKJACK:
        if insur_decision == Insurance.YES:
            return bankroll + (stake * blackjack_payout) - insurance_bet
        else:
            return bankroll + (stake * blackjack_payout)
    elif outcome == RoundOutcome.DEALER_BLACKJACK:
        if insur_decision == Insurance.YES:
            return bankroll - stake + (insurance_bet * insurance_payout)
        else:
            return bankroll - stake
    else:
        raise ValueError("Invalid outcome or insurance decision")