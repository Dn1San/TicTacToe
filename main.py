import random
import numpy as np

print("Welcome to Tic Tac Toe")
print("----------------------")

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3
leaveLoop = False
turnCounter = 0

class Board:
    def __init__(self):
        self.squares = np.zeros((rows, cols))

    def markedSquares(self, row, col, player):
        pass
        

class AI:
    def __init__(self, level=0, player=2):
        self.level = level
        self.player = player

    def rndChoice(self, board):
        aiChoice = random.choice(possibleNumbers)

    def eval(self, gameBoard):
        if self.level == 0:
            pass
        else:
            #minimax algoritham choice
            pass
            

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

def checkForWinner(gameBoard):
    # x axis
    if(gameBoard[0][0] == "X" and gameBoard[0][1] == "X" and gameBoard[0][2] == "X"):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0] == "O" and gameBoard[0][1] == "O" and gameBoard[0][2] == "O"):
        print("O has won!")
        return "O"
    elif(gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and gameBoard[1][2] == "X"):
        print("X has won!")
        return "X"
    elif(gameBoard[1][0] == "O" and gameBoard[1][1] == "O" and gameBoard[1][2] == "O"):
        print("O has won!")
        return "O"
    elif(gameBoard[2][0] == "X" and gameBoard[2][1] == "X" and gameBoard[2][2] == "X"):
        print("X has won!")
        return "X"
    elif(gameBoard[2][0] == "O" and gameBoard[2][1] == "O" and gameBoard[2][2] == "O"):
        print("O has won!")
        return "O"
    # y axis
    elif(gameBoard[0][0] == "X" and gameBoard[1][0] == "X" and gameBoard[2][0] == "X"):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0] == "O" and gameBoard[1][0] == "O" and gameBoard[2][0] == "O"):
        print("O has won!")
        return "O"
    elif(gameBoard[0][1] == "X" and gameBoard[1][1] == "X" and gameBoard[2][1] == "X"):
        print("X has won!")
        return "X"
    elif(gameBoard[0][1] == "O" and gameBoard[1][1] == "O" and gameBoard[2][1] == "O"):
        print("O has won!")
        return "O"
    elif(gameBoard[0][2] == "X" and gameBoard[1][2] == "X" and gameBoard[2][2] == "X"):
        print("X has won!")
        return "X"
    elif(gameBoard[0][2] == "O" and gameBoard[1][2] == "O" and gameBoard[2][2] == "O"):
        print("O has won!")
        return "O"
    # z axis
    elif(gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X"):
        print("X has won!")
        return "X"
    elif(gameBoard[0][0] == "O" and gameBoard[1][1] == "O" and gameBoard[2][2] == "O"):
        print("O has won!")
        return "O"
    elif(gameBoard[0][2] == "X" and gameBoard[1][1] == "X" and gameBoard[2][0] == "X"):
        print("X has won!")
        return "X"
    elif(gameBoard[0][2] == "O" and gameBoard[1][1] == "O" and gameBoard[2][0] == "O"):
        print("O has won!")
        return "O"
    

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
            aiChoice = random.choice(possibleNumbers)
            print("\nAi Choice: ", aiChoice)
            if(aiChoice in possibleNumbers):
                modifyArray(aiChoice, "O")
                possibleNumbers.remove(aiChoice)
                turnCounter += 1
                break
    
    winner = checkForWinner(gameBoard)
    if winner == "X" or winner == "O":
        leaveLoop = True
    else:
        leaveLoop = False
            
        