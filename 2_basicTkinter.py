import tkinter as tk
from tkinter import ttk


def button_func():
    print("The button is pressed")

# Create Window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# Create Widgets
textArea = tk.Text(window)
textArea.pack()

label = ttk.Label(window, text='This is a test')
label.pack()

entry = ttk.Entry(window)
entry.pack()

label2 = ttk.Label(window, text='my label')
label2.pack()

button = ttk.Button(window, text='A button', command=button_func)
button.pack()

# Run
window.mainloop()