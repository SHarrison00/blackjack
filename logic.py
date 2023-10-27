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
    # TO DO (Conor):

    # Hint: 
        # Consider ranks of all cards, i.e. ['2', ...,  '10', 'J', 'Q', 'K', 'A']
        # The value for some cards are easier than others
        # Could we use "if elif else" statements?
    pass