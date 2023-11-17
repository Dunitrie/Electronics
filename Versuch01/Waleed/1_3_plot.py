import matplotlib.pyplot as plt
import pandas as pd

# Read the data from the text file
data = pd.read_csv('led_simulation.txt', delim_whitespace=True)

# Extracting column names
columns = data.columns.tolist()
print(columns)

plt.figure(figsize=(10, 6))
for col in columns[1:]:
    #print(col[0])
    plt.plot(data[columns[0]], data[col], label=col)

plt.xlabel('V[V1]')
plt.ylabel('I[mA]')
plt.legend()
plt.grid(True)
plt.show()
