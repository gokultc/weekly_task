import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("temp.csv")
data['date']=pd.to_datetime(data['date'])
# data['year'] = data['year'].dt.year

plt.figure(figsize=(10,5))

plt.plot(data['date'],data['temp'],label='temp',color='red')

plt.xlabel('date')
plt.ylabel('temp')

plt.grid(True)

plt.tight_layout()

plt.legend()

plt.show()