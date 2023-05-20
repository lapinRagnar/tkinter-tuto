import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
window = tk.Tk()
window.title('scrolled text')

# # slider
# scale_float = tk.IntVar(value=15)
# scale = ttk.Scale(
#   window, 
#   command=lambda e: print(scale_float.get()), 
#   from_=0, 
#   to=25,
#   length=200,
#   orient='vertical',
#   variable=scale_float
# )
# scale.pack()

# # progress bar
# progress = ttk.Progressbar(
#   window, 
#   variable=scale_float, 
#   maximum=25,
#   length=200,
# )
# progress.pack()

exercice_int = tk.IntVar()
exercice_progress = ttk.Progressbar(window, orient='vertical', variable=exercice_int)
exercice_progress.pack()
exercice_progress.start()

# scrolledtext
scrolled_text = scrolledtext.ScrolledText(window, width=50, height=5)
scrolled_text.pack()

label = ttk.Label(window, textvariable=exercice_int)

exercice_scale = ttk.Scale(window, variable=exercice_int, from_=0, to=50)
exercice_scale.pack()

# run
window.mainloop()
