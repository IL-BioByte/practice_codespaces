import random


table = ["   " for _ in range(36)]

current_player = random.choice(["X", "O"]) #ramdomly select who play first

#GAME LOOP
def main():
    global current_player
    print(f"Player {current_player} will start the game!!!")

    while True:
        print_table()
        player_move(current_player)

        winner = check_winner ()
        if winner:
            print_table() #show the final table
            print(f"The winner is: {winner}!!!")
            break

        if table_full():
            print_table()
            print("End of game, It's a draw!")
            break

        current_player = "X" if current_player == "O" else "O" #switch player


def print_separator(): #the separator for each line of space
    print("+---+---+---+---+---+---+")

def print_table ():
    print_separator() #top separator
    for row in range (6): #looping through the rows
        print("|" + "|".join(table[row * 6:(row + 1) * 6]) + "|") #using a joint function to print the | and two spaces
        print_separator() #print separator after each row


def player_move (player): #player, which will be either X or O depending on which player's turn
    while True: #a while loop so it keeps asking until valid input
        try:
            move = int(input(f"Player {player}, enter a position (1~36): ")) - 1 #ask player for a number, -1 so it match with the range
            if 0 <= move < 36 and table[move] == "   ": #check if input is valid and the space is still empty
                table[move] = " X " if player == "X" else " O "
                break #break out of while loop
            else:
                print("Invalid move, try again")
        except ValueError:
            print("Invalid input!")



def check_winner (): 
    for row in range (6): # Check rows for 4 in a row
        for col in range (3):
            #check if the rows contain the same input, and the input is not empty
            if table[row * 6 + col] == table[row * 6 + col + 1] == table[row * 6 + col + 2] == table[row * 6 + col + 3] != "   ":
                return table[row * 6 + col] #there is a winner
    for col in range (6): # Check columns for 4 in a col
        for row in range (3):
                #check if the col contain the same input, and the input is not empty
            if table[row * 6 + col] == table[(row + 1) * 6 + col] == table[(row + 2) * 6 + col] == table[(row + 3) * 6 + col] != "   ":
                return table[row * 6 + col]  # there is a winner
    # Check down-right diagonals
    for row in range(3):  # Check only the first 2 rows
        for col in range(3):  # Check columns 0, 1
            if table[row * 6 + col] == table[(row + 1) * 6 + (col + 1)] == table[(row + 2) * 6 + (col + 2)] == table[(row + 3) * 6 + (col + 3)] != "   ":
                return table[row * 6 + col]

    # Check down-left diagonals
    for row in range(3):  # Check only the first 2 rows
        for col in range(3, 6):  # Check columns 4 and 3 (0-indexed)
            if table[row * 6 + col] == table[(row + 1) * 6 + (col - 1)] == table[(row + 2) * 6 + (col - 2)] == table[(row + 3) * 6 + (col - 3)] != "   ":
                return table[row * 6 + col]
    
    return None #No winner


def table_full ():
    return "   " not in table

def redo ():
    return 
main()