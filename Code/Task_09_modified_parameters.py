import numpy as np

# MODIFIED PARAMETER: one extra link is added between node A and node D.
# link_A_D = 0.0 is the original network (no link); 1.0 adds the link.
link_A_D = 1.0

# Adjacency matrix for a small undirected network.
# Node order: A, B, C, D
A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])
A[0, 3] = link_A_D      # link A -> D
A[3, 0] = link_A_D      # link D -> A (undirected, so the matrix stays symmetric)

eigenvalues, eigenvectors = np.linalg.eig(A)

# Dominant eigenvalue/eigenvector
index = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[index])
dominant_vector = np.abs(np.real(eigenvectors[:, index]))
centrality = dominant_vector / dominant_vector.sum()

nodes = ["A", "B", "C", "D"]
print("Link between A and D:", link_A_D)
print("Links per node:", A.sum(axis=1))
print("Dominant eigenvalue:", dominant_value)
print("Eigenvector-based importance:")
for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")

# Verify Av = lambda*v
v = np.real(eigenvectors[:, index])
print("Verification error:",
      np.linalg.norm(A @ v - dominant_value * v))