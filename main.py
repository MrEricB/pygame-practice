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

gameExit = False


while not gameExit:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [400,300,10,10])
    # better way to draw rec but more complexe, since fill can be graphics accelerated
    gameDisplay.fill(red, rect=[200,200,50,50])


    pygame.display.update()


# to exit pygame
pygame.quit() # uninitilzes pygame
quit() # exits python

