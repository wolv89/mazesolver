from window import Window
from maze import Maze

win = Window(800, 600)

mz = Maze(50, 50, 8, 12, 50, 50, win, 32)

win.wait_for_close()
