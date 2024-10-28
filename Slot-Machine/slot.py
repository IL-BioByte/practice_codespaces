import random

MAX_LINE = 5  #ALL CAP MEANS GLOBAL, IT IS NOT GONNA CHANGE
MAX_BET = 500
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2, #Rare
    "B": 4,
    "C": 6,
    "D": 8 #common
}

def get_slot_spin(rows, cols, symbols):
    # Build a list of all symbols based on their frequency
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        #  all_symbols.extend([symbol] * count)
 # Generate slot spin with fair random sampling
    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)  
        # Randomly sample for each column
        columns.append(column)
    
    return columns
    

#collect user input for deposit
def deposit():
    while True:
        amount = input("How much would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be more than 0.")
        else:
            print("Please enter a whole number greater than 0.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINE) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a whole number greater than 0.")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be bettwen {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a whole number greater than 0.")

    return amount  


#main game loop
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}, you need at least ${total_bet}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} Lines. Total bet is ${total_bet}")

slot_spin = get_slot_spin(ROWS, COLS, symbol_count)
for row in zip(*slot_spin):  # Print rows for visualization
    print(row)