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


if __name__ == '__main__':
    unittest.main()