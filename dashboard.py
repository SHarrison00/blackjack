import streamlit as st
from logic2 import *

def start_game():
    deck = generate_deck()
    shuffle(deck)
    
    player_hand = draw_hand(deck)
    st.write("Player's Hand:", player_hand)

    # Note: Continue following the flow diagram here. Also note there should be 
    # clear similarities between here & console2.py. Essentially console2.py
    # will run Blackjack locally, while dashboard will run Blackjack online...

# Streamlit UI elements
st.title("Blackjack Game")

if st.button("Start Game"):
    start_game()