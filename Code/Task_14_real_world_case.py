from pathlib import Path

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Real-world case: calibrating a temperature sensor (like a TMP36).
# The data are SIMULATED, not real measurements: true line is
# voltage = 500 + 10*T (mV) plus random noise of about 5 mV.
rng = np.random.default_rng(42)
temp_c = np.linspace(0, 70, 8)
voltage_mv = 500 + 10*temp_c + rng.normal(0, 5, temp_c.size)

# Straight-line model: voltage = a*T + b
def line(T, a, b):
    return a*T + b

parameters, covariance = curve_fit(line, temp_c, voltage_mv)
a, b = parameters
predicted = line(temp_c, a, b)
rmse = np.sqrt(np.mean((voltage_mv - predicted)**2))

print(f"Fitted line: voltage = {a:.4f} * T + {b:.2f} mV")
print(f"RMSE: {rmse:.2f} mV")

# Use the calibration backwards: convert a new reading to temperature
reading_mv = 800.0
temperature_estimate = (reading_mv - b) / a
print(f"Reading of {reading_mv:.0f} mV corresponds to {temperature_estimate:.2f} C")

x_plot = np.linspace(0, 70, 200)
plt.scatter(temp_c, voltage_mv, label="Simulated calibration data")
plt.plot(x_plot, line(x_plot, a, b), label="Fitted line")
plt.xlabel("Reference temperature (C)")
plt.ylabel("Sensor voltage (mV)")
plt.title("Sensor calibration by curve fitting (simulated data)")
plt.legend()
plt.grid(True)
plt.savefig(Path(__file__).with_name("Task_14_real_world_case.png"), dpi=150)
plt.show()