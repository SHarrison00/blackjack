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
        card = ('2', 'Hearts') 
        result = card_value(card)
        self.assertEqual(result, 2)


    def test_face_card_value(self):
        card = ('K', 'Spades')
        result = card_value(card)
        self.assertEqual(result, 10)


    def test_ace_card_value(self):
        card = ('A', 'Diamonds')
        result = card_value(card)
        self.assertEqual(result, 11)    


if __name__ == '__main__':
    unittest.main()