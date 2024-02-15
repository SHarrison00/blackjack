from enum import Enum
import random
from logic2 import RoundOutcome, InsuranceOption
from console2 import start_round


def ask_player_stake(bankroll):
    # Defining the list of possible stake options
    available_stakes = [1, 2, 5, 10, 20, 50, 100]

    # Ask the player to choose from the available options
    while True:
        print(f"Your current bankroll is {bankroll}. Choose your stake:")
        print(", ".join(map(str, available_stakes)))
        try:
            stake = int(input("Enter your stake: "))
            if stake not in available_stakes:
                print("Invalid stake. Please choose from the available options.")
            elif stake > bankroll:
                print("You cannot stake more than your bankroll.")
            else:
                return stake
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def ask_player_end_game():
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return False
        elif choice in ['no', 'n']:
            return True
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    

def play():

    bankroll = 100
    end_game_flag = False
    
    while bankroll > 0 and end_game_flag == False:

        stake = ask_player_stake(bankroll)

        outcome, insur_decision = start_round()
        print(f"Outcome: {outcome}, Insurance: {insur_decision}")

        # Update bankroll based on outcome
        if outcome == RoundOutcome.DEALER_BLACKJACK:
            if insur_decision == InsuranceOption.YES:
                bankroll += stake * 2 # Insurance payout is 2:1
            else:
                bankroll -= stake
        elif outcome == RoundOutcome.PLAYER_BLACKJACK:
            bankroll += stake * 1.5 # Blackjack payout for player is 3:2
        elif outcome == RoundOutcome.PLAYER_WIN:
            bankroll += stake
        elif outcome == RoundOutcome.DEALER_WIN:
            bankroll -= stake
        elif outcome == RoundOutcome.PUSH:
            # In case of a push, stake is returned to the player
            pass
        elif insur_decision == InsuranceOption.YES:
            bankroll -= stake/2 # Player loses half of the insurance bet if dealer does not have blackjack
        
        # Check if bankroll is zero
        if bankroll <= 0:
            print("You have run out of money. Game over!")
            break

        print(f"Bankroll: {bankroll}")

        end_game_flag = ask_player_end_game()
        
    print("Thank you for playing!")

# Play the game..
play()