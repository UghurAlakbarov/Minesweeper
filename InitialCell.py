from Cell import Cell


class InitialCell(Cell):
    
    """When clicked, sends a request to initialize
    the final version of the field with no mines
    on the clicked cell and around it"""

    def __init__(self, master, row, column):
        super().__init__(master, row, column)
    
    
    def handle_opening(self, _=None):
        self.master.init_final_field(self.row, self.column)
