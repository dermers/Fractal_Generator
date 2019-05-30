from turtle import RawTurtle, TurtleScreen
from tkinter import Tk, Canvas

# A point is a tuple of (float, float)
# A line is a tuple of (point, point)

WIDTH = 1200
HEIGHT = 675
START_POS = (-WIDTH / 2), HEIGHT / 2
# print(START_POS)

root = Tk()

# set up canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness=0)
turtle_screen = TurtleScreen(canvas)
turtle_screen.bgcolor("black")
canvas.pack()

# set up turtle
turt = RawTurtle(turtle_screen)
turt.hideturtle()
turt.pencolor("RED")
turt.width(3)
turt.up()
turt.setx(START_POS[0])
turt.sety(START_POS[1])
turt.down()
turt.speed(0)

farthest_pos = [0, 0]

def update_pos():
    tpos = turt.pos()
    pos = [tpos[0] - START_POS[0], tpos[1] + START_POS[1]]
    if abs(pos[0]) > abs(farthest_pos[0]):
        farthest_pos[0] = pos[0]
    if abs(pos[1]) > abs(farthest_pos[1]):
        farthest_pos[1] = pos[1]

def draw_fractal(n):
    if n <= 0:
        turt.forward(80)
        update_pos()
        turt.left(45)
        turt.forward(80)
        update_pos()
        turt.right(90)
        turt.forward(80)
        update_pos()
        turt.left(45)
        turt.forward(80)
        update_pos()
    else:
        draw_fractal(n-1)
        turt.left(45)
        draw_fractal(n-1)
        turt.right(90)
        draw_fractal(n-1)
        turt.left(45)
        draw_fractal(n - 1)


draw_fractal(4)
# print(farthest_pos)
canvas.scale("all", START_POS[0], START_POS[1],
             WIDTH / farthest_pos[0], HEIGHT / farthest_pos[1])

root.mainloop()