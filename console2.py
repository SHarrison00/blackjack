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
            return RoundOutcome.PUSH
        else:
            return RoundOutcome.PLAYER_BLACKJACK
    else:
        # Check for the dealer's upcard being an Ace
        if dealer_hand[0][1] == 'A':
            insurance_decision = offer_insurance()
            
            if insurance_decision:
                print("Insurance taken!") # Reminder to implement logic for insurance and payout later!
            else:
                print("No insurance taken.")

    # Players Turn
    result = player_turn(deck, player_hand)

    # Check for Player Bust
    if result == "BUST":
        print("Player busts! Dealer wins.")
        return RoundOutcome.DEALER_WIN
    elif result is None:
        print("Player's turn ends.")
    
    # Note: Continue following the flow diagram here...

if __name__ == "__main__":
    result = start_round()

    # Note: When exiting start_round(), think about combining the Enums for
    # RoundOutcome() & Insurance() somehow to dictate what happens next... 
    print("Round Outcome:", result)
