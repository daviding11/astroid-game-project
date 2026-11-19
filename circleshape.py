import pygame
import math

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other) -> bool:

        #distance = math.dist(self.position,other.position)
        #distance = pygame.math.Vector2.distance_to(self.position,other.position)
        distance = self.position.distance_to(other.position)
        radius_sum = self.radius + other.radius

        return distance <= (self.radius + other.radius)

        # if distance > radius_sum:
        #     return False
        # else:
        #     return True
