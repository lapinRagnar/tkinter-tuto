import tkinter as tk
from tkinter import ttk

def create_segment(parent, label_text, button_text):
  frame = ttk.Frame(master=parent)
  
  # grid layout
  frame.rowconfigure(0, weight=1, uniform='a')
  frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
  
  # widgets
  ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky='nsew')
  ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky='nsew')
  
  return frame

""" class Segment(ttk.Frame):
  def __init__(self, parent, label_text, button_text):
    super().__init__(master=parent)
    
    # grid layout
    self.rowconfigure(0, weight=1, uniform='a')
    self.columnconfigure((0, 1, 2), weight=1, uniform='a')
    ttk.Label(self, text=label_text).grid(row=0, column=0, sticky='nsew')
    ttk.Button(self, text=button_text).grid(row=0, column=1, sticky='nsew')
    
    self.pack(expand=True, fill='both') """

# window
window = tk.Tk()
window.geometry('400x600')
window.title('widgets and return')
window.bind('<Escape>', lambda e: window.quit())

# widget
""" Segment(window, 'label', 'button')
Segment(window, 'test', 'click')
Segment(window, 'hello', 'test')
Segment(window, 'bye', 'dinner')
Segment(window, 'last one', 'exit') """

# widget
create_segment(window, 'test', 'click').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'hello', 'test').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'bye', 'dinner').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'last one', 'exit').pack(expand=True, fill='both', padx=10, pady=10)




# run
window.mainloop()