import unittest
from logic import *

class TestShuffleFunction(unittest.TestCase):

    def test_shuffle(self):
        # Create a sorted deck
        sorted_deck = build_deck()
        
        # Shuffle the sorted deck
        shuffled_deck = shuffle(sorted_deck)
        
        # Assert shuffled deck is not the same as sorted deck
        self.assertNotEqual(sorted_deck, shuffled_deck)


    def test_number_card_value(self):
        card = ('Hearts', '2') 
        result = card_value(card)
        self.assertEqual(result, 2)


    def test_face_card_value(self):
        card = ('Spades', 'K')
        result = card_value(card)
        self.assertEqual(result, 10)


    def test_ace_card_value(self):
        card = ('Diamonds', 'A')
        result = card_value(card)
        self.assertEqual(result, 11)

    
    def test_hand_value_no_aces(self):
        # Test a hand with no Aces
        hand = [('Hearts', '7'), ('Clubs', '9')]  # Total value = 7 + 9 = 16
        result = hand_value(hand)
        self.assertEqual(result, 16)


    def test_hand_value_with_aces(self):
        # Test a hand with Aces, where one Ace is counted as 11 and the other as 1
        hand = [('Diamonds', 'A'), ('Spades', '5'), ('Hearts', 'A')]  # Total value = 11 + 5 + 1 = 17
        result = hand_value(hand)
        self.assertEqual(result, 17)


if __name__ == '__main__':
    unittest.main()