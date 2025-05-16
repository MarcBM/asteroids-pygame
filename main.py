import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0.0
  
  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  
  Player.containers = (updateable, drawable)
  Asteroid.containers = (updateable, drawable, asteroids)
  AsteroidField.containers = (updateable)
  Shot.containers = (updateable, drawable, shots)
  
  player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
  asteroid_field = AsteroidField()
  
  # Game Loop
  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    
    # Update - FIRST UPDATE STEP
    for sprite in updateable:
        sprite.update(dt)
      
    # Check for collisions
    for asteroid in asteroids:
      if player.collides(asteroid):
        print("Game Over!")
        sys.exit()
      for shot in shots:
        if shot.collides(asteroid):
            asteroid.kill()
            shot.kill()
            break
    
    # Draw - FIRST DRAW STEP
    screen.fill((0, 0, 0))  # Fill the screen with black
    
    for sprite in drawable:
        sprite.draw(screen)
    
    pygame.display.flip()  # Update the display - LAST DRAW STEP
    dt = clock.tick(60) / 1000  # Limit the frame rate to 60 FPS
      

if __name__ == "__main__":
    main()