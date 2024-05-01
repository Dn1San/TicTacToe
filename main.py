import random
import copy
import numpy as np

print("Welcome to Tic Tac Toe")
print("----------------------")
print("\nPlease pick a difficulty level from numbers 1 - 3")
print("1 = Easy")
print("2 = Hard")
print("3 = Master")
diffecultyLevel = input()


possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3
leaveLoop = False
turnCounter = 0
      

def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameBoard[x][y], end=" |")
    
    print("\n+---+---+---+")

def modifyArray(num, turn):
    num -= 1
    if(num == 0):
        gameBoard[0][0] = turn
    elif(num == 1):
        gameBoard[0][1] = turn
    elif(num == 2):
        gameBoard[0][2] = turn
    elif(num == 3):
        gameBoard[1][0] = turn
    elif(num == 4):
        gameBoard[1][1] = turn
    elif(num == 5):
        gameBoard[1][2] = turn
    elif(num == 6):
        gameBoard[2][0] = turn
    elif(num == 7):
        gameBoard[2][1] = turn
    elif(num == 8):
        gameBoard[2][2] = turn


    
def checkGameIsOver(gameBoard):
    for i in range(3):
        #check x axis
        if(gameBoard[i][0] == gameBoard[i][1] and gameBoard[i][1] == gameBoard[i][2]):
           return gameBoard[i][0]
        #check y axis
        if(gameBoard[0][i] == gameBoard[1][i] and gameBoard[1][i] == gameBoard[2][i]):
           return gameBoard[0][i]
    #check diagonals
    if(gameBoard[0][0] == gameBoard[1][1] and gameBoard[1][1] == gameBoard[2][2]):
        return gameBoard[0][0]
    if(gameBoard[0][2] == gameBoard[1][1] and gameBoard[1][1] == gameBoard[2][0]):
        return gameBoard[0][2]
    #check draw (board full but no winner)
    for x in range(3):
        for y in range(3):
            if not (gameBoard[x][y] == "X" or gameBoard[x][y] == "O"):
                return False
                # game is still going on
    return "Draw" #game is a draw  
    
def easyAI():
    return random.choice(possibleNumbers)

def hardAI():
    tempBoard = copy.deepcopy(gameBoard)
    for num in range(len(possibleNumbers)):
        if(num == 0):
            tempBoard[0][0] = "O"
        elif(num == 1):
            tempBoard[0][1] = "O"
        elif(num == 2):
            tempBoard[0][2] = "O"
        elif(num == 3):
            tempBoard[1][0] = "O"
        elif(num == 4):
            tempBoard[1][1] = "O"
        elif(num == 5):
            tempBoard[1][2] = "O"
        elif(num == 6):
            tempBoard[2][0] = "O"
        elif(num == 7):
            tempBoard[2][1] = "O"
        elif(num == 8):
            tempBoard[2][2] = "O"
        winner = checkGameIsOver(tempBoard)
    
        if winner == "O":
            choice = num
        elif 


    for x in range(len(possibleNumbers)):
        if possibleNumbers[x] == 5:
            choice = x

    else:
        choice = random.choice(possibleNumbers)
    
    return choice
    
def masterAI(gameBoard, depth, ismaximizer):
    case = checkGameIsOver(gameBoard)

    # player wins
    if case == "X":
        return 1
    #ai wins
    if case == "O":
        return -1
    #draw
    if case == "Draw":
        return 0
    
    if ismaximizer:
        pass

    elif not ismaximizer:
        minEval = 100
        bestMove = None
        emptySquares = possibleNumbers

        for (row, col) in emptySquares:
            tempBoard = copy.deepcopy(gameBoard)
            tempBoard

while(leaveLoop == False):
    # It's the players turn
    if(turnCounter % 2 == 1):
        printGameBoard()
        numberPicked = int(input("\nChoose a number between 1 and 9: "))
        if(numberPicked >= 1 or numberPicked <= 9):
            modifyArray(numberPicked, "X")
            possibleNumbers.remove(numberPicked)
        else:
            print("Input is already in use. Please pick another number!")
        turnCounter += 1  
    # It's the ai's turn
    else:
        # Test ai
        while(True):
            if diffecultyLevel == "1":
                aiChoice = easyAI()
            elif diffecultyLevel == "2":
                aiChoice = hardAI()
            elif diffecultyLevel == "3":
                aiChoice = masterAI()
            print("\nAi Choice: ", aiChoice)
            if(aiChoice in possibleNumbers):
                modifyArray(aiChoice, "O")
                possibleNumbers.remove(aiChoice)
                turnCounter += 1
                break
    
    winner = checkGameIsOver(gameBoard)
    if winner == "X":
        print("X has won!")
        leaveLoop = True
    elif winner == "O":
        print("O has won!")
        leaveLoop = True
    elif winner == "Draw":
        print("Draw!")
        leaveLoop = True
    else:
        leaveLoop = False
            
        