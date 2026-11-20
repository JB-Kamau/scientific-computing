import numpy as np
from scipy.integrate import simpson, trapezoid

# ---- THE ONE CHANGED PARAMETER -------------------------------------------
# Original program used 1.8 kW at 06:00. Here it is 2.4 kW.
PEAK_POWER_KW = 2.4
# --------------------------------------------------------------------------

# Smart-meter readings taken every two hours
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, PEAK_POWER_KW, 1.6, 1.2, 0.9])

energy_trapezoid = trapezoid(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)

print(f"Energy using trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule: {energy_simpson:.3f} kWh")
print(f"Difference between estimates: {abs(energy_simpson - energy_trapezoid):.3f} kWh")