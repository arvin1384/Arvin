first_name = input("Enter your number!!")
input_list = []

while(first_name):
    input_list.append(first_name)
    first_name = input("Enter your number!!")

sum_list = 0
for number in input_list:
    sum_list = sum_list + number

print(f"Sum of my numbers: {sum_list}")