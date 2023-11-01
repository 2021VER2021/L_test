import json

FILE_FOLDER = "data" + "\\"

def get_instructions(file_name='pythagoras.txt'):
    with open(FILE_FOLDER+file_name, 'r') as file:
        return json.load(file)

def set_instructions(file_name):
    pass