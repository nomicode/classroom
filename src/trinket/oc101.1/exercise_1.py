import time
import turtle

# Configure the desired number of sides of the polygon you want to draw (e.g.,
# 3 for a triangle)
SIDES = 3

# Hint: Try setting the value `SIDES` to 12. The turtle will go out-of-bounds
# because the size of the polygon scales in proportion to the square of the
# number of sides.

# Configure the desired side length
SIDE_LENGTH = 100

# Hint: Try setting `SIDES` to 36 and `SIDE_LENGTH` to 10. The result should
# provide visual insight into what we are actually drawing.

# Initialize a green turtle
turty = turtle.Turtle()
turty.hideturtle()
turty.color("green")
turty.shape("turtle")
turty.width(2)

# Reposition the turtle so the polygon is always centered on screen
turty.penup()
turty.goto(-SIDE_LENGTH // 2, -SIDE_LENGTH // 2)
turty.pendown()

# Show the turtle and pause briefly before moving
turty.showturtle()
time.sleep(0.5)

# The sum of the exterior angles of any polygon is always 360 degrees
exterior_angle = 360 / SIDES

# Draw the polygon
for _ in range(SIDES):
    turty.forward(SIDE_LENGTH)
    turty.left(exterior_angle)

# Pause briefly before hiding the turtle
time.sleep(0.5)
turty.hideturtle()
