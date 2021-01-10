import string 
print(string.punctuation)
txt = """
Deserunt, minim! fuigat^& adipisi*&*cing mollit
"""

for word in txt.split():
    new_word = ''
    for chracter in word:
        if chracter in word:
            pass
    else:
        new_word += chracter
    print(new_word.lower())