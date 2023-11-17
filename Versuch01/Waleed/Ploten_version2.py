import pandas as pd
import matplotlib.pyplot as plt

file_path = '1_2_e_D3.csv' 
data = pd.read_csv(file_path, header=None)

# Daten in Float-Werte umwandeln
data = data.apply(lambda x: x.astype(float))

# Ploten der Werte
plt.figure(figsize=(8, 6))  
plt.plot(data)
plt.xlabel('egal')
plt.ylabel('egal')
plt.title('egal')
plt.legend(data.columns)  
plt.show()
