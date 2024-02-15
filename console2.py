from logic2 import *

def start_round():        
    deck = generate_deck()
    shuffle(deck)
        
    # Deal both Player and Dealer hands
    player_hand = draw_hand(deck)
    dealer_hand = draw_hand(deck)
        
    print("Player's Hand:", player_hand)
    print("Dealer's Hand:", [dealer_hand[0], '??'])

    result = None # Initialize variables
    insurance_option = None

    # Check if the player has a blackjack
    if check_for_blackjack(player_hand):
        if check_for_blackjack(dealer_hand):
            print("Push! Both player and dealer have blackjack.")
            result = RoundOutcome.PUSH
        else:
            print("Player has blackjack! Player wins")
            result = RoundOutcome.PLAYER_BLACKJACK
    else:
        # Check for the dealer's upcard being an Ace
        if dealer_hand[0][1] == 'A':
            insurance_decision = offer_insurance()
            if insurance_decision:
                print("Insurance taken!")
                insurance_option = InsuranceOption.YES
                if check_for_blackjack(dealer_hand):
                    print("Dealer has blackjack! Insurance payout.") # reminded to implement insurance logic later!
                    result = RoundOutcome.DEALER_BLACKJACK
                else:
                    print("Dealer does not have blackjack. No insurance payout.")
            else:
                print("No insurance taken.")
                insurance_option = InsuranceOption.NO

    # Player's turn
    while ask_player_for_hit():
        player_hand.append(draw_card(deck))
        print("Player's Hand:", player_hand)
            
        # Check if player has 21
        if hand_value(player_hand) == 21:
            print("You have 21!")
            break

        # Check for bust
        if check_for_bust(hand_value(player_hand)):
            print("Player Bust! Dealer wins")
            result = RoundOutcome.DEALER_WIN
            break

    print("Player stands.")

    if result is None:
        #Dealer's turn
        print("Dealer's Hand:", dealer_hand)
        
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(draw_card(deck))
            print("Dealer hits:", dealer_hand)

        if check_for_bust(hand_value(dealer_hand)):
            print("Dealer busts! Player wins.")
            result = RoundOutcome.PLAYER_WIN
        elif hand_value(player_hand) == hand_value(dealer_hand):
            print("Push! Both Player and Dealer have the same hand value")
            result = RoundOutcome.PUSH
        elif hand_value(player_hand) > hand_value(dealer_hand):
            print("Player wins!")
            result = RoundOutcome.PLAYER_WIN
        else:
            print("Dealer wins!")
            result = RoundOutcome.DEALER_WIN
    
    if insurance_option is None:
        insurance_option = InsuranceOption.NO
        
    return (result, insurance_option)
    
if __name__ == "__main__":
        result, insurance_option = start_round()
        print("Round Result:", result, insurance_option)

        
