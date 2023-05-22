import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
# window.geometry('600x400+500+200')                # geometry('widthxHeight+left+top')
window.title('confgurer le window')
window.iconbitmap('img/favicon.ico')

# exercice - start the window at the middle of the screen
window_width = 800
window_height = 600
display_width = window.winfo_width()
display_height = window.winfo_height()

left = int(display_width/2 - display_width/2)
top = int(display_height/2 - display_height/2)

window.geometry(f'{window_width}x{window_height}+{left}+{top}')

# window sizes
window.minsize(200, 100)
window.maxsize(1000, 700)
window.resizable(True, False)                      # resizable(x, y)

# screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
window.attributes('-alpha', 0.9)                   # transparence
window.attributes('-topmost', True)                # mettre en premier plan de l'ecran

# security event
window.bind('<Escape>', lambda event: window.quit() )

window.attributes('-disable', False)
window.attributes('-fullscreen', False)

# title bar - winwdow without title bar
# window.overrideredirect(True)
# grip = ttk.Sizegrip(window)
# grip.place(relx=1.0, rely=1.0, anchor='se')

# run
window.mainloop()