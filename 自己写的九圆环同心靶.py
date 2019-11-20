import turtle
turtle.setup(650,350,200,200)
def target(radius,x):
   for i in range(10):
      turtle.circle(radius,360)
      turtle.penup()
      turtle.goto(0,x)
      radius = radius + 10
      x = x - 10
      turtle.pendown()
turtle.setup(650,350,200,200)
turtle.pendown()
target(0,0)
turtle.done()
   
