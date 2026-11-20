from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# Real-world case: reliability of an IoT sensor network.
# 10 sensors each work on a given day with probability 0.95.
# The network is "degraded" if fewer than 9 sensors work.
# The probability 0.95 is ASSUMED, and the days are SIMULATED.
rng = np.random.default_rng(42)

n_sensors = 10
p_working = 0.95
min_working = 9
N = 100_000          # number of simulated days

# Each row is one day, each column is one sensor (True = working)
working = rng.random((N, n_sensors)) < p_working
count_working = working.sum(axis=1)

degraded = count_working < min_working
degraded_probability = degraded.mean()

print(f"Estimated probability of a degraded network: {degraded_probability:.4%}")
print(f"Number of degraded days: {degraded.sum()} out of {N}")
print(f"Average number of working sensors: {count_working.mean():.3f}")

counts = np.bincount(count_working, minlength=n_sensors + 1)
plt.bar(np.arange(n_sensors + 1), counts / N)
plt.xlabel("Number of working sensors")
plt.ylabel("Fraction of simulated days")
plt.title("Sensor network reliability (simulated data)")
plt.grid(True, axis="y")
plt.savefig(Path(__file__).with_name("Task_20_real_world_case.png"), dpi=150)
plt.show()