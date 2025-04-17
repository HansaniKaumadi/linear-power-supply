import numpy as np
import matplotlib.pyplot as plt

# Input voltages
input_voltages = np.array([15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5])

# Output voltages corresponding to different fixed output voltages
output_voltages = {
    "4.0V": [3.87, 3.92, 3.96, 4.01, 4.05, 4.09, 4.13],
    "4.5V": [4.33, 4.39, 4.44, 4.50, 4.55, 4.60, 4.65],
    "5.0V": [4.81, 4.87, 4.94, 5.00, 5.06, 5.13, 5.19],
    "5.5V": [5.28, 5.35, 5.43, 5.50, 5.57, 5.64, 5.70],
    "6.0V": [5.76, 5.84, 5.92, 6.00, 6.07, 6.14, 6.21],
    "6.5V": [6.25, 6.34, 6.42, 6.50, 6.58, 6.65, 6.73],
    "7.0V": [6.76, 6.85, 6.93, 7.01, 7.08, 7.15, 7.22],
    "7.5V": [7.27, 7.35, 7.43, 7.50, 7.57, 7.64, 7.70],
    "8.0V": [7.78, 7.86, 7.93, 8.00, 8.06, 8.11, 8.17],
}

# Plot
plt.figure(figsize=(8, 6))
for label, values in output_voltages.items():
    plt.plot(input_voltages, values, marker='o', linestyle='-', label=f"Output {label}")

plt.xlabel("Input Voltage (V)")
plt.ylabel("Output Voltage (V)")
plt.title("Output Voltage vs Input Voltage")
plt.legend()
plt.grid(True)
plt.show()

