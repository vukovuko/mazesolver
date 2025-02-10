import time
import random
from cell import Cell


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        if seed is not None:
            random.seed(seed)
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = [
            [None for _ in range(self._num_rows)] for _ in range(self._num_cols)
        ]
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True

        while True:
            neighbors = []
            if j > 0 and not self._cells[i][j - 1].visited:
                neighbors.append(("up", i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                neighbors.append(("down", i, j + 1))
            if i > 0 and not self._cells[i - 1][j].visited:
                neighbors.append(("left", i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                neighbors.append(("right", i + 1, j))

            if not neighbors:
                self._draw_cell(i, j)
                return

            direction, ni, nj = random.choice(neighbors)

            if direction == "up":
                current.has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            elif direction == "down":
                current.has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            elif direction == "left":
                current.has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            elif direction == "right":
                current.has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            self._draw_cell(i, j)
            self._draw_cell(ni, nj)
            self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        current = self._cells[i][j]
        self._animate()
        current.visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        if j > 0:
            neighbor = self._cells[i][j - 1]
            if (
                not neighbor.visited
                and not current.has_top_wall
                and not neighbor.has_bottom_wall
            ):
                current.draw_move(neighbor)
                if self._solve_r(i, j - 1):
                    return True
                else:
                    current.draw_move(neighbor, undo=True)

        if j < self._num_rows - 1:
            neighbor = self._cells[i][j + 1]
            if (
                not neighbor.visited
                and not current.has_bottom_wall
                and not neighbor.has_top_wall
            ):
                current.draw_move(neighbor)
                if self._solve_r(i, j + 1):
                    return True
                else:
                    current.draw_move(neighbor, undo=True)

        if i > 0:
            neighbor = self._cells[i - 1][j]
            if (
                not neighbor.visited
                and not current.has_left_wall
                and not neighbor.has_right_wall
            ):
                current.draw_move(neighbor)
                if self._solve_r(i - 1, j):
                    return True
                else:
                    current.draw_move(neighbor, undo=True)

        if i < self._num_cols - 1:
            neighbor = self._cells[i + 1][j]
            if (
                not neighbor.visited
                and not current.has_right_wall
                and not neighbor.has_left_wall
            ):
                current.draw_move(neighbor)
                if self._solve_r(i + 1, j):
                    return True
                else:
                    current.draw_move(neighbor, undo=True)

        return False
