import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('frames ans parenting')

# frame
frame = ttk.Frame(
  window,
  width=300,
  height=200,
  borderwidth=10,
  relief=tk.GROOVE  
  )
frame.pack_propagate(False)
frame.pack(side='left')                                  # frame.pack(side='left') or 'right' or 'down'   

# master setting (parenting)
label = ttk.Label(frame, text='label in frame')
label.pack()

button = ttk.Button(frame, text='button in a frame')
button.pack()

# example 2
label2 = ttk.Label(window, text='label outside frame')
label2.pack(side='left')

# exercice
exercice_frame = ttk.Frame(window)
ttk.Label(exercice_frame, text='label in frame 2').pack()
ttk.Button(exercice_frame, text='button in frame 2').pack()
ttk.Entry(exercice_frame).pack()
exercice_frame.pack(side='left')


# run
window.mainloop()