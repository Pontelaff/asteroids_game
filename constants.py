### This file contains constants and config values for the asteroids game

# Window settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FRAMES_PER_SECOND = 60

# Player settings
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_MOVE_SPEED = 200
PLAYER_SHOT_COOLDOWN = 0.25
PLAYER_DEFAULT_COLOR = (255, 255, 255)

# Asteroid settings
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_COLOR = (255, 255, 255)

# Bullet settings
SHOT_RADIUS = 5
SHOT_SPEED = 500
SHOT_DEFAULT_COLOR = (255, 255, 255)

# Powerup settings
POWERUP_RADIUS = 15
POWERUP_ACTIVE_SECONDS = 10
POWERUP_SPAWN_TIME_SECONDS = 3
POWERUP_COLORS = {"invincibility": (200, 200, 0),
                  "triple_shot": (255, 0, 0),
                  "quick_shot": (0, 50, 255),
                  "score_multiplier": (0, 255, 50)}