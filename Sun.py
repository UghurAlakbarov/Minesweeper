from enum import Enum
from tkinter import ttk

from PIL import Image, ImageTk


class State(Enum):

        START = 0
        HAPPY = 1
        WON = 2
        LOST = 3

class Sun(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.suns = [ImageTk.PhotoImage(Image.open(f'assets/sun{i}.png').resize((25, 25))) for i in range(4)]
        self.lbl_sun = None
        self.show_sun(State.START)

    def show_sun(self, state : Enum):
        if self.lbl_sun is not None: self.lbl_sun.pack_forget()

        self.lbl_sun = ttk.Label(self, image=self.suns[state.value])
        self.lbl_sun.pack()
