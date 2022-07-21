import pygame
from pygame.sprite import Group

# Собственые модули
from settings import Settings
import biblioteka_functions as bf
from kletka_plochadi import KletkaPlochadi

def start_gruzon():
    # Создаём обьект экранап
    pygame.init()
    gz_settings = Settings()
    screen = pygame.display.set_mode((
        gz_settings.screen_width,
        gz_settings.screen_height,
        ))
    pygame.display.set_caption('GruZon')
    #screen_icon = pygame.image.load(gz_settings.screen_icon)
    #pygame.display.set_icon(screen_icon)

    # Пробую создать карту

    #ur_karta = KletkaPlochadi(screen, gz_settings,
    #    {'naprav': 'levo',
    #    'adres_kartinki': 'pictures/dorojka/dorojka_levo.png',
    #    'po_x': 0,
    #    'po_y': 0,
    #    })

    full_karta = Group()

    # Генерирую карту
    bf.generik_karta(screen, gz_settings, full_karta)

    while True:
        # Отслеживание клавиатуры и мышки
        bf.check_event()

        # Задаёт фон игры
        screen.fill(gz_settings.screen_color)

        # Сценарий выполнения игры
        if gz_settings.uroveny_play == 0:
            pass
        elif gz_settings.uroveny_play == 1:
            # Рисую прощать
            #ur_karta.risuyu()
            pass

        # Обновление основного экрана игры
        bf.update_screen(gz_settings, screen, full_karta)


"""
Запуск игры (GruZon)
"""
start_gruzon()
