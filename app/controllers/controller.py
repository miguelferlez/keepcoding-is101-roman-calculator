import tkinter as tk
from app.views.view import Calculator, ButtonTypes
from app.models.calculate import Calculate, Status
from app.models.roman_number import Roman_Number, RomanNumberError

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
                if self.calculate.status == Status.EMPTY:
                    self.calculate.x = Roman_Number(button_text)
                elif self.calculate.status == Status.PARTIAL:
                    roman_number = f'{self.calculate.x}{button_text}'
                    self.calculate.x = Roman_Number(roman_number)
                self.calc.display.show(self.calculate.x)
            except RomanNumberError:
                pass
        elif button_text in self.calc.keyboard.btn_types[ButtonTypes.OPERATIONS]:
            if self.calculate.status == Status.PARTIAL:
                #self.calculate.operation = 
                #TODO self.calculate.operation
                pass

    def run(self):
        self.mainloop()
