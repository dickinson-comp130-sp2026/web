# Draw a grid of dots using turtle graphics.
# This program demonstrates the use of a nested for loop.

import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the fastest possible drawing speed for this turtle
t.speed(0)

for i in range(3):
    x = 20 * i
    for j in range(5):
        y = 20 * j
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.circle(4)

# Keep the turtle window open
turtle.mainloop()
