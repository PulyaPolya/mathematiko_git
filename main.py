import game_functions as gf
import pygame
from settings import Settings
from random_square import RandomSquare
from randomizer import Random
from text import Text
from table import Table


def run_game():
    pygame.init()
    g_settings = Settings()
    screen = pygame.display.set_mode((g_settings.screen_width, g_settings.screen_height))
    square_positions = gf.get_square_positions()
    squares = gf.get_squares(screen,  square_positions)[0]
    dict_squares = gf.get_squares(screen,  square_positions)[1]
    keys = dict_squares.keys()
    free_squares = []
    for key in keys:
        free_squares.append(key)
    table = Table(5,g_settings, keys)
    random = Random()
    random_square = RandomSquare(screen)
    arr_numbers = []
    text = Text(screen,g_settings)
    while True:
        gf.update_screen(screen, g_settings, squares, random, random_square, dict_squares,
                         arr_numbers,  text,  table)


run_game()
