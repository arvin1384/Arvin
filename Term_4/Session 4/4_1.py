import tkinter
from Translator import *
string = input("Enter your message: ")
my_object = Translator()
print(string)
print(my_object.translate_to_leet(string))
print(my_object.translate_to_morse(string))
