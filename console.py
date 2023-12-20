from logic import *

def main():
    deck = build_deck()
    shuffle(deck)

    while True:
        player_hand = draw_initial_hand(deck)
        dealer_hand = draw_initial_hand(deck)
    
        display_player_hand(player_hand)
        display_dealer_hand(dealer_hand, reveal_hole_card=False)

        if check_for_blackjack(player_hand):
            print("Player has a blackjack!")
            break
        if check_for_blackjack(dealer_hand):
            print("Dealer has a blackjack!")
            break
        
        while True:
            # Calculate and display player value 
            player_value = hand_value(player_hand)
            print(f"Player's hand value: {player_value}")
            print("")

            user_decision = ask_user_hit_or_stand()
            print("")

            if user_decision == "Hit":
                player_hand.append(draw_card(deck))
                display_player_hand(player_hand)

                if check_for_bust(player_hand):
                    print("Player Busted!")
                    break

            elif user_decision == "Stand":
                break  
            
        playout_dealer_hand(deck, dealer_hand)

        determine_winner(player_hand, dealer_hand)

        play_again = input("Do you want to play again? (yes/no)").strip().lower()
        if play_again == "no":
            print("Thanks for playing! Goodbye.")
            break # End the game loop if the player chooses not to play again

if __name__ == "__main__":
    main()