import tkinter as tk #پنجره اصلی رو برای ما ایجاد میکنه Tk
from tkinter import messagebox


def login():
    u = e1.get()
    p = e2.get()
    if u == username:
        if p == password:
            messagebox.showinfo(title='Succesful Login',
                                       message='Welcome Back!')
        elif p == '':
            messagebox.showerror(title='Enter Password',
                                       message = "You must enter a Password")
        else:
            messagebox.showerror(title='Wrong Password',
                                       message="You entered invalid Password")
    else:
         messagebox.showerror(title='Wrong Usernamne',
                                    message = "You entered invalid Username")
        
        
username = 'Poulstar'
password = 'Poulstar'

root= tk.Tk()
tk.Label(root, text='Username:').pack()
e1 = tk.StringVar()
tk.Entry(root, textvariable=e1).pack()

tk.Label(root, text='Password:').pack()
e2 = tk.StringVar()
tk.Entry(root, textvariable=e2).pack()

tk.Button(root, text='Login', command=login).pack()
root.mainloop()