import sys
import pygame
from random import choice

# Мои модули
from kletka_plochadi import KletkaPlochadi

def check_event():
    """
    Отслеживание события мыши и клавиатуры
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(gz_settings, screen, full_karta):
    """
    Обновление основного экрана игры
    """
    # рисую карту
    full_karta.draw(screen)

    # Отображение последнего прорисованного главного окна
    pygame.display.flip()

def generik_karta(screen, gz_settings, full_karta):
    """
    Генерирую карту случайным образом
    """
    # Это можно создать функцыю для создания списка вида карт карт
    varianti_karti = []
    for key in gz_settings.varianti_plojatki:
        varianti_karti.append(key)

    # генерю карту рандом полную
    #gener_karta = choice(varianti_karti)
    #print(gener_karta)
    #gg = choice(varianti_karti)
    #print(gg)
    #print(gz_settings.varianti_plojatki[gg])

    # добавить уровень ещ

    # задаю начальные кординаты
    po_x = gz_settings.screen_panely_grugovik
    po_y = gz_settings.screen_razm_verh_panely

    for y in range(kolich_liniy_po_y(gz_settings)):
        for x in range(kolich_stolp_po_x(gz_settings)):
            # создаю площадь
            ploj = choice(varianti_karti)
            new_ploj = KletkaPlochadi(screen, gz_settings, ploj,
                gz_settings.varianti_plojatki[ploj])
            # задаю кординаты площади
            new_ploj.rect.x = po_x
            new_ploj.rect.y = po_y

            po_x += new_ploj.rect.width

            full_karta.add(new_ploj)
        po_y += new_ploj.rect.height
        po_x = gz_settings.screen_panely_grugovik


def kolich_stolp_po_x(gz_settings):
    """ размер карты по столбам """
    rez = (gz_settings.screen_width -
        (gz_settings.screen_panely_grugovik +
        gz_settings.screen_panely_sklad)) // 64
    return rez

def kolich_liniy_po_y(gz_settings):
    """ размер карты по строкам """
    rez = (gz_settings.screen_height -
        (gz_settings.screen_razm_verh_panely +
        gz_settings.screen_razm_niz_panely)) // 65
    return rez
