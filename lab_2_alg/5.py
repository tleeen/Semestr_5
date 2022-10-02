import turtle


def triangle(s, n):
    if n != 0:
        turtle.left(60)
        turtle.forward(s)
        turtle.right(120)
        turtle.forward(s)
        turtle.right(120)
        turtle.forward(s)
        turtle.right(120)
        turtle.forward(s)
        turtle.right(120)
        turtle.forward(s/4)
        turtle.right(60)
        turtle.forward(s/4)
        turtle.right(120)
        turtle.forward(s/4)
        turtle.right(60)
        turtle.forward(s / 4)
        turtle.right(120)
        turtle.forward(s)
        turtle.left(60)
        triangle(300, n - 1)
        triangle(400, n - 1)
        triangle(300, n - 1)
        triangle(200, n - 1)


def main():
    turtle.up()
    turtle.setposition(-700, -350)
    turtle.down()
    triangle(200, 2)
    turtle.mainloop()

main()