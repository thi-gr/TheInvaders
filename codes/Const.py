import pygame

# C

C_BLACK = (0, 0, 0)
C_YELLOW = (255, 255, 0)
C_WHITE = (255, 255, 255)

# E

ENTITY_SPEED = {
    'Level1-0': 0,
    'Level1-1': 1,
    'Level1-2': 2,
    'Level1-3': 3,
    'Level1-4': 4,
    'Level1-5': 5,
    'Level1-6': 6,
    'Player1': 13,
    'Player2': 15,
    'Enemy1': 1,
    'Enemy2': 2,
    'Enemy3': 3,
    'Enemy4': 4,
    'Enemy5': 5,
}

ENTITY_HEALTH ={
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
