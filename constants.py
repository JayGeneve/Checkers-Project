import pygame
WIDTH, HEIGHT = 800, 800

#Rows and columns
ROWS, COLS = 8,8

SQUARE_SIZE = WIDTH//COLS

#RGB COLORS - numbers only go to 255 
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/king.png'), (44, 25))
