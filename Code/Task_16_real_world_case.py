import numpy as np
from scipy.integrate import simpson, trapezoid

# Real-world case: battery use of an IoT sensor node over one duty cycle.
# The current readings are SIMULATED (made up), not real measurements.
# Cycle: sleep -> wake up -> transmit -> wake down -> sleep.
time_s = np.arange(0, 9, dtype=float)                    # one reading per second
current_ma = np.array([0.5, 0.5, 15.0, 120.0, 120.0, 15.0, 0.5, 0.5, 0.5])

charge_trapezoid = trapezoid(current_ma, time_s)         # mA*s
charge_simpson = simpson(current_ma, x=time_s)           # mA*s

cycle_time_s = time_s[-1] - time_s[0]
average_current_ma = charge_trapezoid / cycle_time_s

battery_mah = 1000.0                                     # assumed battery capacity
battery_life_hours = battery_mah / average_current_ma     # if the cycle repeats forever

print(f"Charge per cycle (trapezoid): {charge_trapezoid:.2f} mA*s")
print(f"Charge per cycle (Simpson): {charge_simpson:.2f} mA*s")
print(f"Charge per cycle: {charge_trapezoid / 3600:.5f} mAh")
print(f"Average current: {average_current_ma:.2f} mA")
print(f"Estimated battery life: {battery_life_hours:.1f} hours")