import tkinter as tk
from app.views.view import Calculator, ButtonTypes, Record
from app.models.calculate import Calculate, Status, Operation
from app.models.roman_number import RomanNumber, RomanNumberError
from app.models.log import OperationLog, Log

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('roman calculator')
        self.pack_propagate(True)
        self.config(padx=5, pady=5)

        self.calculator_panel = Calculator(self, self.handle_click)
        self.calculator_panel.grid(row=0, column=0)
        self.record_panel = Record(self)
        self.record_panel.grid(row=0, column=1)

        self.record_panel.read_record()
        self.log = Log()
        self.log.read_record()
        last_log = self.log.get_log(-1)

        self.calculate = Calculate()
        if last_log is not None:
            self.calculate.x = last_log.op.calculate(last_log.x, last_log.y)
            self.calculator_panel.display.show(self.calculate.x)


    def handle_click(self, button_text:str):
        if button_text in self.calculator_panel.keyboard.btn_types[ButtonTypes.DIGITS]:
            try:
                if self.calculate.status == Status.EMPTY:
                    self.calculate.x = RomanNumber(button_text)
                    self.calculator_panel.display.show(self.calculate.x)
                elif self.calculate.status == Status.PARTIAL:
                    roman_number = f'{self.calculate.x}{button_text}'
                    self.calculate.x = RomanNumber(roman_number)
                    self.calculator_panel.display.show(self.calculate.x)
                elif self.calculate.status == Status.PENDING:
                    self.calculate.y = RomanNumber(button_text)
                    self.calculator_panel.display.show(self.calculate.y)
                elif self.calculate.status == Status.COMPLETE:
                    roman_number = f'{self.calculate.y}{button_text}'
                    self.calculate.y = RomanNumber(roman_number)
                    self.calculator_panel.display.show(self.calculate.y)
            except RomanNumberError:
                pass
        elif button_text in self.calculator_panel.keyboard.btn_types[ButtonTypes.OPERATIONS]:
            if self.calculate.status == Status.PARTIAL:
                self.calculate.operation = self.get_operation_by_symbol(button_text)
        elif button_text in self.calculator_panel.keyboard.btn_types[ButtonTypes.EQUAL]:
            operation_result = None
            operation_output = ''
            if self.calculate.status == Status.COMPLETE:
                if self.calculate.operation == Operation.SUB and self.calculate.x < self.calculate.y:
                    operation_result = None
                    self.calculator_panel.display.show('ERROR')
                elif self.calculate.operation == Operation.DIV and self.calculate.result < 1:
                    operation_result = None
                    self.calculator_panel.display.show('ERROR')
                else:
                    operation_result = self.calculate.result
                    operation_output = f'{self.calculate.x} {self.calculate.operation.symbol} {self.calculate.y} {button_text} {operation_result}'
                    operation_log = OperationLog(self.calculate.x, self.calculate.y, self.calculate.operation)
                    self.calculator_panel.display.show(operation_result)
                    self.set_operation(operation_output)
                    self.log.write_record(operation_log)
            self.calculate = Calculate()
            self.calculate.x = operation_result
        elif button_text in self.calculator_panel.keyboard.btn_types[ButtonTypes.RESET]:
            self.calculator_panel.display.show('')
            self.calculate = Calculate()

    def get_operation_by_symbol(self, symbol:str):
        for op in Operation:
            if op.value[1] == symbol:
                return op
        return None
    
    def set_operation(self, output:str):
        self.record_panel.txt.config(state=tk.NORMAL)
        self.record_panel.txt.insert('end', output + '\n')
        self.record_panel.txt.config(state=tk.DISABLED)

    def run(self):
        self.mainloop()
