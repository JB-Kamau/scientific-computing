from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# Real-world case: wheel speed of a small robot from a rotary encoder.
# The encoder counts are SIMULATED (made up), not real measurements.
COUNTS_PER_REV = 20          # encoder pulses per wheel revolution
WHEEL_CIRCUMFERENCE = 0.20   # metres travelled per revolution
METRES_PER_COUNT = WHEEL_CIRCUMFERENCE / COUNTS_PER_REV

time = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6])        # seconds
counts = np.array([0, 12, 31, 57, 90, 128, 171], dtype=float)
position = counts * METRES_PER_COUNT                         # metres

# np.gradient uses forward/backward differences at the ends and
# central differences in the middle, like the GPS program.
speed = np.gradient(position, time)
acceleration = np.gradient(speed, time)

for t, x, v, a in zip(time, position, speed, acceleration):
    print(f"t={t:.1f}s, position={x:.3f}m, speed={v:.3f}m/s, acceleration={a:.3f}m/s^2")

plt.plot(time, speed, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Wheel speed (m/s)")
plt.title("Robot speed from encoder counts (simulated data)")
plt.grid(True)
plt.savefig(Path(__file__).with_name("Task_15_real_world_case.png"), dpi=150)
plt.show()