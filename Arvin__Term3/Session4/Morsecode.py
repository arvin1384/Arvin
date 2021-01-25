import tkinter as tk
from tkinter import StringVar, ttk


def translate():
    new_text = text1.get().upper()
    text_translated = ""
    for character in new_text:
        text_translated += MORSE[character] + ' '
    Text_box.delete('1.0' , tk.END)
    Text_box.insert(tk.END , text_translated)






MORSE = {
        'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----', ', ':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-' , ' ' : ' '
}

      

title= "Translate Text to Morse"
root1 = tk.Tk()
root1.geometry('400x300')
text1 = StringVar()
tk.Label( root1 , text=title , font=('times') , bg='blue' ).grid(row=0 , column=0)
tk.Entry(root1  , textvariable=text1 ,font='times' ).grid(row=1 , column=0)
Text_box = tk.Text(root1 ,  bg='yellow' , height=5 , width=52)
Text_box.grid(row=2 , column=0)
Text_box.insert(tk.END , 'Your translated here')
tk.Button(root1 , text="Translate" , font=('times'), command=translate).grid(row=3 , column=0)


root1.mainloop()