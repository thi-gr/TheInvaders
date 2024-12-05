#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from codes.Background import Background
from codes.Const import WIN_WIDTH
from codes.Enemy import Enemy
from codes.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1-':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1-{i}', (0, 0)))
                    list_bg.append(Background(f'Level1-{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (200, WIN_WIDTH / 2.3))
            case 'Player2':
                return Player('Player2', (WIN_WIDTH - 300, WIN_WIDTH / 2.3))

            case 'Enemy1':
                return Enemy('Enemy1', (random.randint(5, WIN_WIDTH - 75), -10))
            case 'Enemy2':
                return Enemy('Enemy2', (random.randint(5, WIN_WIDTH - 75), -10))
