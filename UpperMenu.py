import tkinter as tk

from Sun import Sun


class UpperMenu(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(bg='grey', border=2)

        self.sun = Sun(self)
        self.sun.pack()
