import tkinter as tk
from tkinter import ttk

def on_button_click(entry_string):
  print('bouton pressed')
  print(entry_string.get())

# setup
window = tk.Tk()
window.title('button, function with argument')

# widget
entry_string = tk.StringVar(value='test')
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text='mon bouton', command=lambda: on_button_click(entry_string))
button.pack()




# run
window.mainloop()