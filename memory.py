from exceptions import *

memory = {}

def printmemory():
    print("Objects in memory:")
    i = 1
    if len(memory) != 0:
        for x in memory:
            print("\t",i," ",x)
            i +=1
    else:
        print("\tNone")

def deleteclass(num):
    try:
        if num <= len(memory):
            del list(memory)[num-1]
            del memory[list(memory)[num-1]]
        else:
            raise IndexTooBigException("Index is bigger then number of items")
    except IndexTooBigException as e:
            print("Error: ",e) 

def wipememory():
    global memory
    for x in list(memory):
        del x
    memory = {}
    print("Memory wiped")

def remember(functions):
    def save_args(*args):
        #print("args >> ", args)
        try:
            if args[1:] in memory.values():
                raise ClassExistException("Class already exist")
            else:
                memory[args[0]] = args[1:]
                #print("memory >> ", memory)
                functions(*args)
        except ClassExistException as e:
            print("Error: ",e)     

    return save_args    