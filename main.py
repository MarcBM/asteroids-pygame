import pygame
from constants import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  
  # Game Loop
  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    
    screen.fill((0, 0, 0))  # Fill the screen with black
    
    
    pygame.display.flip()  # Update the display - LAST DRAW STEP
    dt = clock.tick(60)  # Limit the frame rate to 60 FPS
      

if __name__ == "__main__":
    main()