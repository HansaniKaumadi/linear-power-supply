import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Given data points
output_voltage = np.array([4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8])
average_line_regulation = np.array([8.733, 10.867, 12.533, 14.333, 15.2, 15.933, 15.2, 14.467, 13.133])

# Generate smooth curve using cubic spline interpolation
x_smooth = np.linspace(output_voltage.min(), output_voltage.max(), 200)  # More points for a smooth curve
y_smooth = make_interp_spline(output_voltage, average_line_regulation, k=3)(x_smooth)  # Cubic spline (k=3)

# Plot the smooth curve
plt.figure(figsize=(8, 6))
plt.plot(x_smooth, y_smooth, label=' Avg. Line Regulation', color='b')
plt.scatter(output_voltage, average_line_regulation, color='r', marker='o', label='Data Points')  # Original points

# Labels and title
plt.xlabel('Output Voltage (V)')
plt.ylabel('Average Line Regulation')
plt.title('Average Line Regulation vs. Output Voltage')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
