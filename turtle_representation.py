import turtle
import json
import copy

stack = []

def update(curr_state, pos, angle, color):
    curr_state['pos'] = pos
    curr_state['angle'] = angle
    curr_state['color'] = color
    curr_state['fp'] *= 1.05
    curr_state['wp'] *= 0.97
    return curr_state


def draw(S:str, instructions, init_values = {'pos':[0, 0], 'angle':0, 'color':(0, 0, 0), 'fp':1, 'wp':1}):
    curr_state = init_values
    for chr in S:
        if chr in instructions['keys']:
            instr = instructions['instructions'][chr]
            instr_keys = dict.keys(instr)
            turtle.pensize(instr['wd']*curr_state['wp'])
            turtle.pencolor(instr['color'])
            if 'on_stack' in instr_keys and instr['on_stack']:
                stack.append(copy.deepcopy(curr_state))
            if  'from_stack' in instr_keys and instr['from_stack']:
                #print(curr_state)
                curr_state = stack.pop(-1)
                turtle.penup()
                turtle.goto((curr_state['pos'][0], curr_state['pos'][1]))
                turtle.seth(curr_state['angle'])
                turtle.pendown()
            if 'fd' in instr_keys and instr['fd'] != None:
                turtle.forward(instr['fd']*curr_state['fp'])
            if 'rt' in instr_keys and instr['rt'] != None:
                turtle.rt(instr['rt'])
            curr_state = update(curr_state, turtle.pos(), turtle.heading(), turtle.pencolor())
    turtle.hideturtle()
    input()




