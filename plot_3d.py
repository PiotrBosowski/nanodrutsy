import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib


matplotlib.use('TkAgg')

csv_file = "/mnt/c/Users/piotr/Desktop/processed_data-csv.csv"
output_file = "/mnt/c/Users/piotr/Desktop/stacked-spectra.png"
data = pd.read_csv(csv_file)

wavelengths = data.iloc[:, 0]
experiment_times = pd.to_numeric(data.columns[1:], errors='coerce')
spectra = data.iloc[:, 1:]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

for i, time in enumerate(experiment_times):
    intensity = spectra.iloc[:, i]
    ax.plot(wavelengths, [time] * len(wavelengths), intensity, label=f'Time: {time} min')

ax.set_xlabel('Wavelength [nm]')
ax.set_ylabel('Time of the experiment [min]')
ax.set_zlabel('Intensity')
ax.set_title('3D Stacked Spectra Visualization')
plt.show()
