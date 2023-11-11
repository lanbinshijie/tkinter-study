import tkinter as tk
from tkinter import ttk


def button_func():
    # print(entry.get())

    # Update Label
    # label.config(text="some Other TeXT")
    # label['text'] = entry.get()
    entry['state'] = 'disabled'
    # print(label.configure())

def enable():
    entry['state'] = 'enable'



# Window
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry("250x160")

# Widgets
label = ttk.Label(window, text='Some Text')
label.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='The Button', command=button_func)
button.pack()

exercise = ttk.Button(window, text='unlock', command=enable)
exercise.pack()


# Run
window.mainloop()