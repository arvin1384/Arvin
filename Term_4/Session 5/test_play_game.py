from tkinter.ttk import Combobox
from test import *
from tkinter import * 
from random import *
from random import choice
window = Tk()
window.geometry('200x300')

human1 = human(100 , 70 , "Arvin")
human2 = human(100 , 75 , "delavar")
human3 = human(100 , 65 , "jangjoo") 
human4 = human(100 , 80 , "jomoong")

monster_g = monster("gonde mahal")

def update_buttons():
    if button_monster_g['state'] == DISABLED:
        button_h1['state'] = DISABLED
        button_h2['state'] = DISABLED
        button_h3['state'] = DISABLED
        button_h4['state'] = DISABLED
        button_monster_g['state'] = NORMAL
    else:
        button_h1['state'] = NORMAL
        button_h2['state'] = NORMAL
        button_h3['state'] = NORMAL
        button_h4['state'] = NORMAL
        button_monster_g['state'] = DISABLED
    if human1.is_alive == False:
        button_h1['state'] = DISABLED
    if human2.is_alive == False:
        button_h2['state'] = DISABLED
    if human3.is_alive == False:
        button_h3['state'] = DISABLED
    if human4.is_alive == False:
        button_h4['state'] = DISABLED
    check_game_state()

def check_game_state():
    if monster_g.is_alive == False:
        print("Humans Win!")
        exit()
    elif (human1.is_alive == False and human2.is_alive == False and
        human3.is_alive== False and human4.is_alive == False):
        print("Monster Win!")
        exit()
    else:
        print("Continue")



def human_attack(h):
    multipliers = [0.8 , 1 , 1.2 , 1.4]
    if h.name == human1.name:
        monster_g.decrease_health_m(human1.attack(choice(multipliers)))
        print(human1.health)
    elif h.name == human2.name:
        monster_g.decrease_health_m(human2.attack(choice(multipliers)))
        print(human1.health)
    elif h.name == human3.name:
        monster_g.decrease_health_m(human3.attack(choice(multipliers)))
        print(human1.health)
    elif h.name == human4.name:
        monster_g.decrease_health_m(human4.attack(choice(multipliers)))
        print(human1.health)
    update_buttons()




def monster_attack(name):
    multipliers = [0.8 , 1 , 1.2 , 1.4]
    if name == human1.name:
        human1.decrease_health_h(monster_g.attack(choice(multipliers)))
    elif name == human2.name:
        human2.decrease_health_h(monster_g.attack(choice(multipliers)))
    elif name == human3.name:
        human3.decrease_health_h(monster_g.attack(choice(multipliers)))
    elif name == human4.name:
        human4.decrease_health_h(monster_g.attack(choice(multipliers)))
    update_buttons()




button_h1 = Button(window , text=human1.name+"attack" , command=lambda : human_attack(human1))
button_h2 = Button(window , text=human2.name+"attack" , command=lambda : human_attack(human2))
button_h3 = Button(window , text=human3.name+"attack" , command=lambda : human_attack(human3))
button_h4 = Button(window , text=human4.name+"attack" , command=lambda : human_attack(human4))
button_monster_g = Button(window , text=monster_g.name + "attack" , command=lambda : monster_attack(cb_monster_choice.get()) , state=DISABLED)
cb_monster_choice = Combobox(window ,
    values=[human1.name , human2.name , human3.name , human4.name],
    state='readonly')
button_h1.pack(side=TOP)
button_h2.pack(side=TOP)
button_h3.pack(side=TOP)
button_h4.pack(side=TOP)
button_monster_g.pack(side=BOTTOM)
cb_monster_choice.pack(side=BOTTOM)

window.mainloop()





