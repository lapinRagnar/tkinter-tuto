import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x200')
window.title('combo and spin')

# combobox
items = ('ice cream', 'pizza', 'broccoli')
food_string = tk.StringVar(value=items[0])

combo = ttk.Combobox(window, textvariable=food_string)
combo['values'] = items
# combo.config(values=items)
combo.pack()

# events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text=f'Selected value: {food_string.get()}'))

# combo_label = ttk.Label(window, text='a label', textvariable=food_string)
combo_label = ttk.Label(window, text='a label', textvariable=food_string)
combo_label.pack()


# Spinbox
spin_int = tk.IntVar(value=5649)
spin = ttk.Spinbox(
  window, 
  from_=5644, 
  to=5655, 
  increment=5, 
  command=lambda: print(f'la valeur selectionné {spin_int.get()}'), 
  textvariable=spin_int
)
# spin['values'] = (1454, 25451, 8454, 70, 4512)

spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))

spin.pack()


# exercice
exercice_letters = ('A', 'B', 'C', 'D', 'E', 'F') 
exercice_string = tk.StringVar(value=exercice_letters[0])
exercice_spin = ttk.Spinbox(window, textvariable=exercice_string)
exercice_spin['values'] = exercice_letters
exercice_spin.pack()

exercice_spin.bind('<<Decrement>>', lambda event: print(exercice_string.get()) )

# run
window.mainloop()