#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from codes.Const import C_WHITE, WIN_HEIGHT, MENU_OPTIONS, EVENT_ENEMY, SPAWN_TIME, C_BLUE, C_RED, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from codes.Enemy import Enemy
from codes.Entity import Entity
from codes.EntityFactory import EntityFactory
from codes.EntityMediator import EntityMediator
from codes.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + '-'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)

        if game_mode == MENU_OPTIONS[1]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]) -> bool:
        # Inicializa música do nível
        pygame.mixer_music.load(f'./assets/musics/{self.name}.wav')
        pygame.mixer_music.set_volume(0.3)

        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            # Atualizar entidades Desenhar tela
            self.update_entities(player_score)

            # Processar eventos
            if not self.handle_events(player_score):
                return False  # Sem jogadores, finalizar jogo

            # Exibir informações Level
            self.display_level_info(clock)

            # Atualizar tela
            pygame.display.flip()

            # Verificar colisões / entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # Verifica se o timeout chegou a zero
            if self.timeout <= 0:
                self.save_scores(player_score)
                return True  # Nível concluído

    # Funções Auxiliares
    def update_entities(self, player_score: list[int]):
        """Atualiza entidades e desenha na tela."""
        for ent in self.entity_list:
            # Atualizar score e HP jogadores
            if isinstance(ent, Player):
                color = C_BLUE if ent.name == 'Player1' else C_RED
                y_offset = 35 if ent.name == 'Player1' else 65
                self.level_text(24, f'{ent.name} - HP:{ent.health} | Score: {ent.score}', color, (10, y_offset))

            # Atualiza superfície e movimento
            self.window.blit(source=ent.surf, dest=ent.rect)
            ent.move()

            # Adiciona disparos de jogadores e inimigos
            if isinstance(ent, (Player, Enemy)):
                shot = ent.shot()
                if shot is not None:
                    self.entity_list.append(shot)

    def handle_events(self, player_score: list[int]) -> bool:
        """Processa eventos do Pygame e gerencia estados do jogo."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Criação de inimigos com base no nível
            if event.type == EVENT_ENEMY:
                enemy_type = self.get_enemy_type()
                self.entity_list.append(EntityFactory.get_entity(enemy_type))

            # Gerenciamento de timeout
            if event.type == EVENT_TIMEOUT:
                self.timeout -= TIMEOUT_STEP

        # Verifica se ainda há jogadores
        if not any(isinstance(ent, Player) for ent in self.entity_list):
            return False  # Nível falhou (sem jogadores restantes)

        return True

    def get_enemy_type(self) -> str:
        """Retorna o tipo de inimigo baseado no nível atual."""
        match self.name:
            case 'Level1':
                return random.choice(('Enemy1', 'Enemy2'))
            case 'Level2':
                return random.choice(('Enemy3', 'Enemy4'))
            case 'Level3':
                return 'Enemy5'

    def save_scores(self, player_score: list[int]):
        """Salva os scores dos jogadores ao final do tempo."""
        for ent in self.entity_list:
            if isinstance(ent, Player):
                if ent.name == 'Player1':
                    player_score[0] = ent.score
                elif ent.name == 'Player2':
                    player_score[1] = ent.score

    def display_level_info(self, clock):
        """Exibe informações do nível na tela."""
        self.level_text(24, f'{self.name} - TimeOut: {self.timeout / 1000 :.1f}s', C_WHITE, (10, 5))
        self.level_text(14, 'THIAGO GARCIA RODRIGUES - RU 4478564', C_WHITE, (10, WIN_HEIGHT - 35))
        self.level_text(14, 'CST ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - EAD', C_WHITE, (10, WIN_HEIGHT - 20))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
