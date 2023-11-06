from exceptions import *

class Shape3d:
    def __init__(self, width: int, height: int, depth: int):
        try:
            if self.is_correct_size(width):
                self.__width = width
            else:
                raise IncorrectSizeException("Incorrect width")
        except IncorrectSizeException as e:
            print("Error: ",e)

        try:
            if self.is_correct_size(height):
                self.__height = height
            else:
                raise IncorrectSizeException("Incorrect height")
        except IncorrectSizeException as e:
            print("Error: ",e)
        
        try:
            if self.is_correct_size(depth):
                self.__depth = depth
            else:
                raise IncorrectSizeException("Incorrect depth")
        except IncorrectSizeException as e:
            print("Error: ",e)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        try:
            if self.is_correct_size(width):
                self.__width = width
            else:
                raise IncorrectSizeException("Incorrect width")
        except IncorrectSizeException as e:
            print("Error: ",e)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        try:
            if self.is_correct_size(height):
                self.__height = height
            else:
                raise IncorrectSizeException("Incorrect height")
        except IncorrectSizeException as e:
            print("Error: ",e)

    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, depth: int):
        try:
            if self.is_correct_size(depth):
                self.__depth = depth
            else:
                raise IncorrectSizeException("Incorrect depth")
        except IncorrectSizeException as e:
            print("Error: ",e)

    def is_correct_size(self, size: int) -> bool:
        return isinstance(size, int) and size >= 0
    
    def volume(self)-> int:
        return (self.width * self.height * self.depth)
