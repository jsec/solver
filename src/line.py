from tkinter import Canvas
from point import Point


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )
        canvas.pack()

    def __str__(self) -> str:
        return f"(Line) start: {self.start} end: {self.end}"
