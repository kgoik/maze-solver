from window import Window
from cell import Cell
win = Window(800, 600)

x = 1 
y = 1
cell_width = 20
previous_cell = None
for i in range(0, 5):
   sides = [False for j in range(0,4)]
   if i < 4:
     sides[i] = True
   else: 
      sides = [True for j in range(0,4)]
   print(sides)
   cell = Cell(win, sides[0], sides[1], sides[2], sides[3])
   cell.draw(x, y, x + cell_width, y + cell_width)
   x += cell_width * 2
   y += cell_width * 2
   if previous_cell is not None:
      previous_cell.draw_move(cell)
   previous_cell = cell

win.wait_for_close()



