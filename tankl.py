import turtle
turtle.Screen().bgcolor("cyan")
turtle.Screen().setup(500,500)

tortice = turtle.Turtle()
tortice.pensize(3)
tortice.color("black")

tortice.penup()
tortice.goto(-50, 50)
tortice.pendown()

for i in range(4):
    tortice.forward(100)
    tortice.right(90)
turtle.done()