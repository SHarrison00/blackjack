from logic2 import *

def start_round():
    deck = generate_deck()
    shuffle(deck)
    
    player_hand = draw_hand(deck)
    print(player_hand) # Note: You might want to insert print statements like 
                       # this to help, or you wrap/abstract complicated print 
                       # as a functions in the logic script... up to you...
    
    # Check if the player has a blackjack
    if check_for_blackjack(player_hand):
        dealer_hand = draw_hand(deck)
        if check_for_blackjack(dealer_hand):
            return RoundOutcome.PUSH
        else:
            return RoundOutcome.PLAYER_BLACKJACK
    else:
        return None
    
    # Note: Continue following the flow diagram here...

if __name__ == "__main__":
    result = start_round()

    # Note: When exiting start_round(), think about combining the Enums for
    # RoundOutcome() & Insurance() somehow to dictate what happens next... 
    print("Round Outcome:", result)
