import numpy as np

# MODIFIED PARAMETER: same weather station, same day, but every reading
# is 5 degrees Celsius hotter (a heat-wave day).
warming_c = 5.0

# 24 hourly temperature readings in degrees Celsius (original data)
original_c = np.array([
18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

# Vectorized change: add the warming to every reading at once
temperatures_c = original_c + warming_c

mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)

# Vectorized Celsius-to-Fahrenheit conversion (new and original data)
temperatures_f = 1.8 * temperatures_c + 32
original_f = 1.8 * original_c + 32

print(f"Warming applied: +{warming_c:.1f} C")
print(f"Daily mean temperature: {mean_temp:.2f} C")
print(f"Minimum temperature: {min_temp:.2f} C")
print(f"Maximum temperature: {max_temp:.2f} C")
print("First six Fahrenheit readings:", temperatures_f[:6])

# Compare with the original day
print(f"Change in mean: {mean_temp - np.mean(original_c):+.2f} C")
print("Change in first six Fahrenheit readings:",
      np.round(temperatures_f[:6] - original_f[:6], 2))