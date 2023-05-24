import tkinter as tk
from tkinter import ttk
# import pprint

def button_func():
  # get the content of the entry
  entry_text = entry.get()
  
  # update the label
  # label.config(text='I change the text label with this text')  # ou label.configure(text='text.....') ou
  label['text'] = entry_text
  
  entry['state'] = 'disabled'
  
  # how to get the parameters of labels
  # pprint.pprint(label.configure())

def button_func_2():
  entry['state'] = 'enabled'
  label['text'] = "Mon label"
  
  


# window
window = tk.Tk()
window.title('getting and setting widgets')

# widgets
label = ttk.Label(master=window, text='mon label')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='mon bouton', command=button_func)
button.pack()

button_2 = ttk.Button(master=window, text='another button', command=button_func_2)
button_2.pack()

# run
window.mainloop()
