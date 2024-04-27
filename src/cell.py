from __future__ import annotations

from line import Line
from point import Point
from window import Window


class Cell:
    def __init__(self, window: Window, x1: int, y1: int, x2: int, y2: int) -> None:
        self.__window = window
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def get_center(self) -> Point:
        x = self.__x1 + ((self.__x2 - self.__x1) / 2)
        y = self.__y1 + ((self.__y2 - self.__y1) / 2)

        return Point(x, y)

    def draw(self, color: str) -> None:
        if self.has_top_wall:
            top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__window.draw_line(top_wall, color)

        if self.has_bottom_wall:
            bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__window.draw_line(bottom_wall, color)

        if self.has_left_wall:
            left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__window.draw_line(left_wall, color)

        if self.has_right_wall:
            right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__window.draw_line(right_wall, color)

    def draw_move(self, to_cell: Cell, undo: bool = False):
        color = "gray" if undo else "red"
        line = Line(self.get_center(), to_cell.get_center())
        self.__window.draw_line(line, color)
