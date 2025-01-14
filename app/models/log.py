from app.models.roman_number import RomanNumber
from app.models.calculate import Operation

class OperationLog:
    def __init__(self, x:RomanNumber, y:RomanNumber, op:Operation):
        self.x = x
        self.y = y
        self.op = op

    def __str__(self):
        return f'{self.x};{self.y};{self.op.name}'
    
    def __repr__(self):
        return self.__str__()
    
class Log:
    def __init__(self):
        self.records = []

    def write_record(self, record:OperationLog):
        self.records.append(record)
        log_file = open('log.txt', 'w')
        for record in self.records:
            rec = record.__str__()
            log_file.write(rec + '\n')
        log_file.close()

    def read_record(self):
        log_file = open('log.txt', 'r')
        for line in log_file.readlines():
            self.records.append(line.strip())
        log_file.close()
    
    def get_log(self, index:int):
        log_file = open('log.txt', 'r')
        lines = log_file.readlines()
        if len(lines) > 0:
            clean_line = lines[index].strip()
            operation_log = clean_line.split(';')
            x = RomanNumber(operation_log[0])
            y = RomanNumber(operation_log[1])
            op = getattr(Operation, operation_log[2])
            log = OperationLog(x, y, op)
            return log
        return None