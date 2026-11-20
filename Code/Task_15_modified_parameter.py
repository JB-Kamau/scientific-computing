from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# ---- THE ONE CHANGED PARAMETER -------------------------------------------
# Original program sampled every 1.0 s. Here the same positions are
# recorded every 0.5 s.
SAMPLE_INTERVAL = 0.5
# --------------------------------------------------------------------------

# GPS samples: time in seconds and position in metres
time = np.arange(7) * SAMPLE_INTERVAL
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])

speed = np.zeros_like(position)

# Forward difference at the beginning
speed[0] = (position[1] - position[0]) / (time[1] - time[0])

# Central differences for interior points
for i in range(1, len(time) - 1):
    speed[i] = (
        position[i + 1] - position[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Backward difference at the end
speed[-1] = (
    position[-1] - position[-2]
) / (
    time[-1] - time[-2]
)

for t, x, v in zip(time, position, speed):
    print(f"t={t:.1f}s, position={x:.1f}m, estimated speed={v:.2f}m/s")

plt.plot(time, speed, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Speed estimated from GPS position data (modified)")
plt.grid(True)
plt.savefig(Path(__file__).with_name("Task_15_modified_parameter.png"), dpi=150)
plt.show()