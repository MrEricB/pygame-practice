import pygame

pygame.init() #does return a tuple so it can be assigned to varialbe

#define colors RGB 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

# takes a tuple or list
# returns a pygame surface obj
gameDisplay = pygame.display.set_mode((800, 600)) # the canvas that is displayed

# updates entire pygame surface at once
# pygame.display.flip()
pygame.display.set_caption('Slither')

# only updates the part of the surface you give it. If no params then updates whole surface
pygame.display.update()

# simple game loop
gameExit = False

# first block in the snake, ie head of the snake
lead_x = 300
lead_y = 300
lead_x_change = 0

clock = pygame.time.Clock() # return a pygame clock obj for FPS

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            # make sure was an arrow and then witch arrow
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10
        # allows use to keep moving while holding key down, stops when key is up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0


    lead_x += lead_x_change

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])
    # better way to draw rec but more complexe, since fill can be graphics accelerated
    # gameDisplay.fill(red, rect=[200,200,50,50])
    pygame.display.update()

    clock.tick(15) # seting FPS here

# to exit pygame
pygame.quit() # uninitilzes pygame
quit() # exits python

