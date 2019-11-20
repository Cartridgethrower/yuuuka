import turtle
for i in range(9):
    turtle.circle((i+1)*25)
    turtle.penup()
    turtle.goto(0,-(i+1)*25)
    turtle.pendown()
turtle.done()
