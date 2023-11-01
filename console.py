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