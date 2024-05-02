import sys
import pygame
import numpy as np
import random
import copy

from math import inf
from constants5 import *

boards = 0

#Pygame Setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE AI")
screen.fill(BG_COLOUR)

class Board():
    
    def __init__(self):
        self.squares = np.zeros((ROWS,COLS))
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0
        
    def final_state(self, show = False):
        #Vertical Wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] == self.squares[3][col] == self.squares[4][col] != 0:
                if show:
                    color = CIRC_COLOUR if self.squares[0][col] == 2 else CROSS_COLOUR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20)
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col]

        # horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] == self.squares[row][3] == self.squares[row][4] != 0:
                if show:
                    color = CIRC_COLOUR if self.squares[row][0] == 2 else CROSS_COLOUR
                    iPos = (20, row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]

        # desc diagonal
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] == self.squares[3][3] == self.squares[4][4] != 0:
            if show:
                color = CIRC_COLOUR if self.squares[1][1] == 2 else CROSS_COLOUR
                iPos = (20, 20)
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # asc diagonal
        if self.squares[4][0] == self.squares[3][1] == self.squares[2][2]== self.squares[1][3]== self.squares[0][4] != 0:
            if show:
                color = CIRC_COLOUR if self.squares[1][1] == 2 else CROSS_COLOUR
                iPos = (20, HEIGHT - 20)
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # no win yet
        return 0
            
    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs +=1

    def empty_sqr(self,row, col):
        return self.squares[row][col] == 0
    
    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in  range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row, col))
        return empty_sqrs
    
    def is_full(self):
        return self.marked_sqrs == 25
    
    def is_empty(self):
        return self.marked_sqrs == 0

class AI:
    def __init__(self, level=2, player = 2):
        self.level = level
        self.player = player

    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_sqrs))

        return empty_sqrs[idx]
    
    def minimax(self, board, depth, maximizing, alpha = -inf, beta = -inf):
        case = board.final_state()

        #Player 1 Win
        if case == 10 + depth:
            return 1, None #eval, move
        #Player 2 Win
        if case == 2:
            return -10 - depth, None
        #Draw
        elif board.is_full():
            return 0, None
        
        global boards
        boards += 1

        best_move = None
        value = None
    
        
        empty_sqrs = board.get_empty_sqrs()

        for (row, col) in empty_sqrs:
            temp_board = copy.deepcopy(board)
            temp_board.mark_sqr(row, col, self.player)
            value = self.minimax(temp_board,depth + 1, True)[0]
            if (value is not None and (value > alpha if maximizing else value < beta)):
                if maximizing:
                    alpha = value
                else:
                    beta = value
                if (alpha != -inf and beta != inf and alpha >= beta if maximizing else beta >= alpha):
                    break
                best_move = row, col

            #test
            print(temp_board.squares)
            print(f'best move is {best_move} eval score is {beta}')
        if maximizing:
            return alpha, best_move

        return beta, best_move

        
        
    def extended_ai(self, board):
        case = board.final_state()
        empty_sqrs = board.get_empty_sqrs()

        for (row, col) in empty_sqrs:
            temp_board = copy.deepcopy(board)
            temp_board.mark_sqr(row, col, self.player)
            case = temp_board.final_state()
            if case == 2:
                return row,col
            
        for (row, col) in empty_sqrs:
            temp_board = copy.deepcopy(board)
            temp_board.mark_sqr(row, col, self.player % 2 + 1)
            case = temp_board.final_state()
            if case == 1:
                return row,col

        if (1, 1) in empty_sqrs:
            print('exists')
            return [1, 1]
        else:
            idx = random.randrange(0, len(empty_sqrs))
            print(empty_sqrs)
            return empty_sqrs[idx]
            

    def eval(self, main_board):

        global boards
        boards = 0

        if self.level == 0:
            #Random Choice
            eval = 'random'
            move = self.rnd(main_board)
        elif self.level == 1:
            #Extended AI Choice
            eval = 'test'
            move = self.extended_ai(main_board)
        else:
            #Minimax Algorithim Choice
            eval, move = self.minimax(main_board, 5, False)
            if move is None:
                move = self.rnd(main_board)
            print(f'calls to minimax: {boards}')

        print(f'AI has chosen to mark the square in pos {move} with eval of {eval}')

        return move
    
class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1
        self.gamemode = 'ai'
        self.running = True
        self.show_lines()

    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    def show_lines(self):
        screen.fill(BG_COLOUR)

        blockSize = 120 #Set the size of the grid block
        for x in range(0, WIDTH, blockSize):
            for y in range(0, HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(screen, LINE_COLOUR, rect, 1)
       
    def draw_fig(self, row, col):
        if self.player == 1:
            #desc line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOUR, start_desc, end_desc, CROSS_WIDTH)
            #asc line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOUR, start_asc, end_asc, CROSS_WIDTH)
        elif self.player == 2:
            center = (col * SQSIZE +SQSIZE // 2, row * SQSIZE +SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOUR, center, RADIUS, CIRC_WIDTH)
    def next_turn(self):
        self.player = self.player % 2 + 1

    def change_gamemode(self):
        if self.gamemode == 'pvp': self.gamemode = 'ai'
        else: self.gamemode = 'pvp'

    def is_over(self):
        if self.board.final_state() != 0:
            print(f'player {self.board.final_state()} has Won the game!')
        elif self.board.is_full():
            print('The game is a draw!')
        return self.board.final_state(show=True) != 0 or self.board.is_full()

    def reset(self):
        self.__init__()

def main():
    #Object
    game = Game()
    ai = game.ai
    board = game.board

    #Main Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                #g-gamemode
                if event.key == pygame.K_g:
                    game.change_gamemode()
                #r-restart game
                if event.key == pygame.K_r:
                    game.reset()
                    ai = game.ai
                    board = game.board
                # 0-random ai
                if event.key == pygame.K_0:
                    ai.level = 0
                # 1-extended ai
                if event.key == pygame.K_1:
                    ai.level = 1
                # 2-extended ai
                if event.key == pygame.K_2:
                    ai.level = 2
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] //SQSIZE
                if board.empty_sqr(row, col) and game.running:
                   game.make_move(row, col)

                   if game.is_over():
                       game.running = False
                #test
                #print(board.squares)

        if game.gamemode == 'ai' and game.player == ai.player and game.running:
            pygame.display.update()

            row, col = ai.eval(board)
            game.make_move(row, col)

            if game.is_over():
                game.running = False

        pygame.display.update()


main()