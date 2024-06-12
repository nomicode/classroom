import time
import turtle

# User configurable font size
FONT_SIZE = 65

# Typeface geometry
# =============================================================================

# X-height is the height of a lowercase "x" and is typically 0.5 to 0.7 times
# the font size
x_height = FONT_SIZE * 0.5

# Stroke width is typically 0.1 to 0.15 times the font size
stroke_width = FONT_SIZE * 0.1

# The first stem of the "n" typically connects with the x-height
first_stem_height = x_height

# The height of the second stem of the "n" character is typically about 0.8 to
# 0.9 times the x-height for screen typefaces, but we need to use a lower value
# to accommodate the prominent curve of the shoulder (more reminiscent of
# hand-written forms)
second_stem_height = x_height * 0.6

# For a simple handwriting style typeface, the shoulder can be drawn as a
# perfect semi-circle (unlike the more elliptical curves in screen typefaces)
# with a radius that makes up the space between the x-height and the top of the
# second stem
shoulder_radius = x_height - second_stem_height
shoulder_angle = 180

# Ornaments and swashes that descend below the baseline typically extend about
# 0.2 to 0.4 times the x-height
swash_radius = x_height * 0.2
swash_angle = 90

# Turtle
# =============================================================================

turty = turtle.Turtle()

# Use a circle to emulate a pen on paper
turty.shape("circle")
turty.width(stroke_width)

# Encapsulate some of the drawing logic
# -----------------------------------------------------------------------------

# Heading constants
_UP_HEADING = 90
_DOWN_HEADING = -90


def draw_line(heading, distance):
    """Draw a line with the given heading and distance"""
    turty.setheading(heading)
    turty.forward(distance)


def draw_arc(radius, angle):
    """Draw an arc with the given radius and angle"""
    turty.circle(radius, angle)


# Draw the letter "n" the way it would be written by hand
# -----------------------------------------------------------------------------

# Move the pen to the starting position at x-height
turty.penup()
turty.goto(0, x_height)
turty.pendown()

# A downward stroke starting to the baseline
draw_line(_DOWN_HEADING, first_stem_height)

# An upward stroke to form the shoulder, second stem, and swash
draw_line(_UP_HEADING, second_stem_height)
draw_arc(-shoulder_radius, shoulder_angle)  # Negative radius to arc right
draw_line(_DOWN_HEADING, second_stem_height)
draw_arc(swash_radius, swash_angle)

# A brief pause before lifting the pen up and off the paper
time.sleep(0.2)
turty.penup()
turty.hideturtle()
