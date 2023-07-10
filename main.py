import random as rd
import pygame as pg
import os


# VARIABLES:
HEAD = "Knight's Tour Problem (FINAL PROJECT)"
WINDOW = '400,70'
SIZE = 8
WIDTH = 800
HEIGHT = 800
SPEED = 100
SQUARE = 100

# SPECIFIC COLORS:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CORAL = (255, 127, 80)
BLUE = (96, 147, 172)
GREEN = (98, 172, 141)
YELLOW = (255, 255, 153)
GREY = (128, 128, 128)
MAROON = (128, 0, 0)
PURPLE = (184, 137, 230)

# DEFINED AS NUMBER TO BE CHOSEN RANDOMLY:
colors = {
    1: WHITE,
    2: YELLOW,
    3: CORAL,
    4: BLUE,
    5: GREEN,
    6: BLACK,
    7: GREY,
    8: MAROON,
    9: PURPLE
}

# Knights Movements:
def knight_moves(position):
    x, y = position
    return [
        (x + 1, y + 2),
        (x + 1, y - 2),
        (x + 2, y + 1),
        (x + 2, y - 1),
        (x - 1, y + 2),
        (x - 1, y - 2),
        (x - 2, y + 1),
        (x - 2, y - 1)
        ]


# Warnsdorff's Algorithm

# Defining the Whole Board as an Available PLace to be positioned on:
def is_available(grid, position):
    size = len(grid)
    i, j = position
    return 0 <= i < size and 0 <= j < size and not grid[i][j]

# Valid Places to be placed on:
def is_possible(grid, position):
    moves = knight_moves(position)
    # Initial Knight Moves Count:
    ct = 0
    for move in moves:
        if is_available(grid, move):
            ct += 1
    return ct

# Possible minimum Knight Moves:
def possible_min(grid, position):
    moves = knight_moves(position)
    min_val = 8
    min_position = ()
    for move in moves:
        if is_available(grid, move):
            val = is_possible(grid, move)
            if val < min_val:
                min_val = val
                min_position = move
    return min_position

#BOARD SET UP AND DRAWINGS CLASS:
class Solution:
    #Initilizing the variables will be using in this class:
    def __init__(self, show_up, square_size, axis):
        self.show_up = show_up
        self.c = show_up.get_width() // square_size
        self.r = show_up.get_height() // square_size
        self.square_size = square_size
        self.axis = axis
        self.board = [
            [() for _ in range(self.c)]
            for _ in range(self.r)
        ]
        self.font = pg.font.SysFont('MV Boli', 8, False)

    def draw_knight(self, position, val, color):
        x, y = position
        x *= self.square_size
        y *= self.square_size
        fill, border = color
        rect1 = pg.Rect(x, y, self.square_size, self.square_size)
        self.show_up.fill(fill, rect1)
        pg.draw.rect(self.show_up, border, rect1, 1)
        if val:
            font = pg.font.SysFont('MV Boli', 60 - 2 * self.r - len(str(self.r)) * 5, True)
            # Stepping font color:
            text = font.render(str(val), True, WHITE)
            coord = (3 * self.square_size) // 13
            self.show_up.blit(text, (x + coord + 5, y + coord))
        label = str(
            (y + x * self.r) // self.square_size + 1
        )
        text = pg.font.SysFont('MV Boli', 0, True).render(label, True, WHITE)
        self.show_up.blit(text, (x + 5, y + 5))

    #SETTING UP THE SQUARES THAT THE KNIGHT VISITED:
    def draw_board(self, position, visited, number_color, square_color):
        for row in range(self.r):
            xA = row * self.square_size
            for col in range(self.c):
                yA = col * self.square_size
                key = (row, col)
                if key in visited:
                    self.draw_knight(key, visited[key], square_color)
                else:
                    if self.axis:
                        open = ' '
                        if col < 10:
                            open += ' '
                        text = self.font.render(open + str(col + row * self.r + 1), True, BLACK)
                        self.show_up.blit(text, (xA, yA + 5))
                    rect = pg.Rect(xA, yA, self.square_size, self.square_size)
                    pg.draw.rect(self.show_up, BLACK, rect, 1)
        self.draw_knight(position,
                         0 if position not in visited else visited[position],
                         number_color)

#WINDOW SET UP
class Window:
    DISABLED = pg.Color('lightsalmon1')
    ABLED = pg.Color('lightyellow1')

    #Defining Some Specific Variables that will be used in this Class:
    def __init__(self, x, y, z, u, text=''):
        self.rect = pg.Rect(x, y, z, u)
        self.color = self.DISABLED
        self.text = text
        self.text_show = pg.font.Font(None, 32).render(text, True, self.color)
        self.active = False

    def action_handle(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            #WHEN CLICKING ON THE USER ENTERING BOX.
            if self.rect.collidepoint(event.pos):
                #TOGGLE THE ACTION.
                self.active = not self.active
            else:
                self.active = False
            #WHEN CLICKING THE ENTERING BOX THE COLOR CHANGES.
            self.color = self.ABLED if self.active else self.DISABLED
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_show = pg.font.Font(None, 32).render(self.text, True, self.color)

    def update(self):
        width = max(700, self.text_show.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.text_show, (self.rect.x+5, self.rect.y+15))
        pg.draw.rect(screen, self.color, self.rect, 2)



#SETTING UP THE WINDOW PAGE (STARING PAGE):
if __name__ == '__main__':
    os.environ['SDL_VIDEO_WINDOW_POS'] = WINDOW
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption(HEAD)
    time = pg.time.Clock()
    run = True
    xyL = True

    enter1 = Window(50, 100, 300, 50, "Enter the Chess Board Size: ")
    enter2 = Window(50, 200, 300, 50, 'Column: ')
    enter3 = Window(50, 300, 300, 50, 'Row: ')
    all_enter = [enter1, enter2, enter3]

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    run = False
                    break
            for enter in all_enter:
                enter.action_handle(event)

        for enter in all_enter:
            enter.update()

        screen.fill((50, 50, 50))
        for enter in all_enter:
            enter.draw(screen)

        pg.display.flip()
        time.tick(50)

    # validating inputs
    try:
        SIZE = int(enter1.text.split(' ')[-1])
        if not 5 <= SIZE <= 20:
            raise ValueError
    except ValueError:
        SIZE = 8

    SQUARE = HEIGHT // SIZE
    board = Solution(show_up = screen, square_size = SQUARE, axis = xyL)
    hover = False
    run = True

    position = [rd.randrange(SIZE), rd.randrange(SIZE)]
    x, y = enter2.text.split(' ')[-1], enter3.text.split(' ')[-1]
    if x.isalnum() and 0 < int(x) <= SIZE:
        position[0] = int(x) - 1
    if y.isalnum() and 0 < int(y) <= SIZE:
        position[1] = int(y) - 1

    grid = [[0] * SIZE for _ in range(SIZE)]
    position = tuple(position)
    last_pos = position
    val = 1
    visited = {position: val}
    key = True

    #Each Running Time will show different Color, for the square and the knight square:
    number_color = (
        colors[rd.randrange(3, 10)],
        colors[rd.randrange(1, 10)]
    )
    square_color = (
        colors[rd.randrange(3, 10)],
        colors[rd.randrange(1, 10)]
    )

    # main loop
    while run:
        time.tick(SPEED)
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                run = False

        if key:
            x, y = position
            last_pos = position
            grid[x][y] = val
            visited.update({position: val})
            val += 1
            position = possible_min(grid, position)
            key = False

            if val > SIZE ** 2:
                screen.fill(WHITE)
                board.draw_board(last_pos, visited, number_color, square_color)
                pg.display.flip()

        if position and not key:
            screen.fill(WHITE)
            board.draw_board(last_pos, visited, number_color, square_color)
            pg.display.flip()
            last_x, last_y = last_pos
            x, y = position
            if last_x < x:
                last_x += 1
            elif last_x > x:
                last_x -= 1
            else:
                if last_y < y:
                    last_y += 1
                elif last_y > y:
                    last_y -= 1
                else:
                    key = True

            last_pos = (last_x, last_y)
    print(val)
    pg.quit()
