import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('sizing issue with tkinter')
window.geometry('600x400')

# widgets
label1 = ttk.Label(window, text='label 1', background='green')
label2 = ttk.Label(window, text='label 2', background='red', width=50)

# layout
label1.pack()
label2.pack(fill='x')   # with override the width=50 of label 2

# run
window.mainloop()