"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
import turtle
from freegames import vector

screen = Screen()

#Dibuja una linea en una posición random
def line(start, end):
    "Draw line from start to end."
    color('red')
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)
#Dibuja un cuadrado en una posición random
def square(start, end):
    "Draw square from start to end."
    color('red')
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Dibuja un circulo en una posición random
def Circle(start, end):
    t=turtle.Turtle()
    color('red') 
    r=50
    col="blue"
    t.fillcolor(col)
    t.begin_fill()
    t.circle(r)
    t.end_fill
    

#Dibuja un rectángulo en una posición random
def rectangle(start, end):
    "Draw rectangle from start to end."
    #posicionamiento
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    #dibuja un rectángulo
    for count in range (2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
    end_fill()


#Dibuja un triángulo en una posición random
def triangle(start, end):
    #posicionamiento
    up()
    goto(start.x,end.y)
    begin_fill()
    down()
    #comienza a dibujar
    forward(end.y - start.y)
    left(90)
    forward(end.x - start.x)
    left(180-(math.degrees((math.atan((end.y - start.y)/(end.x - start.x))))))
    forward(math.sqrt(((end.y - start.y)**2)+((end.x - start.x)**2)))
    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

#creación de la instancia
state = {'start': None, 'shape': rectangle}
setup(420, 420, 370, 0)

#Screen call
onscreenclick(tap)
listen() 

#Letras para cambiar el estado de las figuras
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()