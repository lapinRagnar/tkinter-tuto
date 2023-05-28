import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('400x600+500+100')
window.title('pack in detail')
window.bind('<Escape>', lambda event: window.quit() )

# widgets
label1 = ttk.Label(master=window, text='First label', background='#274f8f')
label2 = ttk.Label(master=window, text='label 2', background='#a1817a')
label3 = ttk.Label(master=window, text='last of the label', background='#07ded7')
button = ttk.Button(window, text='button')

# layout
label1.pack(side='top', fill='both', expand=True, padx=10, pady=10)
label2.pack(side='left', expand=True, fill='both')
label3.pack(side='top', expand=True, fill='both')
button.pack(side='top', fill='both', expand=True)


# run
window.mainloop()