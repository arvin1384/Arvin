class Student:
    _family = ''
    __grade = 0

    def __init__(self , name):
        self.name = name 

    def set_grade(self, grade):
        self.__oiuy = grade #setter definition

    def get_grade(self):
        return self.__grade #getter definition