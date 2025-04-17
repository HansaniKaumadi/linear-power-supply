import matplotlib.pyplot as plt

# Fixed output voltage (first column)
fixed_voltage = [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]

# Measured output voltages for different load resistances
measured_voltage = {
    "220 Ω": [3.92, 4.35, 4.81, 5.24, 5.69, 6.11, 6.50, 6.89, 7.31],
    "330 Ω": [3.96, 4.43, 4.90, 5.36, 5.82, 6.28, 6.73, 7.18, 7.64],
    "470 Ω": [3.96, 4.45, 4.93, 5.40, 5.87, 6.32, 6.80, 7.29, 7.75],
    "2.2k Ω": [4.01, 4.49, 4.98, 5.48, 5.98, 6.46, 6.94, 7.44, 7.93],
    "3.3k Ω": [3.99, 4.49, 4.99, 5.49, 5.98, 6.48, 6.96, 7.48, 7.95]
}

# Plotting
plt.figure(figsize=(8, 6))
for label, values in measured_voltage.items():
    plt.plot(fixed_voltage, values, marker='o', label=f"Load {label}")

plt.xlabel("Fixed Output Voltage (V)")
plt.ylabel("Measured Output Voltage (V)")
plt.title("Measured Output Voltage vs Fixed Output Voltage")
plt.legend()
plt.grid(True)
plt.show()