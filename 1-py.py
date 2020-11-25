first_input = input("enter your number:")
even_list = []
odd_list = []

while first_input:
    first_input = int(first_input)
    if first_input % 2 == 0:
        even_list.append(first_input)
    else:
        odd_list.append(first_input)
    first_input = input("enter your number:")
print(f"odd{odd_list}\n even{even_list}")