import tkinter as tk
from tkinter.font import Font
from typing import Callable
from enum import Enum

BUTTON_WIDTH = 90
BUTTON_HEIGHT = 50

class ButtonTypes(Enum):
    RESET = 0
    EQUAL = 1
    OPERATIONS = 2
    DIGITS = 3

class CalcButton(tk.Frame):
    def __init__(self, parent:object, text:str, command:Callable, background:str=None):
        super().__init__(parent, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        self.text = text
        self.command = command

        self.pack_propagate(False)
        btn_font = Font(size=14)
        btn = tk.Button(self, text=text, font=btn_font, command=self.get_text, background=background)
        btn.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    def get_text(self):
        self.command(self.text)

class KeyBoard(tk.Frame):
    btn_text = (
            'clear', '%',    '/', 
            'I',     'V',    '*', 
            'X',     'L',    '-', 
            'C',     'D',    '+', 
            'M',     '•',    '=')
    btn_types = {
        ButtonTypes.RESET: ['clear'],
        ButtonTypes.EQUAL: ['='],
        ButtonTypes.OPERATIONS: ['%', '/', '*', '-', '+'],
        ButtonTypes.DIGITS: ['I', 'V', 'X', 'L', 'C', 'D', 'M', '•']
    }
    def __init__(self, parent:object, command:Callable):
        super().__init__(parent, width=3*BUTTON_WIDTH, height=5*BUTTON_HEIGHT)
        self.grid_propagate(False)

        index = 0
        
        for row in range(5):
            for col in range(3):
                if row == 0 or col == 2:
                    btn = CalcButton(self, self.btn_text[index], command=command, background='#c2c2c2')
                else:
                    btn = CalcButton(self, self.btn_text[index], command=command)
                btn.grid(column=col, row=row)
                index += 1

class Display(tk.Frame):
    def __init__(self, parent:object, text:str=''):
        super().__init__(parent, width=3*BUTTON_WIDTH, height=BUTTON_HEIGHT)
        self.text = text
        
        self.pack_propagate(False)
        lb_font = Font(size=20)
        self.lb = tk.Label(self, text=text, background='#1f1f1f', foreground='white', font=lb_font, anchor=tk.E, padx=10)
        self.lb.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    def show(self, value:str):
        self.lb.config(text=value)

class Calculator(tk.Frame):
    def __init__(self, parent:object, command:Callable):
        super().__init__(parent)

        self.display = Display(self)
        self.display.pack()

        self.keyboard = KeyBoard(self, command)
        self.keyboard.pack()



