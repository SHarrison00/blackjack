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