# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import *
from shot import Shot

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
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for upd_obj in updateable:
            upd_obj.update(dt)
        
        for ast in asteroids:
            if ast.check_collision(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if ast.check_collision(shot):
                    shot.kill()
                    ast.kill()
        
        screen.fill(color=(0,0,0))
        
        for drw_obj in drawable:
            drw_obj.draw(screen)
        
        pygame.display.flip()
        print("Screen updated")
        
        # limit FPS to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
