from pathlib import Path

import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# ---- THE ONE CHANGED PARAMETER -------------------------------------------
# Original program used 25.5 C at 13:00. Here it is 28.0 C (a warm spike).
TEMP_AT_13H = 28.0
# --------------------------------------------------------------------------

# Hourly temperature measurements
hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, TEMP_AT_13H, 25.0])

linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

# Estimate every 10 minutes = 1/6 hour
ten_minute_times = np.arange(8, 14 + 1/6, 1/6)
linear_estimates = linear(ten_minute_times)
cubic_estimates = cubic(ten_minute_times)

target_time = 10.5  # 10:30
print(f"Linear estimate at 10:30: {float(linear(target_time)):.2f} C")
print(f"Cubic estimate at 10:30: {float(cubic(target_time)):.2f} C")

plt.scatter(hours, temperature, label="Hourly measurements")
plt.plot(ten_minute_times, linear_estimates, label="Linear")
plt.plot(ten_minute_times, cubic_estimates, label="Cubic spline")
plt.xlabel("Hour of day")
plt.ylabel("Temperature (C)")
plt.title("Temperature interpolation (modified)")
plt.legend()
plt.grid(True)
plt.savefig(Path(__file__).with_name("Task_13_modified_parameter.png"), dpi=150)
plt.show()