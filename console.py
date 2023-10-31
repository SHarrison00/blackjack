from logic import *

deck = build_deck()

print(deck)

# TO DO: Conor
    # Challenge: Start to implement Blackjack in the console.

# For example, you might want to keep start above. 
# 
# I think this is ok for now.
#
# Next, we might want to draw some cards. Then, we might want to reveal some 
# cards in the console. Then, we might want the user to make a decision, i.e.
# hit/stand etc. etc. etc. ...
print('')


player_hand = [('2', 'Hearts'), ('Ace', 'Spades')]


display_player_hand(player_hand)


dealer_hand = [('2', 'Hearts'), ('Ace', 'Spades')]


display_dealer_hand(dealer_hand, reveal_hole_card=False)