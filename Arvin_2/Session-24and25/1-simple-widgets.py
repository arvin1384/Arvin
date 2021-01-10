import tkinter as tk

root = tk.Tk()  #پنجره اصلی رو برای ما ایجاد میکنه Tk
def login():
    print(e1.get(),e2.get())

l1 = tk.Label(root,text='Username')
l1.pack()

e1 = tk.Entry(root)
e1.pack()


l2 = tk.Label(root,text='Password')
l2.pack()

e2 = tk.Entry(root)
e2.pack()

b1 = tk.Button(root,text='Login',command=login)#ویجت باتن button
b1.pack()

root.mainloop()