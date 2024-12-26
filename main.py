# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# this imports all the variables from the constants file 
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    activeGame = True
    while activeGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()

# ensures that this main fuction only runs if this script is called
if __name__ == "__main__":
    main()