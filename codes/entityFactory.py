#!/usr/bin/python
# -*- coding: utf-8 -*-
from codes.Const import WIN_WIDTH, WIN_HEIGHT
from codes.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1-':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1-{i}', (0,0)))
                    list_bg.append(Background(f'Level1-{i}', (WIN_WIDTH, 0)))
                return list_bg
