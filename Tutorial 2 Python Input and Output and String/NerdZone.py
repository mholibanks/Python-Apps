#a program that draws my initials, Mholi Mncube
#Mholi Mncube
#created 2 May 2014
def main():
    import turtle
    a=100
    turtle.speed(1)
    turtle.pencolor("blue")
    turtle.penup()
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(a)
    turtle.right(150)
    turtle.forward(a)
    turtle.left(120)
    turtle.forward(a)
    turtle.right(150)
    turtle.forward(a)
    turtle.penup()
    turtle.home()
    def dot():
        turtle.pendown()
        turtle.pencolor("black")
        turtle.left(90)
        turtle.forward(a/5)
        turtle.right(90)
        turtle.forward(a/5) 
        turtle.right(90)
        turtle.forward(a/5)
        turtle.right(90)
        turtle.forward(a/5)
        turtle.home()
        def m():
            turtle.speed(1)
            turtle.pencolor("red")
            turtle.penup()
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.pendown()
            turtle.forward(a)
            turtle.right(180)
            turtle.forward(a/2)
            turtle.left(90)
            turtle.forward(a)
            turtle.left(90)
            turtle.forward(a/2)
            turtle.right(180)
            turtle.forward(a)
            turtle.penup()
            turtle.home()
            turtle.exitonclick()
        m()
    dot()
main()
