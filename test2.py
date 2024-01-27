from logic2 import *
import unittest

class TestCardFunctions(unittest.TestCase):

    def test_hand_value(self):
        hand1 = [('Hearts', '7'), ('Spades', 'A')]
        self.assertEqual(hand_value(hand1), 18)

        hand2 = [('Diamonds', 'Q'), ('Clubs', 'K')]
        self.assertEqual(hand_value(hand2), 20)

        hand3 = [('Hearts', 'A'), ('Spades', 'K')]
        self.assertEqual(hand_value(hand3), 21)

        hand4 = [('Diamonds', 'A'), ('Clubs', 'A'), ('Hearts', 'A')]
        self.assertEqual(hand_value(hand4), 13)


    def test_check_for_blackjack(self):
        hand1 = [('Hearts', '7'), ('Spades', 'A')]
        self.assertFalse(check_for_blackjack(hand1))

        hand2 = [('Hearts', 'A'), ('Spades', 'K')]
        self.assertTrue(check_for_blackjack(hand2))


if __name__ == '__main__':
    unittest.main()