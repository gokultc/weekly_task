import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("weather_data.csv")
data['date']=pd.to_datetime(data['date'])

plt.figure(figsize=(10,5))

plt.plot(data['date'],data['temp_max'],label='max temp',color='green')
plt.plot(data['date'],data['temp_min'],label='min temp',color='blue')

plt.title('Temperature')
plt.xlabel('date')
plt.ylabel('temp')

plt.grid(True)

plt.tight_layout()

plt.legend()

plt.show()