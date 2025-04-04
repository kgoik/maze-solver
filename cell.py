from graphics import Line, Point
from window import BACKGROUND

class Cell():
    def __init__(self, win=None, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = None 
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1 
        self._x2 = x2
        self._y1 = y1 
        self._y2 = y2
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self._win != None:
            self._win.draw_line(line, "red" if self.has_left_wall else BACKGROUND)
        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self._win != None:
            self._win.draw_line(line, "red" if self.has_right_wall else BACKGROUND)
        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self._win != None:
            self._win.draw_line(line, "red" if self.has_top_wall else BACKGROUND)
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self._win != None:
            self._win.draw_line(line, "red" if self.has_bottom_wall else BACKGROUND)
 
    def draw_move(self, to_cell, undo=False):
        color = "red"

        if undo:
            color = "gray"

        middle_x_from = abs(self._x1 + self._x2) // 2 
        middle_y_from = abs(self._y1 + self._y2) // 2 
        
        middle_x_to = abs(to_cell._x1 + to_cell._x2) // 2 
        middle_y_to = abs(to_cell._y1 + to_cell._y2) // 2 
        
        self._win.draw_line(Line(Point(middle_x_from, middle_y_from), Point(middle_x_to, middle_y_to)), color)