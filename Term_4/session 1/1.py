class Human:
    def __init__(self , age2 , name2 , height2 , weight2):   
        self.age = age2
        self.name = name2
        self.height = height2 
        self.weight = weight2
    def f():
        print("function f called!")
    def __del__(self):
        print(self.name , "destroyed")

#print(ali.height) # height is an attribute here.
ali = Human(30 , "ali" , 170 , 70)
reza = Human(25 , "Reza" , 160 , 60)
print(ali.height)


ali.f()
