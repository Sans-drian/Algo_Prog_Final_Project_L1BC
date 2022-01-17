import pygame

#Initialize pygame sources
pygame.init()
pygame.font.init()

#the variables are constants, hence why they are all in capital
#defining the colors that will be used in the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#PRIMARY COLORS
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
#SECONDARY COLORS
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
VIOLET = (128, 0, 255)
#OTHER/MIXED COLORS
ROSE = (199, 21, 133)
MAGENTA = (255, 0, 255)
CHARTREUSE = (128, 255, 0)
SPRINGGREEN = (0, 255, 128)
CYAN = (0, 255, 255)
AZURE = (0, 128, 255)



#defining the framerate for game
FPS = 120

#defining the size of the pygame window
WIDTH, HEIGHT = 600, 750

#create the size of the pixels
ROWS = COLS = 70

#defining the size of the toolbar
TOOLBAR_HIEGHT = HEIGHT - WIDTH

#specifying/clarifying the width and height of each pixel
PIXEL_SIZE = WIDTH // COLS

#define the canvas color
BG_COLOR = WHITE

#make the grid to see where pixels are placed on the screen
DRAW_GRID_LINES = False

#function that returns a font object with a specific size
def get_font(size):
    return pygame.font.SysFont("consolas", size)