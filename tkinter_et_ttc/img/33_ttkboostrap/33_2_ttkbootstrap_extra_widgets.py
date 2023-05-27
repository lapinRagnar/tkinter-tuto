import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip

# window
window = ttk.Window(themename='darkly')
window.title('extra widgets - ttkbootstrap')
window.geometry('800x600')

# scrollable frame
scroll_frame = ScrolledFrame(window)
scroll_frame.pack()

for i in range(100):
  ttk.Label(scroll_frame, text=f'label : {i}').pack(fill='x')
  ttk.Button(scroll_frame, text=f'bouton {i}').pack(fill='x')
  
# toast
toast = ToastNotification(
  title='ceci est le titre du toast', 
  message='et ceci est le message!', 
  duration=2000,
  bootstyle='warning'
  )
  
ttk.Button(window, text='afficher le toast', command=toast.show_toast).pack(pady=50)

# tooltip
button = ttk.Button(window, text='tooltip button', bootstyle='success')
button.pack(pady=10)
ToolTip(button, text='ceci est mon tooltip message', bootstyle='danger-inverse')

  
# run
window.mainloop()
