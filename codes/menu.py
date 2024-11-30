#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from codes.Const import WIN_WIDTH, WIN_HEIGHT, C_BLACK, MENU_OPTIONS


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.transform.scale(pygame.image.load('./assets/images/menuBg.png'), (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./assets/musics/menuMusic.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(200, 'The Invaders', C_BLACK, ((WIN_WIDTH/2), 150))

            for i in range(len(MENU_OPTIONS)):
                self.menu_options(70, MENU_OPTIONS[i], C_BLACK, ((WIN_WIDTH / 2), 400 + 80 * i))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./assets/fonts/Together.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def menu_options(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("comic sans", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
