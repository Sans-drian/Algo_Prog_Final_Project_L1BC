from .settings import *

class Button:
    ##-------------- The initializer function
    
    def __init__(self, x, y, width, height, color, text = None, text_color = BLACK): 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    ##--------------- The function to draw the buttons and it's characteristics

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height)) #Draw the rectangle itself
        pygame.draw.rect(win, BLACK, (self.x, self.y, self.width, self.height), 2) #Draw the outline of the rectangle

        #If there is text, draw the text
        if self.text:
            button_font = get_font(17) #set size of font
            text_surface = button_font.render(self.text, 1, self.text_color) #render the text
            win.blit(text_surface, (self.x + self.width/2 - text_surface.get_width()/2, self.y + self.height/2 - text_surface.get_height()/2)) #place the text on the window/screen

    ##-------------- The function to check if a certain position of the mouse is clicked by the user

    def clicked(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width): #check if the mouse position is not in the x bound of the rect
            return False
        if not (y >= self.y and y <= self.y + self.height): #check if the mouse position is not in the y bound of the rect
            return False

        return True #if the mouse position is in the x and y bound of the rect, click.