import turtle
turtle.bgcolor("red")
turtle.fillcolor("yellow")
turtle.pencolor("yellow")
turtle.speed(5)
#大星
turtle.begin_fill()
turtle.up()
turtle.goto(-600,200)
turtle.down()
for i in range (5):
    turtle.forward(150)
    turtle.right(144)
turtle.end_fill()
#第一个小星
turtle.begin_fill()
turtle.up()
turtle.goto(-400,300)
turtle.setheading(-55)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.left(144)
turtle.end_fill()
#第二个小星
turtle.begin_fill()
turtle.up()
turtle.goto(-350,212)
turtle.setheading(30)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()
#第三个小星
turtle.begin_fill()
turtle.up()
turtle.goto(-350,145)
turtle.setheading(5)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()
#第四个小星
turtle.begin_fill()
turtle.up()
turtle.goto(-400,90)
turtle.setheading(300)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()



