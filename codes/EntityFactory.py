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
        # Função auxiliar criar listas Backgrounds.
        def create_continuous_backgrounds(level_prefix, win_width):
            return [
                Background(f'{level_prefix}{i}', (WIN_WIDTH * j, 0))
                for i in range(7)
                for j in range(2)  # 2 instâncias/imagem (1 continuação)
            ]

        match entity_name:
            # Casos Níveis
            case level if level.startswith('Level') and level.endswith('-'):
                return create_continuous_backgrounds(level, WIN_WIDTH)

            # Casos Jogadores
            case 'Player1':
                return Player('Player1', (200, WIN_WIDTH / 2.3))
            case 'Player2':
                return Player('Player2', (WIN_WIDTH - 300, WIN_WIDTH / 2.3))

            # Casos Inimigos
            case enemy if enemy.startswith('Enemy'):
                return Enemy(enemy, (random.randint(5, WIN_WIDTH - 75), -10))
