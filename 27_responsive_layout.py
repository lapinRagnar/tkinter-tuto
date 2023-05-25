import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
  def __init__(self, start_size):
    super().__init__()
    self.title('responsive layout')
    self.geometry(f'{start_size[0]}x{start_size[1]}')
    self.bind('<Escape>', lambda e: self.quit())
    
    self.frame = ttk.Frame(self)
    self.frame.pack(expand=True, fill='both')
    
    SizeNotifier(
      self, 
      {
        1200: self.create_large_layout, 
        600: self.create_medium_layout, 
        300: self.create_small_layout
      }
    )    
    
    self.mainloop()
  
  def create_small_layout(self):
    
    print('small layout')
    
    self.frame.pack_forget()
    self.frame = ttk.Frame(self)
    
    ttk.Label(self.frame, text='label 1', background='purple').pack(expand=True, fill='both', padx=10, pady=5)
    ttk.Label(self.frame, text='label 2', background='#5fa124').pack(expand=True, fill='both', padx=10, pady=5)
    ttk.Label(self.frame, text='label 3', background='#d8daa4').pack(expand=True, fill='both', padx=10, pady=5)
    ttk.Label(self.frame, text='label 4', background='#c5cc00').pack(expand=True, fill='both', padx=10, pady=5)
    
    self.frame.pack(expand=True, fill='both')
  
  def create_medium_layout(self):
    print('medium layout')
    self.frame.pack_forget()
    self.frame = ttk.Frame(self)
    self.columnconfigure((0, 1), weight=1, uniform='a')
    self.rowconfigure((0, 1), weight=1, uniform='a')
    self.frame.pack(expand=True, fill='both')
    
    ttk.Label(self.frame, text='label 1', background='purple').grid(column=0, row=0, padx=10, pady=10, sticky='nsew')
    ttk.Label(self.frame, text='label 2', background='#5fa124').grid(column=1, row=0, padx=10, pady=10, sticky='nsew')
    ttk.Label(self.frame, text='label 3', background='#d8daa4').grid(column=0, row=1, padx=10, pady=10, sticky='nsew')
    ttk.Label(self.frame, text='label 4', background='#c5cc00').grid(column=1, row=1, padx=10, pady=10, sticky='nsew')
  
  def create_large_layout(self):
    print('large layout')
    
    self.frame.pack_forget()
    self.frame = ttk.Frame(self)
    self.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
    self.rowconfigure(0, weight=1, uniform='a')
    self.frame.pack(expand=True, fill='both')
    
    ttk.Label(self.frame, text='label 1', background='purple').grid(column=0, row=0, sticky='ns', padx=10, pady=10)
    ttk.Label(self.frame, text='label 2', background='#5fa124').grid(column=1, row=0, sticky='nsew', padx=10, pady=10)
    ttk.Label(self.frame, text='label 3', background='#d8daa4').grid(column=2, row=0, sticky='nsew', padx=10, pady=10)
    ttk.Label(self.frame, text='label 4', background='#c5cc00').grid(column=3, row=0, sticky='nsew', padx=10, pady=10)
    
    
    

class SizeNotifier:
  def __init__(self, window, size_dict):
    self.window = window
    self.size_dict = {key: value for key, value in sorted(size_dict.items())}
    self.current_min_size = None
    self.window.bind('<Configure>', self.check_size)
    
    self.window.update()
    min_height = self.window.winfo_height()
    min_width = list(self.size_dict)[0]
    self.window.minsize(min_width, min_height)
    
    print(f'hauteur minimum : {min_height} - largeur minimum : {min_width}')
  
  def check_size(self, event):
    if event.widget == self.window:
      
      window_width = event.width
      checked_size = None
      
      for min_size in self.size_dict:
        delta = window_width - min_size
        if delta >= 0:
          checked_size = min_size
      
      if checked_size != self.current_min_size:
        self.current_min_size = checked_size
        self.size_dict[self.current_min_size]()
    
    
  






app = App((400, 300))