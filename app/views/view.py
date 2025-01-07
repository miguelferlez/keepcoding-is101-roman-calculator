import tkinter as tk
from typing import Callable

BUTTON_WIDTH = 90
BUTTON_HEIGHT = 50

class CalcButton(tk.Frame):
    def __init__(self, parent:object, text:str, command:Callable):
        super().__init__(parent, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        self.text = text
        self.command = command

        self.pack_propagate(False)
        btn = tk.Button(self, text=text, command=self.get_text)
        btn.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

    def get_text(self):
        self.command(self.text)

class KeyBoard(tk.Frame):
    def __init__(self, parent:object, command:Callable):
        super().__init__(parent, width=3*BUTTON_WIDTH, height=5*BUTTON_HEIGHT)
        self.grid_propagate(False)

        index = 0
        btn_text = (
            'CLEAR', '%',    '/', 
            'I',     'V',    '*', 
            'X',     'L',    '-', 
            'C',     'D',    '+', 
            'M',     '*',    '=')
        for row in range(5):
            for col in range(3):
                btn = CalcButton(self, btn_text[index], command=command)
                btn.grid(column=col, row=row)
                index += 1
        

