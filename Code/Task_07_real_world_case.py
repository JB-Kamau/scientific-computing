import numpy as np
from scipy.linalg import lu_factor, lu_solve

# REAL-WORLD CASE: node voltages in a resistor network when the input
# currents change over time (nodal analysis).
#
#   Three nodes in a row. Each node connects to ground through a resistor,
#   and neighbouring nodes are connected by resistors:
#     node 1 - ground: 10 ohm     node 1 - node 2: 10 ohm
#     node 2 - ground: 20 ohm     node 2 - node 3: 20 ohm
#     node 3 - ground: 10 ohm
#   A current source injects current into each node (amperes).
#   Kirchhoff's current law gives:  G v = i
#   where G is the conductance matrix (siemens), v the node voltages and
#   i the injected currents.
#
# ASSUMPTIONS
#  - Ideal resistors, steady DC at each time step.
#  - The network (so G) never changes; only the injected currents change.
#  - The four sets of injected currents are invented for this exercise.

g_ground = np.array([1/10, 1/20, 1/10])     # node-to-ground conductances (S)
g12 = 1/10                                   # node 1 - node 2 (S)
g23 = 1/20                                   # node 2 - node 3 (S)

G = np.array([
    [g_ground[0] + g12, -g12,                    0.0],
    [-g12,               g12 + g_ground[1] + g23, -g23],
    [0.0,                -g23,                    g23 + g_ground[2]]
])

# Injected currents (A) at four time steps: [node 1, node 2, node 3]
current_steps = [
    np.array([0.5, 0.0, 0.2]),
    np.array([0.4, 0.1, 0.2]),
    np.array([0.3, 0.2, 0.2]),
    np.array([0.2, 0.3, 0.2])
]

# Factor G only once, reuse for every time step
lu, piv = lu_factor(G)

for step, i_inj in enumerate(current_steps, start=1):
    v = lu_solve((lu, piv), i_inj)
    residual = i_inj - G @ v
    current_to_ground = np.sum(g_ground * v)      # current leaving to ground
    print(f"Time step {step}")
    print("Injected currents (A):", i_inj)
    print("Node voltages (V):", np.round(v, 4))
    print("Residual norm:", np.linalg.norm(residual))
    print(f"Current injected: {i_inj.sum():.4f} A | "
          f"current into ground: {current_to_ground:.4f} A")
    print()