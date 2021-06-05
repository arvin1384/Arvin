from tkinter import *
import sys
def do_it():
    mystr.set(entry1.get())
def exit_sys():
    sys.exit()

root = Tk()
root.geometry('200x200')
mystr = StringVar()
label1 = Label(root , textvariable=mystr)
mystr.set('')
label1.pack()
entry1 = Entry()
entry1.pack()
button1 = Button (root , text='Ok' , command=do_it)
button1.pack()
button2 = Button (root , text='Exit' , command=exit_sys)
button2.pack()
mainloop()