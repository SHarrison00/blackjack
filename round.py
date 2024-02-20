from logic import *
import time

def start_round():        
    deck = generate_deck()
    shuffle(deck)
        
    # Deal hands
    player_hand = draw_hand(deck)
    dealer_hand = draw_hand(deck)
        
    print("\nPlayer's Hand:", player_hand)
    print("Dealer's Hand:", [dealer_hand[0], '??'], "\n")

    result = None
    insurance_option = None

    if check_for_blackjack(player_hand):
        if check_for_blackjack(dealer_hand):
            print("Push! Both player and dealer have blackjack.")
            result = RoundOutcome.PUSH
        else:
            print("Player has blackjack! Player wins")
            result = RoundOutcome.PLAYER_BLACKJACK
            return result, insurance_option
    else:
        # Check dealer's upcard is an Ace
        if dealer_hand[0][1] == 'A':
            insurance_decision = offer_insurance()
            if insurance_decision:
                print("Insurance taken!")
                insurance_option = InsuranceOption.YES
                if check_for_blackjack(dealer_hand):
                    print("Dealer has blackjack! Insurance payout.")
                    result = RoundOutcome.DEALER_BLACKJACK
                else:
                    print("Dealer does not have blackjack. No insurance payout.")
            else:
                insurance_option = InsuranceOption.NO

    # Player's turn
    while ask_player_for_hit():
        player_hand.append(draw_card(deck))
        print("Player's Hand:", player_hand)
            
        if hand_value(player_hand) == 21:
            print("You have 21!\n")
            time.sleep(2.5)
            break

        if check_for_bust(hand_value(player_hand)):
            print("Player Bust! Dealer wins\n")
            time.sleep(3)
            result = RoundOutcome.DEALER_WIN
            break

    if result is None:
        print("Dealer's Hand:", dealer_hand)
        
        # Dealer keeps hitting
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(draw_card(deck))
            print("Dealer hits:", dealer_hand)
            time.sleep(2.5)

        if check_for_bust(hand_value(dealer_hand)):
            print("Dealer busts! Player wins.\n")
            time.sleep(3)
            result = RoundOutcome.PLAYER_WIN
        elif hand_value(player_hand) == hand_value(dealer_hand):
            print("Push! Both Player and Dealer have the same hand value.\n")
            time.sleep(3)
            result = RoundOutcome.PUSH
        elif hand_value(player_hand) > hand_value(dealer_hand):
            print("Player wins!\n")
            time.sleep(3)
            result = RoundOutcome.PLAYER_WIN
        else:
            print("Dealer wins!\n")
            time.sleep(3)
            result = RoundOutcome.DEALER_WIN
    
    if insurance_option is None:
        insurance_option = InsuranceOption.NO
        
    return (result, insurance_option)