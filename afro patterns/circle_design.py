import random
import turtle


def draw_circle(t, radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_fractal_circles(t, radius, depth, colors):
    if depth == 0:
        return
    else:

        draw_circle(t, radius, colors[-depth])
        # Recursively draw smaller circles within the current circle
        draw_fractal_circles(t, radius/(3/2), depth-1, colors)

# Set up the screen and turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("orange")

t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

colors = ["red", "pink", "red", "orange", "purple", "blue", "green"]


def Place_circle(x, y):
    for i in range(6):
        t.penup()
        t.goto(x, y)
        t.pendown()
        draw_fractal_circles(t, 50, 5, colors)
        x += 220

def Place_circleP2(a, b):
    for i in range(6):
        t.penup()
        t.goto(a, b)
        t.pendown()
        draw_fractal_circles(t, -(50 * 2 / 3), 5, colors)
        a += 220

def Pattern2_circle(e):
    for i in range(6):
        t.penup()
        t.goto(e, -75)
        t.pendown()
        draw_fractal_circles(t, -(50 * 2 / 3), 5, colors)
        e +=220
def Pattern3(r):
    for i in range(6):
        t.penup()
        t.goto(r, -170)
        t.pendown()
        draw_fractal_circles(t, (50), 5, colors)
        r += 220


def Pattern4(u):
    for i in range(6):
        t.penup()
        t.goto(u, -65)
        t.pendown()
        draw_fractal_circles(t, (50), 5, colors)
        u += 220
def Pattern5(o):
    for i in range(6):
        t.penup()
        t.goto(o, 0)
        t.pendown()
        draw_fractal_circles(t, -(50 * 2 / 3), 5, colors)
        o += 220


def Pattern6(z):
    for i in range(6):
        t.penup()
        t.goto(z, 125)
        t.pendown()
        draw_fractal_circles(t, -(50), 5, colors)
        z += 220

def Pattern7(s):
    for i in range(6):
        t.penup()
        t.goto(s, 55)
        t.pendown()
        draw_fractal_circles(t, (50 * 2 / 3), 5, colors)
        s += 220
x = -250
y = -250

a = -140
b = -180

r = -140
e = -250

u = -250
o = -140

z = -140
s = -250
Place_circle(x, y)
Place_circleP2(a,b)
Pattern2_circle(e)
Pattern3(r)
Pattern4(u)
Pattern5(o)
Pattern6(z)
Pattern7(s)




# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()