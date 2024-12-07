#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from codes.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from codes.Level import Level
from codes.Menu import Menu
from codes.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_option = menu.run()

            if menu_option in [MENU_OPTIONS[0], MENU_OPTIONS[1]]:
                player_scores = [0, 0]  # [Player1, Player2]
                levels = ['Level1', 'Level2', 'Level3']  # Lista de níveis

                for level_name in levels:
                    level = Level(self.window, level_name, menu_option, player_scores)

                    if not level.run(player_scores):
                        break  # Interromper looping jogador derrotado

                score.save(menu_option, player_scores)

            elif menu_option == MENU_OPTIONS[2]:
                score.show()

            elif menu_option == MENU_OPTIONS[3]:
                pygame.quit()
                quit()
