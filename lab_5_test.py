from cube import Cube
from memory import printmemory,deleteclass,wipememory
from saveload import save, load
from exceptions import *

import pytest

@pytest.fixture()
def basic_savefile():
    wipememory()
    Cube(5)
    Cube(10)
    Cube(1)
    save()
    wipememory()

@pytest.fixture
def default():
    wipememory()
    save()

def test_class_exist(default):
    assert Cube(5)
    assert Cube(2)
    assert Cube(5),(ClassExistException)

def test_incorrect_size(default):
    assert Cube(1)
    assert Cube(-1),(IncorrectSizeException)
