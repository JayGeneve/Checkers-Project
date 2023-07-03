import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.game import Game
from checkers.board import  Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jay's Checkers")

#Tells us what row and column we are in based on the position of our mouse-->Can select a piece and where we want to go using our mouse
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True 
    #make sure it doesn't run too fast or too slow 
    clock = pygame.time.Clock()
    game = Game(WIN)

    
    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner("You're the Winner!"))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            #If we press a button on our mouse it will tell us what piece is chosen/ whose turn it is 
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row,col)
                

        game.update()

    pygame.quit()


main()