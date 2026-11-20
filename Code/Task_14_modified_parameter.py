from pathlib import Path

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# ---- THE ONE CHANGED PARAMETER -------------------------------------------
# Original program used 305 ms at 350 users. Here it is 400 ms.
RESPONSE_AT_350 = 400.0
# --------------------------------------------------------------------------

# Concurrent users and measured server response time (milliseconds)
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, RESPONSE_AT_350], dtype=float)

# A simple quadratic model for increasing delay
def model(x, a, b, c):
    return a*x**2 + b*x + c

parameters, covariance = curve_fit(model, users, response_ms)
a, b, c = parameters
predicted = model(users, a, b, c)
rmse = np.sqrt(np.mean((response_ms - predicted)**2))

print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 400 users: {model(400, a, b, c):.2f} ms")

x_plot = np.linspace(users.min(), 400, 300)
plt.scatter(users, response_ms, label="Measurements")
plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted curve")
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting (modified)")
plt.legend()
plt.grid(True)
plt.savefig(Path(__file__).with_name("Task_14_modified_parameter.png"), dpi=150)
plt.show()