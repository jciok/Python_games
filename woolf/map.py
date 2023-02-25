# file with map settings

# impoort pygame library
import pygame as pg

# set _ as False for better perception of map below
_ = False

# minimap with false for empty spaces and true for walls
mini_map= [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, 1, 1, 1, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, _, 1, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, _, 1, _, _, _, _, 1, _, _, 1],
    [1, _, _, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 1, _, _, _, 1, 1, _,_, _, _, 1, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# map class
class Map:
    # constructor with passed object game
    def __init__(self, game):

        #  przypisuje obiekt gry przekazany jako argument do atrybutu game nowo 
        # tworzonego obiektu
        self.game = game

        #  przypisuje obiekt mini_map do atrybutu mini_map,
        self.mini_map = mini_map

        # tworzy pusty słownik word_map
        self.world_map = {}

        # wywołuje metodę get_map() dla nowo utworzonego obiektu.
        self.get_map()

    # functon that generate game map from mini_map
    def get_map(self):

        # for loop which is iterate by row in mini_map and for every row is 
        # iterate by value, this loop return position of each element in 
        # mini_map and save it to world_map
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[i, j] = value

    # function that draw world_map on screen
    def draw(self):

        # list comprehasion -- we drow squares for elements in world_map
        # sqares will be gray 100x100 with 2 px border
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0]*100, pos[1]*100, 100, 100), 2) for pos in self.world_map]
