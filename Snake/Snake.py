from turtle import *
from random import randint
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    clear()
    #Changes the color of the snake and chooses one of 5 colors, but no red
    for body in snake:
        colors = ['black', 'blue', 'purple', 'yellow', 'brown', 'lightgreen',
                 'green', 'teal', 'cyan', 'indigo', 'fuchsia', 'deeppink']
        rColor = randint(0,11)
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()


    #makes a random choice and moves the food
    list = [1, 2, 3, 4, 9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
    if random.choice(list) == 1:
      food.x += 10
    elif random.choice(list) == 2:
      food.y += 10
    elif random.choice(list) == 3:
      food.x -= 10
    elif random.choice(list) == 4:
      food.y -= 10
      
    ontimer(move, 100)

      
    

setup(420, 420, -370, 0) #tamaño de la ventana
hideturtle()
tracer(False) #delay quit
listen() #escucha las acciones del usuario

#changes direction of the snake
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
#Adding moves

#Up
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, 10), 'W')
#Down
onkey(lambda: change(0, -10), 's')
onkey(lambda: change(0, -10), 'S')
#Rigth
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(10, 0), 'D')
#Left
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(-10, 0), 'A')
move()
done()