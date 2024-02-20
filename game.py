from logic import RoundOutcome, InsuranceOption
from round import start_round

def ask_player_stake(bankroll):
    available_stakes = [1, 2, 5, 10, 20, 50, 100]

    while True:
        print(f"\n\n\n\n\nYour current bankroll is ${bankroll}. Choose your stake:")
        print(", ".join([f"${stake}" for stake in available_stakes]))
        try:
            stake = int(input("Enter your stake: $"))
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
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return False
        elif choice in ['no', 'n']:
            return True
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def update_bankroll(bankroll, stake, outcome, insur_decision):
    # Insurance bet is half the stake
    insurance_bet = stake / 2
    
    # Payout ratios
    blackjack_payout = 1.5
    insurance_payout = 2  

    if outcome == RoundOutcome.DEALER_WIN:
        if insur_decision == InsuranceOption.YES:
            return bankroll - stake - insurance_bet
        else:
            return bankroll - stake
    elif outcome == RoundOutcome.PLAYER_WIN:
        if insur_decision == InsuranceOption.YES:
            return bankroll + stake - insurance_bet
        else:
            return bankroll + stake
    elif outcome == RoundOutcome.PUSH:
        if insur_decision == InsuranceOption.YES:
            return bankroll - insurance_bet
        else:
            return bankroll
    elif outcome == RoundOutcome.PLAYER_BLACKJACK:
        if insur_decision == InsuranceOption.YES:
            return bankroll + (stake * blackjack_payout) - insurance_bet
        else:
            return bankroll + (stake * blackjack_payout)
    elif outcome == RoundOutcome.DEALER_BLACKJACK:
        if insur_decision == InsuranceOption.YES:
            return bankroll - stake + (insurance_bet * insurance_payout)
        else:
            return bankroll - stake
    else:
        raise ValueError("Invalid outcome or insurance decision")
    

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

if __name__ == "__main__":
    start_game()