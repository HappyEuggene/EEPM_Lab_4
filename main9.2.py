import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# Визначення диференціального рівняння
def mouse_population(t, N):
    return -0.008 * N ** 2 + 0.8 * N


# Часовий проміжок для розв'язку
t_span = (0, 20)  # від 0 до 20 місяців
t_eval = np.linspace(t_span[0], t_span[1], 400)  # точки, у яких буде розраховано розв'язок

# Сценарії початкових умов
initial_conditions = [180, 10]

plt.figure(figsize=(10, 6))

for N0 in initial_conditions:
    # Розв'язування диференціального рівняння
    sol = solve_ivp(mouse_population, t_span, [N0], t_eval=t_eval)

    # Побудова графіка
    plt.plot(sol.t, sol.y[0], label=f'Initial N={N0}')

plt.title('Dynamics of Mouse Population Over Time')
plt.xlabel('Time (months)')
plt.ylabel('Population Size')
plt.legend()
plt.grid(True)
plt.show()
