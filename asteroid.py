import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle (screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.randint(20,50)
        first_asteroid_velocity = self.velocity.rotate(random_angle)
        second_asteroid_velocity = self.velocity.rotate(0 - random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid_one.velocity = first_asteroid_velocity * 1.2
        asteroid_two.velocity = second_asteroid_velocity * 1.2


