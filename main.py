#!/usr/bin/env python3

import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def init_game_environment() -> tuple[pygame.time.Clock, pygame.Surface]:
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    _, numfail = pygame.init()
    if numfail != 0:
        print(f"Failed to initialize {numfail} pygame modules")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    return clock, screen

def init_game_objects() -> tuple[pygame.sprite.Group, pygame.sprite.Group]:
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    return updatable, drawable

def main() -> int:
    clock, screen = init_game_environment()
    updatable, drawable = init_game_objects()
    delta_t_seconds = 0

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0

        screen.fill((0,0,0))
        updatable.update(delta_t_seconds)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        delta_t_seconds = clock.tick(FRAMES_PER_SECOND)/1000


if __name__ == "__main__":
    sys.exit(main())