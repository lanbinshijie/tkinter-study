import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    lb_output_string.set(km_output)

# Create Window
window = ttk.Window(themename='journal')
window.title("Demo")
window.geometry("300x150")

# Title
lb_title = ttk.Label(window, text='Miles to kilometers', font='Calibri 24 bold')
lb_title.pack()

# Input field
fr_input = ttk.Frame(window)
entry_int = tk.IntVar()
entry = ttk.Entry(fr_input, textvariable=entry_int)
btn = ttk.Button(fr_input, text='Convert', command=convert)
entry.pack(side='left', padx=8)
btn.pack(side='left')
fr_input.pack(pady=10)

# Output
lb_output_string = tk.StringVar()
lb_output = ttk.Label(
    window, 
    text='Output', 
    font='Calibri 24', 
    textvariable=lb_output_string)
lb_output.pack()

# Run
window.mainloop()