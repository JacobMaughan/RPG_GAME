# Descripion: Game Enums
# Author: Jacob Maughan

# Sys Imports
from enum import Enum

class GameState(Enum):
    MAIN_MENU = 1
    GAME = 2
    PAUSE = 3

class Direction(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4
    LEFT_UP = 5
    LEFT_DOWN = 6
    RIGHT_UP = 7
    RIGHT_DOWN = 8

class PlayerState(Enum):
    IDLE = 1
    WALKING = 2
    ATTACKING = 3
    INTERACTING = 4
    KNOCKED = 5

class EnemyState(Enum):
    IDLE = 1
    WALKING = 2