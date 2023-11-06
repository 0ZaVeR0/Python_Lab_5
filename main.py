from cube import Cube
from memory import printmemory,deleteclass,wipememory
from saveload import save, load
from exceptions import *


running = True
while running:
    #print menu
    print("\n--Hi^_^----------------------------------\n\
    1. Create cube\n\
    2. Print info about all objects\n\
    3. Delete object\n\
    4. Wipe memory\n\
    5. Save memory to file\n\
    6. Load memory from file\n\
    7. Close program\n\
----------------------------------ZaVeR--")

    print(">> ", end="")
    nav = int(input())
    try:
        match nav:
            case 1:
                #create
                print("Input size >> ", end="")
                a = input()
                try:
                    if int(a) >= 0:
                        Cube(int(a))
                    else:
                        raise IncorrectSizeException("Size should be >= 0")
                except ValueError:
                    print("Error: Size should be a number")
                except IncorrectSizeException as e:
                    print("Error: ",e)

            case 2:
                #info
                printmemory()
            case 3:
                #delete
                printmemory()
                print("Who should be destroyed? >> ", end="")
                b = input()
                try:
                    if int(b) >= 1:
                        deleteclass(int(b))
                    else:
                        raise IncorrectDeletionIndexException("Index should be >= 1")
                except ValueError:
                    print("Error: Index should be a number")
                except IncorrectDeletionIndexException as e:
                    print("Error: ",e)
            case 4:
                wipememory()
            case 5:
                #save
                save()
            case 6:
                #load
                load()
                printmemory()
            case 7:
                #close
                running = False
            case _:
                #err
                raise IncorrectMenuIndexException("Unknown menu key")
    except IncorrectMenuIndexException as e:
        print("Error: ",e)
        
print("Bye!")
