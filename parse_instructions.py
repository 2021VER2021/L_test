import json

def parsing_function(i, instr):
    for key in instr['keys']:
        if key == i:
            return instr['instructions'][key]
    print("Error_occure")

def parse(S : str, instr):
    S = list(map(lambda i: parsing_function(i, instr) , S))
    S = ''.join(S)
    return S