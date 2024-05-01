import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Constants for the model
epsilon1 = 1.0  # Adjust these parameters as necessary
epsilon2 = 0.5
gamma11 = 1.1
gamma12 = 0.4
gamma21 = 0.4
gamma22 = 1.1

# Lotka-Volterra Equations
def lotka_volterra(X, t):
    N1, N2 = X
    dN1_dt = (epsilon1 - gamma11 * N1 - gamma12 * N2) * N1
    dN2_dt = (-epsilon2 + gamma21 * N1 - gamma22 * N2) * N2
    return [dN1_dt, dN2_dt]

# Initial conditions
N1_0 = 10
N2_0 = 5
X0 = [N1_0, N2_0]

# Time vector
t = np.linspace(0, 50, 500)

# Solve the differential equations
solutions = odeint(lotka_volterra, X0, t)

# Plotting the results
plt.figure(figsize=(12, 5))

# Plotting the population trajectories
plt.subplot(1, 2, 1)
plt.plot(t, solutions[:, 0], label='N1(t)')
plt.plot(t, solutions[:, 1], label='N2(t)')
plt.title('Population trajectories')
plt.xlabel('Time')
plt.ylabel('Population size')
plt.legend()

# Plotting the phase portrait
plt.subplot(1, 2, 2)
plt.plot(solutions[:, 0], solutions[:, 1], label='Phase portrait')
plt.title('Phase portrait')
plt.xlabel('N1')
plt.ylabel('N2')
plt.legend()

plt.tight_layout()
plt.show()
