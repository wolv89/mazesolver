from window import Window
from maze import Maze

win = Window(800, 600)

mz = Maze(50, 50, 8, 12, 50, 50, win)
mz._draw_cells()
mz._break_entrance_and_exit()

win.wait_for_close()
