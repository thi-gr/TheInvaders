import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_ESCAPE, K_BACKSPACE, K_RETURN
from pygame.font import Font

from codes.Const import C_WHITE, SCORE_POS, MENU_OPTIONS, C_BLACK
from codes.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/images/scoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./assets/musics/scoreMusic.wav')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(72, 'PARABÉNS!!!', C_BLACK, SCORE_POS['Title'], True)
            if game_mode == MENU_OPTIONS[0]:
                score = player_score[0]
                text = 'Mago Azul entre com seu nome (4 caracteres):'
            if game_mode == MENU_OPTIONS[1]:
                if player_score[0] > player_score[1]:
                    score = player_score[0]
                    text = 'Mago Azul entre com seu nome (4 caracteres):'
                elif player_score[0] < player_score[1]:
                    score = player_score[1]
                    text = 'Mago Vermelho entre com seu nome (4 caracteres):'
                else:
                    score = (player_score[0] + player_score[1]) / 2
                    text = 'Empate! Entre com seu nome do Time (4 caracteres):'

            self.score_text(36, text, C_BLACK, SCORE_POS['EnterName'], True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(48, name, C_BLACK, SCORE_POS['Name'], False)
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./assets/musics/scoreMusic.wav')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(72, 'RESULTADOS - TOP 10', C_BLACK, SCORE_POS['Title'], True)
        self.score_text(48, 'NOME      PLACAR            DATA      ', C_BLACK, SCORE_POS['Label'], True)
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_player, name, score, date = player_score
            self.score_text(48, f'{name}      {score :06d}      {date}', C_BLACK,
                            SCORE_POS[list_score.index(player_score)], False)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.key == K_RETURN:
                        return

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, bld: bool):
        text_font: Font = pygame.font.SysFont("courier new", text_size, bld)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
