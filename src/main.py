from cell import Cell
from window import Window


def main():
    win = Window(800, 600)
    cell = Cell(win, 20, 20, 100, 100)
    cell.draw("red")
    cell2 = Cell(win, 120, 120, 200, 200)
    cell2.draw("blue")
    cell.draw_move(cell2, undo=True)
    win.wait_for_close()


main()
