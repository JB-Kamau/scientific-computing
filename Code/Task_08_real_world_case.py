from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# REAL-WORLD CASE: steady-state temperature along a copper strip on a circuit
# board, between a hot chip and a cooler connector.
#
# ASSUMPTIONS
#  - One-dimensional heat flow along the strip, steady state, no heat lost
#    sideways and no heat generated inside the strip.
#  - The strip is split into 20 equally spaced interior points.
#  - The chip end is held at 85 C and the connector end at 25 C.
#  - Each interior temperature is the average of its two neighbours, which gives
#    the same matrix form as the original task: 2 T[i] - T[i-1] - T[i+1] = 0.
#  - All numbers are chosen for the exercise, not measured.
#  - With 20 points the iterations need more steps, so max_iter is raised.

n_points = 20
t_chip, t_connector = 85.0, 25.0

A = 2 * np.eye(n_points) - np.eye(n_points, k=1) - np.eye(n_points, k=-1)
b = np.zeros(n_points)
b[0] = t_chip
b[-1] = t_connector

def jacobi(A, b, tol=1e-8, max_iter=20000):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=20000):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (
                b[i]
                - A[i, :i] @ x[:i]
                - A[i, i+1:] @ old[i+1:]
            ) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

# Theory: with no heat source the profile is a straight line between the ends
positions = np.arange(1, n_points + 1)
x_line = t_chip + (t_connector - t_chip) * positions / (n_points + 1)

print("First three temperatures (Gauss-Seidel):", np.round(x_gs[:3], 3), "C")
print("Last three temperatures (Gauss-Seidel): ", np.round(x_gs[-3:], 3), "C")
print("Jacobi iterations:", len(err_j))
print("Gauss-Seidel iterations:", len(err_gs))
print(f"Largest difference, Jacobi vs direct: {np.max(np.abs(x_j - x_exact)):.2e} C")
print(f"Largest difference, Gauss-Seidel vs direct: {np.max(np.abs(x_gs - x_exact)):.2e} C")
print(f"Largest difference, direct vs straight line: {np.max(np.abs(x_exact - x_line)):.2e} C")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
ax1.plot(positions, x_gs, "o-", label="Gauss-Seidel")
ax1.plot(positions, x_line, "--", label="Straight line (theory)")
ax1.set_xlabel("Point along the strip (1 = chip end)")
ax1.set_ylabel("Temperature (C)")
ax1.set_title("Temperature along the strip")
ax1.legend()
ax1.grid(True)
ax2.semilogy(err_j, label="Jacobi")
ax2.semilogy(err_gs, label="Gauss-Seidel")
ax2.set_xlabel("Iteration")
ax2.set_ylabel("Maximum change")
ax2.set_title("Convergence")
ax2.legend()
ax2.grid(True)
plt.tight_layout()
plt.savefig(Path(__file__).parent / "Task_08_real_world_case.png", dpi=150)
plt.show()