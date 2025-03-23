import pygame
import math
from circleshape import CircleShape
from shot import Shot
from powerup import PowerUpType
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED, PLAYER_SHOT_COOLDOWN, POWERUP_ACTIVE_SECONDS, POWERUP_COLORS

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.color = (255, 255, 255)
        self.shot_cooldown = 0.0
        self.powerup = None
        self.powerup_time = 0.0

    def triangle(self) -> list[int]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, self.color, self.triangle(), 2)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt

    def shoot(self) -> None:
        if self.shot_cooldown <= 0.0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            self.shot_cooldown = PLAYER_SHOT_COOLDOWN
            if self.powerup == PowerUpType.QUICK_SHOT:
                self.shot_cooldown /= 3
                shot.color = (0, 50, 255)
            if self.powerup == PowerUpType.TRIPPLE_SHOT:
                shot2 = Shot(self.position.x, self.position.y)
                shot3 = Shot(self.position.x, self.position.y)
                shot2.velocity = pygame.Vector2(0, 1).rotate(self.rotation + 20)
                shot3.velocity = pygame.Vector2(0, 1).rotate(self.rotation - 20)
                shot.color = (255, 0, 0)
                shot2.color = (255, 0, 0)
                shot3.color = (255, 0, 0)

    def get_score_multiplier(self) -> PowerUpType:
        if self.powerup == PowerUpType.SCORE_MULTIPLIER:
            return 3
        return 1

    def apply_powerup(self) -> None:
        if self.powerup_time <= 0:
            self.powerup = None
            self.color = (255, 255, 255)
            return

        if self.powerup == PowerUpType.INVINCIBLE:
            red = 200 + 50*math.sin(self.powerup_time*5)
            green = 200 + 50*math.sin(self.powerup_time*5 + 1)
            blue = 200 + 50*math.sin(self.powerup_time*5 + 2)
            self.color = (red, green, blue)
            return

        if self.powerup == PowerUpType.SCORE_MULTIPLIER:
            self.color = POWERUP_COLORS["score_multiplier"]

    def update(self, dt: float) -> None:
        self.shot_cooldown -= dt
        self.powerup_time -= dt

        if self.powerup is not None:
            self.apply_powerup()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Rotate right
            self.rotate(dt)
        if keys[pygame.K_s]:
            # Move backwards
            self.move(-dt)
        if keys[pygame.K_w]:
            # Move forward
            self.move(dt)
        if keys[pygame.K_SPACE]:
            # Shoot
            self.shoot()

    def collect_powerup(self, powerup: PowerUpType) -> None:
        self.powerup_time = POWERUP_ACTIVE_SECONDS
        self.powerup = powerup