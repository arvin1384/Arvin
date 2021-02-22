import tkinter as tk
import datetime 
import json


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
        'number' : number.get(), 
        'date' : date,
        'time' : time,
        'POI' : poi
        }
    )
    text_box.delete('1.0' , tk.END)
    text_box.insert(tk.END , msg.format(number.get() , date ,time ,poi))




def operator(operator_number):
    addad = {
        1: c1,
        2: c2,
        3: c3
    }
    if waiting:
        poped = waiting.pop(0)
        poped['call'] = datetime.datetime.now().strftime("%H:%M:%S")
        poped['operator'] = operator_number
        addad[operator_number].set(poped['number'])
        with open('Arvin/data.json' , 'r') as file:
           file_json = json.load(file)
        file_json.append(poped)
        with open('Arvin/data.json' , 'w') as outfile:
            json.dump(file_json ,outfile , indent=4)






waiting  = []
root  = tk.Tk()
number = tk.IntVar()
text_box  = tk.Text(root , bg='khaki', width=21 , height=8)
text_box.grid(row=0 , column=0)
text_box.insert(tk.END , 'You will be the first one!!')
tk.Button(root , text='Press!' , command=pressed).grid(row=1 , column=0)


top = tk.Toplevel()
tk.Button(top , text='Operator1' , command=lambda: operator(1)).grid(row=0 , column=0)
tk.Button(top , text='Operator2' , command=lambda: operator(2)).grid(row=1 , column=0)
tk.Button(top , text='Operator3' , command=lambda: operator(3)).grid(row=2 , column=0)

c1= tk.IntVar()
tk.Label(top ,textvariable=c1).grid(row=0 , column=1)

c2= tk.IntVar()
tk.Label(top ,textvariable=c2).grid(row=1 , column=1)

c3= tk.IntVar()
tk.Label(top ,textvariable=c3).grid(row=2 , column=1)
root.mainloop()