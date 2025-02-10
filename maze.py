import time
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = [[None for _ in range(self._num_rows)] for _ in range(self._num_cols)]

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                x1 = self._x1 + i * self._cell_size_x
                y1 = self._y1 + j * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                self._cells[i][j] = Cell(self._win, x1, y1, x2, y2)
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is not None:
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)
