import numpy as np
from scipy.optimize import root_scalar

# Real-world case: reading temperature from an NTC thermistor on a
# microcontroller ADC pin. All numbers below are ASSUMED, not measured.
#
# Circuit: Vcc -- fixed resistor -- (ADC pin) -- thermistor -- GND
VCC_COUNTS = 1023       # 10-bit ADC: counts run from 0 to 1023
R_FIXED = 10000.0       # fixed resistor (ohms)
adc_count = 384         # assumed ADC reading

# Thermistor resistance from the voltage divider
r_measured = R_FIXED * adc_count / (VCC_COUNTS - adc_count)

# Thermistor model (beta equation), temperatures in kelvin
R0 = 10000.0            # resistance at T0 (ohms)
T0 = 298.15             # 25 C in kelvin
B = 3950.0              # beta constant (K)

def thermistor_resistance(T):
    return R0 * np.exp(B * (1/T - 1/T0))

def f(T):
    return thermistor_resistance(T) - r_measured

def df(T):
    return thermistor_resistance(T) * (-B / T**2)

newton = root_scalar(f, fprime=df, x0=300.0, method="newton", xtol=1e-10)
secant = root_scalar(f, x0=290.0, x1=320.0, method="secant", xtol=1e-10)

# Closed-form answer, used only as a check
T_exact = 1 / (1/T0 + np.log(r_measured / R0) / B)

print(f"Thermistor resistance: {r_measured:.1f} ohm")
print(f"Newton-Raphson temperature: {newton.root - 273.15:.4f} C")
print(f"Secant temperature: {secant.root - 273.15:.4f} C")
print(f"Closed-form check: {T_exact - 273.15:.4f} C")
print(f"Newton iterations: {newton.iterations}")
print(f"Secant iterations: {secant.iterations}")