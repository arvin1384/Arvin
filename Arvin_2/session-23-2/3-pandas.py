import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('persons.csv' )
print(df)
plt.hist([df['coolidity'],df['age']],bins=15,range=(1,15),color='g')
plt.show()
print(df)
# bins = عرض