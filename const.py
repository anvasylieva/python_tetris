WIDTH, HEIGHT = 10, 20
TILE: int = 35
GAME_RES = WIDTH * TILE, HEIGHT * TILE
RES = 650, 750
# speed of frames
FPS = 60

FIGURES_POSITIONS = [
    [(-2, -1), (-1, -1), (0, -1), (1, -1)],
    [(0, -1), (0, 0), (0, 1), (0, 2)],
    [(0, -1), (-1, -1), (-1, 0), (0, 0)],
    [(-1, -1), (0, 0), (-1, 0), (0, 1)],
    [(0, -1), (0, 0), (-1, 0), (-1, 1)],
    [(0, 0), (0, -1), (0, 1), (-1, -1)],
    [(0, -1), (-1, -1), (-1, 0), (-1, 1)],
    [(0, 0), (0, -1), (0, 1), (-1, 0)],
    [(0, 0), (0, -1), (0, 1), (-1, 0)],
]

ANIM_COUNT, ANIM_SPEED, ANIM_LIMIT = 0, 60, 2000

score, lines = 0, 0
SCORES = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}
