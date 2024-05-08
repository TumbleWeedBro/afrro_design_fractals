import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("#DDDBCB")

# Function to draw a rectangle
def draw_rectangle(width, height):
    colors = ["#050505", "#008080"]
    for _ in range(1,3,1):
        t.begin_fill()
        t.color(colors[_ % 2])
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
        t.end_fill()


# Create a Turtle object
t = turtle.Turtle()
t.speed(0)
t.color("blue")
x_axis = -250
y_axis = -150
for i in range(1,21,1):

    # draw vertical rectangles
    rectangle_width = 90
    rectangle_height = 110
    x=x_axis
    y=y_axis
    for _ in range(5):
        t.penup()
        t.goto(x,y)
        t.pendown()
        draw_rectangle(rectangle_width, rectangle_height)
        t.penup()
        t.forward(rectangle_width+7)  # Move to the right for the next rectangle
        t.pendown()
        x+=10

    # Move to draw vertically
    t.penup()
    t.goto(0+x_axis,y_axis -120)  # Position to start drawing vertically
    t.pendown()

    # Draw 3 rectangles horizontally
    rectangle_width = 130
    rectangle_height = 20
    for _ in range(3):
        draw_rectangle(rectangle_width, rectangle_height)
        t.penup()
        t.forward(0)  # Stay in the same column
        t.right(90)
        t.forward(rectangle_height+7)  # Move down for the next rectangle
        t.left(90)
        t.pendown()
    if i%2==0:
        x_axis*=-1
    else: 
        y_axis*=-1
    
    if i%5==0 and x_axis<0:
        x_axis -=100
    else:
        x_axis *=-1
        x_axis -=100
# Hide the turtle and display the result
t.hideturtle()
screen.exitonclick()