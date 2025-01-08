import tkinter as tk
from app.views.view import Calculator

def get_click(btn_text:str):
    calc.display.show(btn_text)

root = tk.Tk()
root.title('roman calculator')
root.pack_propagate(True)
root.config(padx=10, pady=10)

calc = Calculator(root, get_click)
calc.pack()

root.mainloop()