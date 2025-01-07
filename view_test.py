import tkinter as tk
from app.views.view import CalcButton, KeyBoard

def get_click(btn_text:str):
    print(btn_text)

root = tk.Tk()
root.pack_propagate(True)

# btn1 = CalcButton(root, 'btn1', lambda : print('btn1'))
# btn1.pack()

# btn2 = CalcButton(root, 'btn2', lambda : print('btn2'))
# btn2.pack()

kb = KeyBoard(root, get_click)
kb.pack()

root.mainloop()