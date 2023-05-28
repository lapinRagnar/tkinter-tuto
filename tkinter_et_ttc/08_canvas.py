import tkinter as tk
from tkinter import ttk
# setup
window = tk.Tk()
window.title('canvas')
window.geometry('600x400')

# canvas
canvas = tk.Canvas(window, bg='#42ab66')
canvas.pack()

canvas.create_rectangle((54, 65, 200, 200), fill="green") 
canvas.create_line((300, 10, 100, 100))
canvas.create_text((200, 30), text='ceci est un texte', fill='red', font=('Helvetica','30','bold'))
canvas.create_window((150, 230), height=50,window=ttk.Label(window, text="mon texte avec create windows et ttk"))

# run
window.mainloop()