import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# window
window = ctk.CTk()
window.title('customtikinter app')
window.geometry('600x400')
window.bind('<Escape>', lambda e: window.quit())

# widgets
# string_var = tk.StringVar(value='ma variable tk')
string_var = ctk.StringVar(value='ma variable tk')
label = ctk.CTkLabel(
  window, 
  text='a ctk label',
  fg_color='pink',
  text_color='blue',
  corner_radius=10,
  textvariable=string_var
)
label.pack()

button = ctk.CTkButton(window, text='a ctk button', fg_color=('#11ccbb', '#ff00aa'))
button.pack()

button = ctk.CTkButton(window, text='set light color mode', fg_color='#bc66fa', command=lambda: ctk.set_appearance_mode('light') )
button.pack(expand=True)
button = ctk.CTkButton(window, text='set dark color mode', fg_color='#bc66fa', command=lambda: ctk.set_appearance_mode('light') )
button.pack()

frame = ctk.CTkFrame(window)
frame.pack(expand=True, side='top')

slider =  ctk.CTkSlider(frame)
slider.pack()

# exercice
switch = ctk.CTkSwitch(
  frame,
  text='ctk switch exercice',
  fg_color=('blue', 'red'),
  progress_color='pink',
  button_color='green',
  button_hover_color='yellow',
  switch_width=60,
  switch_height=40,
  corner_radius=10
).pack()

# run
window.mainloop()