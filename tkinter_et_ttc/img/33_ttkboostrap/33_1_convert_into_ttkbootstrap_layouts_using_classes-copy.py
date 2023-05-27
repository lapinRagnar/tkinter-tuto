# import tkinter as tk
# from tkinter import ttk
# import customtkinter as ctk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class App(ttk.Window):
  def __init__(self, title, size):
    # main setup
    super().__init__(themename='journal')
    self.title(title)
    self.geometry(f'{size[0]}x{size[1]}')
    self.minsize(size[0], size[1])
    self.bind('<Escape>', lambda e: self.quit())
    
    # widgets
    self.Menu = Menu(self)
    self.Main = Main(self)
    
    # run
    self.mainloop()

class Menu(ttk.Frame):
  def __init__(self, parent):
    super().__init__(parent)
    
    self.place(x=0, y=0, relwidth=0.3, relheight=1)
    
    self.create_widgets()
  
  def create_widgets(self):
    # create the widgets
    menu_button_1 = ttk.Button(self, text='button 1', bootstyle='secondary')
    menu_button_2 = ttk.Button(self, text='button 2', bootstyle='succes-outline')
    menu_button_3 = ttk.Button(self, text='button 3', bootstyle='dark')

    menu_slider_1 = ttk.Scale(self, orient='vertical')
    menu_slider_2 = ttk.Scale(self, orient='vertical')

    toggle_frame = ttk.Frame(self)
    menu_toggle_1 = ttk.Checkbutton(toggle_frame, text='check 1')
    menu_toggle_2 = ttk.Checkbutton(toggle_frame, text='check 2')

    entry = ttk.Entry(self)
    
    # create the grid
    self.columnconfigure((0, 1, 2), weight=1, uniform='a')
    self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

    # place the widgets
    menu_button_1.grid(row=0, column=0, sticky='nesw', columnspan=2, padx=4, pady=4)
    menu_button_2.grid(row=0, column=2, sticky='nesw', padx=4, pady=4)
    menu_button_3.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=4, pady=4)

    menu_slider_1.grid(row=2, column=0, rowspan=2, sticky='ns', pady=20)
    menu_slider_2.grid(row=2, column=2, rowspan=2, sticky='ns', pady=20)

    # toggle layout
    toggle_frame.grid(row=4, column=0, columnspan=3, sticky='nsew')
    menu_toggle_1.pack(side='left', expand=True)
    menu_toggle_2.pack(side='left', expand=True)

    # entry layout
    entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')

class Main(ttk.Frame):
  def __init__(self, parent):
    super().__init__(parent)
    self.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
  
    Entry(self, 'Entry 1', 'Button 1', 'green')
    Entry(self, 'Entry 2', 'Button 2', 'orange')
    

class Entry(ttk.Frame):
  def __init__(self, parent, label_text, button_text, label_back_ground):
    super().__init__(parent)
    
    label = ttk.Label(self, text=label_text, background=label_back_ground)
    button = ttk.Button(self, text=label_text)
    
    label.pack(expand=True, fill='both')
    button.pack(expand=True, fill='both', pady=10)
    self.pack(side='left', expand=True, fill='both', padx=20, pady=20)
    
    
    
App('class based app with ctk', (800, 650))
  