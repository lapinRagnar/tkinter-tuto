import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('basic of grid layouot')
window.geometry('600x400')
window.bind('<Escape>', lambda event: window.quit())

# widgets
label1 = ttk.Label(window, text='label 1', background='red')
label2 = ttk.Label(window, text='label 2', background='blue')
label3 = ttk.Label(window, text='label 3', background='green')
label4 = ttk.Label(window, text='label 4', background='yellow')
button1 = ttk.Button(window, text='button 1')
button2 = ttk.Button(window, text='button 2')
entry = ttk.Entry(window)

# define the grid
window.columnconfigure((0,1,2), weight=1, uniform='a')
window.columnconfigure(3, weight=2, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')
window.rowconfigure(1, weight=1, uniform='a')
window.rowconfigure(2, weight=1, uniform='a')
window.rowconfigure(3, weight=1, uniform='a')

# place a widget
label1.grid(row=0, column=0, sticky='nesw')
label2.grid(row=1, column=1, rowspan=3, sticky='nsew')
label3.grid(row=1, column=0, sticky='nesw', columnspan=3, padx=20, pady=10)
label4.grid(row=3, column=3, sticky='se')

# exercice
button1.grid(row=0, column=3, columnspan=3, sticky='nsew')
button2.grid(row=2, column=2, sticky='nsew')
entry.grid(row=3, column=3, sticky='n')

# run
window.mainloop()