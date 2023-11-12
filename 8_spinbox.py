import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
window.title('Combo')
window.geometry('600x400')


# Widgets
# si = tk.IntVar(value=12)
si = tk.StringVar(value='A')
spin = ttk.Spinbox(window, from_=3, to=20, increment=3, command=lambda: print('Pressed'), textvariable=si)
spin['values'] = ['A', 'B','C','D','E']
spin.pack()
spin.bind('<<Increment>>', lambda e: print('Up'))
spin.bind('<<Decrement>>', lambda e: print('Down'))

# Run
window.mainloop()