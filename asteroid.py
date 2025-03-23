import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (255, 255, 255)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def get_size(self) -> int:
        return self.radius

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle) * 1.2
        vector2 = self.velocity.rotate(-angle)
        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid1.velocity = vector1
        asteroid2.velocity = vector2
