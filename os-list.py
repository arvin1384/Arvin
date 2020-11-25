import os



base = os.getcwd()

print(base)

print(os.listdir(base))


files_list = os.listdir(base)
for i in files_list:
    print(i)
address_list = []
for i in files_list:
    adress = base + "/" + i
    if adress.endswith(".txt"):
        address_list.append(adress)

print(address_list)

for file in address_list:
    os.remove(file)


