import turtle
import random

CELL_SIZE = 8

class LifeBoardsnake:
    "Game of Life board, a rectangular board with live and dead cells"

    def __init__(self, width, height):
        "Create a new Game of Life board of specified size."
        self.body = []
        self.width, self.height = width, height
        self.head=(2,2)
        self.food=(8,8)
        self.generator=0
        self.direction=None
        self.switch=1
    def newfood(self):
        "Fill the board with a random pattern"
        if self.generator==1:
            j, k = random.randint(0,self.width), random.randint(0,self.height)
            if (j,k) in self.body or (j,k)==self.head:
                self.newfood()
            else:
                self.food=(j,k)
                self.generator=0
    
    #def eatfood(self):
        #return self.head==self.food

    def a(self):
        if self.direction!='right' and self.direction!='left': self.direction='left'
    def d(self):
        if self.direction!='right' and self.direction!='left': self.direction='right'
    def s(self):
        if self.direction!='up' and self.direction!='down': self.direction='down'
    def w(self):
        if self.direction!='up' and self.direction!='down': self.direction='up'

    def step(self):
        "Compute the next generation according to Conway's rule."
        if self.head in self.body or self.head[0]<-10 or self.head[0]>self.width or \
        self.head[1]<-10 or self.head[1]>self.height:
            self.switch=0
        self.body.insert(0,self.head)
        if self.direction=='up':
            self.head=(self.head[0],self.head[1]+1)
        if self.direction=='down':
            self.head=(self.head[0],self.head[1]-1)
        if self.direction=='left':
            self.head=(self.head[0]-1,self.head[1])
        if self.direction=='right':
            self.head=(self.head[0]+1,self.head[1])
        if self.head==self.food:
            self.generator =1
        else:
            self.body.remove(self.body[-1])
    
    def display(self):
        "Draw the whole board"
        turtle.clear()
        turtle.color('black')
        turtle.setheading(0)
        for [x, y] in self.body:
            turtle.penup()
            turtle.setpos(x * CELL_SIZE, y * CELL_SIZE)
            turtle.pendown()
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(CELL_SIZE - 1)
                turtle.left(90)
            turtle.end_fill()
        turtle.penup()
        turtle.setpos(self.head[0] * CELL_SIZE, self.head[1] * CELL_SIZE)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(CELL_SIZE - 1)
            turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.setpos(self.food[0] * CELL_SIZE, self.food[1] * CELL_SIZE)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(CELL_SIZE - 1)
            turtle.left(90)
        turtle.end_fill()
        turtle.update()
    