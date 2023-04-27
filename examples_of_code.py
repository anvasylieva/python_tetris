import pygame
from copy import deepcopy
from random import choice
from const import *

# to create an empty black window
WIDTH, HEIGHT = 10, 20
TILE: int = 30
GAME_RES = WIDTH * TILE, HEIGHT * TILE
# GAME_RES = 800, 600

pygame.init()
game_sc = pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()
grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(WIDTH) for y in range(HEIGHT)]

figures = [[pygame.Rect(x + WIDTH // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in FIGURES_POSITIONS]
figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)

# figure = deepcopy(choice(figures))
figure = figures[3]

while True:
    game_sc.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # draw figures
    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_sc, pygame.Color("white"), figure_rect)

    # draw grid
    [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]

    pygame.display.flip()
    clock.tick()
