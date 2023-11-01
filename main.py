import turtle

S = "0"
stack = []
pos_stack = []

N = 8

turtle.speed(100)

def func(a):
    if a == "1":
            return "11"
    if a == "0":
         return "1[0]0"
    if a == "[":
         return "["
    if a == "]":
         return "]"


for i in range(N):
    S = list(map(lambda i: func(i) , S))
    S = ''.join(S)

print(S)
length = 1
angle = 0
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
for i in S:
    if i == '1':
        turtle.forward(length)
    if i == '0':
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






