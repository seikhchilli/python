import turtle

length = eval(input("Length: "))

width = eval(input("Width: "))


turtle.forward(length)
turtle.lt(90)
turtle.forward(width)
turtle.lt(90)
turtle.forward(length)
turtle.lt(90)
turtle.forward(width)
turtle.fillcolor("red")
turtle.done()

