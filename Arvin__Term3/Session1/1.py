import tkinter as tk 

root = tk.Tk()
f1=tk.Frame(root)
f2=tk.Frame(root)
f1.pack()
f2.pack()

tk.Entry(f1, bg='red' ).pack()
tk.Button(f1, text='Say my name').pack()

tk.Entry(f2, bg='blue' ).pack()
tk.Button(f2, text='Say my name').pack()

root.mainloop()