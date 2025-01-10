from enum import Enum

class Status(Enum):
    EMPTY = 0
    PARTIAL = 1
    PENDING = 2
    COMPLETE = 3
    FINISHED = 4

class Operation(Enum):
    ADD = (lambda x, y: x + y, '+')
    SUB = (lambda x, y: x - y, '-')
    MULT = (lambda x, y: x * y, '*')
    DIV = (lambda x, y: x // y, '/')
    MOD = (lambda x, y: x % y, '%')

    def __init__(self, operation, symbol=None):
        self.op = operation
        self.symbol = symbol

    def calculate(self, x:int, y:int):
        return self.op(x, y)
    
class Calculate():
    def __init__(self, x=None, y=None, operation:Operation=None):
        self.x = x
        self.y = y
        self.operation = operation
        self.__is_finished = False

    @property
    def result(self):
        result = None

        if self.operation is not None:
            if self.x is not None and self.y is not None:
                self.__is_finished = True
                result = self.operation.calculate(self.x, self.y)

        return result
        
    @property
    def status(self):
        status = None

        if self.x is None:
            status = Status.EMPTY
        elif self.operation is None:
            status = Status.PARTIAL
        elif self.y is None:
            status = Status.PENDING
        elif not self.__is_finished:
            status = Status.COMPLETE
        else:
            status = Status.FINISHED

        return status
