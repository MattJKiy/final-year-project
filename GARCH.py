import numpy as np
import matplotlib.pyplot as plt

# GARCH(1, 1) Simulation
# Here we initialise n, alpha_0, alpha_1 and beta_1. We create an time series as a pandas array.

n = 10000
alpha_0 = 0.00001
alpha_1 = 0.34
beta_1 = 0.05

# Initialising the two arrays and assigning x_t[0] = 0 and sigma_t[0] = alpha_0
x_t = np.array([0], dtype=float)
sigma_t = np.array([alpha_0], dtype=float)

for i in range(1, n):
    sigma_value = alpha_0 + alpha_1 * np.square(x_t[i - 1]) + beta_1 * sigma_t[i - 1]
    sigma_t = np.append(sigma_t, sigma_value)

    x_value = np.sqrt(sigma_t[i]) * np.random.normal(0, 1)
    x_t = np.append(x_t, x_value)

# The initial stock price is set to 10

y_t = np.array([10], dtype=float)
for i in range(1, n):
    y_value = y_t[i - 1] * np.exp(x_t[i])
    y_t = np.append(y_t, y_value)

# Plot the stock price
plt.plot(y_t)
plt.show()
