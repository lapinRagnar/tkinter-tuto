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

class Segment(ttk.Frame):
  def __init__(self, parent, label_text, button_text, exercice_text):
    super().__init__(master=parent)
    
    # grid layout
    self.rowconfigure(0, weight=1, uniform='a')
    self.columnconfigure((0, 1, 2), weight=1, uniform='a')
    
    # widgets
    ttk.Label(self, text=label_text).grid(row=0, column=0, sticky='nsew')
    ttk.Button(self, text=button_text).grid(row=0, column=1, sticky='nsew')
    
    self.create_exercice_box(exercice_text).grid(row=0, column=2, sticky='nsew')
    
    self.pack(expand=True, fill='both')
  
  def create_exercice_box(self, text):
    frame = ttk.Frame(master=self)
    ttk.Entry(frame).pack(expand=True, fill='both')
    ttk.Button(frame, text=text).pack(expand=True, fill='both')
    
    return frame

# window
window = tk.Tk()
window.geometry('400x600')
window.title('widgets and return')
window.bind('<Escape>', lambda e: window.quit())

# widget
Segment(window, 'label', 'button', 'exercie')
Segment(window, 'test', 'click', 'ha ha ha')
Segment(window, 'hello', 'test', 'kaiza eeeh')
Segment(window, 'bye', 'dinner', 'ooooh la la')
Segment(window, 'last one', 'exit', 'pory')

# widget
""" create_segment(window, 'test', 'click').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'hello', 'test').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'bye', 'dinner').pack(expand=True, fill='both', padx=10, pady=10)
create_segment(window, 'last one', 'exit').pack(expand=True, fill='both', padx=10, pady=10)
 """



# run
window.mainloop()