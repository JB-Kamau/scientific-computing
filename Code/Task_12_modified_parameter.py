import numpy as np
from scipy.optimize import root

# ---- THE ONE CHANGED PARAMETER -------------------------------------------
# Original program used a circle of radius 2. Here the radius is 3.
RADIUS = 3.0
# --------------------------------------------------------------------------

# Find intersections of:
# Circle: x^2 + y^2 = RADIUS^2
# Parabola: y = x^2 - 1
def equations(z):
    x, y = z
    return [
        x**2 + y**2 - RADIUS**2,
        y - (x**2 - 1)
    ]

for guess in ([1.0, 1.0], [-1.0, 1.0]):
    solution = root(equations, guess)
    print("Initial guess:", guess)
    print("Intersection:", solution.x)
    print("Residuals:", np.array(equations(solution.x)))
    print("Converged:", solution.success)
    print()