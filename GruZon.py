import pygame

# Собственые модули
from settings import Settings
import biblioteka_functions as bf

def start_gruzon():
    # Создаём обьект экранап
    pygame.init()
    gz_settings = Settings()
    screen = pygame.display.set_mode((
        gz_settings.screen_width,
        gz_settings.screen_height,
        ))
    pygame.display.set_caption('GruZon')
    screen_icon = pygame.image.load(gz_settings.screen_icon)
    pygame.display.set_icon(screen_icon)


    while True:
        # Отслеживание клавиатуры и мышки
        bf.check_event()

        # Обновление основного экрана игры
        bf.update_screen(gz_settings, screen)


"""
Запуск игры (GruZon)
"""
start_gruzon()
