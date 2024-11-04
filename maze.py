
import time, random

from window import Window
from cell import Cell

class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win: Window, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        
        if seed != None:
            random.seed(seed)

        self._create_cells()
        self._draw_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cell_status()
    
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
        for row in self.__cells:
            for cl in row:
                cl.draw()

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__cells[0][0].draw()
        self.__cells[-1][-1].has_bottom_wall = False
        self.__cells[-1][-1].draw()

    def _break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            to_visit = []

            # Top
            if i > 0 and not self.__cells[i-1][j].visited:
                to_visit.append((i-1,j,"up"))

            # Bottom
            if i < len(self.__cells) - 1 and not self.__cells[i+1][j].visited:
                to_visit.append((i+1,j,"down"))

            # Left
            if j > 0 and not self.__cells[i][j-1].visited:
                to_visit.append((i,j-1,"left"))

            # Right
            if j < len(self.__cells[0]) - 1 and not self.__cells[i][j+1].visited:
                to_visit.append((i,j+1,"right"))
            
            if len(to_visit) == 0:
                self.__cells[i][j].draw()
                return

            dir = random.randrange(0, len(to_visit))
            next = to_visit[dir]

            if next[2] == "up":
                self.__cells[i][j].has_top_wall = False
                self.__cells[next[0]][next[1]].has_bottom_wall = False
            elif next[2] == "down":
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[next[0]][next[1]].has_top_wall = False
            elif next[2] == "left":
                self.__cells[i][j].has_left_wall = False
                self.__cells[next[0]][next[1]].has_right_wall = False
            elif next[2] == "right":
                self.__cells[i][j].has_right_wall = False
                self.__cells[next[0]][next[1]].has_left_wall = False

            self._break_walls_r(next[0], next[1])

    def _reset_cell_status(self):
        for row in self.__cells:
            for cl in row:
                cl.visited = False
