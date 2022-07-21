import pygame
from pygame.sprite import Sprite

class KletkaPlochadi(Sprite):
    """
    Создаёт клетку для части карты
    """
    def __init__(self, screen, gz_settings, napravlenie, adres_kartinki):
        super().__init__()
        self.screen = screen
        self.napravlenie = napravlenie
        self.adres_kartinki = adres_kartinki
        self.po_x = 0
        self.po_y = 0

        # загруска скрина площади
        self.image = pygame.image.load(self.adres_kartinki)
        self.rect = self.image.get_rect()

        # Начальные расположения
        self.rect.x = self.po_x
        self.rect.y = self.po_y

    def risuyu(self):
        """
        Рисую клетку с направлением на главное окно
        """
        self.screen.blit(self.image, self.rect)
