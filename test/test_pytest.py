import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculator import fun1, fun2, fun3, fun4

def test_fun1():
    assert fun1(2, 3) == 5
    assert fun1(-1, 1) == 0
    assert fun1(0, 0) == 0

def test_fun2():
    assert fun2(5, 3) == 2
    assert fun2(10, 5) == 5
    assert fun2(3, 3) == 0

def test_fun3():
    assert fun3(2, 3) == 6
    assert fun3(4, 5) == 20
    assert fun3(0, 10) == 0

def test_fun4():
    assert fun4(2, 3) == 10  # (2+3) + (2-3) + (2*3) = 5 + (-1) + 6 = 10
    assert fun4(5, 5) == 35  # (5+5) + (5-5) + (5*5) = 10 + 0 + 25 = 35
