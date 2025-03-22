import pygame
from enum import Enum
from circleshape import CircleShape
from constants import POWERUP_RADIUS

class PowerUpType(Enum):
    INVINCIBLE = 1

class PowerUp(CircleShape):
    def __init__(self, x: int, y: int, type: PowerUpType):
        super().__init__(x, y, POWERUP_RADIUS)
        self.type = type
        self.color = self.get_color_from_type(type)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def get_color_from_type(self, type: PowerUpType) -> tuple[int, int, int]:
        match type:
            case PowerUpType.INVINCIBLE:
                return (200, 200, 0)
            case _:
                return (255, 255, 255)