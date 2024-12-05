#!/usr/bin/python
# -*- coding: utf-8 -*-

from codes.Entity import Entity
from codes.Const import ENTITY_SPEED


class EnemyShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centery += ENTITY_SPEED[self.name]
