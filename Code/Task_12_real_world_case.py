import numpy as np
from scipy.optimize import root

# Real-world case: locating an IoT sensor node from two receivers.
# Each receiver estimates its distance to the node (for example from signal
# strength). All numbers below are ASSUMED (simulated), not measurements.
#
# Receiver 1 at (0, 0) m, receiver 2 at (10, 0) m.
anchor1 = np.array([0.0, 0.0])
anchor2 = np.array([10.0, 0.0])
d1 = 5.0                 # assumed distance from receiver 1 (m)
d2 = np.sqrt(45.0)       # assumed distance from receiver 2 (m), about 6.708

# Two circles: the node lies on both.
def equations(z):
    x, y = z
    return [
        (x - anchor1[0])**2 + (y - anchor1[1])**2 - d1**2,
        (x - anchor2[0])**2 + (y - anchor2[1])**2 - d2**2
    ]

for guess in ([3.0, 2.0], [3.0, -2.0]):
    solution = root(equations, guess)
    print("Initial guess:", guess)
    print("Node position (x, y):", solution.x)
    print("Residuals:", np.array(equations(solution.x)))
    print("Converged:", solution.success)
    print()