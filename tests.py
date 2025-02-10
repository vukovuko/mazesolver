import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_different_sizes(self):
        m2 = Maze(10, 10, 5, 8, 20, 20)
        self.assertEqual(len(m2._cells), 8)
        self.assertEqual(len(m2._cells[0]), 5)

    def test_maze_no_window(self):
        m3 = Maze(0, 0, 3, 3, 15, 15, win=None)
        self.assertIsNone(m3._win)
        self.assertEqual(len(m3._cells), 3)
        self.assertEqual(len(m3._cells[0]), 3)

    def test_break_entrance_and_exit(self):
        num_rows = 3
        num_cols = 3
        maze = Maze(0, 0, num_rows, num_cols, 10, 10, win=None)
        self.assertTrue(maze._cells[0][0].has_top_wall)
        self.assertTrue(maze._cells[num_cols - 1][num_rows - 1].has_bottom_wall)
        maze._break_entrance_and_exit()
        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

    def test_reset_cells_visited(self):
        maze = Maze(0, 0, 3, 3, 15, 15, win=None, seed=0)

        for i in range(maze._num_cols):
            for j in range(maze._num_rows):
                maze._cells[i][j].visited = True

        maze._reset_cells_visited()

        for i in range(maze._num_cols):
            for j in range(maze._num_rows):
                self.assertFalse(maze._cells[i][j].visited)

    def test_maze_solvable(self):
        m = Maze(0, 0, 5, 5, 20, 20, win=None, seed=0)
        self.assertTrue(m.solve())


if __name__ == "__main__":
    unittest.main()
