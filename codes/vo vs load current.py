import matplotlib.pyplot as plt

# Data for 6V Output
load_current_6V = [24.3, 17.82, 12.42, 2.66, 1.79]
output_voltage_6V = [5.69, 5.82, 5.87, 5.98, 5.98]

# Data for 7V Output
load_current_7V = [29.7, 20.58, 14.72, 3.2, 2.13]
output_voltage_7V = [6.50, 6.73, 6.80, 6.94, 6.96]

# Plot the data
plt.figure(figsize=(8, 6))
plt.plot(load_current_6V, output_voltage_6V, marker='o', linestyle='-', label='6V Output')
plt.plot(load_current_7V, output_voltage_7V, marker='s', linestyle='-', label='7V Output')

# Labels and Title
plt.xlabel('Load Current (mA)')
plt.ylabel('Output Voltage (V)')
plt.title('Output Voltage vs. Load Current')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
