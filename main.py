import pygame
from constants import *
from player import Player

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0.0
  
  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  
  Player.containers = (updateable, drawable)
  
  player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
  
  # Game Loop
  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    
    # Update - FIRST UPDATE STEP
    for sprite in updateable:
        sprite.update(dt)
    
    # Draw - FIRST DRAW STEP
    screen.fill((0, 0, 0))  # Fill the screen with black
    
    for sprite in drawable:
        sprite.draw(screen)
    
    pygame.display.flip()  # Update the display - LAST DRAW STEP
    dt = clock.tick(60) / 1000  # Limit the frame rate to 60 FPS
      

if __name__ == "__main__":
    main()