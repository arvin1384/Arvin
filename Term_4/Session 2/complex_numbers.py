class ComplexNumbers():
    def __init__(self , real=0 , imaginary=0):
       self.real = real
       self.imaginary = imaginary
       
    def my_print(self):
        print(self.real , "+" , self.imaginary , "j")

    def add(self , num2):
        result = ComplexNumbers()
        result.real = self.real + num2.real
        result.imaginary = self.imaginary + num2.imaginary
        return result

    def sub(self , num2):
        result = ComplexNumbers()
        result.real = self.real - num2.real
        result.imaginary = self.imaginary - num2.imaginary
        return result

    def __gt__(self , other):
        length1 = self.real*self.real + self.imaginary*self.imaginary
        length2 = other.real*other.real + other.imaginary*other.imaginary
        return (length1 > length2)

    def __eq__(self, other):
        return(self.real == other.real and self.imaginary == other.imaginary)



num1 = ComplexNumbers(6 , 4)
num2 = ComplexNumbers(9 , 3) 
num1.my_print()
num2.my_print()
num3 = num1.add(num2)
num4 = num1.sub(num2)
num4.my_print()