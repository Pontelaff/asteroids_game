#!/usr/bin/env python3

import sys
import pygame
from constants import *

def main() -> int:
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    numpass, numfail = pygame.init()
    if numfail != 0:
        return -1
    clock = pygame.time.Clock()
    delta_t_seconds = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        screen.fill((0,0,0))
        pygame.display.flip()
        delta_t_seconds = clock.tick(FRAMES_PER_SECOND)/1000


if __name__ == "__main__":
    sys.exit(main())