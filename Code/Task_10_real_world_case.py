from pathlib import Path

import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Real-world case: a silicon diode in series with a resistor on a 5 V supply
# (for example a protection/indicator diode on a microcontroller board).
# All numbers are ASSUMED values for an ideal-diode model, not measurements.
Vs = 5.0          # supply voltage (V)
R = 1000.0        # series resistor (ohms)
Is = 1e-12        # diode saturation current (A), assumed
n = 1.0           # diode ideality factor, assumed
Vt = 0.02585      # thermal voltage at about 300 K (V)

# Diode voltage Vd must satisfy two rules at the same time:
#   resistor:  I = (Vs - Vd) / R
#   diode:     Vd = n*Vt*ln(I/Is + 1)
# Putting the resistor current into the diode rule gives  Vd = g(Vd).
def g(Vd):
    return n * Vt * np.log((Vs - Vd) / (R * Is) + 1)

def f(Vd):
    return Vd - g(Vd)

# Bisection on f(Vd) = Vd - g(Vd), bracket [0, 5] V
bis = root_scalar(f, bracket=[0.0, 5.0], method="bisect", xtol=1e-12)

# Fixed-point iteration Vd_new = g(Vd)
Vd = 0.7
history = [Vd]
for _ in range(100):
    Vd_new = g(Vd)
    history.append(Vd_new)
    if abs(Vd_new - Vd) < 1e-12:
        break
    Vd = Vd_new

Vd_bis = bis.root
Vd_fp = history[-1]
I_mA = (Vs - Vd_bis) / R * 1000

print(f"Bisection diode voltage: {Vd_bis:.6f} V")
print(f"Fixed-point diode voltage: {Vd_fp:.6f} V")
print(f"Bisection iterations: {bis.iterations}")
print(f"Fixed-point iterations: {len(history) - 1}")
print(f"Operating current: {I_mA:.4f} mA")

# Graph: diode curve and resistor load line; they cross at the operating point
v = np.linspace(0, 0.8, 400)
diode_mA = Is * (np.exp(v / (n * Vt)) - 1) * 1000
load_mA = (Vs - v) / R * 1000
plt.plot(v, diode_mA, label="Diode current")
plt.plot(v, load_mA, label="Resistor (load line)")
plt.plot(Vd_bis, I_mA, "o", label="Operating point")
plt.ylim(0, 6)
plt.xlabel("Diode voltage (V)")
plt.ylabel("Current (mA)")
plt.title("Diode + resistor operating point (assumed values)")
plt.legend()
plt.grid(True)
plt.savefig(Path(__file__).with_name("Task_10_real_world_case.png"), dpi=150)
plt.show()