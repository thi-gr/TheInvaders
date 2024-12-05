#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from codes.Const import WIN_WIDTH, ENTITY_SPEED, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from codes.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left >= 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right <= WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass