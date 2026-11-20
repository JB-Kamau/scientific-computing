import numpy as np

# MODIFIED PARAMETER: the rotation angle changes from 45 degrees (original)
# to 90 degrees. The scaling (2.0 and 1.5) is unchanged.
angle_deg = 90

# Print neatly: 4 decimals, and show tiny round-off values (like 1e-16) as 0
np.set_printoptions(precision=4, suppress=True)

# Four corners of a square: each row is [x, y]
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

angle = np.deg2rad(angle_deg)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

# Combined transformation: scale first, then rotate
transformation = rotation @ scale

# Row-vector form requires multiplication by transpose
transformed_points = points @ transformation.T

print(f"Rotation angle: {angle_deg} degrees")
print("Original points:\n", points)
print("Transformation matrix:\n", transformation)
print("Transformed points:\n", transformed_points)
print("Determinant:", np.linalg.det(transformation))