import pygame
import random
from constants import POWERUP_SPAWN_TIME_SECONDS, SCREEN_WIDTH, SCREEN_HEIGHT
from powerup import PowerUp, PowerUpType


class PowerUpSpawner(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > POWERUP_SPAWN_TIME_SECONDS:
            self.spawn_timer = 0.0
            x_pos = random.randint(30, SCREEN_WIDTH - 30)
            y_pos = random.randint(30, SCREEN_HEIGHT - 30)
            type = random.choice(list(PowerUpType))
            PowerUp(x_pos, y_pos, type)