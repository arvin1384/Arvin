import tkinter as tk
from tkinter import Button, messagebox
import hashlib
from tkinter import ttk
import json
import datetime
import random



def read_json(file_path):
    with open(file_path , 'r') as names:
        return json.load(names)

def write_json(file_path , data):
    with open(file_path , 'w') as names:
        json.dump(data , names , indent=4)


def get_card_number():
    n = read_json('names.json')
    if n:
        print('beyne 1000 ta 9999')
        return n[-1]['card_number'] + random.randint(1000 , 9999)
    else:
        print('beyne 7000000000 ta 60000000000')
        return random.randint(6000000000000000 , 7000000000000000)

def get_destination(card):
    names = read_json('names.json')
    for name in names:
        if str(name['card_number']) == card:
            return names.index(name)
    return None

########## def Register Button############
def confirm():
    info={}
    info["username"] = username_r.get()
    info["Password"] = sha(password_r.get())
    info["created_at"] = created_at_()
    info["card_number"] = get_card_number()
    info["balance"] = 10000
    names_json = read_json('names.json')
    names_json.append(info)
    write_json('names.json' , names_json)
    messagebox.showinfo(title='Success!' , message='You Registered success')
    username_r.set('')
    password_r.set('')




def sha(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest()


def created_at_():
    dt= datetime.datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")



############################### def login button ######################
def log_in():
    global person , ind
    names = read_json('names.json')
    for name in  names:
        if name['username'] == username_l.get():
            if name['Password']== sha(password_l.get()):
                root.withdraw()#این تابع رووت رو محو میکنه و deiconify هم برش میگردونه
                menu.deiconify()
                person = name
                messagebox.showinfo(title='Success!' , message='You Loged-in successfully!')
                return None
        ind += 1
    messagebox.showerror(title='Failed', message='Username or password Invalid!')


######################### withdraw ####################
def withdraw():
    def withdrawal():
        global person
        amount = withdraw_amount.get()
        if person["balance"] > amount:
            names = read_json('names.json')
            names[ind]["balance"] -= amount
            write_json('names.json' , names)
            messagebox.showinfo(title='Successfully Done!' , message='Withdraw  successfully!!!')
            withdraw_root.withdraw()
        else:
            messagebox.showerror(title='Failed', message='Not enough Money!!')

        # persons = read_json('names.json')
        # for p in persons:
        #     if p["username"] == person["username"]:
        #         if p["balance"] > amount:
        #             messagebox.showinfo(title='Success!' , message='Withdraw  successfully!!!')
        #         else:
        #             messagebox.showerror(title='Failed', message='Not enough Money!!')

    withdraw_root  = tk.Toplevel()
    withdraw_amount = tk.IntVar()
    tk.Entry(withdraw_root , textvariable=withdraw_amount , cnf=conf).grid(row=0 , column =0 , sticky=tk.E + tk.W)
    Button(withdraw_root , text='Withdraw' , cnf=conf , command=withdrawal).grid(row=1 , column= 0 , sticky=tk.E + tk.W)
    Button(withdraw_root , text='Close' , cnf=conf , command=withdraw_root.destroy).grid(row=2 , column=0 , sticky=tk.E + tk.W)



######################### balance ####################
def balance():
    username_l.get()
    balance_top = tk.Toplevel()
    now = datetime.datetime.now()
    msg= now.strftime('%Y-%m-%d\n')  + now.strftime('%H:%M:%S')
    tk.Label(balance_top , text=msg , cnf=conf ).grid(row=0 , column=0)
    msg1 = 'Your balance:\n' + str(person['balance'])
    tk.Label(balance_top , text=msg1 , cnf=conf ).grid(row=1 , column=0)
    Button(balance_top , text='Close' , cnf=conf , command=balance_top.destroy).grid(row=2 , column=0)
    
    

######################### transfer ####################
def transfer():
    def transfer_money():
        global person, ind
        amount = transfer_amount.get()
        if person["balance"] > amount:
            if get_destination(des.get()):
                names = read_json('names.json')
                names[ind]["balance"] -= amount
                names[get_destination(des.get())]["balance"] += amount
                write_json('names.json' , names)
                messagebox.showinfo(title='Succesfuly Done!' , message= 'Transfer Succesfully!')
            else:
                messagebox.showerror(title='Failed' , message='Not Destination Found!!')
        else:
            messagebox.showerror(title='Failed' , message='Not Enough Money')        
                 

    def validation(var , indx , mode):
        c1= len(des.get()) == 16
        c2 = des.get().isdigit()
        if c1 and c2:
            e1.config(bg="green")
        else:
            e1.config(bg="red")

    transfer_root  = tk.Toplevel()
    tk.Label(transfer_root , text='Amount').grid(row=0 , column=0)
    transfer_amount = tk.IntVar()
    tk.Entry(transfer_root , cnf=conf , textvariable=transfer_amount).grid(row=0 , column=1)

    tk.Label(transfer_root , text="Destination").grid(row=1  , column=0)
    des = tk.StringVar()
    des.trace_add('write', validation)

    e1 = tk.Entry(transfer_root , cnf=conf , textvariable=des)
    e1.grid(row=1 , column=1)

    Button(transfer_root , text='Transfer' , cnf=conf , command=transfer_money).grid(row=2 , column= 0 , sticky=tk.E + tk.W)
    Button(transfer_root , text='Close' , cnf=conf , command=transfer_root.destroy).grid(row=3 , column=0 , sticky=tk.E + tk.W)
######################### change [pass] ####################
def change_pass():
    def change():
        global person,ind
        if person["Password"] == sha(old_password.get()):
            if sha(new_password.get()) == sha(repeat_new_password.get()):
                names = read_json('names.json')
                names[ind]["Password"] == new_password.get()
                write_json('names.json' , names)
                messagebox.showinfo(title='Succesfully Done' , message='Password Changed')
            else:
                messagebox.showerror(title='Failed!' , message='NOt Matched')
        else:
            messagebox.showerror(title='Failed!' , message='Wrong Password')

    change_pass_root = tk.Toplevel()
    old_password = tk.StringVar()
    tk.Label(change_pass_root , text="Your old password:" , cnf=conf).grid(row=0 , column=0)
    tk.Entry(change_pass_root , cnf=conf , textvariable=old_password).grid(row=0 , column=1 , sticky=tk.E + tk.W)


    new_password = tk.StringVar()
    tk.Label(change_pass_root , text="New password:" , cnf=conf).grid(row=1 , column=0)
    tk.Entry(change_pass_root , textvariable=new_password).grid(row=1 , column=1 ,sticky=tk.E + tk.W )


    repeat_new_password = tk.StringVar()
    tk.Label(change_pass_root , text="Repeat New password:" , cnf=conf).grid(row=2 , column=0)
    tk.Entry(change_pass_root , textvariable=repeat_new_password).grid(row=2 , column=1 , sticky=tk.E + tk.W)


    tk.Button(change_pass_root , text="Change" , cnf=conf , command=change).grid(row=3  ,column=0)



root = tk.Tk()
conf = {
    'font' : ('times' , 25)
}
ind = 0
person = None
menu = tk.Toplevel()
######################################################
########################## Note book #################
######################################################

note = ttk.Notebook()
note.grid(row=0 , column=0)
register = tk.Frame(note)
login = tk.Frame(note)
note.add(register, text='Registration Form')
note.add(login , text= 'Log-in')

################# Register ###################

tk.Label(register , text='username' ).grid(row=0 , column=0)
username_r = tk.StringVar()
tk.Entry( register , textvariable=username_r).grid(row=0 , column=1)


tk.Label(register , text='password' ).grid(row=1 , column=0)
password_r = tk.StringVar()
tk.Entry( register , textvariable=password_r ,  show= '*').grid(row=1 , column=1)

button_register = tk.Button( register , text='Register' , command=confirm)
button_register.grid(row=2 , column=0 , columnspan=2,sticky=tk.W + tk.E)
button_register.bind("<Return>" , confirm)
tk.Button( register , text='Cancel', command=root.destroy ).grid(row=3 , column=0 , columnspan=2, sticky=tk.W + tk.E)


##################### Login ######################
tk.Label(login, text='username' ).grid(row=0 , column=0)
username_l = tk.StringVar()
tk.Entry( login, textvariable=username_l).grid(row=0 , column=1)


tk.Label(login, text='password' ).grid(row=1 , column=0)
password_l = tk.StringVar()
tk.Entry( login, textvariable=password_l , show= '*').grid(row=1 , column=1)

button_log = tk.Button( login, text='Login' , command=log_in)
button_log.grid(row=2 , column=0 , columnspan=2,sticky=tk.W + tk.E)
button_log.bind("<Return>" , log_in)
tk.Button( login, text='Cancel', command=root.destroy ).grid(row=3 , column=0 , columnspan=2, sticky=tk.W + tk.E)


######################################################
########################## Menu ######################
######################################################


tk.Button( menu, text='Balance' , command=balance).grid(row=0 , column=0 )
tk.Button( menu, text='Withdraw' , command=withdraw).grid(row=0 , column=1 )
tk.Button( menu, text='Transfer' , command=transfer).grid(row=1 , column=0)
tk.Button( menu, text='Change password' , command=change_pass).grid(row=1 , column=1 )


menu.withdraw()
root.mainloop()






