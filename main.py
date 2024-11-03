from window import Window
from cell import Cell

win = Window(800, 600)

c1 = Cell(win, 0, 0, 50, 50)
c1.has_right_wall = False
c1.draw()

c2 = Cell(win, 50, 0, 100, 50)
c2.has_left_wall = False
c2.draw()

c3 = Cell(win, 50, 50, 100, 100)
c3.has_bottom_wall = False
c3.has_right_wall = False
c3.draw()

c3.draw_move(c2)
c1.draw_move(c2, True)

win.wait_for_close()
