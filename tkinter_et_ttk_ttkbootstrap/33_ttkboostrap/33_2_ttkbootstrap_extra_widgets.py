import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge

# window
window = ttk.Window(themename='darkly')
window.title('extra widgets - ttkbootstrap')
window.geometry('800x800')

# scrollable frame
# scroll_frame = ScrolledFrame(window)
# scroll_frame.pack()

# for i in range(100):
#   ttk.Label(scroll_frame, text=f'label : {i}').pack(fill='x')
#   ttk.Button(scroll_frame, text=f'bouton {i}').pack(fill='x')
  
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

# calendar
calendar = DateEntry(window)
calendar.pack(pady=10)
ttk.Button(window, text='get calendar date', command=lambda: print(calendar.entry.get())).pack(pady=10)

# progress bar -> floodgauge
progress_int = tk.IntVar(value=50)
progress = Floodgauge(
  window, 
  text="bar d'avancement", 
  variable=progress_int, 
  bootstyle='danger', 
  mask='mon progression {}%'
  )
progress.pack(fill='x')
ttk.Scale(window, from_=0, to=100, variable=progress_int).pack()

# meter
meter = ttk.Meter(
    metersize=180,
    padding=5,
    amountused=25,
    metertype="semi",
    subtext="miles per hour",
    interactive=True,
)
meter.pack(pady=30)
  
# run
window.mainloop()
