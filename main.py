import data_reading
import parse_instructions
import turtle_representation
import pygame_representation

S = "A"
stack = []
pos_stack = []

N = 7

instructions = data_reading.get_instructions('plant.txt')

for i in range(N):
    S = parse_instructions.parse(S, instructions)

#print(S)

pygame_representation.draw(S, data_reading.get_instructions('plant_t_rep.txt'))
 


