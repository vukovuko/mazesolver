class Cell:
    def __init__(self, win=None, x1=0, y1=0, x2=0, y2=0):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1, self._y1 = x1, y1
        self._x2, self._y2 = x2, y2
        self._win = win

    def draw(self):
        if self._win is None:
            return
        canvas = self._win.get_canvas()
        if self.has_left_wall:
            canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill="black", width=2)
        if self.has_top_wall:
            canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill="black", width=2)
        if self.has_right_wall:
            canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill="black", width=2)
        if self.has_bottom_wall:
            canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill="black", width=2)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        canvas = self._win.get_canvas()
        color = "gray" if undo else "red"

        x1, y1 = (self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2
        x2, y2 = (to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2

        canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
