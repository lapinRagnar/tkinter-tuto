import tkinter as tk
from tkinter import ttk

def on_button_click():
  print(f"la valeur de la variable StringVar est : {string_var.get()} ")
  string_var.set('on a appuyé sur le bouton')

# window
window = tk.Tk()
window.title('tkinter variables')

# tkinter variable
string_var = tk.StringVar(value='valeur au debut')

# widgets
label = ttk.Label(master=window, text='mon label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='mon bouton', command=on_button_click)
button.pack()

# run
window.mainloop()

