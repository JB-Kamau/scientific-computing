from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# ---- THE ONE CHANGED PARAMETER -------------------------------------------
# Original program used a capacity of 1000. Here it is 1100.
capacity = 1100.0
# --------------------------------------------------------------------------

rng = np.random.default_rng(42)

mean_demand = 850.0
std_demand = 120.0
N = 100_000

# Random demand scenarios
demand = rng.normal(mean_demand, std_demand, N)
overloaded = demand > capacity
overload_probability = overloaded.mean()

print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

# Running probability to show convergence
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)
indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

plt.semilogx(
    indices + 1,
    running_probability[indices]
)
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk (capacity = 1100)")
plt.grid(True)
plt.savefig(Path(__file__).with_name("Task_20_modified_parameter.png"), dpi=150)
plt.show()