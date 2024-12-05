import pygame

# C

C_BLACK = (0, 0, 0)
C_BLUE = (0, 0, 255)
C_RED = (255, 0, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)

# E

ENTITY_DAMAGE = {
    'Level1-0': 0,
    'Level1-1': 0,
    'Level1-2': 0,
    'Level1-3': 0,
    'Level1-4': 0,
    'Level1-5': 0,
    'Level1-6': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
}

ENTITY_SCORE = {
    'Level1-0': 0,
    'Level1-1': 0,
    'Level1-2': 0,
    'Level1-3': 0,
    'Level1-4': 0,
    'Level1-5': 0,
    'Level1-6': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 10,
    'Enemy1Shot': 0,
    'Enemy2': 20,
    'Enemy2Shot': 0,
}

ENTITY_SPEED = {
    'Level1-0': 0,
    'Level1-1': 1,
    'Level1-2': 2,
    'Level1-3': 3,
    'Level1-4': 4,
    'Level1-5': 5,
    'Level1-6': 6,
    'Player1': 13,
    'Player1Shot': 5,
    'Player2': 15,
    'Player2Shot': 5,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1.5,
    'Enemy2Shot': 5,
    'Enemy3': 2,
    'Enemy3Shot': 5,
    'Enemy4': 2,
    'Enemy4Shot': 5,
    'Enemy5': 3,
    'Enemy5Shot': 5,
}

ENTITY_HEALTH = {
    'Level1-0': 999,
    'Level1-1': 999,
    'Level1-2': 999,
    'Level1-3': 999,
    'Level1-4': 999,
    'Level1-5': 999,
    'Level1-6': 999,
    'Player1': 200,
    'Player1Shot': 1,
    'Player2': 200,
    'Player2Shot': 2,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 50,
    'Enemy2Shot': 1,
    'Enemy3': 50,
    'Enemy3Shot': 1,
    'Enemy4': 50,
    'Enemy4Shot': 1,
    'Enemy5': 50,
    'Enemy5Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 30,
    'Player2': 30,
    'Enemy1': 150,
    'Enemy2': 130,

}

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTIONS = ('1 Jogador',
                '2 Jogadores',
                'Recorde',
                'Sair')

# P

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOT = {'Player1': pygame.K_RCTRL,
                   'Player2': pygame.K_LCTRL}

# S

SPAWN_TIME = 2000

# W

WIN_WIDTH = 1280  # 640 HD 1280 FullHD 1920
WIN_HEIGHT = 720  # 360 HD 720 FullHD 1080
