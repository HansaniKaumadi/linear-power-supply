import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Given data for 6V
load_current_6V = np.array([24.3, 17.82, 12.42, 2.66, 1.79])
output_voltage_6V = np.array([5.69, 5.82, 5.87, 5.98, 5.98])

# Given data for 7V
load_current_7V = np.array([29.7, 20.58, 14.72, 3.2, 2.13])
output_voltage_7V = np.array([6.5, 6.73, 6.8, 6.94, 6.96])

# Sort the data to ensure strictly increasing x-values
sorted_indices_6V = np.argsort(load_current_6V)
load_current_6V = load_current_6V[sorted_indices_6V]
output_voltage_6V = output_voltage_6V[sorted_indices_6V]

sorted_indices_7V = np.argsort(load_current_7V)
load_current_7V = load_current_7V[sorted_indices_7V]
output_voltage_7V = output_voltage_7V[sorted_indices_7V]

# Generate smooth curve
load_current_6V_smooth = np.linspace(load_current_6V.min(), load_current_6V.max(), 300)
load_current_7V_smooth = np.linspace(load_current_7V.min(), load_current_7V.max(), 300)

output_voltage_6V_smooth = make_interp_spline(load_current_6V, output_voltage_6V, k=3)(load_current_6V_smooth)
output_voltage_7V_smooth = make_interp_spline(load_current_7V, output_voltage_7V, k=3)(load_current_7V_smooth)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(load_current_6V_smooth, output_voltage_6V_smooth, label="6V Output", color='b')
plt.plot(load_current_7V_smooth, output_voltage_7V_smooth, label="7V Output", color='r')

# Plot original data points
plt.scatter(load_current_6V, output_voltage_6V, color='b', marker='o', label="6V Data Points")
plt.scatter(load_current_7V, output_voltage_7V, color='r', marker='s', label="7V Data Points")

plt.xlabel("Load Current (mA)")
plt.ylabel("Output Voltage (V)")
plt.title("Output Voltage vs. Load Current")
plt.legend()
plt.grid(True)

plt.show()
