import pytest
from main import MathOperations

@pytest.mark.parametrize("a, b, expected", [(10, 5, 15), (2.5, 3.5, 6.0)])
def test_add(a, b, expected):
    assert MathOperations.add(a, b) == expected


