import numpy as np

# REAL-WORLD CASE: which node of a wireless sensor mesh is the most influential?
# Six sensor nodes are joined by radio links. The most connected node is not
# always the most important one: a node linked to other well-connected nodes
# matters more than a node linked to dead-end nodes. Eigenvector centrality
# captures that, so we compare it with simply counting links.
#
# ASSUMPTIONS
#  - Links are two-way and all links count equally.
#  - Node order: C1, C2, C3, H, L1, L2
#      C1, C2, C3 form a tightly linked core (each linked to the other two).
#      C1 is also linked to the hub H.
#      H is linked to two leaf nodes L1 and L2, which have no other links.
#  - The network is invented for this exercise, not a real deployment.

nodes = ["C1", "C2", "C3", "H", "L1", "L2"]
links = [("C1", "C2"), ("C1", "C3"), ("C2", "C3"),
         ("C1", "H"), ("H", "L1"), ("H", "L2")]

n = len(nodes)
A = np.zeros((n, n))
for a, b in links:
    i, j = nodes.index(a), nodes.index(b)
    A[i, j] = 1.0
    A[j, i] = 1.0

degree = A.sum(axis=1)                       # number of links per node

eigenvalues, eigenvectors = np.linalg.eig(A)
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
v = np.real(eigenvectors[:, index])
dominant_vector = np.abs(v)
centrality = dominant_vector / dominant_vector.sum()

print(f"Dominant eigenvalue: {dominant_value:.4f}")
print(f"Average links per node: {degree.mean():.2f} | most links on one node: {degree.max():.0f}")
print()
print("Node  links  centrality")
for node, d, c in zip(nodes, degree, centrality):
    print(f"{node:<5} {d:>5.0f}  {c:>10.4f}")
print()
print("Ranking by links:      ", [nodes[i] for i in np.argsort(-degree, kind="stable")])
print("Ranking by centrality: ", [nodes[i] for i in np.argsort(-centrality)])
print("Verification error:", np.linalg.norm(A @ v - dominant_value * v))