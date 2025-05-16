import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    
  def update(self, dt):
    self.position += self.velocity * dt
    
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      spawn_angle = random.uniform(20, 50)
      new_forward_1 = self.velocity.rotate(spawn_angle) * 1.2
      new_forward_2 = self.velocity.rotate(-spawn_angle) * 1.2
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      
      new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
      new_asteroid_1.velocity = new_forward_1
      new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
      new_asteroid_2.velocity = new_forward_2
    
  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)