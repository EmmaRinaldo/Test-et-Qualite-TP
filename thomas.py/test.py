from main import MathOperations
import pytest

@pytest.mark.parametrize("a,b,ab",[
    (11,2,13),
    (-5,-2,-7),
    (0,0,0),
    (0,5,5),
    (5,0,5),
    (3.5,2.5,6),
    (-3.5,-2.5,-6),
    (-3.5,2.5,-1),
    (3.5,-2.5,1),
    ('a','b','ab')
])	
def test_addition(a, b, ab):
    assert MathOperations.addition(a,b) == ab

@pytest.mark.parametrize("a,b,ab",[
    (11,2,9),
    (-5,-2,-3),
    (0,0,0),
    (0,5,-5),
    (5,0,5),
    (3.5,2.5,1),
    (2.5,3.5,-1),
    (-3.5,-2.5,-1),
    (-2.5,-3.5,1),
    ('a','b','ab')
])	
def test_soustraction(a, b, ab):
    assert MathOperations.soustraction(a,b) == ab

@pytest.mark.parametrize("a,b,ab",[
    (11,2,22),
    (-5,-2,10),
    (0,0,0),
    (0,5,0),
    (5,0,0),
    (3.5,2.5,8.75),
    (2.5,3.5,8.75),
    (-3.5,-2.5,8.75),
    (-2.5,-3.5,8.75),
    ('a','b','ab')
])
def test_multiplication(a, b, ab):
    assert MathOperations.multiplication(a,b) == ab

@pytest.mark.parametrize("a,b,ab",[
    (11,2,5.5),
    (-5,-2,2.5),
    (0,5,0),
    (5,0,ValueError),
    (3.5,2.5,1.4),
    (2.5,3.5,0.7142857142857143),
    (-3.5,-2.5,1.4),
    (-2.5,-3.5,0.7142857142857143),
    ('a','b','ab')
])
def test_division(a, b, ab):
    assert MathOperations.division(a,b) == ab

@pytest.mark.parametrize("a,b,ab",[
    (11,2,121),
    (-5,-2,0.04),
    (0,0,1),
    (0,5,0),
    (5,0,1),
    (1.5,2.5,2.7556759606310752),
    (-2,0.5,ValueError),
    ('a','b','ab')
])
def test_puissance(a, b, ab):
    assert MathOperations.puissance(a, b) == ab

@pytest.mark.parametrize("a,b,ab",[
    (11,2,1),
    (-5,-2,-1),
    (0,0,0),
    (0,5,0),
    (5,0,ValueError),
    (3.5,2.5,1),
    (2.5,3.5,2.5),
    (-3.5,-2.5,-1),
    (-2.5,-3.5,-2.5),
    ('a','b','ab')
])
def test_modulo(a, b, ab):
    assert MathOperations.modulo(a,b) == ab