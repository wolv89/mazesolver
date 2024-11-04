
import time

from window import Window
from line import Line
from point import Point

class Cell:
    def __init__(self, window: Window, x1, y1, x2, y2):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.__top_left = Point(x1, y1)
        self.__top_right = Point(x2, y1)
        self.__bottom_left = Point(x1, y2)
        self.__bottom_right = Point(x2, y2)
        midx = x1 + abs(x2 - x1)/2
        midy = y1 + abs(y2 - y1)/2
        self.__centre = Point(midx, midy)
        self.__win = window
        self.visited = False

    def get_centre(self):
        return self.__centre

    def draw(self):

        # print(f"Drawing Cell @ {self.__centre.x} x {self.__centre.y} - {self.has_left_wall} {self.has_top_wall} {self.has_right_wall} {self.has_bottom_wall}")

        if self.has_left_wall:
            self.__win.draw_line(Line(self.__top_left, self.__bottom_left), "black")
        else:
            self.__win.draw_line(Line(self.__top_left, self.__bottom_left), "white")
        
        if self.has_top_wall:
            self.__win.draw_line(Line(self.__top_left, self.__top_right), "black")
        else:
            self.__win.draw_line(Line(self.__top_left, self.__top_right), "white")
        
        if self.has_right_wall:
            self.__win.draw_line(Line(self.__top_right, self.__bottom_right), "black")
        else:
            self.__win.draw_line(Line(self.__top_right, self.__bottom_right), "white")
        
        if self.has_bottom_wall:
            self.__win.draw_line(Line(self.__bottom_left, self.__bottom_right), "black")
        else:
            self.__win.draw_line(Line(self.__bottom_left, self.__bottom_right), "white")

        self.__win.redraw()
        time.sleep(0.01)

    def draw_move(self, to_cell, undo=False):

        colour = "red"
        if undo:
            colour = "gray"

        self.__win.draw_line(Line(self.__centre, to_cell.get_centre()), colour)

        self.__win.redraw()
        time.sleep(0.01)
