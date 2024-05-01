from sympy import symbols, Eq, solve
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

N = symbols('N', real=True, positive=True)

birth_coefficient = 11.2
death_rate = 1.6
competition_intensity = 4.0

equation = Eq(birth_coefficient * (N**2 / (1 + N)) - death_rate * N - competition_intensity * N**2, 0)

stationary_points = solve(equation, N)
print("Стационарні точки:", stationary_points)

def population_growth(t, N):
    return birth_coefficient * (N**2 / (1 + N)) - death_rate * N - competition_intensity * N**2


t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 300)


initial_conditions = [0.1, 0.3, 0.5, 1, 2]

plt.figure(figsize=(12, 8))
for N0 in initial_conditions:
    sol = solve_ivp(population_growth, t_span, [N0], t_eval=t_eval, method='RK45')
    plt.plot(sol.t, sol.y[0], label=f'Initial N={N0}')

plt.title('Динаміка чисельності населення з часом')
plt.xlabel('Час')
plt.ylabel('Чисельність населення N(t)')
plt.legend()
plt.grid(True)
plt.show()
