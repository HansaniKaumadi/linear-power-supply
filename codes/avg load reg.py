import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Given data
output_voltage = np.array([4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8])
avg_load_reg = np.array([0.8124536709, 1.319488221, 1.60256116, 1.994547416, 
                         2.28489705, 2.732420345, 3.216927439, 3.452944996, 3.777725495])

# Generate smooth curve
output_voltage_smooth = np.linspace(output_voltage.min(), output_voltage.max(), 300)
spline = make_interp_spline(output_voltage, avg_load_reg, k=3)
avg_load_reg_smooth = spline(output_voltage_smooth)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(output_voltage_smooth, avg_load_reg_smooth, label="Average Load Regulation", color='b')

# Plot original data points
plt.scatter(output_voltage, avg_load_reg, color='r', marker='o', label="Data Points")

plt.xlabel("Output Voltage (V)")
plt.ylabel("Average Load Regulation")
plt.title("Average Load Regulation vs. Output Voltage")
plt.legend()
plt.grid(True)

plt.show()
