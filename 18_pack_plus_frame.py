import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('400x600')
window.title('pack parameters')
window.bind('<Escape>', lambda event: window.quit())

# top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text='label 1', background='red')
label2 = ttk.Label(top_frame, text='label 1', background='blue')

# middle widgets
label3 = ttk.Label(window, text='label 1', background='green')

# bottom  frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text='label 1', background='orange')

button = ttk.Button(bottom_frame, text='button')
button2 = ttk.Button(bottom_frame, text=' another button')

# exercice frame
exercice_frame = ttk.Frame(bottom_frame)
button_exercice_1 = ttk.Button(exercice_frame, text='buttom 3')
button_exercice_2 = ttk.Button(exercice_frame, text='buttom 4')
button_exercice_3 = ttk.Button(exercice_frame, text='buttom 5')


# top layout
label1.pack(side='left', fill='both', expand=True)
label2.pack(side='left', fill='both', expand=True)
top_frame.pack(fill='both', expand=True)

# middle layout
label3.pack(expand=True)

# bottom layout
button.pack(side='left', expand=True, fill='both')
label4.pack(side='left', expand=True, fill='both')
button2.pack(side='left', expand=True, fill='both')
bottom_frame.pack(expand=True, fill='both', padx=20, pady=20)

# exercice layout
button_exercice_1.pack(expand=True, fill='both',)
button_exercice_2.pack(expand=True, fill='both',)
button_exercice_3.pack(expand=True, fill='both',)
exercice_frame.pack(expand=True, fill='both', side='left')

# run
window.mainloop()