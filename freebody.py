from turtle import *
from time import sleep

home = (0, 0)
scale = 10

def go_home():
    teleport(home[0], home[1])
    
def draw_square(size):
    teleport((-1*(size/2))*scale, (size/2)*scale)
    for x in range(4):
        forward(size*scale)
        right(90)
    go_home()
    
def draw_arrow(name, x, y):
    goto(x*scale, y*scale)
    goto((x*scale)-(x), y*scale)
    write(name)
    go_home()