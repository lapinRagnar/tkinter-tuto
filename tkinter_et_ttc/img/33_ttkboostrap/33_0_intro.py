import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# window
window = ttk.Window(themename='darkly')
window.title('ttkbootstrap')
window.geometry('800x600')

label = ttk.Label(window, text='a label', font=('', 60))
label.pack()

button1 = ttk.Button(window, text='Button 1', bootstyle=SUCCESS)
button1.pack(pady=10, side=LEFT, expand=True)

button2 = ttk.Button(window, text='Button 2', bootstyle=WARNING)
button2.pack(pady=10, side=LEFT, expand=True)

button3 = ttk.Button(window, text='Button 3', bootstyle=DANGER)
button3.pack(pady=10, side=LEFT, expand=True)




# run
window.mainloop()

