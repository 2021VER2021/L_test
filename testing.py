import os
import json
S_LENGTH = 2
S_ANGLE = 30
# data representation: 
file_name = "data\\pythagoras.txt"
file_name_2 = "data\\t_rep.txt"
lol = json.dumps({'instructions': { 'A':{'fd' : S_LENGTH, 'rt' : None, 'on_stack' : False, 'from_stack' : False, 'color' : (1.0, 0, 0), 'wd' : 1},
                                    'B':{'fd' : S_LENGTH, 'rt' : None, 'on_stack' : False, 'from_stack' : False, 'color' : (0, 0, 0), 'wd' : 1},
                                    '[':{'fd' : None, 'rt' : S_ANGLE, 'on_stack' : True, 'from_stack' : False, 'color' : (0, 0, 0), 'wd' : 1},
                                    ']':{'fd' : None, 'rt' : -S_ANGLE, 'on_stack' : False, 'from_stack' : True, 'color' : (0, 0, 0), 'wd' : 1}},
                  'keys' : 'AB[]'}, indent=4)

kek = json.dumps({'instructions': {'A': 'B[A]A','B': 'BB', '[':'[', ']':']'}, 'keys' : 'AB[]'}, indent=4)
unKek = json.loads(kek)

print(lol)
kek2 = ''
lol2 = ''


with open(file_name_2, 'w') as file:
    print(lol, file=file)

with open(file_name_2, 'r') as file:
    lol2 = json.load(file)
"""
with open(file_name, 'w') as file:
    print(kek, file=file)

with open(file_name, 'r') as file:
    kek2 = json.load(file)
print(kek2['instructions'])
print('')
"""