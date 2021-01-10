import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

choices = ["-select-","Us","Ir","UK"]
option = tk.StringVar()
option.set("IR")
tk.OptionMenu(root,option, *choices).pack()


root.mainloop()