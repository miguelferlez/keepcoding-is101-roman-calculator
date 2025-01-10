import tkinter as tk
from app.views.view import Calculator, ButtonTypes
from app.models.calculate import Calculate, Status, Operation
from app.models.roman_number import RomanNumber, RomanNumberError

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('roman calculator')
        self.pack_propagate(True)
        self.config(padx=10, pady=10)

        self.calc = Calculator(self, self.handle_click)
        self.calc.pack()

        self.calculate = Calculate()

    def handle_click(self, button_text:str):
        if button_text in self.calc.keyboard.btn_types[ButtonTypes.DIGITS]:
            try:
                #click first roman number
                if self.calculate.status == Status.EMPTY:
                    self.calculate.x = RomanNumber(button_text)
                    self.calc.display.show(self.calculate.x)
                elif self.calculate.status == Status.PARTIAL:
                    roman_number = f'{self.calculate.x}{button_text}'
                    self.calculate.x = RomanNumber(roman_number)
                    self.calc.display.show(self.calculate.x)
                #click second roman number
                elif self.calculate.status == Status.PENDING:
                    self.calculate.y = RomanNumber(button_text)
                    self.calc.display.show(self.calculate.y)
                elif self.calculate.status == Status.COMPLETE:
                    roman_number = f'{self.calculate.y}{button_text}'
                    self.calculate.y = RomanNumber(roman_number)
                    self.calc.display.show(self.calculate.y)
            except RomanNumberError:
                pass
        #click operation
        elif button_text in self.calc.keyboard.btn_types[ButtonTypes.OPERATIONS]:
            if self.calculate.status == Status.PARTIAL:
                self.calculate.operation = self.get_operation(button_text)
        #click equal
        elif button_text in self.calc.keyboard.btn_types[ButtonTypes.EQUAL]:
            operation_result = None
            if self.calculate.status == Status.COMPLETE:
                if self.calculate.operation == Operation.SUB and self.calculate.x < self.calculate.y:
                    operation_result = None
                    self.calc.display.show('ERROR')
                elif self.calculate.operation == Operation.DIV and self.calculate.result < 1:
                    operation_result = None
                    self.calc.display.show('ERROR')
                else:
                    operation_result = self.calculate.result
                    self.calc.display.show(operation_result)
            self.calculate = Calculate()
            self.calculate.x = operation_result
        #click reset
        elif button_text in self.calc.keyboard.btn_types[ButtonTypes.RESET]:
            self.calc.display.show('')
            self.calculate = Calculate()

    def get_operation(self, symbol:str):
        for op in Operation:
            if op.value[1] == symbol:
                return op
        return None
    
    def run(self):
        self.mainloop()
