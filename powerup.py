import pygame
from enum import Enum
from circleshape import CircleShape
from constants import POWERUP_RADIUS, POWERUP_COLORS

class PowerUpType(Enum):
    INVINCIBLE = 1
    TRIPPLE_SHOT = 2
    QUICK_SHOT = 3
    SCORE_MULTIPLIER = 4

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
                return POWERUP_COLORS["invincibility"]
            case PowerUpType.TRIPPLE_SHOT:
                return POWERUP_COLORS["triple_shot"]
            case PowerUpType.QUICK_SHOT:
                return POWERUP_COLORS["quick_shot"]
            case PowerUpType.SCORE_MULTIPLIER:
                return POWERUP_COLORS["score_multiplier"]
            case _:
                return (255, 255, 255)