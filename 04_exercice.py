import tkinter as tk
from tkinter import ttk

# window
window= tk.Tk()

# function
def radio_func():
  print(check_bool.get())
  check_bool.set(False)

# data
radio_var = tk.StringVar()
check_bool = tk.BooleanVar()

# widgets
radio1 = ttk.Radiobutton(
  window,
  text='radio 1',
  value='A',
  variable=radio_var,
  command=radio_func
)

radio2 = ttk.Radiobutton(
  window,
  text='radio 2',
  value='B',
  variable=radio_var,
  command=radio_func
)

# check button

check = ttk.Checkbutton(
  window,
  text='afficher la valeur du bouton radio ci-dessus',
  variable=check_bool,
  command=lambda: print(radio_var.get())
)

# layout
radio1.pack()
radio2.pack()
check.pack()

# run
window.mainloop()

