import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# window
window = ctk.CTk()
window.title('customtkinter app')
window.geometry('600x500')
window.bind('<Escape>', lambda event: window.quit())

# widgets
string_var = tk.StringVar(value='a custom string')
label = ctk.CTkLabel(
    master=window, 
    text='a ckt label', 
    fg_color='purple', 
    text_color='white', 
    corner_radius=5, 
    textvariable=string_var

)
label.pack()

button = ctk.CTkButton(master=window, text='a ctk button', bg_color='#fa54aa', hover_color='#1a14aa', command=lambda: print('ca marche!'))
button.pack(pady=20)

frame = ctk.CTkFrame(window)
frame.pack(pady=20)

slider = ctk.CTkSlider(frame)
slider.pack(padx=20, pady=20)

# exercice

def switch_event():
    print("switch toggled, current value:", switch_var.get())

switch_var = ctk.StringVar(value="on")

switch = ctk.CTkSwitch(
    window, 
    text="CTkSwitch", 
    command=switch_event,
    variable=switch_var, 
    onvalue="on", 
    offvalue="off"
)

switch.pack(pady=20)

# run
window.mainloop()