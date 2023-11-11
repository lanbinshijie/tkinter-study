import tkinter as tk
from tkinter import ttk


# Setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# Button
def button_func():
    print("A basic button")

button_string = tk.StringVar(value="A button with string var")
button = ttk.Button(window, text='A simple button', command=button_func, textvariable=button_string)
button.pack()

# CheckButton
check_var = tk.BooleanVar()
check = ttk.Checkbutton(
    window, 
    text='checkbox1', 
    command=lambda: print(check_var.get()),
    variable=check_var,
    onvalue=True,
    offvalue=False)
check.pack()

# RadioButtons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, text='RadioButton1', value='radio1', variable=radio_var, command=lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, text='RadioButton2', value='radio2', variable=radio_var, command=lambda: print(radio_var.get()))
radio2.pack()


# Run
window.mainloop()