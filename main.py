from turtle import Turtle, Screen

din = Turtle()
screen = Screen()


def move_forwards():
    din.forward(10)


def move_backwards():
    din.backward(10)


def turn_clockwise():
    din.right(10)


def turn_counterclockwise():
    din.left(10)


def clear():
    din.clear()
    din.penup()
    din.home()
    din.pendown()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkeypress(key="a", fun=turn_counterclockwise)
screen.onkey(clear, "c")
screen.exitonclick()
