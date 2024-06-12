import time
import turtle

# Configure the desired font size
FONT_SIZE = 50

# Configure glyph geometry
stroke_width = FONT_SIZE * 0.2
stem_height = FONT_SIZE * 0.6
shoulder_radius = FONT_SIZE - stem_height
shoulder_angle = 180
swash_radius = FONT_SIZE * 0.2
swash_angle = 60


def draw_line(pen, heading, distance):
    """Draw a line with the given heading and distance"""
    pen.setheading(heading)
    pen.forward(distance)


def draw_arc(pen, radius, angle):
    """Draw an arc with the given radius and angle"""
    pen.circle(radius, angle)


# Initialize a turtle that resembles pen on paper
pen = turtle.Turtle()
pen.hideturtle()
pen.shape("circle")
pen.width(stroke_width)

# Move the pen to the starting point at the top of the letter
pen.penup()
pen.goto(0, FONT_SIZE)
pen.pendown()

# Show the turtle
pen.showturtle()

# A downward stroke to the baseline
draw_line(pen, -90, FONT_SIZE)
# An upward stroke to stem height
draw_line(pen, 90, stem_height)
# Form the shoulder
draw_arc(pen, -shoulder_radius, shoulder_angle)  # Negative radius to arc right
# Continue to the baseline
draw_line(pen, -90, stem_height)
# Finish with a swash
draw_arc(pen, swash_radius, swash_angle)

# Pause briefly before hiding the turtle
time.sleep(0.5)
pen.hideturtle()
