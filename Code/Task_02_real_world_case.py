import numpy as np

# REAL-WORLD CASE: temperature monitoring inside an equipment cabinet.
# An ESP32 with a DHT22 sensor logs the cabinet temperature once per hour
# (hour 0 = midnight). Electronics run hotter and age faster when the
# cabinet is too warm, so we flag every hour above an alarm threshold.
#
# ASSUMPTIONS
#  - One reading per hour, 24 readings, starting at 00:00.
#  - Readings are in degrees Celsius.
#  - The alarm threshold is 30 C (a value chosen for this exercise).
#  - The values below are sample data for the exercise, not real measurements.

threshold_c = 30.0

cabinet_c = np.array([
24.0, 23.8, 23.6, 23.5, 23.4, 23.6,
24.2, 25.1, 26.3, 27.4, 28.5, 29.6,
30.8, 31.5, 32.1, 31.2, 30.4, 29.1,
27.8, 26.5, 25.6, 24.9, 24.4, 24.1
])

mean_temp = np.mean(cabinet_c)
min_temp = np.min(cabinet_c)
max_temp = np.max(cabinet_c)
hour_of_max = np.argmax(cabinet_c)          # position of the largest value

# Comparing an array with a number gives True/False for every element
too_hot = cabinet_c > threshold_c
hours_too_hot = np.sum(too_hot)             # True counts as 1
hot_hour_numbers = np.where(too_hot)[0]     # positions where it is True
percent_too_hot = 100 * hours_too_hot / cabinet_c.size

# Vectorized Celsius-to-Fahrenheit conversion
cabinet_f = 1.8 * cabinet_c + 32

print(f"Mean cabinet temperature: {mean_temp:.2f} C")
print(f"Minimum temperature: {min_temp:.2f} C")
print(f"Maximum temperature: {max_temp:.2f} C at hour {hour_of_max}")
print(f"Hours above {threshold_c:.0f} C: {hours_too_hot} of {cabinet_c.size}"
      f" ({percent_too_hot:.1f}%)")
print("Hours above threshold:", hot_hour_numbers)
print(f"Average temperature during those hours: {cabinet_c[too_hot].mean():.2f} C")
print("Maximum temperature in Fahrenheit:", round(float(np.max(cabinet_f)), 2), "F")