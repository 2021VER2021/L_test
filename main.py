import data_reading
import parse_instructions
import turtle_representation

S = "A"
stack = []
pos_stack = []

N = 6

instructions = data_reading.get_instructions('pythagoras.txt')

for i in range(N):
    S = parse_instructions.parse(S, instructions)

#print(S)

turtle_representation.draw(S, data_reading.get_instructions('t_rep.txt'))
a = input()



