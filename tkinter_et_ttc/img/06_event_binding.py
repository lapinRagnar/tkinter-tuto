import tkinter as tk
from tkinter import ttk

def get_pos(event):
  print(f"x: {event.x} - y: {event.y}")

# window
window = tk.Tk()
window.title('event binding')
window.geometry('600x500')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text="un bouton")
button.pack()

# event
button.bind('<Alt-KeyPress-a>', lambda event: print('an event'))
window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))
window.bind('<Motion>', get_pos)
entry.bind('<FocusIn>', lambda event: print('entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('entry field was unselected'))

# run
window.mainloop()
