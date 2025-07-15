import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV file
data = pd.read_csv("weather_data.csv")

# Step 2: Convert date to datetime
data['date'] = pd.to_datetime(data['date'])

# Step 3: Plot temperature trends
plt.figure(figsize=(10, 5))
plt.plot(data['date'], data['temp_max'], label='Max Temp', color='red')
plt.plot(data['date'], data['temp_min'], label='Min Temp', color='blue')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Daily Temperature')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 4: Plot rainfall
# plt.figure(figsize=(8, 4))
# plt.bar(data['date'], data['rainfall'], color='skyblue')
# plt.title("Daily Rainfall")
# plt.xlabel("Date")
# plt.ylabel("Rainfall (mm)")
# plt.tight_layout()
# plt.show()
