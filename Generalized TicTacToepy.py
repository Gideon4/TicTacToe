import sys

players=["X","O"]
turn=0
size=3
board=[[" " for i in range(size)] for j in range(size)]

def eachturn():
    global turn
    position=input("It is "+players[turn%len(players)]+"'s turn. Where would you like to go?")
    try:
        if board[ord(position[0].upper())-65][int(position[1])-1]==" ":
            board[ord(position[0].upper())-65][int(position[1])-1]=players[turn%len(players)]
        else:
            print("You can't go there!")
            eachturn()
    except:
        print("That isn't a valid spot!")
        eachturn()
    [print(" ".join(str(board[i][j]) for j in range(size))) for i in range(size)]
    wincond()
    if turn<(size**2-1):
        turn+=1
        eachturn()
    else:
        print("Cats Game")

def wincond():
    numbers=[]
    [numbers.append(row) for row in board]
    [numbers.append([board[j][i] for j in range(size)]) for i in range(size)]
    numbers.append([board[i][i] for i in range(size)])
    numbers.append([board[i][size-1-i] for i in range(size)])
    for row in numbers:
        if row==[players[turn%len(players)] for i in range(size)]:
            print(players[turn%len(players)]+" wins!")
            sys.exit()
    
eachturn()
