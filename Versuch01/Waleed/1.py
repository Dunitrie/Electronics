import pandas as pd
import matplotlib.pyplot as plt

# Dateipfad zur CSV-Datei anpassen
csv_dateipfad = '1_2_e.csv'

# Daten aus der CSV-Datei lesen
data = pd.read_csv(csv_dateipfad, header=None, names=['X', 'Y1', 'Y2'])

# Plot erstellen
plt.figure(figsize=(10, 6))

# Annahme: Die CSV-Datei hat eine Spalte mit dem Namen 'X' und zwei weitere Spalten 'Y1' und 'Y2'
# Hier kannst du die Spaltennamen entsprechend deiner CSV-Datei anpassen.

plt.plot(data['X'], data['Y1'], label='Y1')
plt.plot(data['X'], data['Y2'], label='Y2')

plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Digilent WaveForms Oscilloscope Acquisition')
plt.legend()
plt.show()
