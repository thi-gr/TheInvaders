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
    'Level2-0': 0,
    'Level2-1': 0,
    'Level2-2': 0,
    'Level2-3': 0,
    'Level2-4': 0,
    'Level2-5': 0,
    'Level2-6': 0,
    'Level3-0': 0,
    'Level3-1': 0,
    'Level3-2': 0,
    'Level3-3': 0,
    'Level3-4': 0,
    'Level3-5': 0,
    'Level3-6': 0,
    'Player1': 10,
    'Player1Shot': 10,
    'Player2': 10,
    'Player2Shot': 10,
    'Enemy1': 10,
    'Enemy1Shot': 20,
    'Enemy2': 10,
    'Enemy2Shot': 20,
    'Enemy3': 10,
    'Enemy3Shot': 30,
    'Enemy4': 10,
    'Enemy4Shot': 30,
    'Enemy5': 10,
    'Enemy5Shot': 50,
}

ENTITY_SCORE = {
    'Level1-0': 0,
    'Level1-1': 0,
    'Level1-2': 0,
    'Level1-3': 0,
    'Level1-4': 0,
    'Level1-5': 0,
    'Level1-6': 0,
    'Level2-0': 0,
    'Level2-1': 0,
    'Level2-2': 0,
    'Level2-3': 0,
    'Level2-4': 0,
    'Level2-5': 0,
    'Level2-6': 0,
    'Level3-0': 0,
    'Level3-1': 0,
    'Level3-2': 0,
    'Level3-3': 0,
    'Level3-4': 0,
    'Level3-5': 0,
    'Level3-6': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 10,
    'Enemy1Shot': 0,
    'Enemy2': 20,
    'Enemy2Shot': 0,
    'Enemy3': 30,
    'Enemy3Shot': 0,
    'Enemy4': 40,
    'Enemy4Shot': 0,
    'Enemy5': 50,
    'Enemy5Shot': 0,
}

ENTITY_SPEED = {
    'Level1-0': 0,
    'Level1-1': 1,
    'Level1-2': 2,
    'Level1-3': 3,
    'Level1-4': 4,
    'Level1-5': 5,
    'Level1-6': 6,
    'Level2-0': 0,
    'Level2-1': 1,
    'Level2-2': 2,
    'Level2-3': 3,
    'Level2-4': 4,
    'Level2-5': 5,
    'Level2-6': 6,
    'Level3-0': 0,
    'Level3-1': 1,
    'Level3-2': 2,
    'Level3-3': 3,
    'Level3-4': 4,
    'Level3-5': 5,
    'Level3-6': 6,
    'Player1': 15,
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
    'Level2-0': 999,
    'Level2-1': 999,
    'Level2-2': 999,
    'Level2-3': 999,
    'Level2-4': 999,
    'Level2-5': 999,
    'Level2-6': 999,
    'Level3-0': 999,
    'Level3-1': 999,
    'Level3-2': 999,
    'Level3-3': 999,
    'Level3-4': 999,
    'Level3-5': 999,
    'Level3-6': 999,
    'Player1': 200,
    'Player1Shot': 1,
    'Player2': 200,
    'Player2Shot': 2,
    'Enemy1': 10,
    'Enemy1Shot': 1,
    'Enemy2': 10,
    'Enemy2Shot': 1,
    'Enemy3': 20,
    'Enemy3Shot': 1,
    'Enemy4': 20,
    'Enemy4Shot': 1,
    'Enemy5': 30,
    'Enemy5Shot': 1,
}

ENTITY_SHOT_DELAY = {
    'Player1': 30,
    'Player2': 30,
    'Enemy1': 150,
    'Enemy2': 140,
    'Enemy3': 130,
    'Enemy4': 120,
    'Enemy5': 100,
}

EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2

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

# T

TIMEOUT_LEVEL = 1000  # 20000
TIMEOUT_STEP = 100

# W

WIN_WIDTH = 1280  # 640 HD 1280 FullHD 1920
WIN_HEIGHT = 720  # 360 HD 720 FullHD 1080

# S

SPAWN_TIME = 2000

SCORE_POS = {'Title': (WIN_WIDTH / 2, 80),
             'EnterName': (WIN_WIDTH / 2, 200),
             'Name': (WIN_WIDTH / 2, 350),
             'Label': (WIN_WIDTH / 2, 150),
             0: (WIN_WIDTH / 2, 200),
             1: (WIN_WIDTH / 2, 250),
             2: (WIN_WIDTH / 2, 300),
             3: (WIN_WIDTH / 2, 350),
             4: (WIN_WIDTH / 2, 400),
             5: (WIN_WIDTH / 2, 450),
             6: (WIN_WIDTH / 2, 500),
             7: (WIN_WIDTH / 2, 550),
             8: (WIN_WIDTH / 2, 600),
             9: (WIN_WIDTH / 2, 650),
             }
