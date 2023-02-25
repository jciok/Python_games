from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game=game
        self.x, self.y= PLAYER_POS
        self.angle=PLAYER_ANGLE

    def movement(self):
        # 
        #                *---------  X
        #                |  +a    . dx
        #                |    +   . 
        #                |..... + speed 
        #                  dy
        #                Y
        # dx = speed*cos(a) dy= speed*sin(a)  
        # Po co komu Pitagoras? Do liczenia zmian położenia gracza w 
        # woolfenstainie :D
        # a to kąt , speed to prędkość z jakągracz się porusza wciskając w tym 
        # wypadku W, dx to pozycja x a dy to y  opisująca jak gracz porusza się 
        # na mapie
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle) 

        # ustanowienie początkowej pozycji na 0,
        dx, dy=0,0

        # obliczenie prędkość ruchu gracza w grze, gdzie "PLAYER_SPEED" to 
        # stała prędkość określona dla gracza, a "self.game.delta_time" to 
        # czas, jaki upłynął od ostatniej klatki animacji gry.
        speed=PLAYER_SPEED * self.game.delta_time

        # Te dwie linie kodu obliczają składowe prędkości gracza wzdłuż osi X i 
        # Y na podstawie kierunku ruchu gracza określonego przez kąt "a" (w 
        # radianach). Zmienna "speed" zawiera prędkość gracza obliczoną 
        # wcześniej, a "cos_a" i "sin_a" to wartości cosinusa i sinusa kąta 
        # "a". Wartości te są obliczane przy użyciu funkcji trygonometrycznych 
        # biblioteki matematycznej Pythona. "speed_cos" to składowa prędkości 
        # gracza wzdłuż osi X, a "speed_sin" to składowa prędkości gracza 
        # wzdłuż osi Y. Wykorzystując te składowe prędkości, można określić, 
        # jak bardzo gracz powinien przesunąć się wzdłuż osi X i Y w danej 
        # klatce animacji, aby zachować określoną prędkość i kierunek ruchu
        speed_cos=speed*cos_a
        speed_sin=speed*sin_a

        # Ten fragment kodu w języku Python obsługuje ruch postaci gracza oraz 
        # zmianę jej kierunku na podstawie naciśniętych klawiszy przez 
        # użytkownika. Najpierw pobierane są aktualnie naciśnięte klawisze przy 
        # użyciu funkcji "pg.key.get_pressed()". Następnie, dla każdego z 
        # klawiszy "W", "S", "A", "D", obliczana jest nowa wartość przesunięcia 
        # postaci gracza w osiach X i Y w zależności od aktualnie ustawionego 
        # kierunku ruchu. Jeśli klawisz "W" jest naciśnięty, to przesunięcie 
        # będzie dodatnie wzdłuż składowych prędkości gracza. Jeśli klawisz "S" 
        # jest naciśnięty, to przesunięcie będzie ujemne wzdłuż składowych 
        # prędkości gracza. Analogicznie, klawisze "A" i "D" odpowiadają za 
        # zmianę kierunku ruchu gracza w poziomie. Następnie, przesunięcie jest 
        # dodawane do aktualnej pozycji gracza w osiach X i Y, aby przesunąć 
        # postać o odpowiednią wartość. Jeśli użytkownik naciska klawisze 
        # "LEFT" lub "RIGHT", to kąt obrotu postaci gracza zmieniany jest w 
        # zależności od wartości stałej "PLAYER_ROT_SPEED" i czasu między 
        # kolejnymi klatkami animacji gry. Naciśnięcie klawisza "LEFT" 
        # zmniejsza kąt obrotu, a naciśnięcie klawisza "RIGHT" zwiększa kąt 
        # obrotu. Kąt obrotu postaci gracza jest przechowywany w zmiennej 
        # "angle".
        keys=pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
        
        self.x+=dx
        self.y+=dy

        if keys[pg.K_LEFT]:
            #print("K_LEFT pressed")
            self.angle -=PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            #print("K_RIGHT pressed")
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def draw(self):
        pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                     (self.x * 100 + WIDTH * math.cos(self.angle),
                     self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 
                       15)

    def update(self):
        self.movement()

    # property -- dekoratory, które sądostępne z zewnątrze klasy, ale obliczane 
    # są dynamicznie wewqnątrz klasy, dzięki temu można odczytać pozycję gracza 
    # z innych części kodu
    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)