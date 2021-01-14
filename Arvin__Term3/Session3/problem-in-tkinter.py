import tkinter as tk
from tkinter import StringVar, ttk
import time
import datetime
from tkinter.constants import DISABLED , NORMAL
from threading import Thread


def to_time(seconds):
    return str(datetime.timedelta(seconds=seconds))


def start(a , b , c):
    seconds = spin1.get()
    string = to_time(seconds)
    timer1.set(string)



def start2(a , b , c):
    seconds = spin2.get()
    string = to_time(seconds)
    timer2.set(string)



def timer(number , label , box):
    box.config(state=DISABLED)
    while number:
        time.sleep(1)
        number -=1
        string = to_time(number)
        label.set(string)
    spinbox1.config(state=NORMAL)



def Counter():
    c = spin1.get()
    th1 = Thread(target=timer , args=(c , timer1 , spinbox1))
    th1.start()
    # spin1.set(0)

        


def Counter1():
    c = spin2.get()
    th1 = Thread(target=timer , args=(c , timer2 , spinbox2))
    th1.start()
    # spin2.set(0)




root = tk.Tk()



timer1 = tk.StringVar()
tk.Label(root , textvariable=timer1).grid(row=0 , column=0)
spin1 = tk.IntVar()
spin1.trace('w', start)
spinbox1 = tk.Spinbox(root , textvariable=spin1 , from_=0 , to=36000 , width=5)
spinbox1.grid(row=1 , column=0)
tk.Button(root , text='Start', command=Counter).grid(row=2 , column=0)


timer2 = tk.StringVar()
tk.Label(root , textvariable=timer2).grid(row=0 , column=1)
spin2 = tk.IntVar()
spin2.trace('w', start2)
spinbox2 = tk.Spinbox(root , textvariable=spin2 , from_=0 , to=36000 , width=10)
spinbox2.grid(row=1 , column=1)
tk.Button(root , text='Start' , command=Counter1).grid(row=2 , column=1)


root.mainloop()
