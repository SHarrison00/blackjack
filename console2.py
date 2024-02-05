from logic2 import *

def start_round():
    while True:        
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
                    if check_for_blackjack(dealer_hand):
                        print("Dealer has blackjack! Insurance payout.") # reminded to implement insurance logic later!
                        result = RoundOutcome.DEALER_BLACKJACK
                    else:
                        print("Dealer does not have blackjack. No insurance payout.")
                else:
                    print("No insurance taken.")
                    
        
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
        
        print("Player stands.")

        #Dealer's turn
        print("Dealer's Hand:", dealer_hand)
        while hand_value(dealer_hand) < 17 and not check_for_bust(hand_value(player_hand)):
            dealer_hand.append(draw_card(deck))
            print("Dealer hits:", dealer_hand)

        if check_for_bust(hand_value(dealer_hand)):
            print("Deealer busts! Player wins.")
            result = RoundOutcome.PLAYER_WIN
        else:    
            print("Dealer stands.")

            # Determine winner
            result = determine_winner(player_hand, dealer_hand)
            print("Round Outcome:", result)
    
        if result in [RoundOutcome.DEALER_WIN, RoundOutcome.PLAYER_WIN, RoundOutcome.PUSH, RoundOutcome.PLAYER_BLACKJACK, RoundOutcome.DEALER_BLACKJACK]:
            play_again = input("Do you want to play again? (yes/no)").lower()
            if play_again != 'yes':
                break

    return result
    
if __name__ == "__main__":
        start_round()

        # Note: When exiting start_round(), think about combining the Enums for
        # RoundOutcome() & Insurance() somehow to dictate what happens next... 
        
