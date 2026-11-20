import numpy as np

# REAL-WORLD CASE: correcting the orientation of an accelerometer.
# A 2-axis accelerometer (IMU) is mounted on a robot but is twisted 30 degrees
# counter-clockwise relative to the robot's own x and y axes. Every reading must
# be rotated into the robot's frame before it can be used.
#
# ASSUMPTIONS
#  - Only a rotation about the vertical axis, by 30 degrees, in the x-y plane.
#  - Readings are accelerations in m/s^2 as [x, y] in the SENSOR's axes.
#  - The sample readings below are invented for this exercise, not measured.
#  - The first reading is what the sensor would show if the robot accelerated
#    straight forward at 2 m/s^2 (this gives an easy hand check).

mount_angle = np.deg2rad(30)

np.set_printoptions(precision=4, suppress=True)

# Each row is one reading [x, y] in the sensor frame
sensor_readings = np.array([
    [1.7321, -1.0],
    [0.0,     2.0],
    [-1.0,    1.7321],
    [1.0,     1.0]
])

# Rotation matrix: converts sensor-frame components to robot-frame components
R = np.array([
    [np.cos(mount_angle), -np.sin(mount_angle)],
    [np.sin(mount_angle),  np.cos(mount_angle)]
])

# Row-vector form: multiply by the transpose
robot_readings = sensor_readings @ R.T

# Checks
length_before = np.linalg.norm(sensor_readings, axis=1)
length_after = np.linalg.norm(robot_readings, axis=1)
back_again = robot_readings @ R          # R inverse equals R transpose
inverse_equals_transpose = np.allclose(np.linalg.inv(R), R.T)

print("Sensor-frame readings:\n", sensor_readings)
print("Rotation matrix:\n", R)
print("Robot-frame readings:\n", robot_readings)
print("Length before rotation:", length_before)
print("Length after rotation: ", length_after)
print("Determinant of R:", round(np.linalg.det(R), 4))
print("Inverse of R equals its transpose:", inverse_equals_transpose)
print("Rotating back recovers the original readings:",
      np.allclose(back_again, sensor_readings))