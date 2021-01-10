things = ["ball","tsshirt"]
colors = ["red","blue"]
charactrestics = ["personality","baba"]

for i,y,j in zip(things,colors,charactrestics):
    print(things,charactrestics,colors)

for things,colors,charactrestics in zip(things,colors,charactrestics):
    print(things,colors,charactrestics)