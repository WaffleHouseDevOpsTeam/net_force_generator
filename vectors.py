"""
input follows the format of 'name'<x, y> (ex 'friction'<5, 5>) or 'name'<mag, angle unit> (ex 'push'<50, 30 degrees>)
"""
import re
from math import sin, cos, pi
from turtle import *
import freebody as fr
vectors = {}
sum_vec = [0, 0]

def string_conv(string):
    global vectors
    global sum_vec
    if 'add' in string:
        vector_name = re.findall(r"'(.*?)'", string)
        vector_coords = re.findall(r"<(.*?)>", string)
        vector_coords = vector_coords[0].split(', ')
        if 'deg' in vector_coords[1] or 'rad' in vector_coords[1]:
            magnitude = float(vector_coords[0])
            angle = float(re.findall(r'\d+', vector_coords[1])[0])
            if 'deg' in vector_coords[1]:
                #print("degrees homie")
                angle = angle * (pi / 180)
            x = magnitude * cos(angle)
            y = magnitude * sin(angle)
            vector_coords = [x, y]
    
        vector_coords[0] = float(vector_coords[0])
        sum_vec[0] = sum_vec[0] + vector_coords[0]
        
        vector_coords[1] = float(vector_coords[1])
        sum_vec[1] = sum_vec[1] + vector_coords[1]
        
        print(sum_vec)
        vectors[vector_name[0]] = vector_coords
        fr.draw_arrow(vector_name, vector_coords[0], vector_coords[1])
    elif 'exit' in string:
        exit(-1)
    else:
        print("thats not right, remember to use '' and <>")

def sum_vectors():
    print(f'sum in x direction: {sum_vec[0]}')
    print(f'sum in y direction: {sum_vec[1]}')

print("add a vector with the prefix 'add'")
print("input follows the format of add 'name'<x, y> (ex add 'friction'<5, 5>) or \n add 'name'<mag, angle unit> (ex add 'push'<50, 30 degrees>)'")
ht()
fr.draw_square(5)
while True:
    string_conv(input("> "))
    print(vectors)
    sum_vectors()
#print(string_conv("'friction'(50, 30 degrees)"))