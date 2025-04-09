from cell import Cell
import time
import random

class Maze():

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed) 
        self._create_cells()
    
    def _create_cells(self):
        for c in range(0,self.num_cols):
            if c <= len(self._cells):
                self._cells.append([])
            
            for r in range(0, self.num_rows):
                self._cells[c].append(Cell(self._win))
                
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._draw_cell(i,j)

        self._break_entrnce_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _break_entrnce_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)

        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = self._get_unvisited_neighbors(i,j)
            
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            
            direction = random.randint(0, len(to_visit) - 1)
            new_i, new_j = to_visit[direction]

            if i - new_i != 0:
                if i - new_i > 0:
                    self._cells[i][j].has_left_wall = False
                    self._cells[new_i][j].has_right_wall = False
                if i - new_i < 0:
                    self._cells[i][j].has_right_wall = False
                    self._cells[new_i][j].has_left_wall = False

            if j - new_j != 0:
                if j - new_j > 0:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][new_j].has_bottom_wall = False
                if j - new_j < 0:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][new_j].has_top_wall = False
            
            # self._draw_cell(i,j)
            self._break_walls_r(new_i, new_j)

    def _reset_cells_visited(self):
        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._cells[i][j].visited = False

    def _get_unvisited_neighbors(self, i, j):
        neighbors = []
        if i - 1 >= 0 and not self._cells[i-1][j].visited:
            neighbors.append((i-1, j))
        if i + 1 < len(self._cells) and not self._cells[i+1][j].visited:
            neighbors.append((i+1, j))
        if j - 1 >= 0 and not self._cells[i][j-1].visited:
            neighbors.append((i, j-1))
        if j + 1 < len(self._cells[i]) and not self._cells[i][j+1].visited:
            neighbors.append((i, j+1))
        return neighbors
    
    def _get_unvisited_neighbors_without_walls(self, i, j):
        neighbors = []
        if i - 1 >= 0 and not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
            neighbors.append((i-1, j))
        if i + 1 < len(self._cells) and not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            neighbors.append((i+1, j))
        if j - 1 >= 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            neighbors.append((i, j-1))
        if j + 1 < len(self._cells[i]) and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            neighbors.append((i, j+1))
        return neighbors


    def _draw_cell(self, i, j):
        x1 = self.x1 + (i * self.cell_size_x) 
        y1 = self.y1 + (j * self.cell_size_y) 
        x2 = self.x1 + ((i + 1) * self.cell_size_x) 
        y2 = self.y1 + ((j + 1) * self.cell_size_y) 

        
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        if i == len(self._cells) - 1 and j == len(self._cells[i]) - 1:
            return True
        
        to_visit = self._get_unvisited_neighbors_without_walls(i,j)

        for direction in to_visit:
            new_i, new_j = direction
            self._cells[i][j].draw_move(self._cells[new_i][new_j])

            if self._solve_r(new_i, new_j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[new_i][new_j], True)

        return False


    def _animate(self):
        if self._win != None:
            self._win.redraw()
        time.sleep(0.01)