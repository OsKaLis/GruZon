import sys
import pygame


def check_event():
    """
    Отслеживание события мыши и клавиатуры
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(gz_settings, screen):
    """
    Обновление основного экрана игры
    """
    # Задаёт фон игры
    screen.fill(gz_settings.screen_color)

    # Отображение последнего прорисованного главного окна
    pygame.display.flip()
