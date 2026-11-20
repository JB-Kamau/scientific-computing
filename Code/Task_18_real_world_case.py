from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Real-world case: a supercapacitor keeps a sensor node alive after the
# power supply is cut. All numbers are ASSUMED (made up), not measured.
#   dV/dt = -V / (R_load * C)
V_start = 5.0        # voltage when the supply fails (V)
V_min = 3.3          # node resets (brown-out) below this voltage (V)
R_load = 1000.0      # equivalent load resistance (ohms)
C = 0.1              # supercapacitor (farads)

def discharge(t, V):
    return [-V[0] / (R_load * C)]

t_eval = np.linspace(0, 120, 1201)
solution = solve_ivp(
    discharge,
    (0, 120),
    [V_start],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

voltage = solution.y[0]
exact = V_start * np.exp(-solution.t / (R_load * C))

# First time the voltage drops below the brown-out level
index = np.argmax(voltage < V_min)
t_holdup = solution.t[index]
t_holdup_exact = R_load * C * np.log(V_start / V_min)

print("Solver success:", solution.success)
print(f"Voltage after 120 s: {voltage[-1]:.4f} V")
print(f"Hold-up time (simulation): {t_holdup:.1f} s")
print(f"Hold-up time (formula): {t_holdup_exact:.2f} s")
print(f"Maximum error against exact solution: {np.max(np.abs(voltage - exact)):.3e} V")

plt.plot(solution.t, voltage, label="solve_ivp")
plt.axhline(V_min, linestyle="--", color="red", label="Brown-out level")
plt.axvline(t_holdup_exact, linestyle=":", color="gray")
plt.xlabel("Time (s)")
plt.ylabel("Supercapacitor voltage (V)")
plt.title("Supercapacitor hold-up time (assumed values)")
plt.legend()
plt.grid(True)
plt.savefig(Path(__file__).with_name("Task_18_real_world_case.png"), dpi=150)
plt.show()