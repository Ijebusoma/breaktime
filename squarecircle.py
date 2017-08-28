import turtle
def draw_square(turtlename):
     for i in range(0, 4):
        turtlename.forward(100)
        turtlename.right(90)

def draw_art():
            window = turtle.Screen()
            window.bgcolor("red")
            ness = turtle.Turtle()
            ness.shape("turtle")
            ness.color("yellow")
            ness.speed(6)
            for i in range(0, 36):
                draw_square(ness)
                ness.right(10)
            window.exitonclick()
            draw_art()