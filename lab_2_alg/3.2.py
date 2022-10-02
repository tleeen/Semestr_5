import turtle


def tree(branchLen, t, w):
    t.width(w)
    if (branchLen > 5) and (w > 0):
        if branchLen - 15 <= 5 or w == 0.5:
            t.color("green")
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t, w - 0.5)
        t.left(40)
        tree(branchLen - 15, t, w - 0.5)
        t.right(20)
        t.backward(branchLen)
        t.color("black")


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("black")
    tree(75, t, 4)
    myWin.exitonclick()


main()