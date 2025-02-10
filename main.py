from window import Window
from maze import Maze
from cell import Cell
from point import Point
from line import Line

if __name__ == "__main__":
    win = Window(800, 600)

    p1 = Point(100, 100)
    p2 = Point(300, 100)
    p3 = Point(300, 300)
    p4 = Point(100, 300)

    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p4)
    line4 = Line(p4, p1)

    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "green")
    win.draw_line(line4, "black")

    maze = Maze(50, 50, 10, 10, 40, 40, win)

    win.wait_for_close()
