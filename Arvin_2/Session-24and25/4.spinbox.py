import tkinter as tk
from tkinter import messagebox

root = tk.Tk()


option = tk.IntVar()

tk.Spinbox(root,textvariable= option, from_=0, to_=10,wrap=True).pack()


root.mainloop()