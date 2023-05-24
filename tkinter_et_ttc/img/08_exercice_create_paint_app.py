import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('exercice canvas - create a basic paint app')
window.geometry('600x400')

# canvas
canvas = tk.Canvas(window, bg='#42ab66')
canvas.pack()

def draw_on_canvas(event):
  x = event.x
  y = event.y
  canvas.create_oval((x - brush_size/2, y - brush_size/2, x + brush_size/2, y + brush_size/2 ), fill='green')
  
brush_size = 4
canvas.bind('<B1-Motion>', draw_on_canvas)



# run
window.mainloop()