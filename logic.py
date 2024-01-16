from enum import Enum

class Suit(Enum):
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'

class Rank(Enum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'Jack'
    QUEEN = 'Queen'
    KING = 'King'
    ACE = 'Ace'

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank.value} of {self.suit.value}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        if not self.is_empty():
            return self.cards.pop()
    
    def is_empty(self):
        return len(self.cards) == 0
    

class Player:
    def __init__(self, name):
        self.name = name 
        self.hand = []

    def add_card_to_hand(self, card):
        self.hand.append(card)
    
    def get_hand_value(self):
        total_value = 0
        num_aces = 0

        # Check for blackjack
        if len(self.hand) == 2:
            if any(card.rank == Rank.ACE for card in self.hand) and any(card.rank in (Rank.JACK, Rank.QUEEN, Rank.KING) for card in self.hand):
                return 21 # Blackjack!
            
        for card in self.hand:
            # For numbered cards (2-10), use their numeric value
            if card.rank in (Rank.TWO, Rank.THREE, Rank.FOUR, Rank.FIVE, Rank.SIX, Rank.SEVEN, Rank.EIGHT, Rank.NINE, Rank.TEN):
                total_value += int(card.rank.value)
            # For face cards (Jack, Queen, King), use a value of 10
            elif card.rank in (Rank.JACK, Rank.QUEEN, Rank.KING):
                total_value += 10
            # For Aces, keep track on the number and decide on their value later
            elif card.rank == Rank.ACE:
                num_aces += 1
        
        # Add the value of Aces based on the current total value
        for _ in range(num_aces):
            # If adding 11 doesn't bust, use 11; otherwise use 1
            if total_value + 11 <= 21:
                total_value += 11
            else:
                total_value += 1

        return total_value


