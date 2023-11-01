import turtle
import data_reading
import parse_instructions

S = "A"
stack = []
pos_stack = []

N = 8

turtle.speed(100)

instructions = data_reading.get_instructions('pythagoras.txt')

for i in range(N):
    S = parse_instructions.parse(S, instructions)

#print(S)

length = 1
angle = 0
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
for i in S:
    if i == 'B':
        turtle.forward(length)
    if i == 'A':
        turtle.forward(length)
    if i == '[':
        stack.append(angle)
        angle += 45
        turtle.seth(angle)
        pos_stack.append(turtle.pos())
    if i == ']':
        angle = stack.pop(-1)
        # turtle.rt(angle)
        turtle.penup()
        turtle.goto(pos_stack.pop(-1))
        turtle.pendown()
        angle -=45
        turtle.seth(angle)
a = input()






