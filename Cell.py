from itertools import cycle
from tkinter import ttk

from PIL import Image, ImageTk


class Cell(ttk.Frame):
    def __init__(self, master, row, column):
        super().__init__(master) 

        self.masater = master
        self.row = row
        self.column = column

        self.is_flagged = False
        self.img_opened = None

        # creates an itertools.cycle object which alternates
        # between the flagged and unflagged states of a cell
        self.flagging_images = cycle([ImageTk.PhotoImage(Image.open(f'assets/{i}.png').resize((25, 25))) for i in ('default', 'flag')])
        
        self.lbl_img = ttk.Label(self, image=next(self.flagging_images))
        self.lbl_img.focus_set()
        self.lbl_img.bind('<Button-3>', self.handle_flagging)
        self.lbl_img.pack()

    
    def handle_flagging(self, _):
        self.lbl_img.configure(image=next(self.flagging_images))
        self.is_flagged = not self.is_flagged
    
    def handle_opening(self, _=None):
        self.lbl_img.configure(image=self.img_opened)
