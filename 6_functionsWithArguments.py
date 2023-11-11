import tkinter as tk
from tkinter import ttk

def button_func(entry_str):
    print('A button pressed')
    print(entry_str.get())

def oF(parameter):
    def iF():
        print('ABP')
        print(parameter.get())
    return iF


# Setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')


# Widgets
entry_string = tk.StringVar(value='test')
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text='Button', command=lambda: button_func(entry_string))
button.pack()


# Run
window.mainloop()