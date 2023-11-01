import pygame as pg
import numpy as np
import json
import copy

FPS = 30
TIME_CONST = 1/FPS

#pygame things
pg.init()

WIDTH = HEIGHT = 750

stack = []

def on_screen(screen, S:str, instructions, init_values):
    curr_state = init_values
    for chr in S:
        if chr in instructions['keys']:
            instr = instructions['instructions'][chr]
            if instr['on_stack']:
                stack.append(copy.deepcopy(curr_state))
            if instr['from_stack']:
                #print(curr_state)
                curr_state = stack.pop(-1)
            if instr['fd'] != None:
                pg.draw.line(screen, instr['color'],
                            curr_state['pos'],
                            (curr_state['pos'][0] + np.cos(np.pi*curr_state['angle']/180)*instr['fd'],
                            curr_state['pos'][1] + np.sin(np.pi*curr_state['angle']/180)*instr['fd']),
                            int(instr['wd']*curr_state['wp']))
                curr_state['pos'] = (curr_state['pos'][0] + np.cos(np.pi*curr_state['angle']/180)*instr['fd'],
                                    curr_state['pos'][1] + np.sin(np.pi*curr_state['angle']/180)*instr['fd'])
            if instr['rt'] != None:
                curr_state['angle'] += instr['rt']
            curr_state['fp'] *= 1
            curr_state['wp'] *= 0.99

def draw(S, instructions, init_values= {'pos':[HEIGHT/2, WIDTH], 'angle':-90, 'color':(0, 0, 0), 'fp':1, 'wp':1}):
    scr = pg.display.set_mode((WIDTH, HEIGHT))
    scr.fill((255, 255, 255))
    on_screen(scr, S, instructions, init_values)
    isRunning = True
    Pause = False
    while isRunning:
        for event in pg.event.get():
            if event.type == pg.QUIT:  
                isRunning = False
            if event.type == pg.KEYDOWN:
                # checking if key "A" was pressed
                if event.key == pg.K_SPACE:
                    Pause = not(Pause)
                    pg.time.delay(100)
        pg.display.flip()  
        pg.time.delay(1000//FPS)
    pg.quit()

