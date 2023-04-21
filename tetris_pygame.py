import pygame
from copy import deepcopy
from random import choice, randrange
from const import *


def check_borders(i):
    # check if our object is within borders
    # if not 0 < figure[i].x < WIDTH - 1: (alternative code line, should be tested)
    if figure[i].x < 0 or figure[i].x > WIDTH - 1:
        return False
    elif figure[i].y > HEIGHT - 1 or field[figure[i].y][figure[i].x]:
        return False
    return True


def get_record():
    try:
        with open('record.txt', 'r') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record.txt', 'w') as f:
            f.write('0')


def set_record(record, score):
    rec = max(int(record), score)
    with open('record.txt', 'w') as f:
        f.write(str(rec))


pygame.init()
sc = pygame.display.set_mode(RES)
game_sc = pygame.time.Clock()

# grid = []
# for x in range(WIDTH):
#     for y in range(HEIGHT):
#         grid.append(pygame.Rect(x * TILE, y * TILE, TILE, TILE))

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(WIDTH) for y in range(HEIGHT)]
figures = [[pygame.Rect(x + WIDTH // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in FIGURES_POSITIONS]
field = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

anim_count, anim_speed, anim_limit = ANIM_COUNT, ANIM_SPEED, ANIM_LIMIT

bg = pygame.image.load('img/background.jpg').convert()
game_bg = pygame.image.load('img/background.jpg').convert()

main_font = pygame.font.Font('font/TetrisBlocks-P99g.ttf', 70)
my_font = pygame.font.Font('font/TetrisBlocks-P99g.ttf', 50)

title_tetris = main_font.render('TETRIS', True, pygame.Color('dark-orange'))
title_record = my_font.render('record.txt: ', True, pygame.Color('purple'))
title_score = my_font.render('score: ', True, pygame.Color('green'))

get_color = lambda: (randrange(50, 256), randrange(50, 256), randrange(50, 256))
figure, next_figure = deepcopy(choice(figures)), deepcopy(choice(figures))

score, lines = 0, 0
score = {
    0: 0,
    1: 100,
    2: 300,
    3: 900,
    4: 2000
}

while True:
    record = get_record()
    dx, rotate = 0, False
    sc.blit(bg, (0, 0))
    sc.blit(game_bg, (20, 20))
    # game_bg.blit(game_sc, (0, 0))

    for i in range(lines):
        pygame.time.wait(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                anim_limit = 100
            elif event.key == pygame.K_UP:
                rotate = True

    # move x
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break

    # move y
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] = color
                figure, color = next_figure, next_color
                next_figure, next_color = deepcopy(choice(figures)), get_color()
                anim_limit = 2000

    # rotate
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x - x
            figure[i].y = center.y + y
            if not check_borders():
                figure = deepcopy(figure_old)
                break

    # check lines
    line, lines = HEIGHT - 1, 0
    for row in range(HEIGHT - 1, -1, -1):
        count = 0
        for i in range(WIDTH):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < WIDTH:
            line -= 1
        else:
            anim_speed += 3
            lines += 1

    # score
    score += score[lines]

    # draw grid
    [pygame.draw.rect(game_bg, (35, 35, 35), i_rect, 1) for i_rect in grid]

    # draw figures
    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_bg, color, figure_rect)

    # draw field
    for y, raw in enumerate(field):
        for x, col





