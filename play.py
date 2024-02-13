from enum import Enum
import random

class RoundOutcome(Enum):  # Import these classes! ... Have a read about "what an import is"... 
    DEALER_WIN = "DEALER_WIN"
    PLAYER_WIN = "PLAYER_WIN"
    PUSH = "PUSH"
    PLAYER_BLACKJACK = "PLAYER_BLACKJACK"
    DEALER_BLACKJACK = "DEALER_BLACKJACK"

class InsuranceOption(Enum): # Import these classes! ... 
    YES = "YES"
    NO = "NO"




def start_round(): # This function lives in a different file ... i.e. import from wherever ... 
    """Return [RoundOutcome, InsuranceOption]"""

    return RoundOutcome.DEALER_BLACKJACK, InsuranceOption.NO


def ask_player_stake(bankroll):
    # Fixed number of possible stakes
    # Make sure don't go past zero bankroll
    return 1 # Stake always 1 


def ask_player_end_game():
    return True # True == don't play again. False == play again



def play():

    bankroll = 100
    end_game_flag = False
    
    while bankroll > 0 and end_game_flag == False:

        stake = ask_player_stake(bankroll) # Ask player stake, should "know" bankroll

        outcome, insur_decision = start_round()
        print(f"Outcome: {outcome}, Insurance: {insur_decision}")

        # Decide what happens next
            # Update bankroll
            # Ask user player again?
                # If yes: do nothing
                # If no: change end_game_flag to True
            # Think about about Insurance!!!
        
        # For example, let's update the bankroll...


        if outcome == RoundOutcome.DEALER_BLACKJACK:
            bankroll -= stake
        elif outcome == RoundOutcome.PLAYER_BLACKJACK:
            bankroll += stake
        else:
            # Add more checks here, for each outcome... 
            pass
        
        print(f"Bankroll: {bankroll}")

        end_game_flag = ask_player_end_game()
        
    print("Thank you for playing!")



# Play the game..
play()