from .logic import *
from .round import start_round
    
def start_game():
    bankroll = 100
    end_game_flag = False
    
    while bankroll > 0 and end_game_flag == False:
        stake = ask_player_stake(bankroll)
        outcome, insur_decision = start_round()
        print(f"\nOutcome: {outcome}, Insurance: {insur_decision}")

        # Update bankroll based on outcome
        bankroll = update_bankroll(bankroll, stake, outcome, insur_decision)

        if bankroll <= 0:
            print("You have run out of money. Game over!")
            break

        print(f"Bankroll: ${bankroll}")
        end_game_flag = ask_player_end_game()
        
    print("Thank you for playing!")