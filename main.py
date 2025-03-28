#!/usr/bin/env python3

import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerup import PowerUp, PowerUpType
from powerupspawner import PowerUpSpawner
from scoreboard import Scoreboard

def init_game_environment() -> tuple[pygame.time.Clock, pygame.Surface]:
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    _, numfail = pygame.init()
    pygame.font.init()
    if numfail != 0:
        print(f"Failed to initialize {numfail} pygame modules")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    return clock, screen

def init_object_groups() -> tuple[pygame.sprite.Group, pygame.sprite.Group, pygame.sprite.Group, pygame.sprite.Group]:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    PowerUp.containers = (powerups, drawable)
    PowerUpSpawner.containers = updatable
    Scoreboard.containers = drawable

    return updatable, drawable, asteroids, shots, powerups

def end_game() -> None:
    print("Game Over!")
    pygame.event.post(pygame.event.Event(pygame.QUIT))

def main() -> int:
    clock, screen = init_game_environment()
    updatable, drawable, asteroids, shots, powerups = init_object_groups()
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    scoreboard = Scoreboard()
    _ = AsteroidField()
    _ = PowerUpSpawner()
    delta_t_seconds = 0

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

        screen.fill((0,0,0))
        updatable.update(delta_t_seconds)
        for powerup in powerups:
            if player.collides_with(powerup):
                player.collect_powerup(powerup.type)
                powerup.kill()
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                if player.powerup == PowerUpType.INVINCIBLE:
                    scoreboard.add_score(asteroid.get_size(), player.get_score_multiplier())
                    asteroid.split()
                else:
                    end_game()
            for shot in shots:
                if shot.collides_with(asteroid):
                    scoreboard.add_score(asteroid.get_size(), player.get_score_multiplier())
                    asteroid.split()
                    shot.kill()
                    break
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        delta_t_seconds = clock.tick(FRAMES_PER_SECOND)/1000


if __name__ == "__main__":
    sys.exit(main())