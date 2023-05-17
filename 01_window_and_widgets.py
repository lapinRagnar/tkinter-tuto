import tkinter as tk
from tkinter import ttk

def button_func():
  print('salut')

# create window
window = tk.Tk()
window.title('window and widgets')
window.geometry('800x500')

# widgets
# ttk label
label = ttk.Label(master=window, text='this is a test')
label.pack()

# tk text
text = tk.Text(master=window)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk button
button = ttk.Button(master=window, text='a button', command=button_func)
button.pack()

# run
window.mainloop()

