import copy as cp
import numpy as np
import pygame as pg

def init_stack():
    global stack
    stack = []
    return stack

def on_stack(stack, curr_state):
    stack.append(cp.deepcopy(curr_state))

def from_stack(stack):
    return stack.pop(-1)

def simple_set_color(colour, curr_state):
    curr_state['color'] = (colour[0] * 255, colour[1] * 255, colour[2] * 255)

def simple_draw_line(screen, fd, wd, curr_state):
    pg.draw.line(screen, curr_state['color'],
                curr_state['pos'],
                (curr_state['pos'][0] + np.cos(np.pi*curr_state['angle']/180)*fd,
                curr_state['pos'][1] + np.sin(np.pi*curr_state['angle']/180)*fd),
                int(wd*curr_state['wp']))
    curr_state['pos'] = (curr_state['pos'][0] + np.cos(np.pi*curr_state['angle']/180)*fd,
                        curr_state['pos'][1] + np.sin(np.pi*curr_state['angle']/180)*fd)

def scale_draw_line(screen, fd, wd, curr_state, scale):
    pg.draw.line(screen, curr_state['color'],
                curr_state['pos'],
                (curr_state['pos'][0] + scale*np.cos(np.pi*curr_state['angle']/180)*fd,
                curr_state['pos'][1] + scale*np.sin(np.pi*curr_state['angle']/180)*fd),
                int(wd*curr_state['wp']))
    curr_state['pos'] = (curr_state['pos'][0] + scale*np.cos(np.pi*curr_state['angle']/180)*fd,
                        curr_state['pos'][1] + scale*np.sin(np.pi*curr_state['angle']/180)*fd)

def simple_set_angle(angle, curr_state):
    curr_state['angle'] = angle

def scale_set_angle(angle, curr_state, scale):
    curr_state['angle'] += scale*angle





    
