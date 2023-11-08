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
        return int(rank)
    

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
            # TODO: Conor ...

    # In this 'while' loop:
    # Check if there are 'Ace' cards in the hand (ace_count > 0)
    # and if the total_value exceeds 21 (total_value > 21)
    while ace_count > 0 and total_value > 21:
        # If both conditions are met, adjust the value of 'Ace' cards:
        # - Deduct 10 from total_value, i.e change the value of 'Ace' from 11 to 1
        # - Decrement ace_count for each 'Ace' adjusted
            # TODO: Conor ...
        pass

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


def get_user_decision():
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
            # TODO: Implement the code for "Hit" choice here
            pass
        elif user_input == "stand":
            # TODO: Implement the code for "Stand" choice here
            pass
        else:
            # If the input is not valid, prompt the user again
            print("Invalid input. Please enter 'Hit' or 'Stand'.")
