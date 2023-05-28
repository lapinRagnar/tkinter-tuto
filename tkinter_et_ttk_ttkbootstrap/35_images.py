import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk

def stretch_image(event):
  global resized_tk
  width = event.width
  height = event.height
  # create an image
  resized_image = image_original.resize((width, height))
  resized_tk = ImageTk.PhotoImage(resized_image)
  # place on the canvas
  canvas.create_image(0, 0, image=resized_tk, anchor='nw') 

def fill_image(event):
  global resized_tk
  
  # current ratio of the canvas
  canvas_ratio = canvas.winfo_width() / canvas.winfo_height()
  
  # get the coordonates of the image
  if canvas_ratio > image_ratio:                # canvas is wider than image
    width = int(event.width)
    height = int(width / image_ratio)
  else:
    height = int(event.height)
    width = int(height * image_ratio)
  
  resized_image = image_original.resize((width, height))
  resized_tk = ImageTk.PhotoImage(resized_image)
  # place on the canvas
  canvas.create_image(int(event.width/2), int(event.height/2), image=resized_tk, anchor='center') 

def show_full_image(event):
  global resized_tk
  
  # current ratio of the canvas
  # canvas_ratio = canvas.winfo_width() / canvas.winfo_height()
  canvas_ratio = event.width / event.height
  
  # get the coordonates of the image
  if canvas_ratio > image_ratio:                # canvas is wider than image
    height = int(event.height)
    width = int(height * image_ratio)
  else:
    width = int(event.width)
    height = int(width / image_ratio)
  
  resized_image = image_original.resize((width, height))
  resized_tk = ImageTk.PhotoImage(resized_image)
  # place on the canvas
  canvas.create_image(int(event.width/2), int(event.height/2), image=resized_tk, anchor='center')
  


# set up the window
window = tk.Tk()
window.title("Images")
window.geometry("600x600")
window.bind('<Escape>', lambda event: window.destroy())

# grid layout
window.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
window.rowconfigure(0, weight=1)

# import images
image_original = Image.open('img/black_puma.jpg')
image_ratio = image_original.size[0]/ image_original.size[1]
print(image_ratio)
image_tk = ImageTk.PhotoImage(image_original)

image_home_tk = ctk.CTkImage(
  light_image=Image.open('img/home.jpg').resize((50, 50)), 
  dark_image=Image.open('img/home2.png').resize((50, 50)),
)

image_settings_tk = ctk.CTkImage(
  light_image=Image.open('img/settings.jpg').resize((50, 50)),
  dark_image=Image.open('img/settings2.png').resize((50, 50)),
)
  

# widget
# label = ttk.Label(window, text= 'Black Puma', image=image_tk)
# label.pack()

button_frame = ttk.Frame(window)

button_home = ctk.CTkButton(button_frame, text="mon home", image=image_home_tk, compound='right')
button_home.pack(pady=10)

button = ctk.CTkButton(button_frame, text="mon settings", image=image_settings_tk, compound='right')
button.pack(pady=10)

button_frame.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')

# canvas for the image
canvas = ctk.CTkCanvas(window, background='gray', bd=0, highlightthickness=0, relief='ridge')
canvas.grid(column=1, row=0, columnspan=3, padx=10, pady=10, sticky='nsew')

# canvas.create_image(0, 0, image=image_tk, anchor='nw')
# canvas.bind('<Configure>', fill_image)
canvas.bind('<Configure>', stretch_image)
# canvas.bind('<Configure>', show_full_image)

# run the main loop
window.mainloop()