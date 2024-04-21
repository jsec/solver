from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.root = Tk()
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()
