import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()

# slider
scale_float = tk.IntVar(value=15)
scale = ttk.Scale(
  window, 
  command=lambda e: print(scale_float.get()), 
  from_=0, 
  to=25,
  length=200,
  orient='vertical',
  variable=scale_float
)
scale.pack()

# progress bar
progress = ttk.Progressbar(
  window, 
  variable=scale_float, 
  maximum=25,
  length=200,
)
progress.pack()




# run
window.mainloop()
