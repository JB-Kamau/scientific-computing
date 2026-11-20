from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# Real-world case: a microcontroller chip heating up while it runs.
# All numbers are ASSUMED (made up), not measured.
#   C_th * dT/dt = P - (T - T_ambient) / R_th
P = 0.5            # power dissipated by the chip (W)
R_th = 40.0        # thermal resistance to the air (K per W)
C_th = 2.0         # heat capacity of the chip (J per K)
T_ambient = 25.0   # air temperature (C)
T_initial = 25.0   # chip starts at air temperature (C)

h = 1.0            # step size (seconds)
end_time = 300.0   # seconds

def heating_rate(T):
    return (P - (T - T_ambient) / R_th) / C_th

time = np.arange(0, end_time + h, h)
temperature = np.zeros_like(time)
temperature[0] = T_initial

for i in range(len(time) - 1):
    temperature[i + 1] = temperature[i] + h * heating_rate(temperature[i])

# Exact solution for validation
tau = R_th * C_th                       # time constant (s)
T_steady = T_ambient + P * R_th         # final temperature (C)
exact = T_steady + (T_initial - T_steady) * np.exp(-time / tau)

print(f"Time constant: {tau:.0f} s")
print(f"Steady-state temperature: {T_steady:.2f} C")
print(f"Euler temperature after 300 s: {temperature[-1]:.2f} C")
print(f"Exact temperature after 300 s: {exact[-1]:.2f} C")
print(f"Final absolute error: {abs(temperature[-1] - exact[-1]):.4f} C")

plt.plot(time, temperature, label="Euler")
plt.plot(time, exact, linestyle="--", label="Exact solution")
plt.axhline(T_steady, linewidth=0.8, color="gray")
plt.xlabel("Time (s)")
plt.ylabel("Chip temperature (C)")
plt.title("Microcontroller heating (assumed values)")
plt.legend()
plt.grid(True)
plt.savefig(Path(__file__).with_name("Task_17_real_world_case.png"), dpi=150)
plt.show()