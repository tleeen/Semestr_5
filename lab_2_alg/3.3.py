from random import randint
import turtle


def tree(branchLen, t, w):
    a = randint(15, 20)
    t.width(w)
    if (branchLen > 5) and (w > 0):
        if branchLen - 15 <= 5 or w == 0.5:
            t.color("green")
        t.forward(branchLen)
        t.right(a)
        tree(branchLen - 15, t, w - 0.5)
        t.left(2 * a)
        tree(branchLen - 15, t, w - 0.5)
        t.right(a)
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
    tree(100, t, 4)
    myWin.exitonclick()


main()
