from enum import Enum

class Operation(Enum):
    ADD = lambda x, y: x + y
    SUB = lambda x, y: x - y
    MUL = lambda x, y: x * y
    DIV = lambda x, y: x / y

class Calculate():
    def __init__(self, x:int, y:int, operation:Operation):
        self.x = x
        self.y = y
        self.operation = operation
        self.result = self.operation(x, y)