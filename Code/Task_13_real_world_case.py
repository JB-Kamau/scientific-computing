from pathlib import Path

import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Real-world case: ADC-to-temperature lookup table for a microcontroller.
# The table values are ASSUMED (simulated), not real calibration data.
adc_counts = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900], dtype=float)
temp_c = np.array([-10.0, 5.0, 15.0, 24.0, 33.0, 42.0, 52.0, 65.0, 82.0])

linear = interp1d(adc_counts, temp_c, kind="linear")
cubic = CubicSpline(adc_counts, temp_c)

# Readings that fall between table entries
for reading in (250, 450, 650, 850):
    print(
        f"ADC {reading}: linear = {float(linear(reading)):.2f} C, "
        f"cubic = {float(cubic(reading)):.2f} C"
    )

fine = np.linspace(100, 900, 400)
plt.scatter(adc_counts, temp_c, label="Lookup table")
plt.plot(fine, linear(fine), label="Linear")
plt.plot(fine, cubic(fine), label="Cubic spline")
plt.xlabel("ADC count")
plt.ylabel("Temperature (C)")
plt.title("ADC lookup table interpolation (assumed data)")
plt.legend()
plt.grid(True)
plt.savefig(Path(__file__).with_name("Task_13_real_world_case.png"), dpi=150)
plt.show()