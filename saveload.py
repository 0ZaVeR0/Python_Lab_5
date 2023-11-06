from memory import memory
import os
from cube import Cube

def save():
    if not os.path.exists("save"):
        os.mkdir("save")
    try:
        with open("save/memory.bin", "wb") as f:
           for x in memory.values():
                line = str()
                for y in x:
                   line = line + str(y) + " "
                line += '\n'
                f.write(line.encode('ascii'))                 
    except IOError:
        print("Error: File failed to open while saving memory")
        return None
    print("Status: memory saving >> Success!")

def load():
    try:
        with open("save/memory.bin", "rb") as f:
            file = f.read().split(b" \n")
            file.pop(-1)
            file = [x.decode() for x in file]
            for param in file:
                Cube(int(param))
    except IOError:
        print("Error: File failed to open while loading memory")
        return None
    print("Status: memory loading >> Success!")

