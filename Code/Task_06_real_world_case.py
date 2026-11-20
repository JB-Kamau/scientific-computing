import numpy as np

# REAL-WORLD CASE: finding the currents in a two-loop resistor circuit
# (mesh-current analysis, from Kirchhoff's voltage law).
#
#   Loop 1 contains V1, R1 and the shared resistor R2.
#   Loop 2 contains V2, R3 and the shared resistor R2.
#   I1 and I2 are the loop currents, both taken clockwise.
#
#   Loop 1:  (R1 + R2) I1 - R2 I2 = V1
#   Loop 2: -R2 I1 + (R2 + R3) I2 = V2
#
# ASSUMPTIONS
#  - Ideal resistors and ideal voltage sources, steady DC.
#  - R1 = R2 = R3 = 10 ohms, V1 = 12 V, V2 = 6 V (values chosen for the exercise).
#  - Both sources push their loop current in the clockwise direction.

R1, R2, R3 = 10.0, 10.0, 10.0      # ohms
V1, V2 = 12.0, 6.0                  # volts

A = np.array([
    [R1 + R2, -R2],
    [-R2,     R2 + R3]
])
b = np.array([V1, V2])

I = np.linalg.solve(A, b)           # [I1, I2] in amperes
I1, I2 = I
residual = b - A @ I

# Current and power in each resistor
I_R2 = I1 - I2                      # current through the shared resistor
power_R1 = I1**2 * R1
power_R2 = I_R2**2 * R2
power_R3 = I2**2 * R3
power_used = power_R1 + power_R2 + power_R3
power_supplied = V1 * I1 + V2 * I2

print(f"Determinant of A: {np.linalg.det(A):.1f}")
print(f"Loop current I1: {I1:.4f} A")
print(f"Loop current I2: {I2:.4f} A")
print(f"Current through shared resistor R2: {I_R2:.4f} A")
print("Residual:", residual)
print(f"Power used by resistors: {power_used:.2f} W")
print(f"Power supplied by sources: {power_supplied:.2f} W")