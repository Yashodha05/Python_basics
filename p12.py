import turtle

def triangle(t, x, y, size, depth):
    if depth==0:
        t.penup()
        t.goto(x, y)
        t.pendown()

        for i in range(3):
            t.forward(size)
            t.left(120)

    else:
        triangle(t, x, y, size/2,  depth-1)
        triangle(t, x+size/2, y, size/2, depth-1)
        triangle(t, x+size/4, y+(size/2)*(3*0.5)/2, size/2, depth-1)

        if depth==change_depth:
            t.fillcolor('pink')
            t.begin_fill()
            triangle(t, x+size/4, y+(size/2)*(3*0.5)/2, size/2, 0)
            t.end_fill()

            t.fillcolor('lightblue')
            t.begin_fill()
            triangle(t, x, y, size/2, 0)
            t.end_fill()        

            t.fillcolor('green')
            t.begin_fill()
            triangle(t, x+size/2, y, size/2, 0)
            t.end_fill()

t=turtle.Turtle()
t.speed(2)

change_depth=2
triangle(t, -200, -200, 400, change_depth)
turtle.done()