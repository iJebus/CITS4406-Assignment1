import mock
from project1 import *


def test_getInputs():
    with mock.patch('builtins.input', return_value=(5, 5, 10)):
        assert getInputs() == (5, 5, 10)


def test_gcd():
    assert gcd(24, 16) == 8


def test_getNumberOfPoints():
    assert getNumberOfPoints(5, 3, 360) == 1080