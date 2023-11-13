import pandas as pd
import matplotlib.pyplot as plt

csv_dateipfad = '1_2_e_D2.csv'

data = pd.read_csv(csv_dateipfad, header=None, names=['X', 'Y1', 'Y2'])

plt.figure(figsize=(10, 6))

plt.plot(data['X'], data['Y1'], label='C1 V')
plt.plot(data['X'], data['Y2'], label='C2 ms')

plt.xlabel('C2 ms')
plt.ylabel('C1 V')
plt.title('Digilent WaveForms Oscilloscope Acquisition')
plt.legend()
plt.show()