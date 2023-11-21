from logic import *

# Build shuffled deck
deck = build_deck()
shuffle(deck)

# Example hands
player_hand = draw_initial_hand(deck)
dealer_hand = draw_initial_hand(deck)

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

    # Check for player bust
    if check_for_bust(player_hand):
        print("Player busted!")

# Dealer's turn
dealer_turn(deck, dealer_hand)

# Check for dealer bust
if check_for_bust(dealer_hand):
    print("Dealer busted!")