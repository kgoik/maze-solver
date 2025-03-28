from window import Window
from geometry import Line, Point
win = Window(800, 600)

x = 0
y = 1

for i in range(0, 4):
    p1 = Point(x, y)
    if x <= y:
        x += 50 * i
    else:
        y += 50 * i

    p2 = Point(x,y)
    line = Line(p1, p2)

    win.draw_line(line, "red")

win.wait_for_close()



