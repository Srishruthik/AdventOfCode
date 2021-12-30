import numpy as np
def calculate(gameBoard,winNum):
    add = 0
    for row in gameBoard:
        for elem in row:
            if elem != True:
                add+=int(elem)
                
    print(add*int(winNum))
file = open('file.txt','r')
data = []
for i in file:
    data.append(i.split())
key = data[0][0].split(",")
board_ =[]
for i in range(1,len(data)):
    if data[i] != []:
        board_.append(data[i])
gameBoard = []
k = 0 
index = 0
for i in board_:
    if k == 0:
        gameBoard.append([])
    gameBoard[index].append(i)
    k+=1
    if k == 5: 
        k = 0 
        index+=1
def checkWin(board,winNum):
    for game in board:
        for row in game:
            
            if len(set(row)) == 1:
                print(game,winNum)
                calculate(game,winNum)
                return True
    
    for game in board:
        for t in [game,np.transpose(game)]:
            for row in t:
                if len(set(row)) == 1:  
                    calculate(game,winNum)    
                    return True
    return False

doBreak = False
for winNum in key:
    for board in gameBoard:
        for curr in range(len(board)):
            for token in range(len(board[curr])):
                k = (board[curr][token])
                if int(k) == int(winNum):
                    board[curr][token] = True
                    if checkWin(gameBoard,winNum):
                        doBreak = True                
    if doBreak: 
        break       