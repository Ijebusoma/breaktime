import turtle
def square():
     brad = turtle.Turtle()
     window = turtle.Screen()
     window.bgcolor("black")
     brad.color('green')
     brad.shape('classic')
     brad.speed(9)
     brad.forward(200)  # number stands for the distance
     brad.left(90)
     brad.forward(75)
     brad.left(90)
     brad.forward(200)
     brad.left(90)
     brad.forward(80)
     window.exitonclick()
def triangle():
      brad = turtle.Turtle()
      window = turtle.Screen()
      window.bgcolor("black")
      brad.color('red')
      for i in range(0, 5):
       brad.left(200-60)
       brad.forward(150)
       brad.left(200-80)
       brad.forward(150)
       brad.left(200-80)
       brad.forward(150)

      window.exitonclick()

triangle()

