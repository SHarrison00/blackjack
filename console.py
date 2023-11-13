from logic import *

deck = build_deck()

print('')

player_hand = [('2', 'Hearts'), ('Ace', 'Spades')]
# This is an example of a player's hand i.e. a list of tuples

display_player_hand(player_hand)
# This gives us the player's hand in the console

dealer_hand = [('2', 'Hearts'), ('Ace', 'Spades')]
# This is an example of a dealer's hand "" ""

display_dealer_hand(dealer_hand, reveal_hole_card=False)
# This gives us the dealers hand which shows one card (hole card) as ?? ?? (facing down)

if check_for_blackjack(player_hand):
    print("Player has a blackjack!")
else:
    print("Player does not have a blackjack.")
    # Checking for player blackjack
if check_for_blackjack(dealer_hand):
    print("Dealer has a blackjack!")
else:
    print("Dealer does not have a blackjack.")
    # Checking for dealer blackjack

player_hand.append(draw_card(deck))
# Draw a card for the player

display_player_hand(player_hand)
# Display updated player hand

player_value = hand_value(player_hand)
print(f"Player's hand value: {player_value}")
# Calculate and display the value of the player's hand

user_decision = ask_user_hit_or_stand()
# Example: Ask the user if they want to hit or stand

if user_decision == "Hit":
    player_hand.append(draw_card(deck))
    # Draw another card for the player
    display_player_hand(player_hand)
    # Display updated player hand
    player_value = hand_value(player_hand)
    # Calculate and display the value of the player's hand
    print(f"Player's hand value: {player_value}")

if check_for_bust(player_hand):
    print("Player busted!")
else:
    print("Player did not bust.")
    # Check if the player has bust
if check_for_bust(dealer_hand):
    print("Dealer busted!")
else:
    print("Dealer did not bust.")
    # Check if the dealer has bust



