import pyperclip  # autp copy/paste functionality from a function 
import json

json_copy = {}  # empty dictionary to store json data, works as a backup

json_filename = 'comebackapp.json'

with open(json_filename) as f:
    data = json.load(f)
    for k, v in data.items():
        #  print(k, v)  # debug display 
        json_copy[k] = v

with open('backup.json', 'w') as f:
    json.dump(data, f, indent=2)

def write_files():
    """writes json for formatted pasting into Google sheets"""    
    with open('key_data.txt', 'w') as w:  
        # makes a new file, OVERWRITES key_data.txt if it exists!
        for k in json_copy.keys():
            w.write(k)
            w.write('\n')  # new line seperator, formatted pasting to cells
    with open('value_data.txt', 'w') as d:
        for v in json_copy.values():
            d.write(v)
            d.write('\n')

write_files()

def copy_values():
    """ copies first half of data for pasting into sheets"""
    fo = open('key_data.txt', 'r').read()
    pyperclip.copy(fo)  # copies to clipboard the contents of key_data.txt

def copy_keys():
    """copies last half of data, must run / paste copy_values first """
    # TODO: combine steps
    fo = open('value_data.txt', 'r').read()
    pyperclip.copy(fo)

copy_values()

#copy_keys   #  paste copy_values, first.
