import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED, PLAYER_SHOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.color = (255, 255, 255)
        self.shot_cooldown = 0.0

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

    def update(self, dt: float) -> None:
        self.shot_cooldown -= dt
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