import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('layout - place')
window.geometry('400x600')
window.bind('<Escape>', lambda e: window.quit())

# widgets
label1 = ttk.Label(window, text='label 1', background='red')
label2 = ttk.Label(window, text='label 2', background='blue')
label3 = ttk.Label(window, text='label 3', background='green')
button1 = ttk.Button(window, text='buttom 1')
label_exercice = ttk.Label(window, text='label exercice', background='purple')

# layouts
label1.place(x=100, y=200, width=300, height=50)
label2.place(relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5)
label3.place(x=80, y=60, width=160, height=300)
button1.place(relx=1, rely=1, anchor='se')

# frame
frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text='frame label', background='yellow')
frame_button = ttk.Button(frame, text='frame button')

# frame layout
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_button.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# exercice layout
label_exercice.place(relx=0.5, rely=0.5, relwidth=0.2, height=200, anchor='center')


# run
window.mainloop()