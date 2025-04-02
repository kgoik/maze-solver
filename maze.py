from cell import Cell
import time

class Maze():

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        for c in range(0,self.num_cols):
            if c <= len(self._cells):
                self._cells.append([])
            
            for r in range(0, self.num_rows):
                self._cells[c].append(Cell(self.win))
                
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        x1 = self.x1 + (i * self.cell_size_x) 
        y1 = self.y1 + (j * self.cell_size_y) 
        x2 = self.x1 + ((i + 1) * self.cell_size_x) 
        y2 = self.y1 + ((j + 1) * self.cell_size_y) 

        
        self._cells[i][j].draw(x1, y1, x2, y2)

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)