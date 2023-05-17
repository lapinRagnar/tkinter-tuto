import tkinter as tk

# create window
window = tk.Tk()
window.title('window and widgets')
window.geometry('800x500')

# create widgets
text = tk.Text(master=window)
text.pack()
# run
window.mainloop()

