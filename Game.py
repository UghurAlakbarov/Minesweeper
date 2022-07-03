import tkinter as tk
from tkinter import X

from Field import Field
from UpperMenu import UpperMenu


class Game(tk.Tk):
    def __init__(self, mode):
        super().__init__()

        self.mode = mode

        # self.configure(bg='white')
        self.resizable(False, False)

        self.upper_menu = UpperMenu(self)
        self.upper_menu.pack(padx=5, pady=2, fill=X)

        self.field = Field(self, mode)
        self.field.pack(padx=5, pady=2)


if __name__ == "__main__":
  app = Game('easy')
  app.mainloop()
  