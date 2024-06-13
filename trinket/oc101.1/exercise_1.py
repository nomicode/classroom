import time
import turtle

# Constants needed to define a polygon
SIDES = 3
LENGTH = 100

# Calculate the exterior angle, given the number of sides
exterior_angle = 360 / SIDES

# Initialize a green turtle
turty = turtle.Turtle()
turty.color("green")
turty.shape("turtle")
turty.width(4)

# Draw the polygon
for _ in range(SIDES):
    turty.forward(LENGTH)
    turty.left(exterior_angle)

time.sleep(0.2)
turty.hideturtle()
