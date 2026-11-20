from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# MODIFIED PARAMETER: the stopping tolerance changes from 1e-8 (original)
# to 1e-3. Everything else is unchanged.
tolerance = 1e-3

A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

# Boundary influence: left boundary = 100 C, right boundary = 20 C
b = np.array([100., 0., 0., 0., 20.])

def jacobi(A, b, tol=1e-8, max_iter=500):
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

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
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

x_j, err_j = jacobi(A, b, tol=tolerance)
x_gs, err_gs = gauss_seidel(A, b, tol=tolerance)
x_exact = np.linalg.solve(A, b)

print(f"Tolerance: {tolerance}")
print("Jacobi temperatures:", np.round(x_j, 4))
print("Gauss-Seidel temperatures:", np.round(x_gs, 4))
print("Direct solution:", np.round(x_exact, 4))
print("Jacobi iterations:", len(err_j))
print("Gauss-Seidel iterations:", len(err_gs))
print(f"Largest error, Jacobi: {np.max(np.abs(x_j - x_exact)):.6f} C")
print(f"Largest error, Gauss-Seidel: {np.max(np.abs(x_gs - x_exact)):.6f} C")

plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.axhline(tolerance, linestyle="--", color="gray", label="Tolerance")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Convergence with a looser tolerance")
plt.legend()
plt.grid(True)
plt.savefig(Path(__file__).parent / "Task_08_modified_convergence.png", dpi=150)
plt.show()