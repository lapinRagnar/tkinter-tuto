import tkinter as tk
from tkinter import ttk
from random import choice

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

# data
first_name = ['bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_name = ['Smith', 'Brown', 'Wilson', 'Thomas', 'Cook', 'Taylor', 'Walker', 'Clark']

# Treeview()
table = ttk.Treeview(
  window,
  columns=('first', 'last', 'email'),
  show='headings'
)
table.heading('first', text='First Name')
table.heading('last', text='Last Name')
table.heading('email', text='Email')
table.pack(fill='both', expand=True)

# insert values into a table
# table.insert(parent='', index=0, values=('John', 'Doe', 'johnDoe@gmail.com'))
for i in range(100):
  first = choice(first_name)
  last = choice(last_name)
  email = f'{last[0]}_{first}@email.com'
  data = (first, last, email)
  table.insert(parent='', index=0, values=data)  

# event
def item_select(_):
  for i in table.selection():
    print(table.item(i)['values'])

def delete_items(_):
  print('delete')
  for i in table.selection():
    table.delete(i)
  
table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>)', delete_items)

# run
window.mainloop()