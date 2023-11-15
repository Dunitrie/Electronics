import matplotlib.pyplot as plt
import pandas as pd

# Read the data from the text file
data = pd.read_csv('1_3_2.txt', delim_whitespace=True)

# Extracting column names
columns = data.columns.tolist()
print(columns)

plt.figure(figsize=(10, 6))
for col in columns[1:]:
    #print(col[0])
    plt.plot(data[columns[0]], data[col], label=col)

plt.xlabel(columns[0])
plt.ylabel('mA')
plt.legend()
plt.grid(True)
plt.show()
