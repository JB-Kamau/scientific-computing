from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# ---- THE ONE CHANGED PARAMETER -------------------------------------------
# Original program used a step size of 1.0 minute. Here it is 5.0 minutes.
h = 5.0  # minutes
# --------------------------------------------------------------------------

# Newton's law of cooling:
# dT/dt = -k(T - T_ambient)
T_ambient = 25.0
T_initial = 90.0
k = 0.12
end_time = 30.0

def cooling_rate(T):
    return -k * (T - T_ambient)

time = np.arange(0, end_time + h, h)
temperature = np.zeros_like(time)
temperature[0] = T_initial

for i in range(len(time) - 1):
    temperature[i + 1] = (
        temperature[i] + h * cooling_rate(temperature[i])
    )

# Exact solution for validation
exact = T_ambient + (T_initial - T_ambient) * np.exp(-k * time)

print(f"Euler temperature after 30 min: {temperature[-1]:.2f} C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} C")
print(f"Final absolute error: {abs(temperature[-1] - exact[-1]):.4f} C")

plt.plot(time, temperature, marker="o", label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Cooling of a hot object (step size h = 5 min)")
plt.legend()
plt.grid(True)
plt.savefig(Path(__file__).with_name("Task_17_modified_parameter.png"), dpi=150)
plt.show()