from app.models.calculate import Status, Operation, Calculate
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
    calc = Calculate(4, 2, Operation.MULT)
    assert calc.x == 4
    assert calc.y == 2
    assert calc.operation == Operation.MULT
    assert calc.result == 8

    assert Calculate(0, 2, Operation.MULT).result == 0

def test_calculate_division():
    calc = Calculate(4, 2, Operation.DIV)
    assert calc.x == 4
    assert calc.y == 2
    assert calc.operation == Operation.DIV
    assert calc.result == 2

    assert Calculate(5, 2, Operation.DIV).result == 2.5
    assert Calculate(0, 4, Operation.DIV).result == 0
    with pytest.raises(ZeroDivisionError):
        Calculate(4, 0, Operation.DIV).result

def test_calculate_incomplete():
    calc = Calculate()
    assert calc.x is None
    assert calc.y is None
    assert calc.operation is None
    assert calc.result is None

    assert calc.status == Status.EMPTY

def test_calculate_with_x():
    calc = Calculate(1)
    assert calc.x == 1
    assert calc.y is None
    assert calc.operation is None
    assert calc.result is None

    assert calc.status == Status.PARTIAL

def test_calculate_with_operation():
    calc = Calculate(1, operation=Operation.ADD)
    assert calc.x == 1
    assert calc.y is None
    assert calc.operation is Operation.ADD
    assert calc.result is None

    assert calc.status == Status.PENDING

def test_calculate_complete():
    calc = Calculate(1, 2, Operation.ADD)
    assert calc.x == 1
    assert calc.y == 2
    assert calc.operation is Operation.ADD

    assert calc.status == Status.COMPLETE

    assert calc.result == 3
    assert calc.status == Status.FINISHED