import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('800x600')
window.title('layout')

window.bind('<Escape>', lambda event: window.quit() )

# widgets
label1 = ttk.Label(window, text='mon label 1', background='purple')
label2 = ttk.Label(window, text='mon label 2', background='green')

# pack
# label1.pack(side='left', expand=True, fill='both')
# label2.pack(side='right', expand=True, fill='both')

# --------------------------------------------------------------------

# grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)

# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)

# label1.grid(row=0, column=1, sticky='nsew')
# label2.grid(row=1, column=1, columnspan=2, sticky='nsew')

# -------------------------------------------------------------------------------------------------

# place
label1.place(x=0, y=0, width=300, height=600)                                          # valeur absolute
label2.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='center')               # valeur relative - 

# run
window.mainloop()
