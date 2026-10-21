import turtle

# Recursive function to draw the Koch snowflake
def koch_snowflake(t, x1, y1, x2, y2, depth):
    if depth == 0:
        # Base case: Draw a straight line
        t.goto(x2, y2)

    else:
        # Divide the line into three equal parts
        xa = x1 + (x2 - x1) / 3
        ya = y1 + (y2 - y1) / 3

        xb = x1 + 2 * (x2 - x1) / 3
        yb = y1 + 2 * (y2 - y1) / 3

        # Calculate the peak of the triangular bump
        xc = (x1 + x2) / 2 - (y2 - y1) * (3**0.5) / 6
        yc = (y1 + y2) / 2 + (x2 - x1) * (3**0.5) / 6

        # Draw the four smaller segments recursively
        koch_snowflake(t, x1, y1, xa, ya, depth - 1)
        koch_snowflake(t, xa, ya, xc, yc, depth - 1)
        koch_snowflake(t, xc, yc, xb, yb, depth - 1)
        koch_snowflake(t, xb, yb, x2, y2, depth - 1)


# Main drawing setup
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Set the fill color
t.fillcolor('lightblue')

depth = 3
size = 300

# Define the vertices of the initial equilateral triangle
x1 = -size / 2
y1 = size * (3**0.5) / 6

x2 = size / 2
y2 = size * (3**0.5) / 6

x3 = 0
y3 = -size * (3**0.5) / 3

# Move to the starting point
t.penup()
t.goto(x1, y1)
t.pendown()

# Start filling the snowflake
t.begin_fill()

# Draw the three sides continuously
koch_snowflake(t, x1, y1, x2, y2, depth)
koch_snowflake(t, x2, y2, x3, y3, depth)
koch_snowflake(t, x3, y3, x1, y1, depth)

# Finish filling
t.end_fill()

# Keep the window open
turtle.done()
