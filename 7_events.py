import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x}, y: {event.y}')


# Window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Bounding')

# Widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text="A button")
button.pack()

# Events
button.bind('<Alt-KeyPress-p>', lambda event: print('an event'))
# window.bind('<Motion>', get_pos)

window.bind('<KeyPress>', lambda x: print('pressed'))

entry.bind('<FocusIn>', lambda e: print("Entry Field is on focus"))
entry.bind('<FocusOut>', lambda e: print("Entry Field is not on focus"))

# Exercise


# Run
window.mainloop()