bascket = [
    'apple',
    'apple',
    'kiwi',
    'kiwi',
    'watermelon',
    'banana'
]
frequensits = []
for fruit in bascket:
    if fruit in frequensits:
        frequensits[fruit] += 1
    else:
        frequensits[fruit] = 1

print(frequensits)