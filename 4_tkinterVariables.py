import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

window = tk.Tk()
window.title('Tkinter Variables')

string_var = tk.StringVar(value="StartValue")

label = ttk.Label(window, text='label', textvariable=string_var)
label.pack()

entry = ttk.Entry(window, textvariable=string_var)
entry.pack()

button = ttk.Button(window, text="Button", command=button_func)
button.pack()


window.mainloop()
