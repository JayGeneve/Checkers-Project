import pygame
from.constants import RED, WHITE, BLUE, SQUARE_SIZE
from checkers.board import  Board

class Game:
    def __init__(self, win):
        self._init()
        #What piece is selected by the player
        self.selected_piece = None
        self.board = Board()
        self.turn = RED
        #This will show us the valid available moves
        self.valid_moves = {}
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    #Private so the user only calls the reset command and doesn't see everything else 
    def _init(self):
        self.selected = None
        self.board = Board
        self.turn = RED
        self. valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
       self._init()

    def select(self, row, col):
        #If a piece is selected, than lets move try to move to the row and col inputted 
        if self.selected:
            result = self._move(row, col)
            #If the move isn't valid, then the move is reset so you are able to give a different input 
            if not result:
                self.selected = None
                self.select(row, col)

        #If the piece selected is white or black and its that players turn than it will allow you to play, if not than False 
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece 
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
    
        return False

    
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        
        return True
    
    def draw_valid_moves(self,moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,(col*SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED



        
