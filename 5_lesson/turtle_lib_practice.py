import turtle


def drawSquare(size, color):
    turtle.speed(1)
    turtle.color(color)
    turtle.begin_fill()
    def move(len):
        turtle.forward(len)
        turtle.left(90)

    for _ in range(4):
        move(size)

    turtle.end_fill()

drawSquare(100, 'red')
turtle.goto(200, 200)
drawSquare(200, 'blue')