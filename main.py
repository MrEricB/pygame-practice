import pygame
import time
import random

pygame.init() #does return a tuple so it can be assigned to varialbe

#define colors RGB 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600

# takes a tuple or list
# returns a pygame surface obj
gameDisplay = pygame.display.set_mode((display_width, display_height)) # the canvas that is displayed

# updates entire pygame surface at once
# pygame.display.flip()
pygame.display.set_caption('Slither')

# only updates the part of the surface you give it. If no params then updates whole surface
pygame.display.update()

clock = pygame.time.Clock() # return a pygame clock obj for FPS

block_size = 20
FPS = 30

font = pygame.font.SysFont(None, 25)

def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size, block_size])


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2]) # note blit does not render the font to the screen, need update to do thata

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0

    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen('Game over, press C to play again or Q to quit', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop() # recursive, not efficient fix later

        # handle events, ie keypress, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                # make sure was an arrow and then witch arrow
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0   
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        # apple the snake is going to eat
        AppleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        # check for snake running into its self
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        pygame.display.update()


        # if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
        #     if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
        #         randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
        #         randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
        #         snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness 


        clock.tick(FPS) # seting FPS here
    # to exit pygame
    pygame.quit() # uninitilzes pygame
    quit() # exits python


gameLoop()
