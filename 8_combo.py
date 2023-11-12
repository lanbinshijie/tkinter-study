import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
window.title('Combo')
window.geometry('600x400')


# Widgets
items = ('Ice cream', 'Pizza', 'Broccoli')
food_stringVar = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_stringVar)
# combo['values'] = items
combo.config(values=items)
combo.pack()

combo.bind('<<ComboboxSelected>>', lambda e: combo_label.config(text=f'Selected value: {food_stringVar.get()}'))


combo_label = ttk.Label(window, text='A Label')
combo_label.pack()

# Run
window.mainloop()