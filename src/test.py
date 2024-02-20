from .logic import *
from .game import *
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



        
class TestUpdateBankroll(unittest.TestCase):

    def test_dealer_win_no_insurance(self):
        self.assertEqual(update_bankroll(100, 10, RoundOutcome.DEALER_WIN, Insurance.NO), 90)


    def test_dealer_win_with_insurance(self):
        # Loses stake and insurance
        self.assertEqual(update_bankroll(100, 10, RoundOutcome.DEALER_WIN, Insurance.YES), 85) 

    
    def test_player_win_no_insurance(self):
        self.assertEqual(update_bankroll(100, 10, RoundOutcome.PLAYER_WIN, Insurance.NO), 110)

    
    def test_player_win_with_insurance(self):
        # Wins stake, loses insurance
        self.assertEqual(update_bankroll(100, 10, RoundOutcome.PLAYER_WIN, Insurance.YES), 105)

    
    def test_push_no_insurance(self):
        self.assertEqual(update_bankroll(100, 10, RoundOutcome.PUSH, Insurance.NO), 100)

    
    def test_push_with_insurance(self):
        # Stake returned, insurance lost
        self.assertEqual(update_bankroll(100, 10, RoundOutcome.PUSH, Insurance.YES), 95)


    def test_player_blackjack_no_insurance(self):
        # 3:2 payout
        self.assertEqual(update_bankroll(100, 10, RoundOutcome.PLAYER_BLACKJACK, Insurance.NO), 115) 

    
    def test_player_blackjack_with_insurance(self):
        # 3:2 payout, insurance lost
        self.assertEqual(update_bankroll(100, 10, RoundOutcome.PLAYER_BLACKJACK, Insurance.YES), 110)

    
    def test_dealer_blackjack_no_insurance(self):
        self.assertEqual(update_bankroll(100, 10, RoundOutcome.DEALER_BLACKJACK, Insurance.NO), 90)

    
    def test_dealer_blackjack_with_insurance(self):
        # Stake lost, insurance wins
        self.assertEqual(update_bankroll(100, 10, RoundOutcome.DEALER_BLACKJACK, Insurance.YES), 100)


if __name__ == '__main__':
    unittest.main()