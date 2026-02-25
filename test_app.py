# test_app.py
import pytest
from app import add, subtract, multiply, greet

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(5, 0) == 0

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("World") == "Hello, World!"