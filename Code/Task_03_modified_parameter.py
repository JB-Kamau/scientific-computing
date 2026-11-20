import numpy as np
import timeit

# MODIFIED PARAMETER: only the number of readings changes,
# from 1,000,000 (original) to 100,000.
n_readings = 100_000

# Simulated network latency readings in milliseconds
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, n_readings)

def loop_version():
    squared = []
    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)
    return squared

def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds ** 2

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

result = vectorized_version()
print(f"Number of readings: {n_readings:,}")
print("First five squared latency values:", result[:5])
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.6f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")
# Check that both methods give the same answers
print("Both methods agree:", np.allclose(loop_version(), result))