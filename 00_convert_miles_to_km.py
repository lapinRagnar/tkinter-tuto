import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk                # you need to install it with - pip install ttkbootstrap

def convert():
  mile_input = entry_int.get()
  km_output = mile_input * 1.61
  output_string.set(km_output)

# window
window = ttk.Window(themename='journal')
window.title('demo')
window.geometry('350x250')

# title
title_label = ttk.Label(master=window, text='Miles to kilometers', font='Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
  master=window, 
  text='output', 
  font='Calibri 24 bold', 
  textvariable=output_string
)
output_label.pack(pady=5)



# run
window.mainloop()