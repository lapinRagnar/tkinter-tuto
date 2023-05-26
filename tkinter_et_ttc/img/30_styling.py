import tkinter as tk
from tkinter import ttk, font
# import pprint

# window
window = tk.Tk()
window.title('styling')
window.geometry('600x300')

# pprint.pprint(font.families())
# style
style = ttk.Style()
# style.theme_use('clam')  #('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

# print(style.theme_names())

# style.configure(
#   'TButton', 
#   background='orange',
#   foreground='green'
# )

style.configure(
  'new.TButton', 
  background='orange',
  foreground='green'
)

style.map(
  'new.TButton',
  foreground=[('pressed', 'red'), ('disabled', 'orange')],
)

style.configure('TFrame', background='pink')


# widgets
label = ttk.Label(
  window, 
  text='A label\nanother long text for me',
  background='brown',
  foreground='white',
  font=('Courier New Greek', 30),
  padding=20,
  justify='left'
  )
label.pack()

button = ttk.Button(window, text='A button')
button.pack()

frame = ttk.Frame(window, width=200, height=200)
frame.pack(expand=True, fill='both')

# run
window.mainloop()