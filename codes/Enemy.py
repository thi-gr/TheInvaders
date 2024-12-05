#!/usr/bin/python
# -*- coding: utf-8 -*-
from codes.Const import ENTITY_SPEED, WIN_HEIGHT
from codes.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.bottom > WIN_HEIGHT:
            # self.rect.bottom = -10
            pass
