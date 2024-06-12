import turtle

# Configure the number of sides of the polygon you want to draw (e.g., 3 for a
# triangle)
SIDES = 3

# Grab a turty
turty = turtle.Turtle()
turty.color("green")
turty.shape("turtle")
turty.width(2)

# The perimeter of a polygon increases linearly with the number of sides.
# However, the area of a polygon grows roughly with the square of the number
# of sides. This means that if we hard-code the side length, the size of the
# polygon will grow very quickly as `SIDES` is increased.

# To prevent the polygon from going out-of-bounds, we can make the side length
# inversely proportional to the number of sides.

# After some trial and error with Trinket, a scaling factor of 300 seems reasonable.
side_length = 300 / SIDES

# Hint: With the on-screen size of the polygon under control, try setting
# `SIDES` to a value of 36 or higher to gain a visual insight into what we are
# actually drawing.

# The sum of the exterior angles of any polygon is always 360 degrees
exterior_angle = 360 / SIDES

# Draw the polygon
for _ in range(SIDES):
    turty.forward(side_length)
    turty.left(exterior_angle)
