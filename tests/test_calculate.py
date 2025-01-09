from app.models.calculate import Operation, Calculate
import pytest

def test_calculate_add():
    calc = Calculate(1, 2, Operation.ADD)
    assert calc.x == 1
    assert calc.y == 2
    assert calc.operation == Operation.ADD
    assert calc.result == 3

def test_calculate_subtract():
    calc = Calculate(1, 2, Operation.SUB)
    assert calc.x == 1
    assert calc.y == 2
    assert calc.operation == Operation.SUB
    assert calc.result == -1

def test_calculate_multiplication():
    calc = Calculate(4, 2, Operation.MUL)
    assert calc.x == 4
    assert calc.y == 2
    assert calc.operation == Operation.MUL
    assert calc.result == 8

    assert Calculate(0, 2, Operation.MUL).result == 0

def test_calculate_division():
    calc = Calculate(4, 2, Operation.DIV)
    assert calc.x == 4
    assert calc.y == 2
    assert calc.operation == Operation.DIV
    assert calc.result == 2

    assert Calculate(5, 2, Operation.DIV).result == 2.5
    assert Calculate(0, 4, Operation.DIV).result == 0
    with pytest.raises(ZeroDivisionError):
        Calculate(4, 0, Operation.DIV)

