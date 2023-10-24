from itertools import product
import random

def deck():
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
    # TO DO (Conor):

    # Hint: 
        # How might we use the "random" module to shuffle a deck? 
        # https://docs.python.org/3/library/random.html
    pass
