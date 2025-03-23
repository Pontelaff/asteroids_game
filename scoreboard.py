import pygame
import pygame.freetype
from constants import SCREEN_WIDTH

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self.containers)
        self.font = pygame.freetype.Font(None, size = 50)
        self.position = (SCREEN_WIDTH/2 - 100, 30)
        self.score = 0

    def draw(self, surf: pygame.Surface) -> None:
        text = f"SCORE: {self.score}"
        self.font.render_to(surf, self.position, text, fgcolor = (255, 255, 255), size = 40)

    def add_score(self, score: int, multiplier: int) -> None:
        self.score += score * multiplier

