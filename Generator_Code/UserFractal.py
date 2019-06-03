from turtle import RawTurtle, TurtleScreen
from tkinter import Tk, Canvas
from math import atan2, degrees, sqrt

WIDTH = 1200
HEIGHT = 675
POINTS = []
START_POS = []*2
# print(START_POS)


# callback functions
def clicked(event):
    POINTS.append((event.x, event.y))
    print(POINTS)


def enter(event):
    if len(POINTS) < 2:
        return
    global START_POS
    START_POS = [POINTS[0][0] - (WIDTH / 2), (HEIGHT / 2) - POINTS[0][1]]
    turt.up()
    turt.setx(START_POS[0])
    turt.sety(START_POS[1])
    turt.down()
    # print(START_POS)
    draw_fractal(1)
    # print(farthest_pos)
    scale = min(WIDTH / farthest_pos[0], (HEIGHT / farthest_pos[1]) / 1.1)
    canvas.scale('all', START_POS[0], -START_POS[1], scale, scale)
    canvas.move('all', -POINTS[0][0], (HEIGHT - POINTS[0][1]) - 15)


# set up root
root = Tk()
root.bind('<Button-1>', clicked)
root.bind('<Return>', enter)

# set up canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness=0)
turtle_screen = TurtleScreen(canvas)
turtle_screen.bgcolor("black")
canvas.pack()

# set up turtle
turt = RawTurtle(turtle_screen)
turt.hideturtle()
turt.speed(0)
turt.pencolor("RED")
turt.width(3)

farthest_pos = [0, 0]


def update_pos():
    tpos = turt.pos()
    pos = [tpos[0] - START_POS[0], tpos[1] - START_POS[1]]
    if abs(pos[0]) > abs(farthest_pos[0]):
        farthest_pos[0] = pos[0]
    if abs(pos[1]) > abs(farthest_pos[1]):
        farthest_pos[1] = pos[1]


def get_angle(p1, p2):
    dx = p2[0] - p1[0]
    dy = p1[1] - p2[1]
    result = degrees(atan2(dy, dx))
    return result + 360 if result < 0 else result


def get_distance(p1, p2):
    return sqrt(((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))


def draw_fractal(n=0):
    if n <= 0:
        for i in range(0, len(POINTS)-1):
            turt.setheading(0)
            turt.left(get_angle(POINTS[i], POINTS[i+1]))
            # print(get_distance(POINTS[i], POINTS[i + 1]))
            turt.forward(get_distance(POINTS[i], POINTS[i + 1]))
        update_pos()
    else:
        for i in range(0, len(POINTS) - 1):
            turt.setheading(0)
            turt.left(get_angle(POINTS[i], POINTS[i + 1]))
            draw_fractal(n-1)


root.mainloop()