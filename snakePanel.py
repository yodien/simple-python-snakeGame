from snakeControl import *

def main():
    # set up window
    width, height = turtle.screensize()
    turtle.setworldcoordinates(0, - 20, width, height - 20)
    turtle.title('Game of Snake')

    # write instructions
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.setposition(5, -15)
    writer.write("W)move to upsite   S)move to downsite   A)move to leftsite\
        D)move to rightsite    Q)uit", font=('sans-serif', 14, 'normal'))    

    # set up board
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.tracer(0, 0) # turn off animation; update() needs to be called
    board = LifeBoardsnake(width // CELL_SIZE, (height - 20) // CELL_SIZE)
    #board.makeRandom()
    board.display()


    # set up key bindings
    def w():
        board.w()
    turtle.onkey(w, 'w')
    def a():
        board.a()
    turtle.onkey(a, 'a')
    def s():
        board.s()
    turtle.onkey(s, 's')
    def d():
        board.d()
    turtle.onkey(d, 'd')

    turtle.onkey(turtle.bye, 'q')

    def perform_step():
        board.step()
        board.newfood()
        board.display()
        if board.switch==1:
            turtle.ontimer(perform_step, 200)# do again after 25 ms
        else:
            writer.penup()
            writer.pencolor('brown')
            writer.clear()
            writer.setposition(80,100)
            writer.write("GAME OVER", font=('sans-serif', 72, 'normal'))
            writer.penup()
            writer.setposition(145,45)
            writer.write('Press (Q) to quit', font=('sans-serif', 18, 'normal'))
    perform_step()
    
    # set focus on screen and enter the main loop
    turtle.listen()
    turtle.mainloop()