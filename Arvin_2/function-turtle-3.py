import turtle as tr
from turtle import pensize

def square(size,pensize,pen_color):
    tr.pencolor(pen_color)
    tr.pensize(pen_size)
    for i in range(4):
        tr.fd(size)
        tr.lt(90)

pen_color = tr.textinput('Pen color', 'Enter color of pen')
pen_size = tr.numinput('Pen size', 'Enter size of pen')
square_size = tr.numinput('Square size', 'Enter size of your square')
square(square_size,pen_size,pen_color)
tr.done()