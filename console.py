from logic import *

def main():
    while True:
        # Build shuffled deck
        deck = build_deck()
        shuffle(deck)

        # Example hands
        player_hand = draw_initial_hand(deck)
        dealer_hand = draw_initial_hand(deck)
    
        while True:
            # Display hands
            display_player_hand(player_hand)
            display_dealer_hand(dealer_hand, reveal_hole_card=False)

            # Checking for Blackjacks
            if check_for_blackjack(player_hand):
                print("Player has a blackjack!")
            if check_for_blackjack(dealer_hand):
                print("Dealer has a blackjack!")

            # Calculate and display player value 
            player_value = hand_value(player_hand)
            print(f"Player's hand value: {player_value}")
            print("")

            # Ask user for decision
            user_decision = ask_user_hit_or_stand()
            print("")

            if user_decision == "Hit":
                # Draw, calculate value, and display
                player_hand.append(draw_card(deck))
                display_player_hand(player_hand)
                player_value = hand_value(player_hand)
                print(f"Player's hand value: {player_value}")
            else:
                break # Exit the player's turn loop if the player chooses to stand

            # Check for player bust
            if check_for_bust(player_hand):
                print("Player busted!")
                break # Exit the players loop if the player busts

        # Dealer's turn
        dealer_turn(deck, dealer_hand)

        # Check for dealer bust
        if check_for_bust(dealer_hand):
            print("Dealer busted!")

        # Determine the winner of the game
        determine_winner(player_hand, dealer_hand)

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no)").strip().lower()
        if play_again == "no":
            print("Thanks for playing! Goodbye.")
            break # End the game loop if the player chooses not to play again

if __name__ == "__main__":
    main()