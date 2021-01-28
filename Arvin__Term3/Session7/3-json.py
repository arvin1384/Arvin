import json



with  open('names.json' , 'r') as file:
    file_json = json.load(file)

for i in file_json:
    if i["name"] == "romina":
        print(i["Last"])


for i in file_json:
    if i["name"] == "arvin":
        i["Last"] = "al.seyed"

with open('names.json' , 'w') as outfile:
    json.dump(file_json, outfile , indent=4)