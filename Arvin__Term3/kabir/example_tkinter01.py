from tkinter import *

def press():
    name = sv_name.get()
    email = sv_email.get()
    sv_out.set("Name: " + name + "\n" +"Email: " + email)


main = Tk()
main.geometry('320x420')


sv_name = StringVar()
Label(main , text='Name').grid(row=0 , column=0 , sticky= W) 
Entry(main , textvariable=sv_name).grid(row=1 , column=0)


sv_email  = StringVar()
Label(main , text='Email').grid(row=2 , column=0 , sticky= W) 
Entry(main , textvariable=sv_email).grid(row=3 , column=0)


Button(main , text="Click me please" , command=press).grid(row=4 , column=0)

sv_out = StringVar()
Label(main , textvariable=sv_out).grid(row=5 , column=0 , sticky=W)
main.mainloop()