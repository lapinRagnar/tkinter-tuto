import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def ask_yes_no():
  # answer = messagebox.askquestion('Mon titre', 'le body')
  # print(f' la reponse est : {answer}')
  # messagebox.showinfo('mon titre', 'quelques informations')
  messagebox.showerror('mon titre', 'quelques informations')

def create_window():
  global extra_window
  extra_window = tk.Toplevel()
  extra_window.title('mon extra window')
  extra_window.geometry('300x300')
  ttk.Label(extra_window, text='mon label').pack()
  ttk.Button(extra_window, text='mon bouton').pack()
  ttk.Label(extra_window, text='un autre label').pack(expand=True)

def close_window():
  extra_window.destroy()

# window
window = tk.Tk()
window.title('using multiple windows')
window.geometry('600x400')

# widgets
button1 = ttk.Button(window, text='open main window', command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(window, text='close main window', command=close_window)
button2.pack(expand=True)

button3 = ttk.Button(window, text='create a yes-no window', command=ask_yes_no)
button3.pack(expand=True)


# run
window.mainloop()


"""
lien du documentation
https://docs.python.org/3/library/tkinter.messagebox.html
"""