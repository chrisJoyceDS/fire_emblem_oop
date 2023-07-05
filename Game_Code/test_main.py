from User import User
from Session import Session
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    # RENDER YOUR GAME HERE
    while True:
        start = input("Do you want to start the game? Yes/No ").lower()
        if start == 'yes':
            user = User()
            break
        elif start == 'no':
            print("Please restart the game to continue")
            break
        else:
            print("Only yes or no are valid options")

    if user:
        session = Session(user)
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    
    clock.tick(60) # limits fps to 60
    
pygame.quit()