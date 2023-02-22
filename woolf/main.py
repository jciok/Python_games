# impoort pygame library
import pygame as pg

#  import sys library
import sys

# import settings from setins.py
from settings import *

#add game class
class Game:

    # constructor where we initalize pygame modules (konstruktor to specjalna 
    # metoda, która jest wywoływana automatycznie, gdy tworzony jest nowy 
    # obiekt, w pythonie zawsze nazywa się __init__() i przyjmuje argument 
    # self, czyli tworzony obiekt, zdefiniowane tu wartosći zostaną ustawione 
    # na starcie przy tworzeniu każdego obiektu)
    def __init__(self):

        # initialize pygames modules
        pg.init()

        # set screen size to RES -- see settings.py
        self.screen = pg.display.set_mode(RES)

        # create new clock object
        self.clock = pg.time.Clock()

    # new game metod, empty for now
    def new_game(self):
        pass
    
    # metod of screen update, for now cdisplay number of FPS in window caption
    def update(self):

        # function that refresh object on screen
        pg.display.flip()

        # function that limits the program speed to get a certain number FPS 
        self.clock.tick(FPS)

        # Funkcja set_caption() pozwala na ustawienie tytułu okna gry lub 
        # aplikacji. W tej linii kodu, funkcja ta jest wywoływana, aby ustawić 
        # tytuł okna na wartość zwracaną przez funkcję get_fps() zegara (clock) 
        # podzieloną przez 1, zaokrągloną do jednego miejsca po przecinku przy użyciu f stringa -- :`.1f`.
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    # draw mmetod for now screen will be black
    def draw(self):
        # wypełnij ekran na czarno
        self.screen.fill('black')

    # metoda do obłsugi zdarzeń
    def check_events(self):
        
        # pętla for, w której obłsugujemy zdarzenia
        for event in pg.event.get():

            # obłsuga zamknięcia okna przyciskiem lub klawiszem
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()


    #run metod with main loop of the game   
    def run(self):
        #nieskończona pętla while
        while True:
            # wołanie wcześniej utworzonych metod/funkcji
            self.check_events()
            self.update()
            self.draw()


# Stworzenie instancji naszej gry if sprawdza, czy aktualnie wykonywany skrypt 
# jest uruchamiany jako program główny, czy też jest importowany jako moduł do 
# innego skryptu. W Pythonie każdy skrypt lub moduł ma specjalną zmienną o 
# nazwie __name__, która przechowuje nazwę pliku. Gdy plik jest uruchamiany 
# jako program główny, __name__ ma wartość '__main__', a jeśli jest importowany 
# jako moduł do innego skryptu, to ma wartość nazwy pliku.
if __name__ == '__main__':
    # utworzenie obiektu gry
    game = Game()

    #wywołanie metody run dla obiektu game
    game.run()