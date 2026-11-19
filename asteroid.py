import pygame
import random
from logger import log_state, log_event
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self,x:float,y:float,radius: float):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):

        self.position += (self.velocity * dt)

    def split(self):

        pygame.sprite.Sprite.kill(self)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        random_angle = random.uniform(20,50)

        rotated_vector_uno = self.velocity.rotate(random_angle)
        rotated_vector_dos = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_uno = Asteroid(self.position[0],self.position[1],new_radius)
        asteroid_dos = Asteroid(self.position[0],self.position[1],new_radius)

        asteroid_uno.velocity = rotated_vector_uno * 1.2
        asteroid_dos.velocity = rotated_vector_dos * 1.2




    