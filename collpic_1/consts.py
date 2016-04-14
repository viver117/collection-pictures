''' глобальные константы '''
SIZE_CHIP     = 100 # ширина и высота квадратной фишки (в пикселах)
GAP_CHIP      = 1   # зазор между соседними фишками (в пикселах)
SIZE_FIELD    = 3   # ширина и высота игрового поля (в количестве фишек)
WIDTH_BORDER  = 8   # ширина рамки игрового поля
MARGIN_FIELD  = 15  # отступ игрового поля от краёв окна
SIZE_SCREEN   = SIZE_CHIP * SIZE_FIELD + (SIZE_FIELD - 1) * GAP_CHIP + 2 * (MARGIN_FIELD + WIDTH_BORDER) # ширина и высота окна
LENGTH_BORDER = SIZE_SCREEN - 2 * MARGIN_FIELD # длина границы игрового поля
QUALITYMIX    = 500

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
