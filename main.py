# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# this imports all the variables from the constants file 
from constants import *
from player import Player

def main():
    pygame.init()

    # basic game management 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    activeGame = True
    clock = pygame.time.Clock()
    dt = 0

    # groups 
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    Player.containers = (drawable, updatable)

    # actors
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # ====== THE GAME LOOP ======
    while activeGame:
        # Run Events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Draw Screen
        pygame.Surface.fill(screen, (0,0,0))
        for o in updatable:
            o.update(dt)
        for o in drawable:
            o.draw(screen)
        pygame.display.flip()
        # Control FPS
        dt = clock.tick(60) / 1000

# ensures that this main fuction only runs if this script is called
if __name__ == "__main__":
    main()