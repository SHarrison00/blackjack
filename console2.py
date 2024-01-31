from logic2 import *

def start_round():
    deck = generate_deck()
    shuffle(deck)
    
    # Deal both Player and Dealer hands
    player_hand = draw_hand(deck)
    dealer_hand = draw_hand(deck)
    
    print("Player's Hand:", player_hand)
    print("Dealer's Hand:", [dealer_hand[0], '??'])
    
    # Check if the player has a blackjack
    if check_for_blackjack(player_hand):
        if check_for_blackjack(dealer_hand):
            print("Push! Both player and dealer have blackjack.")
            return RoundOutcome.PUSH
        else:
            print("Player has blackjack! Player wins")
            return RoundOutcome.PLAYER_BLACKJACK
    else:
        # Check for the dealer's upcard being an Ace
        if dealer_hand[0][1] == 'A':
            insurance_decision = offer_insurance()
            if insurance_decision:
                print("Insurance taken!")
                if check_for_blackjack(dealer_hand):
                    print("Dealer has blackjack! Insurance payout.") # reminded to implement insurance logic later!
                    return RoundOutcome.PUSH
                else:
                    print("Dealer does not have blackjack. No insurance payout.")
            else:
                print("No insurance taken.")
    

if __name__ == "__main__":
    result = start_round()

    # Note: When exiting start_round(), think about combining the Enums for
    # RoundOutcome() & Insurance() somehow to dictate what happens next... 
    print("Round Outcome:", result)
