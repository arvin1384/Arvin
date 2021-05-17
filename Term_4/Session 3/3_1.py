from resistor import *
from tkinter import *
from tkinter import ttk


def compare():
    r1 = resistor(cb1_1.get(), cb1_2.get(), cb1_3.get())
    r2 = resistor(cb2_1.get(), cb2_2.get(), cb2_3.get())
    print(r1.calculate_resistance())
    print(r2.calculate_resistance())
    if cb_compare.get() == ">":
        print(r1 > r2)
    elif cb_compare.get() == ">=":
        print(r1 >= r2)
    elif cb_compare.get() == "==":
        print(r1 == r2)
    elif cb_compare.get() == "<":
        print(r1 < r2)
    else:
        print(r1 <= r2)


root = Tk()
e1_1 = Entry(root)
constant_colors = ("Black", "Brown", "Red", "Orange",
                   "Yellow", "Green", "Blue", "Violet",
                   "Gray", "White")

cb1_1 = ttk.Combobox(root, values=constant_colors, state='readonly')
cb1_2 = ttk.Combobox(root, values=constant_colors, state='readonly')
cb1_3 = ttk.Combobox(root, values=constant_colors, state='readonly')
cb2_1 = ttk.Combobox(root, values=constant_colors, state='readonly')
cb2_2 = ttk.Combobox(root, values=constant_colors, state='readonly')
cb2_3 = ttk.Combobox(root, values=constant_colors, state='readonly')
cb1_1.set("Black")
cb1_2.set("Black")
cb1_3.set("Black")
cb2_1.set("Black")
cb2_2.set("Black")
cb2_3.set("Black")
cb1_1.grid(row=1, column=1)
cb1_2.grid(row=2, column=1)
cb1_3.grid(row=3, column=1)
cb2_1.grid(row=1, column=2)
cb2_2.grid(row=2, column=2)
cb2_3.grid(row=3, column=2)
cb_compare = ttk.Combobox(root, values=(">", ">=",  "==",  "<",  "<="), state='readonly')
cb_compare.set(">")
cb_compare.grid(row=4, column=1, columnspan=2, sticky="NEWS")
btntxt = StringVar()
btntxt.set("Compare")
button = Button(root, textvariable=btntxt, command=compare, bg='dark red').grid(row=5, column=1, columnspan=2, sticky="NEWS")
root.mainloop()
