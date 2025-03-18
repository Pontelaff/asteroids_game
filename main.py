#!/usr/bin/env python3

import sys
import pygame
from constants import *
from player import Player

def init_game() -> tuple[pygame.time.Clock, pygame.Surface, Player]:
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    _, numfail = pygame.init()
    if numfail != 0:
        print(f"Failed to initialize {numfail} pygame modules")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    return clock, screen, player

def main() -> int:
    clock, screen, player = init_game()
    delta_t_seconds = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        delta_t_seconds = clock.tick(FRAMES_PER_SECOND)/1000


if __name__ == "__main__":
    sys.exit(main())