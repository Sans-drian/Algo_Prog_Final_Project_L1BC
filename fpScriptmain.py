from utils import * #import everything from the utils folder for this main script

#set/define the window of the pygame
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#change the title/caption of the window
pygame.display.set_caption("Sans' Pixel Art Maker")



##----------- Setting up the GRID on screen

#setting up the individual pixel to create the grid
def init_grid(rows, cols, color):
    grid = []

    for i in range(rows): #loop these row of arrays (pixels) to create the grid pattern
        grid.append([])
        for _ in range(cols): #add the color for all these individual pixels
            grid[i].append(color)

    return grid


##----------- Draw functions on the window/program

#function to draw the grid
def draw_grid(win, grid):
    for i, row in enumerate(grid): # for i and for j lines determine the position of each of the individual pixel of the grid 
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    #the + 1 is to add the last missing line on the sides of the window on x and y coordinate
    if DRAW_GRID_LINES:
        for i in range(ROWS + 1): #draw grid lines on the X coordinate/ for the horizontal lines     
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1): #draw grid lines on the y coordinate / for the verticle lines
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HIEGHT))


#function to call of the window's characteristics
def draw(win, grid, buttons): 
    win.fill(BG_COLOR) #fill with bg color (from settings.py)
    draw_grid(win, grid) #draw the grid

    for button in buttons: #draw all the buttons created
        button.draw(win)

    pygame.display.update() #update the display of the program


#find the position of the pixels on the canvas in accordance to the mouse position
def get_row_col_from_pos(pos): 
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS: #detect the non-drawable area
        raise IndexError

    return row, col


##----------- EVENT LOOP/RUNNING THE PROGRAM: Loop to let everything run until the user exits the program

run = True
clock = pygame.time.Clock() #setting up a clock
grid = init_grid(ROWS, COLS, BG_COLOR) #call function to create the grid
drawing_color = BLACK

## Creating the buttons

button_preY1 = HEIGHT - TOOLBAR_HIEGHT/2 - 60 #preset 1 of Y variable to replace in creating Buttons
button_preY2 = HEIGHT - TOOLBAR_HIEGHT/2 - 1 #preset 1 of Y variable to replace in creating Buttons

#Buttons list
buttons = [
    #TOP ROW
    Button(10, button_preY1, 50, 50, RED), #create the red color button
    Button(70, button_preY1, 50, 50, ROSE), #create the rose color button
    Button(130, button_preY1, 50, 50, MAGENTA), #create the magenta color button
    Button(190, button_preY1, 50, 50, VIOLET), #create the violet color button
    Button(250, button_preY1, 50, 50, BLUE), #create the blue color button
    Button(310, button_preY1, 50, 50, AZURE), #create the purple color button
    Button(370, button_preY1, 50, 50, BLACK), #create the black color button    
    Button(430, button_preY1, 50, 50, WHITE, "Erase", BLACK), #create the erase button
    Button(490, button_preY1, 50, 50, WHITE, "Clear", BLACK), #create the clear button
    #BOTTOM ROW
    Button(10, button_preY2, 50, 50, ORANGE), #create the orange color button
    Button(70, button_preY2, 50, 50, YELLOW), #create the yellow color button
    Button(130, button_preY2, 50, 50, CHARTREUSE), #create the chartreuse color button
    Button(190, button_preY2, 50, 50, GREEN), #create the green color button
    Button(250, button_preY2, 50, 50, SPRINGGREEN), #create the spring green color button
    Button(310, button_preY2, 50, 50, CYAN), #create the cyan color button
]

while run:
    clock.tick(FPS) #make sure this loop does not run faster than the set variable of FPS (To balance performance)
    
    for event in pygame.event.get(): #check all events of the pygame that is happening
        if event.type == pygame.QUIT: #if the user has quit the window
            run = False

        if pygame.mouse.get_pressed()[0]: #check if lmb is pressed
            posOfMouse = pygame.mouse.get_pos() #find the x and y position of the mouse

            #Check if the position of the mouse click is inside the drawable area
            try:
                row, col = get_row_col_from_pos(posOfMouse)
                grid[row][col] = drawing_color #if inside the drawable area, change the pixel color
            
            except IndexError: #if not inside drawable area
                for button in buttons: 
                    if not button.clicked(posOfMouse): #check if the position of mouse is not with the button click function
                        continue

                    drawing_color = button.color #change the color based on where the user clicks the buttons

                    #creating the clear function for clear button
                    if button.text == "Clear": 
                        grid = init_grid(ROWS, COLS, BG_COLOR) #to clear the canvas, just reset the canvas (copy the previous grid initializer script)
                        drawing_color = BLACK #after clearing, change the "brush" to black


    draw(WIN, grid, buttons) #call draw function and use the display size to draw the white BG

pygame.quit()