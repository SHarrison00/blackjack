from itertools import product
import random

def build_deck():
    """
    Create a deck of playing cards.

    Returns:
        list of tuples: A deck of playing cards.
    """
    suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = list(product(suits, ranks))
    return deck


def shuffle(deck):
    """
    Shuffle a deck of playing cards.

    Returns:
        list of tuples: A shuffled deck of playing cards.
    """  
    return random.shuffle(deck)


def card_value(card):
    """
    Returns:
        int: Value of a single card.
    """
    rank = card[1]
    if rank in ['K', 'Q', 'J']:
        return 10
    elif rank == 'A':
        return 11
    else:
        numerical_value = rank if rank.isdigit() else 10
        return int(numerical_value)
    

def hand_value(hand):
    """
    Calculate the value of a hand in Blackjack.

    Args:
        hand (list of tuples): The player's hand, i.e., a list of card tuples.

    Returns:
        int: The value of the hand.
    """
    # Initialize the total value of the hand
    total_value = 0  
    # Initialize count for 'Ace' cards in hand
    ace_count = 0

    # Calculate the value of each card in the hand using card_value function
    for card in hand:
        # Calculate the value of the current card using the card_value function
        card_val = card_value(card)
        # Update the total_value by adding the card's value
        total_value += card_val
        # Check if the card is an 'Ace' and update ace_count accordingly
        if card[1] == 'A':
            ace_count += 1

    # In this 'while' loop:
    # Check if there are 'Ace' cards in the hand (ace_count > 0)
    # and if the total_value exceeds 21 (total_value > 21)
    while ace_count > 0 and total_value > 21:
        # If both conditions are met, adjust the value of 'Ace' cards:
        # - Deduct 10 from total_value, i.e change the value of 'Ace' from 11 to 1
        # - Decrement ace_count for each 'Ace' adjusted
            # TODO: Conor ...
        total_value -= 10
        ace_count -= 1
    return total_value

    
def draw_card(deck):
    """
    Draw a single card from the deck.

    Args:
        deck (list of tuples): The deck of playing cards.

    Returns:
        tuple: A single card.
    """
    return deck.pop()
     

def draw_initial_hand(deck):
    """
    Draw an initial hand of two cards from the deck.

    Args:
        deck (list of tuples): The deck of playing cards.

    Returns:
        list: A list containing two cards.
    """
    return [deck.pop(), deck.pop()]


def display_player_hand(player_hand):
    """
    Display the player's hand.

    Args:
        player_hand (list of tuples): Player's hand, i.e list of card tuples.
    """
    print("Player's Hand", player_hand)


def display_dealer_hand(dealer_hand, reveal_hole_card=False):
    """
    Display the dealer's hand.

    Args:
        dealer_hand (list of tuples): Dealer's hand, i.e. list of card tuples.
        reveal_hole_card (bool, optional): Whether to reveal the hole card.
    """
    if reveal_hole_card:
        print("Dealer's Hand", dealer_hand)
    else:
        concealed_card = [('??', '??')]
        visible_cards = concealed_card + dealer_hand[:1]
        print("Dealer's Hand:", visible_cards)


def ask_user_hit_or_stand():
    """
    Get the user's decision in the game, whether to "Hit" or "Stand".

    Returns:
        str: The user's decision, either "Hit" or "Stand".
    """
    while True:
        # Use input() to get user input
        user_input = input("Do you want to 'Hit' or 'Stand'? ").strip().lower()

        # Check if the user's input is valid (either "hit" or "stand")
        if user_input == "hit":
            return "Hit"
        elif user_input == "stand":
            return "Stand"
        else:
            # If the input is not valid, prompt the user again
            print("Invalid input. Please enter 'Hit' or 'Stand'.")


def ask_user_insurance():
    """
    Get the user's decision in the game, whether to "Insurance" or "No Insurance".

    returns:
        str: The user's decision, either "Insurance" or "No Insurance".
    """
    while True:
        # Use input() to get user input
        user_input = input("Do you want 'Insurance' or 'No Insurance'? ").strip().lower()

        # Check if the user's input is valid (either "insurance" or "no insurance")
        if user_input == "insurance":
            return "Insurance"
        elif user_input == "no insurance":
            return "No Insurance"
        else:
            print("Invalid input. Please enter 'Insurance' or 'No Insurance'.")


def ask_user_response():
    pass


def check_for_blackjack(hand):
    """
    Check if a hand is blackjack.

    Args:
        hand (list of tuples): The Player's hand, i.e., a list of card tuples.

    Returns:
        bool: True if the hand is blackjack, False if not.
    """
    # Check if the hand has exactly 2 cards and one of them is an Ace
    if len(hand) == 2 and any(card[1] == 'A' for card in hand):
        # Check if the other card is a 10-point card or a face card
        other_card_rank = hand[0][1] if hand[1][1] == 'A' else hand[1][1]
        if other_card_rank in ['10', 'J', 'Q', 'K']:
            return True
    return False


def check_for_bust(hand):
    """
    Check if the hand is over 21 (bust)

    Args:
        hand (list of tuples): the player's hand, i.e. list of card tuples.

    Returns:
        bool: True if the hand is busted, False if not.
    """
    total_value = hand_value(hand)
    return total_value > 21