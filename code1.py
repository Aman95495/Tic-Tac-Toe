#####  Tic Tac Toe

# Function to check current state of block
def state(x, o):
    if(x == 1):
        return "X"
    
    if(o == 1):
        return "O"
    
    return "1"

# Function to print Table
def printTable(xstate, ostate):
    zero   = ' ' if state(xstate[0], ostate[0]) == "1" else state(xstate[0], ostate[0])
    one    = ' ' if state(xstate[1], ostate[1]) == "1" else state(xstate[1], ostate[1])
    two    = ' ' if state(xstate[2], ostate[2]) == "1" else state(xstate[2], ostate[2])
    three  = ' ' if state(xstate[3], ostate[3]) == "1" else state(xstate[3], ostate[3])
    four   = ' ' if state(xstate[4], ostate[4]) == "1" else state(xstate[4], ostate[4])
    five   = ' ' if state(xstate[5], ostate[5]) == "1" else state(xstate[5], ostate[5])
    six    = ' ' if state(xstate[6], ostate[6]) == "1" else state(xstate[6], ostate[6])
    seven  = ' ' if state(xstate[7], ostate[7]) == "1" else state(xstate[7], ostate[7])
    eight  = ' ' if state(xstate[8], ostate[8]) == "1" else state(xstate[8], ostate[8])

    print(f"\n {zero} | {one} | {two}")
    print(f"---|---|---")
    print(f" {three} | {four} | {five}")
    print("---|---|---")
    print(f" {six} | {seven} | {eight}\n")

# Function to check the winner of the game.
def checkWin(xstate, ostate):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(xstate[win[0]] + xstate[win[1]] + xstate[win[2]] == 3):
            print("\nX Won The Match\n")
            return 2
        elif(ostate[win[0]] + ostate[win[1]] + ostate[win[2]] == 3):
            print("\nO Won The Match\n")
            return 1
        
    if(sum(xstate) + sum(ostate) == 9):
        print("\nMatch Draw\n")
        return 0

    return -1

# Function to check Whether player make correct move or not.
def correctMove(possibility, pos):
    if pos in possibility:
        possibility.pop(possibility.index(pos))
        return 1
    return 0


# main
if __name__ == "__main__":

    # initial states
    xstate = [0]*9
    ostate = [0]*9
    possibility = [i for i in range(1,10)]
    turn = 0  # if 0 x's chance and if 1 o's chance

    while(True):
        # print table
        printTable(xstate, ostate)

        # X's chance
        if(turn == 0):
            print("\nX's Chance")
            pos = int(input("Enter the position (1-9) :: "))
            if(correctMove(possibility, pos)):
                xstate[pos-1] = 1
                turn = 1
            else:
                print("Invalid Move! Try Again")
                turn = 0

        # O's chance
        elif(turn == 1):
            print("\nO's Chance")
            pos = int(input("Enter the position (1-9) :: "))
            if(correctMove(possibility, pos)):
                ostate[pos-1] = 1
                turn = 0
            else:
                print("Invalid Move! Try Again")
                turn = 1

        # win or lose
        cwin = checkWin(xstate, ostate)
        if(cwin != -1):
            printTable(xstate,ostate)
            break

        
        
            