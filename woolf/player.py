from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game=game
        self.x, slef.y= PLAYER_POS
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
        dx, dy=0,0
        speed=PLAYER_SPEED * self.delta_time

        speed_cos=speed*cos_a
        spee_sin=speed*sin_a

        

    def update(self):
        self.movement

    # property -- dekoratory, które sądostępne z zewnątrze klasy, ale obliczane 
    # są dynamicznie wewqnątrz klasy, dzięki temu można odczytać pozycję gracza 
    # z innych części kodu
    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)