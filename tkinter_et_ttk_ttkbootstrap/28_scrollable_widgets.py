import tkinter as tk
from tkinter import ttk

class ListFrame(ttk.Frame):
  def __init__(self, parent, text_data, item_height):
    super().__init__(master=parent)
    self.pack(expand=True, fill='both')
    
    # widget data
    self.text_data = text_data
    self.item_number = len(text_data)
    self.list_height = self.item_number * item_height
    
    # canvas
    self.canvas = tk.Canvas(self, background='#a54bcd', scrollregion=(0, 0, self.winfo_width(), self.list_height))
    self.canvas.pack(expand=True, fill='both')
    
    # display frame
    self.frame = ttk.Frame(self)
    
    # scrollbar
    self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
    self.canvas.configure(yscrollcommand=self.scrollbar.set)
    self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

    for index, item in enumerate(self.text_data):
      print(index, item)
      self.create_item(index, item).pack(expand=True, fill='both', padx=4, pady=10)
      
    self.canvas.create_window(
      (0, 0), 
      window=self.frame, 
      anchor='nw', 
      width=self.winfo_width(), 
      height=self.list_height
      )  
      
    
    # event
    self.canvas.bind_all('<MouseWheel>', lambda e: self.canvas.yview_scroll(-int(e.delta/60), 'units'))
    self.bind('<Configure>', self.update_size)
  
  def update_size(self, event):
    # if self.list_height >= self.winfo_height():
    #   height = self.list_height
    #   self.canvas.bind_all('<MouseWheel>', lambda e: self.canvas.yview_scroll(-int(e.delta/60), 'units'))
    # else:
    #   height = self.winfo_height()
    #   self.canvas.unbind_all('<MouseWhell>')
    #   self.scrollbar.place_forget()
      
    self.canvas.create_window(
      (0, 0), 
      window=self.frame, 
      anchor='nw', 
      width=self.winfo_width(), 
      height=self.list_height 
      # height=self.height
    )
  
  def create_item(self, index, item):
    frame = ttk.Frame(self.frame)
    
    # grid layout
    frame.rowconfigure(0, weight=1, uniform='a')
    frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
    
    # widgets 
    ttk.Label(frame, text=f'#{index}').grid(row=0, column=0)
    ttk.Label(frame, text=f'#{item[0]}').grid(row=0, column=1)
    ttk.Button(frame, text=f'#{item[1]}').grid(row=0, column=2, columnspan=3, sticky='nsew')
    
    return frame

# window
window = tk.Tk()
window.title('scrolling with widgets')
window.geometry('500x400')

text_list = [
  ('label', 'button'),
  ('thing', 'click'),
  ('third', 'something'),
  ('label 1', 'button'),
  ('label 2', 'button 2'),
  ('serie', 'tv'),
  ('blabla', 'car'),
  ('aie aieuuuh', 'les matou b')
]

list_frame = ListFrame(window, text_list, 100)


# run 
window.mainloop()