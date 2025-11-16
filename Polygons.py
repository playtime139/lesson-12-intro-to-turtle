import turtle
turtle.Screen().bgcolor("Orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
num_sides = 10
side_length = 10
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()