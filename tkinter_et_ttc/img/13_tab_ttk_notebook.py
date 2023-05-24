import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('tab widget')

# notebook widget
notebook = ttk.Notebook(window)

# tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text='text in tab 1')
label1.pack()
button1 = ttk.Button(tab1, text='button in tab 1')
button1.pack()

# tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text='text in tab 2')
label2.pack()
entry = ttk.Entry(tab2)
entry.pack()
button2 = ttk.Button(tab2, text='button in tab 2')
button2.pack()

# exercice
tab_exercice = ttk.Frame(notebook)
button_1_exercice = ttk.Button(tab_exercice, text='button exercice 1')
button_1_exercice.pack()
button_2_exercice = ttk.Button(tab_exercice, text='button exercice 2')
button_2_exercice.pack()
label_exercice = ttk.Label(tab_exercice, text='label in tab exercice')
label_exercice.pack()


notebook.add(tab1, text='tab 1')
notebook.add(tab2, text='tab 2')
notebook.add(tab_exercice, text='tab exericie')
notebook.pack()




# run
window.mainloop()