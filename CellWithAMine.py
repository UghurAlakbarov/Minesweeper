from PIL import Image, ImageTk

from Cell import Cell


class CellWithAMine(Cell):
    def __init__(self, master, row, column):
        super().__init__(master, row, column)

        self.img_opened = ImageTk.PhotoImage(Image.open('assets/mine.png').resize((25, 25)))
        self.lbl_img.bind('<Button-1>', self.master.blow_everything_up)
