import numpy as np

# REAL-WORLD CASE: a microcontroller keeps time by adding the tick length
# to a running clock every tick.
#
# ASSUMPTIONS
#  - The timer ticks every 0.1 s, for 1,000,000 ticks.
#  - The exact elapsed time is therefore 100,000 s (about 27.78 hours).
#  - Three ways of keeping the clock are compared:
#      A. float64 running sum (the normal Python / PC number type)
#      B. float32 running sum (a common type on small microcontrollers)
#      C. count whole ticks as an integer, multiply by 0.1 once at the end
#  - No real device is used. This is a simulation of the arithmetic.

tick = 0.1
n_ticks = 1_000_000
exact_time = 100_000.0            # n_ticks * 0.1, worked out in exact decimal

# A. float64 running sum
clock64 = 0.0
for _ in range(n_ticks):
    clock64 += tick

# B. float32 running sum
clock32 = np.float32(0.0)
tick32 = np.float32(tick)
for _ in range(n_ticks):
    clock32 += tick32

# C. integer tick count, one multiplication at the end
clock_int = n_ticks * tick

def report(name, value):
    value = float(value)
    abs_err = abs(value - exact_time)
    rel_err = abs_err / exact_time
    print(f"{name}: {value:.6f} s | absolute error {abs_err:.6f} s | "
          f"relative error {rel_err:.6%}")

print(f"Exact elapsed time: {exact_time:.6f} s")
report("A. float64 running sum", clock64)
report("B. float32 running sum", clock32)
report("C. integer ticks x 0.1", clock_int)
print("float64 sum equals exact time:", clock64 == exact_time)
print("float64 sum close to exact time:", np.isclose(clock64, exact_time))