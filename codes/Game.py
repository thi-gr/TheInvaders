#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from codes.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from codes.Level import Level
from codes.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_retorno = menu.run()

            if menu_retorno in [MENU_OPTIONS[0], MENU_OPTIONS[1]]:
                level = Level(self.window, 'Level1', menu_retorno)
                level_retorno = level.run()
            elif menu_retorno == MENU_OPTIONS[2]:
                pass
            elif menu_retorno == MENU_OPTIONS[3]:
                pygame.quit()
                quit()