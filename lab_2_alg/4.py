import turtle


def sierpinski(s, l):
    if l == 1:
        for i in range(3):
            turtle.fd(s)
            turtle.left(120)
    else:
        sierpinski(s / 2, l - 1)
        turtle.fd(s / 2)
        sierpinski(s / 2, l - 1)
        turtle.bk(s / 2)
        turtle.left(60)
        turtle.fd(s / 2)
        turtle.right(60)
        sierpinski(s / 2, l - 1)
        turtle.left(60)
        turtle.bk(s / 2)
        turtle.right(60)


def main():
    sierpinski(200, 5)
    turtle.mainloop()

main()

