import os
import json
S_LENGTH = 3
S_ANGLE = 25
S_WIDTH = 10
# data representation: X → F+[[X]-X]-F[-FX]+X
file_name = "data\\plant.txt"
file_name_2 = "data\\plant_t_rep.txt"
lol = json.dumps({'instructions': { 'A':{'fd' : None, 'rt' : None, 'on_stack' : False, 'from_stack' : False, 'color' : (255, 0, 0), 'wd' : S_WIDTH},
                                    'B':{'fd' : S_LENGTH, 'rt' : None, 'on_stack' : False, 'from_stack' : False, 'color' : (0, 0, 0), 'wd' : S_WIDTH},
                                    '[':{'fd' : None, 'rt' : None, 'on_stack' : True, 'from_stack' : False, 'color' : (0, 0, 0), 'wd' : S_WIDTH},
                                    ']':{'fd' : None, 'rt' : None, 'on_stack' : False, 'from_stack' : True, 'color' : (0, 0, 0), 'wd' : S_WIDTH},
                                    '-':{'fd' : None, 'rt' : S_ANGLE, 'on_stack' : False, 'from_stack' : False, 'color' : (0, 0, 0), 'wd' : S_WIDTH},
                                    '+':{'fd' : None, 'rt' : -S_ANGLE, 'on_stack' : False, 'from_stack' : False, 'color' : (0, 0, 0), 'wd' : S_WIDTH}},

                  'keys' : 'AB[]+-'}, indent=4)

kek = json.dumps({'instructions': {'A': 'B+[[A]-A]-B[-BA]+A','B': 'BB', '[':'[', ']':']', '+':'+', '-':'-'}, 'keys' : 'AB[]+-'}, indent=4)
unKek = json.loads(kek)

print(lol)
kek2 = ''
lol2 = ''


with open(file_name_2, 'w') as file:
    print(lol, file=file)

with open(file_name_2, 'r') as file:
    lol2 = json.load(file)

with open(file_name, 'w') as file:
    print(kek, file=file)

with open(file_name, 'r') as file:
    kek2 = json.load(file)
print(kek2['instructions'])
print('')
