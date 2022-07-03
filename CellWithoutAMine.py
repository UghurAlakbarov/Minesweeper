from PIL import Image, ImageTk

from Cell import Cell


class CellWithoutAMine(Cell):
    def __init__(self, master, row, column, num_neighbouring_mines):
        super().__init__(master, row, column)

        self.num_neighbouring_mines = num_neighbouring_mines
        self.is_opened = False
        self.img_opened = ImageTk.PhotoImage(Image.open(f'assets/{num_neighbouring_mines}.png').resize((25, 25)))
        self.lbl_img.bind('<Button-1>', self.handle_opening)
    

    def handle_opening(self, _=None):
        super().handle_opening()
        self.is_opened = True
        if self.num_neighbouring_mines == 0:
            self.master.open_the_neigbouring_cells(self.row, self.column)
        self.lbl_img.unbind('<Button-1>')
        self.lbl_img.unbind('<Button-3>')
    