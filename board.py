import pygame 
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        #how many red and how many white pieces do we have
        self.red_left = self.white_left = 12 
        self.red_kings = self.white_kings = 0 
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE,  SQUARE_SIZE, SQUARE_SIZE ))  
    
    def move(self, piece, row, col):
        #Way to swap positions in a list 
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    #Give the board object a row and a column and it will return a piece back 
    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self): 
        for row in range(ROWS):
            #Want to have a list of what each row is going to have inside of it
            self.board.append([])
            for col in range(COLS):
                #Places the checker pieces in a staggered position"If the current row that we are on has a remainder of 2, if that equals the row plus 1, mod 2 we can draw the red or white cube "
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row,col,WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                #If we do not add a piece we are going to add a 0 so that we can seperate the pieces and be able to look at the list and determine where the pieces are 
                else:
                    self.board[row].append(0)


    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
        
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        
        return None
        
    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece. col + 1 
        row = piece.row  

        if piece.color == RED or piece.king:
            #look at "_traverse" parameters to understand
            moves.update(self._traverse_left(row - 1 , max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1 , max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1 , min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1 , min(row+3, ROWS), 1, piece.color, right))

        return moves    
    #How we are able to jump over other pieces and see what pieces are able to be jumped over 
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start,stop,step):
            if left < 0:
                break

            current = self.board[r][left]
            #If its 0 and last existed, then we can jump over it
            if current == 0:
                #If we have skipped for a checkers piece, we found a blank square and we dont have anything we can skip again, we will be unable to move 
                if skipped and not last:
                    break
                #If we skipped and found something else we can skip over, we are able to move again - combing the last piece we just skipped into this "moves" to see whether we can jump one or two and what pieces we need to remove
                elif skipped:
                    moves[(r,left)] = last + skipped
                else:
                    moves[(r,left)] = last
                #If current is equal to 0 and last - #Recursive method- Once we see if we can jump over a piece we see if we are able to do it agian
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left - 1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break 
            else:
                last = [current]
            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start,stop,step):
            if right >= COLS:
                break

            current = self.board[r][right]
            #If its 0 and last existed, then we can jump over it
            if current == 0:
                #If we have skipped for a checkers piece, we found a blank square and we dont have anything we can skip again, we will be unable to move 
                if skipped and not last:
                    break
                #If we skipped and found something else we can skip over, we are able to move again - combing the last piece we just skipped into this "moves" to see whether we can jump one or two and what pieces we need to remove
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r,right)] = last
                #If current is equal to 0 and last - #Recursive method- Once we see if we can jump over a piece we see if we are able to do it agian
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right - 1, skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right= + 1, skipped=last))
                break
            elif current.color == color:
                break 
            else:
                last = [current]
            right += 1
        
        return moves
                                        
