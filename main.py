import pygame
from constants import *
from circleshape import *
from player import *
from asteroids import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH /2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Asteroid_group = pygame.sprite.Group()
    AsteroidField_group = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (Asteroid_group, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(x,y)
    a_field = AsteroidField()


    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
         screen.fill((0,0,0))
         updatable.update(dt)
         for objects in Asteroid_group:
              if objects.collision(player):
                   print("Game over!")
                   exit()
         for players in drawable:
              players.draw(screen)
         pygame.display.flip()
         dt = game_clock.tick(60) / 1000
        
if __name__ == "__main__":
        main()
