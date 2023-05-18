import tkinter as tk
from tkinter import ttk

def on_button_click():
  print('button clicked!')
  print('afficher la valeur du radio button dans la console :', print(radio_var.get()))

# window
window = tk.Tk()
window.title('the buttons')
window.geometry('600x400')

# variables
button_string = tk.StringVar(value='a button with sstringVar')

# buttons
button = ttk.Button(window, text='a simple button', command=on_button_click, textvariable=button_string)
button.pack()

# checkbutton
check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(
  window, 
  text='mon checkbox 1', 
  command=lambda: print(check_var.get()),
  variable=check_var,
  onvalue=10,
  offvalue=5
)
check.pack()

# radio button
radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(
  window, 
  text='radio button 1', 
  value='quelque chose',
  variable=radio_var, 
  command=lambda: print(radio_var.get())
)
radio1.pack()

radio2 = ttk.Radiobutton(
  window, 
  text='radio button 2', 
  value=2, 
  variable=radio_var,
  command=lambda: print(radio_var.get())

)
radio2.pack()

# run
window.mainloop()