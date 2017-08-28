import turtle
def flower():
        brad = turtle.Turtle()
        window = turtle.Screen()
        window.bgcolor("black")
        brad.color('green')
        brad.shape('classic')
        brad.speed(9)
        for i in range(1, 37):
         brad.left(20)
         brad.forward(10)
         brad.circle(100)

        window.exitonclick()
flower();



