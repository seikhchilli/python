import turtle

def drawboxes(size):
    x, y = -size, -size

    check = True
    turtle.speed(0)

    while(y < size):
        check = not check
        x = -size
        while(x < size):
            check = not check
            if(check):
                turtle.fillcolor("black")
            else:
                turtle.fillcolor("white")

            turtle.up()
            turtle.setpos(x, y)
            turtle.seth(0)
            turtle.begin_fill()

            for i in range(4):
                turtle.down()
                turtle.fd(size/4)
                turtle.lt(90)
            
            turtle.end_fill()

            x += (size/4)

        y += (size/4)
        




def chessboard():
    drawboxes(240)
    turtle.done()



def main():
    chessboard()

main()
