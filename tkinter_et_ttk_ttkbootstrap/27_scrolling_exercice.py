import tkinter as tk
from tkinter import ttk
from random import randint, choice

# setup
window = tk.Tk()
window.title('scrolling with canvas')
window.geometry('600x400')
window.bind('<Escape>', lambda e: window.quit())

# canvas 
canvas = tk.Canvas(window, bg='white', scrollregion=(0, 0, 2000, 5000))
canvas.create_line(0, 0, 2000, 5000, fill='green', width=10)
for i in range(100):
  l = randint(0, 2000)
  t = randint(0, 5000)
  r = l + randint(10, 500)
  b = t + randint(10, 500)
  color = choice(('red', 'green', 'blue', 'purple', 'yellow', 'orange', 'black', 'pink'))
  canvas.create_rectangle(l, t, r, b, fill=color)
canvas.pack()

# scroll bar 
scrollbar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

# mousewheel scroling
canvas.bind('<MouseWheel>', lambda e: canvas.yview_scroll(int(e.delta/60), 'units'))

# exercice scrollbar horizontal
scrollbar_botton = ttk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_botton.set)
scrollbar_botton.place(relx=0, rely=1, relwidth=1, anchor='sw')

# add an event to scroll left/right and ctrl + mousewheel
canvas.bind('<ControlMouse>', lambda e: canvas.xview_scroll(int(e.delta/60), 'units'))



# run window
window.mainloop()
