import turtle
def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(30)
        tree(branchLen - 15, t)
        t.left(60)
        tree(branchLen - 15, t)
        t.right(30)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color("green")
    tree(95, t)
    myWin.exitonclick()

main()
