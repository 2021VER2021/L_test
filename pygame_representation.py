import pygame as pg
import numpy as np
import json
import copy
import pygame_actions

FPS = 30
TIME_CONST = 1/FPS

#pygame things
pg.init()

WIDTH = HEIGHT = 600

stack = pygame_actions.init_stack()
# TODO scale - ? ; more parametrs, mb functions?
def on_screen(screen, S:str, instructions, init_values, scale):
    curr_state = init_values
    list.clear(stack)
    for chr in S:
        if chr in instructions['keys']:
            instr = instructions['instructions'][chr]
            instr_keys = dict.keys(instr)
            if 'on_stack' in instr_keys and instr['on_stack']:
                pygame_actions.on_stack(stack, curr_state)
            if 'from_stack' in instr_keys and instr['from_stack']:
                curr_state = pygame_actions.from_stack(stack)
            if 'color' in instr_keys:
                pygame_actions.simple_set_color(instr['color'], curr_state)
            if 'fd' in instr_keys and instr['fd'] != None:
                pygame_actions.scale_draw_line(screen, instr['fd'], instr['wd'], curr_state, scale)
            if 'rt' in instr_keys and instr['rt'] != None:
                pygame_actions.scale_set_angle(instr['rt'], curr_state, scale)
            curr_state['fp'] *= 1.2
            curr_state['wp'] *= 0.99

def draw(S, instructions, init_values= {'pos':[HEIGHT/2, WIDTH], 'angle':-90, 'color':(0, 0, 0), 'fp':1, 'wp':1}):
    scale = 0.1
    scr = pg.display.set_mode((WIDTH, HEIGHT))
    isRunning = True
    Pause = True
    while isRunning:
        if not(Pause):
            scr.fill((255, 255, 255))
            on_screen(scr, S, instructions, copy.deepcopy(init_values), scale)
            scale = scale + 0.01
            pg.display.flip()
        if scale > 1:
            Pause = True
        for event in pg.event.get():
            if event.type == pg.QUIT:  
                isRunning = False
            if event.type == pg.KEYDOWN:
                # checking if key "A" was pressed
                if event.key == pg.K_SPACE:
                    Pause = not(Pause)
                    pg.time.delay(100)  
        pg.time.delay(1000//FPS)
    pg.quit()

