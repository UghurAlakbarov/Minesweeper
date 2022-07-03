import random
import tkinter as tk

from CellWithAMine import CellWithAMine
from CellWithoutAMine import CellWithoutAMine
from Sun import State


class Field(tk.Frame):
    def __init__(self, master, mode):
        super().__init__(master)

        self.configure(bg='grey', border=2)

        if mode == 'easy':
            self.size = 8
            self.num_of_mines = 10

        self.init_mines()
        self.init_value_map()
        self.init_field()


    def init_mines(self):
        """ 
        Adds bombs by randomly choosing both coordinates.
        The simplest (and the most stupid) method.
        """
        self.set_of_mines = set()
        while len(self.set_of_mines) != 10:
            row    = random.randint(0, self.size-1)
            column = random.randint(0, self.size-1)
            self.set_of_mines.add((row, column)) 


    def init_value_map(self):
        self.mat_of_values = [[0 for _ in range(self.size)] for _ in range(self.size)]

        for (i, j) in self.set_of_mines:
            self.increase_value_of_the_neigbouring_cells(i, j)


    def increase_value_of_the_neigbouring_cells(self, row, column):
        for i, j in {
            (row-1, column-1), (row-1, column  ), (row-1, column+1),
            (row  , column-1),                    (row  , column+1),
            (row+1, column-1), (row+1, column  ), (row+1, column+1)
        }:
            if all(x in range(self.size) for x in (i, j)):
                self.mat_of_values[i][j] += 1


    def init_field(self):
        self.field = [[None for _ in range(self.size)] for _ in range(self.size)]
        for row in range(self.size):
            for column in range(self.size):
                if (row, column) in self.set_of_mines:
                    self.field[row][column] = CellWithAMine   (self, row, column)
                else:
                    self.field[row][column] = CellWithoutAMine(self, row, column, self.mat_of_values[row][column])
                self.field[row][column].grid(row=row, column=column)


    def open_the_neigbouring_cells(self, row, column):
        for i, j in {
            (row-1, column-1), (row-1, column  ), (row-1, column+1),
            (row  , column-1),                    (row  , column+1),
            (row+1, column-1), (row+1, column  ), (row+1, column+1)
        }:
            if all(x in range(self.size) for x in (i, j)):
                cell = self.field[i][j]
                if type(cell) == CellWithoutAMine and not cell.is_opened:
                    cell.handle_opening()
    
    def blow_everything_up(self, _):
        # show all mines
        for (i, j) in self.set_of_mines:
            self.field[i][j].handle_opening()
        # change the sun
        self.master.upper_menu.sun.show_sun(State.LOST)
        # make all cells unclickable
        for row in self.field:
            for cell in row:
                cell.lbl_img.unbind('<Button-1>')
                cell.lbl_img.unbind('<Button-3>')
