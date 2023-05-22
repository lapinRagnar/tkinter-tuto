import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('menu widget')

# menu
menu = tk.Menu(window)
window.configure(menu=menu)

# sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='Nouveau', command=lambda: print('nouveau'))
file_menu.add_command(label='Ouvrir', command=lambda: print('Ouvrir'))

file_menu.add_separator()

menu.add_cascade(label='Fichier', menu=file_menu)

file_menu.add_command(label='Fermer', command=lambda: print('Fermer'))

# another sub menu - help menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='besoin aide', command=lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label='cocher', onvalue='on', offvalue='off', variable=help_check_string)

menu.add_cascade(label='Aide', menu=help_menu)

# another menu - exercice avec sous menu et un autre sous menu
exercice_menu = tk.Menu(menu, tearoff=False)
exercice_menu.add_command(label='exercice test 1')

menu.add_cascade(label='exercice', menu=exercice_menu)

exercice_sub_menu = tk.Menu(menu, tearoff=False)
exercice_sub_menu.add_command(label='sous menu 2 ')
exercice_menu.add_cascade(label='moooooore stuff', menu=exercice_sub_menu)

# menu button with ttk
menu_button = ttk.Menubutton(text='menu buttom with ttk')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label='entree 1', command=lambda: print('entree 1'))
button_sub_menu.add_command(label='entree 2', command=lambda: print('entree 2'))
button_sub_menu.add_checkbutton(label='cocher ooooh', command=lambda: print('cocher'))

# menu_button.configure(menu=button_sub_menu)   # est la même chose ci-dessous
menu_button['menu'] = button_sub_menu

# run
window.mainloop()