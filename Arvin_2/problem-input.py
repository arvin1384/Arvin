first_input = input("Enter your number")
input_list = []

while(first_input):
    input_list.append(int(first_input))
    first_input = input("Enter your number")

total = 0
for number in input_list:
    total += number

count = len(input_list)
average = total/count
print(f"Sum of my numbers: {total}")
print(average)