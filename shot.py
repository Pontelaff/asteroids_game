import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SHOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.color = (255, 255, 255)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius, 1)

    def update(self, dt: float) -> None:
        self.position += self.velocity * SHOT_SPEED * dt