import numpy as np
from scipy.optimize import minimize

# Real-world case: choosing how many IoT sensor nodes of two types to
# install so that a farm is covered at the lowest cost.
# All numbers are ASSUMED (made up), not real prices.
#
# x = number of Type A nodes (short range)
# y = number of Type B nodes (long range)
#
# Cost per node:     A = 15,  B = 28
# Coverage per node: A = 40 m^2, B = 90 m^2
# Required coverage: at least 1000 m^2

def cost(z):
    x, y = z
    return 15*x + 28*y

def coverage_constraint(z):
    x, y = z
    return 40*x + 90*y - 1000

constraints = {
    "type": "ineq",
    "fun": coverage_constraint
}

bounds = [(0, None), (0, None)]

solution = minimize(
    cost,
    x0=[10, 5],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x
print("Optimization success:", solution.success)
print(f"Type A nodes: {x:.3f}")
print(f"Type B nodes: {y:.3f}")
print(f"Total coverage: {40*x + 90*y:.2f} m^2")
print(f"Minimum cost: {solution.fun:.2f}")

# Whole nodes are required, so test integer combinations.
best_integer = None
for a in range(0, 30):
    for b in range(0, 30):
        area = 40*a + 90*b
        if area >= 1000:
            total_cost = 15*a + 28*b
            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, area)

print("Best whole-node solution (cost, A, B, coverage):", best_integer)