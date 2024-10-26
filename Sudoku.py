import sys
import pygame as pg

pg.init()
screen_size = 902, 902
line_width = 4
inset = 10
cell_size = (screen_size[0] - 2 * inset) // 9
font = pg.font.Font(None, 60)
screen = pg.display.set_mode(screen_size)

sudoku_grid = [[2 for i in range(9)] for j in range(9)]


def draw_background():
    screen.fill(pg.Color("white"))


def draw_sudoku_grid():
    grid_colour = pg.Color("black")
    pg.draw.rect(screen, grid_colour, pg.Rect(
        inset, inset, screen_size[0] - 2 * inset, screen_size[1] - 2 * inset), line_width)
    # for col in range(9):
    #     for row in range(9):
    #         pg.draw.rect(screen, grid_colour,
    #                      (col * cell_size + inset, row * cell_size + inset, cell_size, cell_size), line_width//4)
    # for i in range(1, 9):
    #     if i % 3 == 0:
    #         line_pos = (i * cell_size) + inset
    #         pg.draw.line(screen, grid_colour, (line_pos, inset),
    #                      (line_pos, screen_size[1] - inset - 1), line_width)
    #         pg.draw.line(screen, grid_colour, (inset, line_pos),
    #                      (screen_size[0] - inset - 1, line_pos), line_width)
    for col in range(1, 9):
        start_pos = (col * cell_size + inset, inset)
        end_pos = (col * cell_size + inset, screen_size[1] - inset - 1)
        pg.draw.line(screen, grid_colour, start_pos, end_pos,
                     line_width//4 if col % 3 != 0 else line_width)
    for row in range(1, 9):
        start_pos = (inset, row * cell_size + inset)
        end_pos = (screen_size[0] - inset - 1,  row * cell_size + inset)
        pg.draw.line(screen, grid_colour, start_pos, end_pos,
                     line_width//4 if row % 3 != 0 else line_width)


def draw_numbers():
    for col in range(9):
        for row in range(9):
            n_text = font.render(
                str(sudoku_grid[row][col]), True, pg.Color("black"))
            # text_width, text_height = n_text.get_size()
            text_rect = n_text.get_rect()
            text_rect.center = (
                (col * cell_size) + inset + cell_size / 2,
                (row * cell_size) + inset + cell_size / 2
            )
            screen.blit(n_text, text_rect.topleft)
            # position = pg.Vector2(
            #    (col * cell_size) + inset + (cell_size - text_width) / 2,
            #    (row * cell_size) + inset + (cell_size - text_height) / 2
            # )
            # screen.blit(n_text, position)
            # screen.blit(n_text, pg.Vector2(
            #    (col * cell_size) + (cell_size - text_width)/2 + inset,
            #    (row * cell_size) + (cell_size - text_height)/2 + inset))


def game_loop():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    draw_background()
    draw_sudoku_grid()
    draw_numbers()
    pg.display.update()


while 1:
    game_loop()
