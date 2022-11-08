import pygame
import time
import random

pygame.init()

display_width=800
display_height=600

black=(0,0,0) #R G B in tuple
white=(255,255,255)
red=(255,0,0)

block_color=(53,115,225)

car_width=150

carImage=pygame.image.load('Car_Image.jpg')

def things(thing_x_loc , thing_y_loc , thing_width , thing_height , color):
    pygame.draw.rect(gameDisplay,color,[thing_x_loc , thing_y_loc ,thing_width , thing_height ])
       
def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text=font.render("Dodged: " +str(count),True,black)
    gameDisplay.blit(text,(0,0))
    
def car(x,y):
    gameDisplay.blit(carImage,(x,y))

def crash():
    message_display('You crashed')

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface , textSurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect = text_objects(text , largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect) #first surface then rectangle aana chaiye
    pygame.display.update()
    time.sleep(2)
    game_loop()

gameDisplay=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("A bit Racey")

clock=pygame.time.Clock()

def game_loop():
    x=display_width*0.35
    y=display_height*0.60

    x_change=0
    #y_change=0

    thing_startx= random.randrange(0,display_width)
    thing_starty= -600
    thing_speed = 3
    thing_width=100
    thing_height=100

    thing_count=0
    
    dodged=0
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():#perframe per second kya event kya ho raha hai
            if event.type==pygame.QUIT:
                pygame.quit()
                                
                
            print(event)
            if event.type==pygame.KEYDOWN: #matlab key press hua hai ki nahi
                if event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5
                #elif event.key==pygame.K_UP:
                    #y_change=-5
                #elif event.key==pygame.K_DOWN:
                    #y_change=5

            if event.type==pygame.KEYUP: #matlab key release hua hai ki nahi
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
                #if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    #y_change=0

        x+=x_change    
        #y+=y_change
        
        gameDisplay.fill(white)

        things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        thing_starty+=thing_speed
        

        
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x< 0:
            crash()

        if thing_starty>display_height:
            thing_starty = 0 - thing_height
            thing_startx=random.randrange(0,display_width)
            dodged+=1
            thing_speed+=1
            thing_width+=(dodged*1.2)
            thing_count+=1

               
        if y<thing_starty+thing_height:
            print('y crossover')
            if x>thing_startx and x<thing_startx+ thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
                print('x crossover')
                crash()
              
       
        pygame.display.update()

        clock.tick(60) #framespersecond

game_loop()
pygame.quit()
