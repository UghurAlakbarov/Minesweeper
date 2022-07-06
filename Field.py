import random
import tkinter as tk

from InitialCell import InitialCell
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
            self.opened_cells_left_for_win = self.size*self.size - self.num_of_mines

        # initialize field temporarily filled with InitialCells
        self.field = [[InitialCell(self, row, column) for column in range(self.size)] for row in range(self.size)]
        for row_num, row in enumerate(self.field):
            for column_num, cell in enumerate(row):
                cell.grid(row=row_num, column=column_num)


    def init_final_field(self, row_num : int, column_num : int):
        # initialize mines
        self.set_of_mines = set()
        while len(self.set_of_mines) != 10:
            row    = random.randint(0, self.size-1)
            column = random.randint(0, self.size-1)
            if  (row, column) not in self.get_valid_neighbours(row_num, column_num)\
            and (row, column)               !=                (row_num, column_num):
                self.set_of_mines.add((row, column)) 

        # initialize values
        self.mat_of_values = [[0 for _ in range(self.size)] for _ in range(self.size)]

        for (row, column) in self.set_of_mines:
            for neighbours_coords in self.get_valid_neighbours(row, column):
                i, j = neighbours_coords
                self.mat_of_values[i][j] += 1

        # initialize the field
        for row, _ in enumerate(self.field):
            for column, _ in enumerate(_):
                if (row, column) in self.set_of_mines:
                    self.field[row][column] = CellWithAMine   (self, row, column)
                else:
                    self.field[row][column] = CellWithoutAMine(self, row, column, self.mat_of_values[row][column])
                self.field[row][column].grid(row=row, column=column)
        
        # open the clicked cell
        self.field[row_num][column_num].handle_opening()


    def open_the_neigbouring_cells(self, row, column):
        for neighbours_coords in self.get_valid_neighbours(row, column):
            i, j = neighbours_coords
            cell = self.field[i][j]
            if type(cell) == CellWithoutAMine and not cell.is_opened:
                cell.handle_opening()
    

    def blow_everything_up(self, _):
        # show all mines
        for (i, j) in self.set_of_mines:
            self.field[i][j].handle_opening()
        
        self.finish_game(State.LOST)
    

    def get_valid_neighbours(self, row : int, column : int) -> list[tuple] :
        """ Given the coordinates of a cell, get a list of its
            neighbours that don't go out of the field's boundaries """
        neighbours = []
        for x, y in {
            (row-1, column-1), (row-1, column  ), (row-1, column+1),
            (row  , column-1),                    (row  , column+1),
            (row+1, column-1), (row+1, column  ), (row+1, column+1)
        }:
            if all(i in range(self.size) for i in (x, y)):
                neighbours.append((x, y))
        return neighbours


    def check_for_win(self):
        self.opened_cells_left_for_win -= 1
        if self.opened_cells_left_for_win == 0:
            self.finish_game(State.WON)


    def finish_game(self, result):
        # change the sun
        self.master.upper_menu.sun.show_sun(result)

        # make all cells unclickable
        for row in self.field:
            for cell in row:
                cell.lbl_img.unbind('<Button-1>')
                cell.lbl_img.unbind('<Button-3>')