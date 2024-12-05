#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from codes.Const import WIN_WIDTH, WIN_HEIGHT, C_BLACK, MENU_OPTIONS, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/images/menuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./assets/musics/menuMusic.wav')
        pygame.mixer_music.play(-1)

        while True:
            # Desenho das imagens
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(200, 'The Invaders', C_BLACK, ((WIN_WIDTH/2), 150))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_opt(70, MENU_OPTIONS[i], C_YELLOW, ((WIN_WIDTH / 2), 400 + 80 * i))
                else:
                    self.menu_opt(70, MENU_OPTIONS[i], C_BLACK, ((WIN_WIDTH / 2), 400 + 80 * i))

            pygame.display.flip()

            # Análise de todos os eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if evento.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1

                    if evento.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./assets/fonts/Together.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def menu_opt(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("comic sans", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
