import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('stacking order')
window.geometry('400x400')
window.bind('<Escape>', lambda e: window.quit())

# widgets ----- the order of the stack depends here - the last label is in top of the screen
label1 = ttk.Label(window, text='label 1', background='green')
label2 = ttk.Label(window, text='label 2', background='red')
label3 = ttk.Label(window, text='label 3', background='black')

# to control the order we have 2 methods - lift() lower()
# label1.lift()
# label2.lower()

button1 = ttk.Button(window, text='raise label 1', command=lambda: label1.tkraise())
button2 = ttk.Button(window, text='raise label 2', command=lambda: label2.tkraise())
button3 = ttk.Button(window, text='raise label 3', command=lambda: label3.tkraise())

# layout
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)
label3.place(x=100, y=120, width=240, height=100)

button1.place(relx=0.8, rely=1, anchor='se')
button2.place(relx=1, rely=1, anchor='se')
button3.place(relx=0.6, rely=1, anchor='se')

# run
window.mainloop()