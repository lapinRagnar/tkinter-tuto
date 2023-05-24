import tkinter as tk
from tkinter import ttk

# windows
window = tk.Tk()
window.title('toggling widgets - hide widgets')
window.geometry('600x400')
window.bind('<Escape>', lambda e: window.quit())

# place
# def toggle_label_place():
#   global label_visible
#   if label_visible:
#     label.place_forget()
#     label_visible = False
#   else:
#     label_visible = True
#     label.place(relx=0.5, rely=0.5, anchor='center')

# button = ttk.Button(window, text='toggle label', command=toggle_label_place)
# button.place(x=10, y=10)

# label_visible = True
# label =ttk .Label(window, text='a label', font=('', 40))
# label.place(relx=0.5, rely=0.5, anchor='center')

# with grid
window.columnconfigure((0, 1), weight=1, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')

def toggle_label_grid():
  global label_visible
  if label_visible:
    label.grid_forget()
    label_visible = False
  else:
    label_visible = True
    label.grid(column=1, row=0)
    

button = ttk.Button(window, text='toggle label', command=toggle_label_grid)
button.grid(column=0, row=0)

label_visible = True
label = ttk.Label(window, text='a label', font=('', 40))
label.grid(column=1, row=0)



# run
window.mainloop()