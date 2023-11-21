import pandas as pd
import matplotlib.pyplot as plt

csv_dateipfad = '1_2_e.csv'
#csv_dateipfad = '1_2_e_D1.csv'
#csv_dateipfad = '1_2_e_D2.csv'
#csv_dateipfad = '1_2_e_D3.csv'
#csv_dateipfad = '1_5_d_c1.csv'
#csv_dateipfad = '1_5_d_c2.csv'
#csv_dateipfad = '1_5_d_ohne.csv'
#csv_dateipfad = '1_5_d_c3.csv'



data = pd.read_csv(csv_dateipfad, header=None, names=['X', 'Y1', 'Y2'])

plt.figure(figsize=(10, 6))


plt.plot(data['X'], data['Y1'], label='C1 [V]')
plt.plot(data['X'], data['Y2'], label='C2 [ms]')

plt.xlabel('C2 [ms]')
plt.ylabel('C1 [V]')
plt.legend()
plt.show()