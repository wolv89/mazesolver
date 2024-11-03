
import time

from window import Window
from cell import Cell

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win: Window):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []

        self._create_cells()
    
    def _create_cells(self):
        for cols in range(self.__num_rows):
            row = []
            for rows in range(self.__num_cols):
                x1 = self.__x1 + (rows * self.__cell_size_x)
                y1 = self.__y1 + (cols * self.__cell_size_y)
                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y
                row.append(Cell(self.__win, x1, y1, x2, y2))
            self.__cells.append(row)
    
    def _draw_cells(self):
        # print("DRAWING ========================================")
        for row in self.__cells:
            # print(row)
            for cl in row:
                cl.draw()
        self._animate()

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        # print("## BREAK")
        self.__cells[0][0].has_top_wall = False
        self.__cells[-1][-1].has_bottom_wall = False
        self._draw_cells()
