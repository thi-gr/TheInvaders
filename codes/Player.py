#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from codes.Const import WIN_WIDTH, ENTITY_SPEED, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOT, ENTITY_SHOT_DELAY
from codes.Entity import Entity
from codes.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left >= 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right <= WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOT[self.name]] and self.rect.left >= 0:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx + 23, self.rect.centery - 35))
