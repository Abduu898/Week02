import turtle

def draw_polygone(sides):
    t = turtle.Turtle()
    angle = 360 / sides
    for i in range(sides):
        t.forward(100)
        t.right(angle)
    turtle.done()

draw_polygone(3)