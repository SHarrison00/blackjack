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
    

def draw_card(deck):
    """
    Draw a single card from the deck.

    Args:
        deck (list of tuples): The deck of playing cards.

    Returns:
        tuple: A single card.
    """
    # TO DO: Conor

        # Hint: .pop()
    pass    


def draw_initial_hand(deck):
    """
    Draw an initial hand of two cards from the deck.

    Args:
        deck (list of tuples): The deck of playing cards.

    Returns:
        list: A list containing two cards.
    """
    # TO DO: Conor
        # Very similar
    pass


def display_player_hand(player_hand):
    """
    Display the player's hand.

    Args:
        player_hand (list of tuples): Player's hand, i.e list of card tuples.
    """
    # TO DO: Conor

    # Example:
    # --------
    # Say the player's hand is
    # player_hand = [('2', 'Hearts'), ('Ace', 'Spades')]
    
    # Then the output should be 
    # display_player_hand(player_hand)
    # >>> Player's Hand: [('2', 'Hearts'), ('Ace', 'Spades')]
    
    # Hint:
        # See how to combine strings and lists using print().
        # The solution is simple, and this is not a trick*. 
    pass


def display_dealer_hand(dealer_hand, reveal_hole_card=False):
    """
    Display the dealer's hand.

    Args:
        dealer_hand (list of tuples): Dealer's hand, i.e. list of card tuples.
        reveal_hole_card (bool, optional): Whether to reveal the hole card.
    """
    # TO DO: Conor

    # Example:
    # --------
    # Let's consider the dealer's hand with an unrevealed hole card:
    # dealer_hand = [('5', 'Diamonds'), ('King', 'Clubs')]
    
    # When calling the function WITHOUT REVEALING the hole card:
    # display_dealer_hand(dealer_hand)
    
    # The output should be:
    # >>> Dealer's Hand: [('5', 'Diamonds'), ('??', '??')]
    
    # When calling the function WITH REVEALING the hole card revealed:
    # display_dealer_hand(dealer_hand, reveal_hole_card=True)
    
    # The output should be:
    # >>> Dealer's Hand: [('5', 'Diamonds'), ('King', 'Clubs')]
    
    # Hint:
    # - Use an if-else statement to decide whether to reveal the hole card.
    # - You can print lists directly to display the hand.
    pass