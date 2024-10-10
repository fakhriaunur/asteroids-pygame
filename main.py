# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    print("Init pygame")
    pygame.init()
    print("Pygame initialized")
    
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0,0,0))
        player.draw(screen)
        pygame.display.flip()
        print("Screen updated")
        
        # limit FPS to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
