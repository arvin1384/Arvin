import tkinter as tk
import datetime 


def pressed():
    msg= """Welcome
Your turn: {}
{}
{}
{} people in line
"""
    number.set(number.get() + 1)
    today = datetime.datetime.now()
    date = today.strftime("%a , %b ,%d , %Y")
    time = today.strftime("%H:%M:%S")
    poi = len(waiting)
    waiting.append(
        {
        'number' : number.get() , 
        'date' : date,
        'time' : time,
        'POI' : poi
        }
    )   
    print(msg.format(number.get() , date ,time ,poi))
    print(waiting)

waiting  = []
root  = tk.Tk()
number = tk.IntVar()
text_box  = tk.Text(root , bg='khaki', width=21 , height=8)
text_box.grid(row=0 , column=0)
text_box.insert(tk.END , 'You will be the first one!!')


tk.Button(root , text='Press!' , command=pressed).grid(row=1 , column=0)
root.mainloop()