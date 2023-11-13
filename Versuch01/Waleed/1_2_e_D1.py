import pandas as pd
import matplotlib.pyplot as plt

# Dateipfad zur CSV-Datei anpassen
csv_dateipfad = '1_2_e_D1.csv'

# Daten aus der CSV-Datei lesen
data = pd.read_csv(csv_dateipfad, header=None, names=['X', 'Y1', 'Y2'])

# Plot erstellen
plt.figure(figsize=(10, 6))

# Annahme: Die CSV-Datei hat eine Spalte mit dem Namen 'X' und zwei weitere Spalten 'Y1' und 'Y2'
# Hier kannst du die Spaltennamen entsprechend deiner CSV-Datei anpassen.

plt.plot(data['X'], data['Y1'], label='C1 V')
plt.plot(data['X'], data['Y2'], label='C2 ms')

plt.xlabel('C2 ms')
plt.ylabel('C1 V')
plt.title('Digilent WaveForms Oscilloscope Acquisition')
plt.legend()
plt.show()