import pandas as pd
import matplotlib.pyplot as plt

# Dateipfad zur CSV-Datei anpassen
csv_dateipfad = '1_2_e.csv'

# Daten aus der CSV-Datei lesen und die Zeichenkodierung angeben
data = pd.read_csv(csv_dateipfad, encoding='latin1', skiprows=1, header=None, names=['X', 'Y1', 'Y2'], dtype=str)

# Konvertiere die Werte in den Spalten zu Float
data['X'] = data['X'].astype(float)
data['Y1'] = data['Y1'].astype(float)
data['Y2'] = data['Y2'].astype(float)

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
