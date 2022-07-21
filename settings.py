class Settings():
    """
    Клас хранения настроек игры (GruZon)
    """
    def __init__(self):
        # Настройки главного окна
        self.screen_width = 840
        self.screen_height = 600
        # отступы для нижней и верхней панели
        self.screen_razm_verh_panely = 50
        self.screen_razm_niz_panely = 50
        # отступ для машин (куда грузят)
        self.screen_panely_grugovik = 100
        # отступ для склада (откуда товар)
        self.screen_panely_sklad = 100

        self.screen_color = (0, 255, 0)
        # иконка для игры
        self.screen_icon = 'pictures/icon_GruZon.png'
        # Картинки для клеток площади
        self.varianti_plojatki = {
            'kletka_ploch_pravo' : 'pictures/dorojka/dorojka_pravo.png',
            'kletka_ploch_levo' : 'pictures/dorojka/dorojka_levo.png',
            'kletka_ploch_niz' : 'pictures/dorojka/dorojka_niz.png',
            'kletka_ploch_verh' : 'pictures/dorojka/dorojka_verh.png',
            }
        # Уровень исполнения игры
        self.uroveny_play = 1
